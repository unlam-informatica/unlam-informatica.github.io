import numpy as np, json, sys
sys.setrecursionlimit(20000)
from PIL import Image
from scipy import ndimage
CFG=json.load(open(sys.argv[1])); OUT=sys.argv[2]
def mask(a,mode,thr=150):
    r,g,b=[a[...,i].astype(int) for i in range(3)]; avg=(r+g+b)/3; sat=a.max(-1).astype(int)-a.min(-1)
    return {'blue':(b>180)&(r<150)&(b-r>60)&(g<190),'lavender':(b-r>35)&(b-g>35)&(r<200),
            'green':(g>100)&(g-r>25)&(g-b>15),'dark':(avg<100)&(sat<45),'darkgray':(avg<thr)&(sat<45),
            'red':(r>200)&(g<150)&(b<150)}[mode]
def rdp(P,eps):
    if len(P)<3: return P
    a,b=np.array(P[0]),np.array(P[-1]); v=b-a; L=np.hypot(*v)
    d=[abs(v[0]*(p[1]-a[1])-v[1]*(p[0]-a[0]))/L if L else np.hypot(*(np.array(p)-a)) for p in P]
    i=int(np.argmax(d))
    if d[i]>eps: return rdp(P[:i+1],eps)[:-1]+rdp(P[i:],eps)
    return [P[0],P[-1]]
res={}
for name,c in CFG.items():
    a=np.asarray(Image.open(f'{name}.png').convert('RGB'))
    H,W=a.shape[:2]; X=lambda px:(px-c['x0'])/c['sx']; Y=lambda py:(c['y0']-py)/c['sy']
    PX=lambda x:c['x0']+x*c['sx']; PY=lambda y:c['y0']-y*c['sy']
    m=mask(a,c['mode'],c.get('thr',150)).copy()
    e=c.get('edge',14); m[:e,:]=m[-e:,:]=False; m[:,:e]=m[:,-e:]=False
    for x0,y0,x1,y1 in c.get('erase',[]): m[y0:y1,x0:x1]=False
    if c['mode'] in('dark','darkgray'):
        k=c.get('axisw',5); X0=int(round(c['x0'])); Y0=int(round(c['y0']))
        m[:,max(0,X0-k):X0+k+1]=False; m[max(0,Y0-k):Y0+k+1,:]=False
    yy,xx=np.mgrid[0:H,0:W]
    for mk in c.get('markers',[]):
        R=c.get('mr',16); m[(xx-PX(mk[0]))**2+(yy-PY(mk[1]))**2<R*R]=False
    lab,n=ndimage.label(m,structure=np.ones((3,3))); sizes=ndimage.sum(m,lab,range(1,n+1))
    br=[]
    for k in [i+1 for i,s in enumerate(sizes) if s>=c.get('minsize',300)]:
        ys,xs=np.where(lab==k)
        cols={}; rows={}
        for x,y in zip(xs,ys): cols.setdefault(x,[]).append(y); rows.setdefault(y,[]).append(x)
        # Cada rama es el gráfico de una función: las medianas por columna, ordenadas por x, dan el orden
        # correcto aunque sean ralas en los tramos empinados. Los puntos por fila (densos en esos tramos) se
        # proyectan sobre esa polilínea gruesa para ubicarlos en el recorrido.
        C=np.array([(float(x),float(np.median(v))) for x,v in sorted(cols.items())])
        Rw=np.array([(float(np.median(v)),float(y)) for y,v in rows.items()])
        if len(C)<2: continue
        seg=np.diff(C,axis=0); L=np.hypot(seg[:,0],seg[:,1]); cum=np.concatenate([[0],np.cumsum(L)])
        def param(p):
            d=p-C[:-1]; t=np.clip((d*seg).sum(1)/np.maximum(L**2,1e-9),0,1)
            proj=C[:-1]+seg*t[:,None]; dist=((proj-p)**2).sum(1); k=int(np.argmin(dist))
            return cum[k]+t[k]*L[k], dist[k]
        P=[(cum[i],tuple(C[i])) for i in range(len(C))]
        for p in Rw:
            tt,dd=param(p)
            if dd<64: P.append((tt,tuple(p)))
        P.sort(key=lambda z:z[0]); path=[p for _,p in P]
        if len(path)>7:
            A=np.array(path); K=5; pad=np.pad(A,((K//2,K//2),(0,0)),mode='edge')
            sm=np.array([pad[i:i+K].mean(0) for i in range(len(A))]); sm[0],sm[-1]=A[0],A[-1]; path=[tuple(p) for p in sm]
        path=rdp(path,1.2)
        xsp=(max(p[0] for p in path)-min(p[0] for p in path))/c['sx']; ysp=(max(p[1] for p in path)-min(p[1] for p in path))/c['sy']
        if max(xsp,ysp)<c.get('minspan',0): continue
        br.append([(round(X(px),3),round(Y(py),3)) for px,py in path])
    br.sort(key=lambda b:b[0][0])
    res[name]={'branches':br}
    if c.get('redfit'):
        rm=mask(a,'red'); ys,xs=np.where(rm); info=[]
        for kind,val in c['redfit']:
            if kind=='v': sel=np.abs(xs-PX(val))<10; info.append(('x=',round(X(np.median(xs[sel])),3)))
            if kind=='h': sel=np.abs(ys-PY(val))<10; info.append(('y=',round(Y(np.median(ys[sel])),3)))
            if kind=='o':
                sel=np.ones_like(xs,bool)
                for k2,v2 in c['redfit']:
                    if k2=='v': sel&=np.abs(xs-PX(v2))>12
                    if k2=='h': sel&=np.abs(ys-PY(v2))>12
                xd,yd=X(xs[sel]),Y(ys[sel]); mm,bb=np.polyfit(xd,yd,1); info.append(('y=mx+b',round(mm,3),round(bb,3)))
        res[name]['red']=info
    print(name,len(br),[ (b[0],b[-1],len(b)) for b in br], res[name].get('red',''))
json.dump(res,open(OUT,'w'))
