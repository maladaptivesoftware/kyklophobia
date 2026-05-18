class BlockEntity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.alive = True

    def update(self, dt, world_ctx):
        pass

    def render(self, manager):
        pass
