from sonolus.script.bucket import buckets, bucket, bucket_sprite, JudgmentWindow, Bucket
from sonolus.script.interval import Interval
from sonolus.script.text import StandardText

from demo.common.skin import Skin


@buckets
class Buckets:
    note: Bucket = bucket(
        sprites=[
            bucket_sprite(
                sprite=Skin.note,
                x=0,
                y=0,
                w=2,
                h=2,
            )
        ],
        unit=StandardText.MillisecondUnit,
    )


note_window = JudgmentWindow(
    perfect=Interval(-0.05, 0.05),
    great=Interval(-0.1, 0.1),
    good=Interval(-0.15, 0.15),
)
