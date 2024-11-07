from sonolus.script.options import options, slider_option
from sonolus.script.text import StandardText


@options
class Options:
    speed: float = slider_option(
        name=StandardText.Speed,
        standard=True,
        default=1,
        min=0.5,
        max=2,
        step=0.05,
        unit=StandardText.PercentageUnit,
    )
    note_size: float = slider_option(
        name=StandardText.NoteSize,
        default=1,
        min=0.1,
        max=2,
        step=0.05,
        unit=StandardText.PercentageUnit,
    )
