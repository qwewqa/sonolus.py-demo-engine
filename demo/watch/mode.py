from sonolus.script.engine import WatchMode

from demo.common.buckets import Buckets
from demo.common.effect import Effects
from demo.common.particle import Particles
from demo.common.skin import Skin
from demo.watch.init import Init
from demo.watch.note import Note
from demo.watch.stage import Stage
from demo.watch.update_spawn import update_spawn

watch_mode = WatchMode(
    archetypes=[Init, Stage, Note],
    skin=Skin,
    effects=Effects,
    particles=Particles,
    buckets=Buckets,
    update_spawn=update_spawn,
)
