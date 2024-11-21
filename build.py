from pathlib import Path
from time import perf_counter

from sonolus.build.cli import build_project

from demo.project import project

start_time = perf_counter()
for _ in range(10):
    build_project(project=project, build_dir=Path("build"))
end_time = perf_counter()
print(f"Build time: {1000 * (end_time - start_time):.2f}ms")
