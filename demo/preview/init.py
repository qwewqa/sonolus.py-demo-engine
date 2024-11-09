from sonolus.script.archetype import PreviewArchetype
from sonolus.script.runtime import (
    screen,
    preview_ui as ui,
    preview_ui_configs as ui_configs,
    set_skin_transform,
)
from sonolus.script.transform import Transform2d
from sonolus.script.vec import Vec2

from demo.preview.chart import PANEL_WIDTH, PANEL_HEIGHT


class Init(PreviewArchetype):
    def preprocess(self):
        init_ui()

        transform = (
            Transform2d.new()
            .translate(Vec2(PANEL_WIDTH / 2, 0))
            .scale(Vec2(screen().h / 20, screen().h / PANEL_HEIGHT))
            .translate(screen().bl)
        )
        set_skin_transform(transform)


def init_ui():
    ui.menu.update(
        anchor=screen().tl + Vec2(0.05, -0.05),
        pivot=Vec2(0, 1),
        dimensions=Vec2(0.15, 0.15) * ui_configs.menu.scale,
        rotation=0,
        alpha=ui_configs.menu.alpha,
        background=True,
    )
    ui.progress.update(
        anchor=screen().bl + Vec2(0.05, 0.05),
        pivot=Vec2(0, 0),
        dimensions=Vec2(screen().w - 0.1, y=0.15 * ui_configs.progress.scale),
        rotation=0,
        alpha=ui_configs.progress.alpha,
        background=True,
    )
