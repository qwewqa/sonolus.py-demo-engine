from sonolus.script.archetype import PreviewArchetype, StandardImport, imported
from sonolus.script.graphics import Rect
from sonolus.script.timing import beat_to_time
from sonolus.script.vec import Vec2

from demo.common.options import Options
from demo.common.skin import Skin
from demo.preview.chart import HEIGHT_SCALE, Chart, pos_at_time


class Note(PreviewArchetype):
    beat: StandardImport.BEAT
    x: float = imported()

    def preprocess(self):
        Chart.beats = max(Chart.beats, self.beat)
        Chart.duration = max(Chart.duration, beat_to_time(self.beat))

    def render(self):
        time = beat_to_time(self.beat)
        pos = pos_at_time(time) + Vec2(self.x, 0)

        layout = Rect.from_center(
            pos, Vec2(Options.note_size, Options.note_size * HEIGHT_SCALE)
        )
        z = 1000 - time

        Skin.note.draw(layout, z=z)
