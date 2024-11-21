from sonolus.script.archetype import PlayArchetype, callback
from sonolus.script.graphics import Rect
from sonolus.script.runtime import touches

from demo.common.effect import Effects
from demo.common.skin import Skin
from demo.play.config import Config
from demo.play.init import Init
from demo.play.input_manager import touch_is_used


class Stage(PlayArchetype):
    def spawn_order(self) -> int:
        return 1

    def should_spawn(self) -> bool:
        return Init.at(0).is_despawned

    @callback(order=2)
    def touch(self):
        for touch in touches():
            if not touch.started:
                continue
            if touch_is_used(touch):
                continue

            Effects.stage.play(0.02)
            return

    def update_parallel(self):
        layout = Rect(
            l=Config.judge_line_l,
            r=Config.judge_line_r,
            t=1 - Config.note_radius / 4,
            b=1 + Config.note_radius / 4,
        )
        Skin.judge_line.draw(layout, z=0, a=1 if touches().size() > 0 else 0.5)
