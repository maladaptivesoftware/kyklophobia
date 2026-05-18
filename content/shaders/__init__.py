import os

_dir = os.path.dirname(__file__)

def load(name):
    with open(os.path.join(_dir, name), encoding='utf-8') as f:
        return f.read()

def prog(ctx, vert, frag):
    return ctx.program(vertex_shader=load(vert), fragment_shader=load(frag))
