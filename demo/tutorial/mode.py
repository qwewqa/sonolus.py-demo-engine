from sonolus.script.engine import TutorialMode

from demo.common.effect import Effects
from demo.common.particle import Particles
from demo.common.skin import Skin
from demo.tutorial.init import preprocess
from demo.tutorial.instructions import Instructions, InstructionIcons
from demo.tutorial.navigate import navigate
from demo.tutorial.update import update

tutorial_mode = TutorialMode(
    skin=Skin,
    effects=Effects,
    particles=Particles,
    instructions=Instructions,
    instruction_icons=InstructionIcons,
    preprocess=preprocess,
    navigate=navigate,
    update=update,
)
