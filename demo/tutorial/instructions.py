from sonolus.script.instruction import (
    instructions,
    StandardInstruction,
    instruction_icons,
    StandardInstructionIcon,
)


@instructions
class Instructions:
    tap: StandardInstruction.TAP


@instruction_icons
class InstructionIcons:
    hand: StandardInstructionIcon.HAND
