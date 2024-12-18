from demo.tutorial.navigate import Segment, State, current_segment, is_new_state
from demo.tutorial.note import note_fall, note_frozen, note_hit, note_intro
from demo.tutorial.stage import draw_stage


def update():
    draw_stage()
    was_new = is_new_state()
    match current_segment():
        case Segment.NOTE_INTRO:
            note_intro()
        case Segment.NOTE_FALL:
            note_fall()
        case Segment.NOTE_FROZEN:
            note_frozen()
        case Segment.NOTE_HIT:
            note_hit()
    if was_new:
        State.is_new = False
