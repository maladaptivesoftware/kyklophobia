import os
import struct
import uuid

_NAME = "Player"


def tokenfile():
    h = os.path.dirname(os.path.abspath(__file__))
    c = os.path.join(os.path.dirname(h), "client")

    return os.path.join(c, "token.bin")


"""
def whoami():
    fp = tokenfile()
    
    if not os.path.exists(fp):
        idt = {'nm': _NAME, 'token': str(uuid.uuid4())}
        setidenty(idt)
        return idt
        
        
    with open(fp, 'r') as f:
        return json.load(f)
"""

def whoami():
    fp = tokenfile()
    if os.path.exists(fp):
        raw = open(fp, 'rb').read()
        
        if len(raw) >= 18:
            # 16b token + 2b nlen + name
            _token = raw[:16]
            nl = struct.unpack_from('<H', raw, 16)[0]
            nm = raw[18:18 + nl].decode('utf-8', errors='replace')
            return {'nm': nm, 'token': str(uuid.UUID(bytes=_token))}

    identity = {'nm': _NAME, 'token': str(uuid.uuid4())}
    setidenty(identity)
    return identity


def setidenty(identity):
    _token = uuid.UUID(identity['token']).bytes
    nmenc = identity['nm'].encode('utf-8')
    with open(tokenfile(), 'wb') as f:
        f.write(_token)
        f.write(struct.pack('<H', len(nmenc)))
        f.write(nmenc)


def get_tokenbytes(identity):
    return uuid.UUID(identity['token']).bytes


def bytetoken(b):
    return str(uuid.UUID(bytes=b))






