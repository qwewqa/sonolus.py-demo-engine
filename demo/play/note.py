from sonolus.script.archetype import (
    PlayArchetype,
    StandardImport,
    entity_memory,
    callback,
    imported,
)
from sonolus.script.bucket import Judgment
from sonolus.script.graphics import Rect
from sonolus.script.interval import Interval
from sonolus.script.runtime import time, touches, scaled_time, input_offset
from sonolus.script.timing import beat_to_time, time_to_scaled_time, beat_to_bpm
from sonolus.script.vec import Vec2

from demo.common.buckets import note_window, Buckets
from demo.play.config import Config
from demo.common.effect import Effects
from demo.play.input_manager import touch_is_used, mark_touch_used
from demo.common.particle import Particles
from demo.common.skin import Skin


class Note(PlayArchetype):
    is_scored = True

    beat: StandardImport.BEAT
    x: float = imported()

    target_time: float = entity_memory()
    visual_time: Interval = entity_memory()
    spawn_time: float = entity_memory()
    input_time: Interval = entity_memory()
    z: float = entity_memory()

    def preprocess(self):
        self.target_time = beat_to_time(self.beat)
        self.visual_time.end = time_to_scaled_time(self.target_time)
        self.visual_time.start = self.visual_time.end - 120 / beat_to_bpm(self.beat)
        self.spawn_time = self.visual_time.start

    def spawn_order(self) -> float:
        return 1000 + self.spawn_time

    def should_spawn(self) -> bool:
        return scaled_time() >= self.spawn_time

    def initialize(self):
        self.input_time = note_window.good + self.target_time + input_offset()
        self.z = 1000 - self.target_time
        self.result.accuracy = note_window.good.end

    @callback(order=1)
    def touch(self):
        if time() not in self.input_time:
            return

        for touch in touches():
            if not touch.started or touch_is_used(touch):
                continue

            mark_touch_used(touch)

            self.result.judgment = note_window.judge(touch.start_time, self.target_time)
            self.result.accuracy = touch.start_time - self.target_time

            self.result.bucket @= Buckets.note
            self.result.bucket_value = self.result.accuracy * 1000

            match self.result.judgment:
                case Judgment.PERFECT:
                    Effects.perfect.play(0.02)
                case Judgment.GREAT:
                    Effects.great.play(0.02)
                case Judgment.GOOD:
                    Effects.good.play(0.02)

            particle_layout = Rect.from_center(
                Vec2(self.x, 1), Vec2(4 * Config.note_radius, -4 * Config.note_radius)
            )

            Particles.note.spawn(particle_layout, duration=0.3)

            self.despawn = True
            return

    def update_parallel(self):
        if time() > self.input_time.end:
            self.despawn = True
        if self.despawn:
            return

        y = self.visual_time.unlerp(scaled_time())
        layout = Rect.from_center(
            Vec2(self.x, y), Vec2(2 * Config.note_radius, -2 * Config.note_radius)
        )
        Skin.note.draw(layout, z=self.z)
