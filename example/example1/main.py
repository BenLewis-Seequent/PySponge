import sys
print(sys.builtin_module_names)
print(1)
try:
    import array
except ImportError, e:
    print(e.message)
print(2)
try:
    from sponge import inject
except ImportError, e:
    print(e.message)
print(3)

def start(plugin):
    plugin.logger.info("Python Plugin")
    inject.logger.info("Injected")
