from sonolus.script.engine import Engine, EngineData
from sonolus.script.project import Project

from demo.common.options import Options
from demo.common.ui import ui_config
from demo.level import demo_level
from demo.play.mode import play_mode
from demo.preview.mode import preview_mode
from demo.tutorial.mode import tutorial_mode
from demo.watch.mode import watch_mode

engine = Engine(
    name="demo",
    title="Demo Engine",
    skin="pixel",
    particle="pixel",
    background="vanilla",
    data=EngineData(
        ui=ui_config,
        options=Options,
        play=play_mode,
        watch=watch_mode,
        preview=preview_mode,
        tutorial=tutorial_mode,
    ),
)

project = Project(
    engine=engine,
    levels=[demo_level],
)
