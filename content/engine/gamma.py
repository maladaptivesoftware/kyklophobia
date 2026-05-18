import numpy as np
import shaders


class Gamma:
    # gamma shader  from the origional minecraft console edition
    # file will not be linked here due to obivous reasons, if you want the original shader files, DM me!
    
    def __init__(self, ctx, width, height):
        self.ctx     = ctx
        self.width   = width
        self.height  = height
        self.enabled = False
        self.gamma   = 2.0

        self.prog = shaders.prog(ctx, "gamma.vert", "gamma.frag")

        quad_verts = np.array([
            -1.0, -1.0, 0.0, 1.0,
             1.0, -1.0, 0.0, 1.0,
             1.0,  1.0, 0.0, 1.0,
            -1.0, -1.0, 0.0, 1.0,
             1.0,  1.0, 0.0, 1.0,
            -1.0,  1.0, 0.0, 1.0,
        ], dtype='f4')

        self.vbo = ctx.buffer(quad_verts.tobytes())
        self.vao = ctx.vertex_array(self.prog, [(self.vbo, '4f', 'Position')])

        self.color_tex = ctx.texture((width, height), 4)
        self.color_tex.filter = (ctx.NEAREST, ctx.NEAREST)
        self.depth_tex = ctx.depth_texture((width, height))
        self.fbo = ctx.framebuffer(
            color_attachments=[self.color_tex],
            depth_attachment=self.depth_tex
        )

        self.prog['gamma'].value = self.gamma
        
        

    def setgamma(self, gamma):
        self.gamma = max(0.1, gamma)
        self.prog['gamma'].value = self.gamma

    def toggle(self):
        self.enabled = not self.enabled
        return self.enabled
        
        
        

    def resize(self, width, height):
        self.width  = width
        self.height = height
        self.color_tex.release()
        self.depth_tex.release()
        
        self.fbo.release()
        self.color_tex = self.ctx.texture((width, height), 4)
        self.color_tex.filter = (self.ctx.NEAREST, self.ctx.NEAREST)
        self.depth_tex = self.ctx.depth_texture((width, height))
        self.fbo = self.ctx.framebuffer(
            color_attachments=[self.color_tex],
            depth_attachment=self.depth_tex
        )
        
        
        

    def release(self):
        self.vbo.release()
        self.vao.release()
        self.color_tex.release()
        self.depth_tex.release()
        self.fbo.release()
        self.prog.release()
        
        
