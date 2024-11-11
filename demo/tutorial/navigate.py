from enum import IntEnum

from sonolus.script.array import Array
from sonolus.script.globals import level_memory
from sonolus.script.instruction import clear_instruction
from sonolus.script.runtime import navigation_direction, time


class Segment(IntEnum):
    NOTE_INTRO = 0
    NOTE_FALL = 1
    NOTE_FROZEN = 2
    NOTE_HIT = 3


SEGMENT_COUNT = 4

navigation_targets = Array(
    Segment.NOTE_INTRO,
    Segment.NOTE_FROZEN,
)


@level_memory
class State:
    segment: int
    segment_start_time: float
    is_new: bool


def current_segment():
    return State.segment


def segment_time():
    return time() - State.segment_start_time


def advance_state():
    State.segment += 1
    if State.segment >= SEGMENT_COUNT:
        State.segment = 0
    State.is_new = True
    State.segment_start_time = time()
    clear_instruction()


def is_new_state():
    return State.is_new


def navigate():
    State.is_new = True
    State.segment_start_time = time()
    direction = navigation_direction()
    clear_instruction()
    while True:
        State.segment += direction
        if State.segment < 0:
            State.segment = SEGMENT_COUNT - 1
        elif State.segment >= SEGMENT_COUNT:
            State.segment = 0
        if State.segment in navigation_targets:
            break
