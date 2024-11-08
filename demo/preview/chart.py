from typing import Literal

from sonolus.script.globals import level_data
from sonolus.script.graphics import Rect
from sonolus.script.interval import Interval
from sonolus.script.math import ceil
from sonolus.script.preview import PrintFormat, PrintColor, print_number
from sonolus.script.runtime import skin_transform, screen, HorizontalAlign
from sonolus.script.sprite import Sprite
from sonolus.script.timing import beat_to_time
from sonolus.script.vec import Vec2

PANEL_WIDTH = 7
PANEL_HEIGHT = 2
HEIGHT_SCALE = PANEL_HEIGHT / 20


@level_data
class Chart:
    beats: int
    duration: float


def panel_count():
    return ceil(Chart.duration / PANEL_HEIGHT)


def x_at_time(time: float):
    return (time // PANEL_HEIGHT) * PANEL_WIDTH


def y_at_time(time: float):
    return time % PANEL_HEIGHT


def pos_at_time(time: float):
    return Vec2(x_at_time(time), y_at_time(time))


def print_at_time(
    value: float,
    time: float,
    *,
    fmt: PrintFormat,
    decimal_places: int = -1,
    color: PrintColor,
    side: Literal["left", "right"],
):
    print_number(
        value=value,
        fmt=fmt,
        decimal_places=decimal_places,
        anchor=_get_anchor(
            pos_at_time(time) + Vec2(-1.5 if side == "left" else 1.5, 0)
        ),
        pivot=Vec2(1 if side == "left" else 0, 0.5),
        dimensions=Vec2(screen().h / 10, screen().h / 20),
        color=color,
        horizontal_align=HorizontalAlign.RIGHT
        if side == "left"
        else HorizontalAlign.LEFT,
        background=False,
    )


def _get_anchor(pos: Vec2):
    anchor = skin_transform().transform_vec(pos)
    anchor.y = Interval(screen().b, screen().t).shrink(screen().h / 40).clamp(anchor.y)
    return anchor


def draw_line(sprite: Sprite, beat: float, a: float = 1):
    pos = pos_at_time(beat_to_time(beat))
    sprite.draw(
        Rect.from_center(pos, Vec2(3, 0.01)),
        z=1,
        a=a,
    )
