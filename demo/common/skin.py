from sonolus.script.sprite import skin, StandardSprite


@skin
class Skin:
    judge_line: StandardSprite.JUDGMENT_LINE
    note: StandardSprite.NOTE_HEAD_CYAN

    stage_middle: StandardSprite.STAGE_MIDDLE
    stage_left_border: StandardSprite.STAGE_LEFT_BORDER
    stage_right_border: StandardSprite.STAGE_RIGHT_BORDER

    beat_line: StandardSprite.GRID_NEUTRAL
    bpm_change_line: StandardSprite.GRID_PURPLE
    timescale_change_line: StandardSprite.GRID_YELLOW
