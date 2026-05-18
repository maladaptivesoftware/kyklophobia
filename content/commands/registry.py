from commands.errors import UnknownCommand


class CommandSpec:
    def __init__(self, nm, handler, aliases=(), usage="", desc=""):
        self.nm      = nm
        self.handler = handler
        self.aliases = aliases
        self.usage   = usage
        self.desc    = desc


class CommandRegistry:
    def __init__(self):
        self._by_name = {}

    def register(self, nm, handler, *, aliases=None, usage="", desc=""):
        sp = CommandSpec(
            nm.lower(), handler,
            tuple(a.lower() for a in (aliases or ())),
            usage, desc,
        )
        for k in (sp.nm,) + sp.aliases:
            self._by_name[k] = sp
        return sp

    def get(self, nm):
        n = nm.lower()
        if n not in self._by_name:
            raise UnknownCommand(f"Unknown command: {nm}")
        return self._by_name[n]

    def list_commands(self):
        seen = {}
        for i in self._by_name.values():
            seen[i.nm] = i
        return sorted(seen.values(), key=lambda s: s.nm)









