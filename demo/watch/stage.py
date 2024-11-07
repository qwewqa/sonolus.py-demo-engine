from sonolus.script.archetype import WatchArchetype
from sonolus.script.graphics import Rect

from demo.common.skin import Skin
from demo.watch.config import Config


class Stage(WatchArchetype):
    def spawn_time(self) -> float:
        return -1e8

    def despawn_time(self) -> float:
        return 1e8

    def update_parallel(self):
        layout = Rect(
            l=Config.judge_line_l,
            r=Config.judge_line_r,
            t=1 - Config.note_radius / 4,
            b=1 + Config.note_radius / 4,
        )
        Skin.judge_line.draw(layout, z=0, a=1)
