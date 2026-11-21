import pypdfium2 as p, sys, json
S=6
d=p.PdfDocument(sys.argv[1]); boxes=json.load(open(sys.argv[2])); out=sys.argv[3]
cache={}
for name,(page,x0,y0,x1,y1) in boxes.items():
    if page not in cache: cache[page]=d[page].render(scale=S).to_pil().convert('RGB')
    k=S/2
    cache[page].crop((int(x0*k),int(y0*k),int(x1*k),int(y1*k))).save(f'{out}/{name}.png')
