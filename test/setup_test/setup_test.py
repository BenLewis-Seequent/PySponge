import os
import sys
import shutil
import zipfile
import difflib

from sponge import *

# this script tests the setup/build logic

# this builds the plugin 8 times for 'dev'/'jar' task, jython bundled or not
# and on and empty build directory and a non empty build directory.

# For each build it compares the expected entries in the jar file with the
# actual entries.

# Finally it copies each jar to the directories of the program arguments

# This requires internet access as it needs to download ivy

gen = False

d = difflib.Differ()

jar_locations = []

for r in range(2):
    for task in ['dev', 'jar']:
        for bundle in [True, False]:
            if bundle:
                name = task+"_bundle"
            else:
                name = task
            build_dir = "build_"+name
            plugin_id = "example_"+name
            jar_loc = os.path.join(build_dir, plugin_id+"-0.1.jar")
            if r == 0:
                if os.path.exists(build_dir):
                    shutil.rmtree(build_dir)
                jar_locations.append(jar_loc)
            print("building "+name)
            plugin(plugin_id,
                   plugin_id,
                   "0.1",
                   main=name,
                   build_dir=build_dir,
                   bundle_jython=bundle,
                   task=task)

            jar = zipfile.ZipFile(jar_loc)
            entries = map(lambda z: z.filename + os.linesep, jar.filelist)
            jar.close()
            if gen:
                print("generating txt file of entries")
                with open(name+".txt", 'w') as f:
                    f.writelines(entries)
            else:
                with open(name+".txt") as f:
                    expected = f.readlines()
                print("diffing entries in jars")
                for line in d.compare(expected, entries):
                    if not line.startswith(" "):
                        print(line)

for i in range(1, len(sys.argv)):
    dest = sys.argv[i]
    for jar in jar_locations:
        shutil.copy(jar, dest)
