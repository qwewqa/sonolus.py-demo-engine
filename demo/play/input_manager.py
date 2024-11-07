from sonolus.script.archetype import PlayArchetype
from sonolus.script.containers import VarArray
from sonolus.script.globals import level_memory
from sonolus.script.runtime import Touch

used_touch_ids = level_memory(VarArray[int, 16])


def touch_is_used(touch: Touch):
    return touch.id in used_touch_ids


def mark_touch_used(touch: Touch):
    used_touch_ids.set_add(touch.id)


class InputManager(PlayArchetype):
    def touch(self):
        used_touch_ids.clear()
