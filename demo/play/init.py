from sonolus.script.archetype import PlayArchetype, archetype_life_of
from sonolus.script.runtime import (
    HorizontalAlign,
    level_life,
    level_score,
    screen,
    set_particle_transform,
    set_skin_transform,
)
from sonolus.script.runtime import (
    play_ui as ui,
)
from sonolus.script.runtime import (
    play_ui_configs as ui_configs,
)
from sonolus.script.transform import Transform2d
from sonolus.script.vec import Vec2

from demo.common.buckets import Buckets, note_window
from demo.common.options import Options
from demo.play.config import Config
from demo.play.input_manager import InputManager
from demo.play.note import Note


class Init(PlayArchetype):
    def spawn_order(self) -> float:
        return 0

    def preprocess(self):
        self.init_buckets()
        self.init_score()
        self.init_life()
        self.init_ui()

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

    def update_sequential(self):
        InputManager.spawn()
        self.despawn = True

    @staticmethod
    def init_ui():
        ui.menu.update(
            anchor=screen().tl + Vec2(0.05, -0.05),
            pivot=Vec2(0, 1),
            dimensions=Vec2(0.15, 0.15) * ui_configs.menu.scale,
            rotation=0,
            alpha=ui_configs.menu.alpha,
            horizontal_align=HorizontalAlign.CENTER,
            background=True,
        )
        ui.judgment.update(
            anchor=Vec2(0, -0.4),
            pivot=Vec2(0.5, 0),
            dimensions=Vec2(0, 0.15) * ui_configs.judgment.scale,
            rotation=0,
            alpha=ui_configs.judgment.alpha,
            horizontal_align=HorizontalAlign.CENTER,
            background=False,
        )
        ui.combo_value.update(
            anchor=Vec2(screen().r * 0.7, 0),
            pivot=Vec2(0.5, 0),
            dimensions=Vec2(0, 0.2) * ui_configs.combo.scale,
            rotation=0,
            alpha=ui_configs.combo.alpha,
            horizontal_align=HorizontalAlign.CENTER,
            background=False,
        )
        ui.combo_text.update(
            anchor=Vec2(screen().r * 0.7, 0),
            pivot=Vec2(0.5, 1),
            dimensions=Vec2(0, 0.12) * ui_configs.combo.scale,
            rotation=0,
            alpha=ui_configs.combo.alpha,
            horizontal_align=HorizontalAlign.CENTER,
            background=False,
        )
        ui.primary_metric_bar.update(
            anchor=screen().tr - Vec2(0.05, 0.05),
            pivot=Vec2(1, 1),
            dimensions=Vec2(0.75, 0.15) * ui_configs.primary_metric.scale,
            rotation=0,
            alpha=ui_configs.primary_metric.alpha,
            horizontal_align=HorizontalAlign.LEFT,
            background=True,
        )
        ui.primary_metric_value.update(
            anchor=screen().tr
            - Vec2(0.05, 0.05)
            - (Vec2(0.035, 0.035) * ui_configs.primary_metric.scale),
            pivot=Vec2(1, 1),
            dimensions=Vec2(0, 0.08) * ui_configs.primary_metric.scale,
            rotation=0,
            alpha=ui_configs.primary_metric.alpha,
            horizontal_align=HorizontalAlign.RIGHT,
            background=False,
        )
        ui.secondary_metric_bar.update(
            anchor=screen().tr
            - Vec2(0.05, 0.05)
            - (Vec2(0, 0.15) * ui_configs.primary_metric.scale)
            - Vec2(0, 0.05),
            pivot=Vec2(1, 1),
            dimensions=Vec2(0.75, 0.15) * ui_configs.secondary_metric.scale,
            rotation=0,
            alpha=ui_configs.secondary_metric.alpha,
            horizontal_align=HorizontalAlign.LEFT,
            background=True,
        )
        ui.secondary_metric_value.update(
            anchor=screen().tr
            - Vec2(0.05, 0.05)
            - (Vec2(0, 0.15) * ui_configs.primary_metric.scale)
            - Vec2(0, 0.05)
            - (Vec2(0.035, 0.035) * ui_configs.secondary_metric.scale),
            pivot=Vec2(1, 1),
            dimensions=Vec2(0, 0.08) * ui_configs.secondary_metric.scale,
            rotation=0,
            alpha=ui_configs.secondary_metric.alpha,
            horizontal_align=HorizontalAlign.RIGHT,
            background=False,
        )

    @staticmethod
    def init_buckets():
        Buckets.note.window @= note_window * 1000

    @staticmethod
    def init_score():
        level_score().update(
            perfect_multiplier=1,
            great_multiplier=0.75,
            good_multiplier=0.5,
            consecutive_great_multiplier=0.01,
            consecutive_great_step=10,
            consecutive_great_cap=50,
        )

    @staticmethod
    def init_life():
        level_life().update(
            consecutive_perfect_increment=50,
            consecutive_perfect_step=10,
        )

        archetype_life_of(Note).update(
            perfect_increment=10,
            miss_increment=-100,
        )
