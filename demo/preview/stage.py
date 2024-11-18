from sonolus.script.archetype import PreviewArchetype, callback
from sonolus.script.graphics import Rect
from sonolus.script.math import floor
from sonolus.script.print import PrintFormat, PrintColor
from sonolus.script.runtime import canvas, ScrollDirection, screen
from sonolus.script.timing import beat_to_time
from sonolus.script.vec import Vec2

from demo.common.skin import Skin
from demo.preview.chart import (
    Chart,
    PANEL_WIDTH,
    panel_count,
    PANEL_HEIGHT,
    draw_line,
    print_at_time,
)


class Stage(PreviewArchetype):
    @callback(order=1)
    def preprocess(self):
        canvas().scroll_direction = ScrollDirection.LEFT_TO_RIGHT
        canvas().size = panel_count() * PANEL_WIDTH * screen().h / 20

    def render(self):
        self.render_panels()
        self.render_beats()
        self.print_times()
        self.print_measures()

    @staticmethod
    def render_panels():
        for i in range(panel_count()):
            x = i * PANEL_WIDTH

            b = 0
            t = PANEL_HEIGHT

            Skin.stage_middle.draw(
                Rect(l=-1.5, r=1.5, b=b, t=t).translate(Vec2(x, 0)),
                z=0,
            )
            Skin.stage_left_border.draw(
                Rect(l=-1.75, r=-1.5, b=b, t=t).translate(Vec2(x, 0)),
                z=0,
            )
            Skin.stage_right_border.draw(
                Rect(l=1.5, r=1.75, b=b, t=t).translate(Vec2(x, 0)),
                z=0,
            )

    @staticmethod
    def render_beats():
        for i in range(floor(Chart.beats) + 1):
            draw_line(Skin.beat_line, beat=i, a=0.25 if i % 4 == 0 else 0.125)

    @staticmethod
    def print_times():
        for i in range(floor(Chart.duration) + 1):
            print_at_time(
                i,
                i,
                fmt=PrintFormat.TIME,
                decimal_places=0,
                color=PrintColor.NEUTRAL,
                side="left",
            )

    @staticmethod
    def print_measures():
        for i in range(0, floor(Chart.beats) + 1, 4):
            print_at_time(
                i / 4 + 1,
                beat_to_time(i),
                fmt=PrintFormat.MEASURE_COUNT,
                decimal_places=0,
                color=PrintColor.NEUTRAL,
                side="right",
            )
