import sys

modules = {}


class Wrapped(object):
    def __init__(self, module):
        self.module = module

    def __getattr__(self, item):
        try:
            return getattr(self.module, item)
        except AttributeError:
            caller = sys._getframe(1)
            plugin = modules[caller.f_globals["__name__"]]
            return getattr(plugin, item)

sys.modules[__name__] = Wrapped(sys.modules[__name__])
