from sonolus.script.archetype import archetype_life_of, WatchArchetype
from sonolus.script.runtime import (
    runtime_ui,
    runtime_ui_configs,
    HorizontalAlign,
    set_skin_transform,
    set_particle_transform,
    screen,
    level_life,
    level_score,
)
from sonolus.script.transform import Transform2d
from sonolus.script.vec import Vec2

from demo.common.buckets import Buckets, note_window
from demo.watch.config import Config
from demo.watch.note import Note


class Init(WatchArchetype):
    def preprocess(self):
        init_buckets()
        init_score()
        init_life()
        init_ui()

        note_radius = 0.2
        judge_line_y = -0.6

        t = screen().t + note_radius
        b = judge_line_y
        h = t - b

        transform = Transform2d.new().scale(h, -h).translate(0, t)

        set_skin_transform(transform)
        set_particle_transform(transform)

        Config.judge_line_l = screen().l / h
        Config.judge_line_r = screen().r / h

        Config.note_radius = note_radius / h


def init_ui():
    runtime_ui.menu.update(
        anchor=screen().tl + Vec2(0.05, -0.05),
        pivot=Vec2(0, 1),
        dimensions=Vec2(0.15, 0.15) * runtime_ui_configs.menu.scale,
        rotation=0,
        alpha=runtime_ui_configs.menu.alpha,
        horizontal_align=HorizontalAlign.CENTER,
        background=True,
    )
    runtime_ui.judgment.update(
        anchor=Vec2(0, -0.4),
        pivot=Vec2(0.5, 0),
        dimensions=Vec2(0, 0.15) * runtime_ui_configs.judgment.scale,
        rotation=0,
        alpha=runtime_ui_configs.judgment.alpha,
        horizontal_align=HorizontalAlign.CENTER,
        background=False,
    )
    runtime_ui.combo_value.update(
        anchor=Vec2(screen().r * 0.7, 0),
        pivot=Vec2(0.5, 0),
        dimensions=Vec2(0, 0.2) * runtime_ui_configs.combo.scale,
        rotation=0,
        alpha=runtime_ui_configs.combo.alpha,
        horizontal_align=HorizontalAlign.CENTER,
        background=False,
    )
    runtime_ui.combo_text.update(
        anchor=Vec2(screen().r * 0.7, 0),
        pivot=Vec2(0.5, 1),
        dimensions=Vec2(0, 0.12) * runtime_ui_configs.combo.scale,
        rotation=0,
        alpha=runtime_ui_configs.combo.alpha,
        horizontal_align=HorizontalAlign.CENTER,
        background=False,
    )
    runtime_ui.primary_metric_bar.update(
        anchor=screen().tr - Vec2(0.05, 0.05),
        pivot=Vec2(1, 1),
        dimensions=Vec2(0.75, 0.15) * runtime_ui_configs.primary_metric.scale,
        rotation=0,
        alpha=runtime_ui_configs.primary_metric.alpha,
        horizontal_align=HorizontalAlign.LEFT,
        background=True,
    )
    runtime_ui.primary_metric_value.update(
        anchor=screen().tr
        - Vec2(0.05, 0.05)
        - (Vec2(0.035, 0.035) * runtime_ui_configs.primary_metric.scale),
        pivot=Vec2(1, 1),
        dimensions=Vec2(0, 0.08) * runtime_ui_configs.primary_metric.scale,
        rotation=0,
        alpha=runtime_ui_configs.primary_metric.alpha,
        horizontal_align=HorizontalAlign.RIGHT,
        background=False,
    )
    runtime_ui.secondary_metric_bar.update(
        anchor=screen().tr
        - Vec2(0.05, 0.05)
        - (Vec2(0, 0.15) * runtime_ui_configs.primary_metric.scale)
        - Vec2(0, 0.05),
        pivot=Vec2(1, 1),
        dimensions=Vec2(0.75, 0.15) * runtime_ui_configs.secondary_metric.scale,
        rotation=0,
        alpha=runtime_ui_configs.secondary_metric.alpha,
        horizontal_align=HorizontalAlign.LEFT,
        background=True,
    )
    runtime_ui.secondary_metric_value.update(
        anchor=screen().tr
        - Vec2(0.05, 0.05)
        - (Vec2(0, 0.15) * runtime_ui_configs.primary_metric.scale)
        - Vec2(0, 0.05)
        - (Vec2(0.035, 0.035) * runtime_ui_configs.secondary_metric.scale),
        pivot=Vec2(1, 1),
        dimensions=Vec2(0, 0.08) * runtime_ui_configs.secondary_metric.scale,
        rotation=0,
        alpha=runtime_ui_configs.secondary_metric.alpha,
        horizontal_align=HorizontalAlign.RIGHT,
        background=False,
    )
    runtime_ui.progress.update(
        anchor=screen().bl + Vec2(0.05, 0.05),
        pivot=Vec2(0, 0),
        dimensions=Vec2(screen().w - 0.1, y=0.15 * runtime_ui_configs.progress.scale),
        rotation=0,
        alpha=runtime_ui_configs.progress.alpha,
        horizontal_align=HorizontalAlign.CENTER,
        background=True,
    )


def init_buckets():
    Buckets.note.window @= note_window * 1000


def init_score():
    level_score().update(
        perfect_multiplier=1,
        great_multiplier=0.75,
        good_multiplier=0.5,
        consecutive_great_multiplier=0.01,
        consecutive_great_step=10,
        consecutive_great_cap=50,
    )


def init_life():
    level_life().update(
        consecutive_perfect_increment=50,
        consecutive_perfect_step=10,
    )

    archetype_life_of(Note).update(
        perfect_increment=10,
        miss_increment=-100,
    )
