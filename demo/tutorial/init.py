from sonolus.script.runtime import (
    screen,
    set_particle_transform,
    set_skin_transform,
)
from sonolus.script.runtime import (
    tutorial_ui as ui,
)
from sonolus.script.runtime import (
    tutorial_ui_configs as ui_configs,
)
from sonolus.script.transform import Transform2d
from sonolus.script.vec import Vec2

from demo.common.options import Options
from demo.tutorial.config import Config
from demo.tutorial.navigate import State


def preprocess():
    init_ui()

    note_radius = 0.2 * Options.note_size
    judge_line_y = -0.6

    t = screen().t + note_radius
    b = judge_line_y
    h = t - b

    transform = Transform2d.new().scale(Vec2(h, -h)).translate(Vec2(0, t))

    set_skin_transform(transform)
    set_particle_transform(transform)

    Config.judge_line_l = screen().l / h
    Config.judge_line_r = screen().r / h

    Config.note_radius = note_radius / h

    State.is_new = True


def init_ui():
    ui.menu.update(
        anchor=screen().tl + Vec2(0.05, -0.05),
        pivot=Vec2(0, 1),
        dimensions=Vec2(0.15, 0.15) * ui_configs.menu.scale,
        rotation=0,
        alpha=ui_configs.menu.alpha,
        background=True,
    )
    ui.previous.update(
        anchor=Vec2(screen().l + 0.05, 0),
        pivot=Vec2(0, 0.5),
        dimensions=Vec2(0.15, 0.15) * ui_configs.navigation.scale,
        rotation=0,
        alpha=ui_configs.navigation.alpha,
        background=True,
    )
    ui.next.update(
        anchor=Vec2(screen().r - 0.05, 0),
        pivot=Vec2(1, 0.5),
        dimensions=Vec2(0.15, 0.15) * ui_configs.navigation.scale,
        rotation=0,
        alpha=ui_configs.navigation.alpha,
        background=True,
    )
    ui.instruction.update(
        anchor=Vec2(0, 0),
        pivot=Vec2(0.5, 0.5),
        dimensions=Vec2(1.2, 0.15) * ui_configs.instruction.scale,
        rotation=0,
        alpha=ui_configs.instruction.alpha,
        background=True,
    )
