"""Separa de un texto lo que lleva ``$`` pero no es una fórmula: operadores MongoDB y montos en pesos.

Trabaja sobre texto ya sin código. Lo comparten ``normalize`` (marca de delimitadores
desbalanceados) y ``qa`` (operadores sin formato de código, montos y fórmulas mal delimitadas).
"""
from __future__ import annotations

import re

_STAGES = """
addFields bucket bucketAuto changeStream collStats count currentOp densify documents facet fill geoNear graphLookup
group indexStats limit listLocalSessions listSessions lookup match merge out planCacheStats project redact
replaceRoot replaceWith sample search searchMeta set setWindowFields skip sort sortByCount unionWith unset unwind
"""
_QUERY = """
eq gt gte in lt lte ne nin and not nor or exists type expr jsonSchema mod regex text where all elemMatch size
bitsAllClear bitsAllSet bitsAnyClear bitsAnySet geoIntersects geoWithin near nearSphere box center centerSphere
geometry maxDistance minDistance polygon comment meta slice
"""
_UPDATE = """
currentDate inc min max mul rename setOnInsert addToSet pop pull push pullAll each position sort bit
"""
_EXPRESSION = """
abs add allElementsTrue anyElementTrue arrayElemAt arrayToObject avg binarySize bsonSize ceil cmp concat
concatArrays cond convert dateAdd dateDiff dateFromParts dateFromString dateSubtract dateToParts dateToString
dateTrunc dayOfMonth dayOfWeek dayOfYear degreesToRadians divide exp filter first firstN floor function
getField hour ifNull indexOfArray indexOfBytes indexOfCP isArray isNumber isoDayOfWeek isoWeek isoWeekYear last
lastN let literal ln log log10 ltrim map maxN median millisecond minN minute month multiply mergeObjects
objectToArray percentile pow radiansToDegrees rand range reduce regexFind regexFindAll regexMatch replaceAll
replaceOne reverseArray round rtrim second setDifference setEquals setField setIntersection setIsSubset setUnion
split sqrt strcasecmp strLenBytes strLenCP substr substrBytes substrCP subtract sum switch toBool toDate toDecimal
toDouble toInt toLong toLower toObjectId toString toUpper trim trunc tsIncrement tsSecond unsetField week year
zip stdDevPop stdDevSamp top topN bottom bottomN count rank denseRank documentNumber shift derivative integral
expMovingAvg covariancePop covarianceSamp locf linearFill now
"""
MONGO_OPERATORS = frozenset((_STAGES + _QUERY + _UPDATE + _EXPRESSION).split())

_OPS = "|".join(sorted(MONGO_OPERATORS, key=len, reverse=True))
# Variables de sistema ($$NOW, $$ROOT, $$CURRENT...) y también variables de usuario de $let/$map ($$item).
MONGO_VAR_RE = re.compile(r"(?<![\\$])\$\$[A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)*")
MONGO_OP_RE = re.compile(rf"(?<![\\$\w])\$(?:{_OPS})(?![\w$])")
FIELD_PATH_RE = re.compile(r"""(["'])\$[A-Za-z_][\w.]*\1""")
# El número se toma completo (atómico, vía lookahead) para que "$1,1,2$" no retroceda hasta "$1,1".
_AMOUNT_RE = re.compile(r"\$[ ]?(?=(\d+(?:[.,]\d+)*))\1(?![\w$\\^_{(+\-*/=<>]|[,;]\s*\d)")
_UNESCAPED_DOLLAR_RE = re.compile(r"(?<!\\)\$")
_MONGO_ANY = re.compile("|".join(f"(?:{r.pattern})" for r in (FIELD_PATH_RE, MONGO_VAR_RE, MONGO_OP_RE)))


def strip_inline_code(text: str) -> str:
    return re.sub(r"(`+)(?:(?!\1).)+?\1", "", text, flags=re.S)


def find_mongo(text: str) -> list[str]:
    """Operadores, variables y rutas de campo MongoDB presentes (sin repetir, en orden de aparición)."""
    found: list[str] = []
    for match in _MONGO_ANY.finditer(text):
        token = match.group(0)
        if token not in found:
            found.append(token)
    return found


def strip_mongo(text: str) -> str:
    return _MONGO_ANY.sub("", text)


def _looks_like_formula(text: str, start: int) -> bool:
    """¿Lo que va entre este ``$`` y el próximo ``$`` parece matemática (sin palabras de 3 letras o más)?"""
    closing = _UNESCAPED_DOLLAR_RE.search(text, start)
    if not closing:
        return False
    segment = re.sub(r"\\[A-Za-z]+", "", text[start:closing.start()])
    segment = segment.replace("\n", " ")
    return "\n\n" not in text[start:closing.start()] and not re.search(r"[^\W\d_]{3,}", segment)


def clean_dollars(text: str) -> tuple[str, list[str], list[str]]:
    """Devuelve ``(texto sin operadores ni montos, operadores, montos)``.

    Un ``$`` seguido de dígito cuenta como monto solo si no cierra una fórmula abierta y lo que sigue
    al número no continúa una expresión (``$2x$``, ``$2$`` y ``$2+3$`` siguen siendo fórmulas).
    """
    operators = find_mongo(text)
    text = strip_mongo(text)
    out: list[str] = []
    amounts: list[str] = []
    is_open = False
    position = 0
    for dollar in _UNESCAPED_DOLLAR_RE.finditer(text):
        if dollar.start() < position:
            continue
        if not is_open:
            amount = _AMOUNT_RE.match(text, dollar.start())
            if amount and _looks_like_formula(text, amount.start() + 1):
                amount = None
            if amount:
                out.append(text[position:dollar.start()])
                amounts.append(amount.group(0))
                position = amount.end()
                continue
        is_open = not is_open
    out.append(text[position:])
    return "".join(out), operators, amounts
