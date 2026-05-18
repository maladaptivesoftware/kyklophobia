import numpy as np

from commands.errors import CommandError
from commands.utils  import parse_range


_ALIAS = {
    "a": "a", "all":    "a",
    "e": "e", "entity": "e",
    "i": "i", "near":   "i",
    "r": "r", "rand":   "r",
    "s": "s", "self":   "s",
}


class TargetSelector:
    def __init__(self, base, args):
        self.base = base
        self.args = args


def parse_sel(tok):
    tok = tok.strip()
    if not tok.startswith("@"):
        raise CommandError(f"Not a selector: {tok}")

    body = tok[1:]
    nm   = body
    astr = ""
    if "[" in body:
        ix = body.index("[")
        nm = body[:ix]
        if not body.endswith("]"):
            raise CommandError(f"Invalid selector args (missing ']'): {tok}")
        astr = body[ix+1:-1]

    if not nm:
        raise CommandError(f"Invalid selector: {tok}")

    base = _ALIAS.get(nm.lower())
    if not base:
        raise CommandError(f"Unknown selector: @{nm}")

    args = {}
    if astr.strip():
        for i in astr.split(","):
            i = i.strip()
            if not i: continue
            if "=" not in i:
                raise CommandError(f"Invalid selector arg (expected k=v): {i}")
                
            k, v = i.split("=", 1)
            args[k.strip().lower()] = v.strip()

    return TargetSelector(base, args)


def _origin(sel, epos):
    o = epos.copy()
    for i, k in enumerate(("x", "y", "z")):
        v = sel.args.get(k)
        if v is not None: o[i] = float(v)
    return o




def _filtdist(ents, origin, rng, out=[]):
    out = []
    dmin, dmax = parse_range(rng)
    for e in ents:
        d = float(np.linalg.norm(e.pos() - origin))
        if dmin is not None and d < dmin: continue
        if dmax is not None and d > dmax: continue
        out.append(e)
    return out




def _sortlim(ents, origin, smode, limit):
    smode = (smode or "arbitrary").lower()
    if   smode == "nearest":
        ents = sorted(ents, key=lambda e: float(np.sum((e.pos() - origin)**2)))
        
        
    elif smode == "furthest":
        ents = sorted(ents, key=lambda e: float(np.sum((e.pos() - origin)**2)), reverse=True)
        
        
    elif smode == "random":
        ents = list(ents)
        np.random.default_rng().shuffle(ents)
        
    if limit is not None:
        ents = ents[:max(0, int(limit))]
        
    return ents







def resolve_sel(sel, executor, entities):
    base = sel.base
    if base == "s": return [executor]

    if   base == "a": cands = [e for e in entities if e.kind == "player"]
    elif base == "e": cands = list(entities)
    
    elif base == "i":
        cands = [e for e in entities if e.kind == "player"]
        sel = TargetSelector(base, {**sel.args,
            "sort":  sel.args.get("sort",  "nearest"),
            "limit": sel.args.get("limit", "1")})
            
    elif base == "r":
        cands = [e for e in entities if e.kind == "player"]
        sel = TargetSelector(base, {**sel.args,
            "sort":  sel.args.get("sort",  "random"),
            "limit": sel.args.get("limit", "1")})
            
    else:
        raise CommandError(f"Unsupported selector base: @{base}")
        

    t = sel.args.get("type")
    if t: cands = [e for e in cands if e.kind.lower() == t.lower()]

    nm = sel.args.get("name")
    if nm: cands = [e for e in cands if (e.nm or "").lower() == nm.lower()]
    

    origin = _origin(sel, executor.pos())

    dist = sel.args.get("distance")
    if dist: cands = _filtdist(cands, origin, dist)

    ls = sel.args.get("limit")
    lim = int(ls) if ls is not None else None

    return _sortlim(cands, origin, sel.args.get("sort", "arbitrary"), lim)




def resolve_target(tok, executor, entities):
    tok = tok.strip()
    if tok.startswith("@"):
        return resolve_sel(parse_sel(tok), executor, entities)
        
    tl = tok.lower()
    m  = [e for e in entities if e.kind == "player" and (e.nm or "").lower() == tl]
    if not m:
        raise CommandError(f"No player named '{tok}'")
    return m















