from sonolus.script.graphics import Rect

from demo.common.skin import Skin
from demo.tutorial.config import Config


def draw_stage():
    layout = Rect(
        l=Config.judge_line_l,
        r=Config.judge_line_r,
        t=1 - Config.note_radius / 4,
        b=1 + Config.note_radius / 4,
    )
    Skin.judge_line.draw(layout, z=0, a=1)
