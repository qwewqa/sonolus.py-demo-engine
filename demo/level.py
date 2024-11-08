from math import sin

from sonolus.script.level import LevelData, BpmChange, Level

from demo.play.init import Init
from demo.play.note import Note
from demo.play.stage import Stage
from demo.preview.bar_line import TimescaleChange


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
            TimescaleChange(beat=298, timescale=1.1),
            TimescaleChange(beat=306, timescale=1.2),
            TimescaleChange(beat=314, timescale=1.3),
            TimescaleChange(beat=322, timescale=1.4),
            TimescaleChange(beat=330, timescale=1.5),
            TimescaleChange(beat=338, timescale=1.6),
            TimescaleChange(beat=346, timescale=1),
            *(Note(beat=beat, x=sin(beat / 2) / 2) for beat in range(2, 581)),
        ],
    ),
)
