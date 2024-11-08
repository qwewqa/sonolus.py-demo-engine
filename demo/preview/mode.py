from sonolus.script.engine import PreviewMode

from demo.common.skin import Skin
from demo.preview.bar_line import BpmChange, TimescaleChange
from demo.preview.init import Init
from demo.preview.note import Note
from demo.preview.stage import Stage

preview_mode = PreviewMode(
    archetypes=[BpmChange, TimescaleChange, Init, Stage, Note],
    skin=Skin,
)
