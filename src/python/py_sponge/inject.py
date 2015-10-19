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
            caller_name = caller.f_globals["__name__"]
            if caller_name in modules:
                plugin = modules[caller_name]
                return getattr(plugin, item)
            else:
                raise RuntimeError("Unrecognised caller")

sys.modules[__name__] = Wrapped(sys.modules[__name__])
