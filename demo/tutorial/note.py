from math import pi

from sonolus.script.interval import remap_clamped
from sonolus.script.quad import Rect
from sonolus.script.runtime import (
    tutorial_ui_configs as ui_configs,
)
from sonolus.script.vec import Vec2

from demo.common.effect import Effects
from demo.common.particle import Particles
from demo.common.skin import Skin
from demo.tutorial.config import Config
from demo.tutorial.instructions import InstructionIcons, Instructions
from demo.tutorial.navigate import advance_state, is_new_state, segment_time


def draw_note(y: float):
    layout = Rect.from_center(
        Vec2(0, y), Vec2(2 * Config.note_radius, -2 * Config.note_radius)
    )
    Skin.note.draw(layout, z=1000)


def note_intro():
    end_time = 1

    a = remap_clamped(0, 0.25, 0, 1, segment_time())
    layout = Rect.from_center(
        Vec2(0, 0.5), Vec2(4 * Config.note_radius, -4 * Config.note_radius)
    )
    Skin.note.draw(layout, z=1000, a=a)
    if segment_time() >= end_time:
        advance_state()


def note_fall():
    end_time = 2

    y = remap_clamped(0, end_time, 0, 1, segment_time())
    draw_note(y)
    if segment_time() >= end_time:
        advance_state()


def note_frozen():
    end_time = 4

    if is_new_state():
        Instructions.tap.show()
    draw_note(1)
    angle = remap_clamped(0.25, 0.75, pi / 6, pi / 3, segment_time() % 1)
    a = (
        remap_clamped(0.75, 1, 1, 0, segment_time() % 1)
        if segment_time() < end_time
        else 0
    )
    position = Vec2(0, -1).rotate(pi / 3) * (
        0.25 * ui_configs.instruction.scale
    ) + Vec2(0, -0.6)
    InstructionIcons.hand.paint(
        position=Vec2(0, 1).rotate(angle) * 0.25 * ui_configs.instruction.scale
        + position,
        size=0.25 * ui_configs.instruction.scale,
        rotation=(180 * angle) / pi,
        z=0,
        a=a * ui_configs.instruction.alpha,
    )
    if segment_time() >= end_time:
        advance_state()


def note_hit():
    end_time = 1

    if is_new_state():
        particle_layout = Rect.from_center(
            Vec2(0, 1), Vec2(4 * Config.note_radius, -4 * Config.note_radius)
        )
        Particles.note.spawn(particle_layout, duration=0.3)
        Effects.perfect.play(0)
    if segment_time() >= end_time:
        advance_state()
