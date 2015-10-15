import os

from sponge import *

p = plugin("example1",
           "Example Plugin",
           "0.1",
           main="main")

# installs the jar in Sponge sub-module run directory
dirname = os.path.dirname
join = os.path.join
sponge_root = join(
    dirname(
        dirname(
            dirname(os.path.abspath(__file__)))), "Sponge")
if os.path.exists(sponge_root):
    game_directory = join(sponge_root, "run")
    if not os.path.exists(game_directory):
        os.mkdir(game_directory)
    p.install(game_directory)
