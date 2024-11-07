from math import sin

from sonolus.script.level import LevelData, BpmChange, Level

from demo.play.init import Init
from demo.play.note import Note
from demo.play.stage import Stage

demo_level = Level(
    name="demo",
    title="Demo Level",
    bgm="bgm.mp3",
    data=LevelData(
        bgm_offset=0,
        entities=[
            Init(),
            Stage(),
            BpmChange(beat=0, bpm=87),
            BpmChange(beat=2, bpm=87),
            BpmChange(beat=34, bpm=174),
            *(Note(beat=beat / 2, x=sin(beat / 2) / 2) for beat in range(0, 256)),
        ],
    ),
)
