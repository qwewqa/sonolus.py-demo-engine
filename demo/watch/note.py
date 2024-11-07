from sonolus.script.archetype import (
    WatchArchetype,
    StandardImport,
    imported,
    entity_memory,
)
from sonolus.script.bucket import Judgment
from sonolus.script.graphics import Rect
from sonolus.script.interval import Interval
from sonolus.script.runtime import is_replay, scaled_time, is_skip
from sonolus.script.timing import beat_to_time, time_to_scaled_time, beat_to_bpm

from demo.common.buckets import Buckets
from demo.common.effect import Effects
from demo.common.particle import Particles
from demo.common.skin import Skin
from demo.watch.config import Config


class Note(WatchArchetype):
    is_scored = True

    beat: StandardImport.Beat
    judgment: StandardImport.Judgment
    accuracy: StandardImport.Accuracy
    x: float = imported()

    initialized: bool = entity_memory()
    visual_time: Interval = entity_memory()
    z: float = entity_memory()

    def preprocess(self):
        self.target_time = beat_to_time(self.beat)
        self.visual_time.end = time_to_scaled_time(self.target_time)
        self.visual_time.start = self.visual_time.end - 120 / beat_to_bpm(self.beat)

        if is_replay():
            hit_time = self.target_time + self.accuracy
        else:
            hit_time = self.target_time
            self.judgment = Judgment.PERFECT
            self.accuracy = 0

        match self.judgment:
            case Judgment.PERFECT:
                Effects.perfect.schedule(hit_time, 0.02)
            case Judgment.GREAT:
                Effects.great.schedule(hit_time, 0.02)
            case Judgment.GOOD:
                Effects.good.schedule(hit_time, 0.02)

        self.result.bucket @= Buckets.note
        self.result.bucket_value = self.accuracy * 1000

    def spawn_time(self) -> float:
        return self.visual_time.start

    def despawn_time(self) -> float:
        return self.visual_time.end

    def initialize(self):
        if self.initialized:
            return

        self.initialized = True
        self.z = 1000 - self.target_time

    def update_parallel(self):
        y = self.visual_time.unlerp(scaled_time())
        layout = Rect.from_center(
            x=self.x, y=y, w=Config.note_radius, h=-Config.note_radius
        )
        Skin.note.draw(layout, z=self.z)

    def terminate(self):
        if is_skip():
            return
        if is_replay() and self.judgment == Judgment.MISS:
            return

        particle_layout = Rect.from_center(
            x=self.x, y=1, w=2 * Config.note_radius, h=-2 * Config.note_radius
        )

        Particles.note.spawn(particle_layout, duration=0.3)