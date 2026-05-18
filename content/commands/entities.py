class CommandEntity:
    def __init__(
        self, kind, nm, get_pos,
        source=None, teleport=None, give_item=None
    ):
        self.kind      = kind        # player | item | ...
        self.nm        = nm
        self.get_pos   = get_pos
        self.source    = source
        self.teleport  = teleport
        self.give_item = give_item

    def pos(self):
        return self.get_pos()
