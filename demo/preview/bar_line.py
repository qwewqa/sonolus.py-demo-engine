from sonolus.script.archetype import (
    PreviewArchetype,
    StandardImport,
    StandardArchetypeName,
)
from sonolus.script.preview import PrintFormat, PrintColor
from sonolus.script.timing import beat_to_time

from demo.common.skin import Skin
from demo.preview.chart import draw_line, print_at_time


class BpmChange(PreviewArchetype):
    name = StandardArchetypeName.BPM_CHANGE

    beat: StandardImport.BEAT
    bpm: StandardImport.BPM

    def render(self):
        draw_line(Skin.bpm_change_line, self.beat, a=0.5)
        print_at_time(
            self.bpm,
            beat_to_time(self.beat),
            fmt=PrintFormat.BPM,
            color=PrintColor.PURPLE,
            side="right",
        )


class TimescaleChange(PreviewArchetype):
    name = StandardArchetypeName.TIMESCALE_CHANGE

    beat: StandardImport.BEAT
    timescale: StandardImport.TIMESCALE

    def render(self):
        draw_line(Skin.timescale_change_line, self.beat, a=0.5)
        print_at_time(
            self.timescale,
            beat_to_time(self.beat),
            fmt=PrintFormat.TIMESCALE,
            color=PrintColor.YELLOW,
            side="left",
        )
