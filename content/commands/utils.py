import re
import shlex

_RANGE_RE = re.compile(r"^(?:(-?\d+(?:\.\d+)?)\.\.)?(?:(-?\d+(?:\.\d+)?))?$")


def splitline(s):
    s = s.strip()
    if not s: return []
    return shlex.split(s, posix=False)


def parse_range(rng):
    rng = rng.strip()
    if ".." not in rng:
        v = float(rng)
        return v, v
        
    m = _RANGE_RE.match(rng)
    if not m:
        raise ValueError(f"invalid range: {rng}")
        
    a, b = m.group(1), m.group(2)
    return (float(a) if a is not None else None, float(b) if b is not None else None)


def try_float(s):
    try: return float(s)
    except: return None


def parse_coord(tok, base):
    # relative ~1.5 => base + 1.5
    tok = tok.strip()
    if tok.startswith("~"):
        return base if tok == "~" else base + float(tok[1:])
    return float(tok)









