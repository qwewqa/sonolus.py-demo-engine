from sonolus.script.engine import PlayMode

from demo.common.buckets import Buckets
from demo.common.effect import Effects
from demo.play.init import Init
from demo.play.input_manager import InputManager
from demo.play.note import Note
from demo.common.particle import Particles
from demo.common.skin import Skin
from demo.play.stage import Stage


play_mode = PlayMode(
    archetypes=[Init, Stage, InputManager, Note],
    skin=Skin,
    effects=Effects,
    particles=Particles,
    buckets=Buckets,
)
