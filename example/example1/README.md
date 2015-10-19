Hello World plugin
==================

This plugin is an example plugin to show how to create plugins.

## Building

Plugins require to be built first so that Sponge can find them.

To build this plugin navigate to this directory and execute `python setup.py dev`
This will create a jar in the `build` directory. Then place that jar in the mods folder 
of the minecraft game directory.

Note that the plugin doesn't need to be rebuilt ever time, ony when something changes in the
`setup.py` file. Also this isn't portable, to build a jar that is portable run `python setup.py jar`
but them ever time any change is made it needs to be rebuilt.
