import sys
import argparse
import logging
from dataclasses import dataclass
import importlib
from common import preamble


logger = logging.getLogger(__name__)


@dataclass(init=True, repr=True, frozen=True)
class Task:
    targ: str
    help_txt: str
    pkg: str
    cls: str

    def __eq__(self, other):
        if type(other) != Task:
            return False
        return self.targ == other.targ

    def __hash__(self):
        return hash(f"{self.targ}-{self.pkg}-{self.cls}")


TASKS = {
    "knearest": Task(targ="knearest", help_txt="K-nearest neighbour", pkg="supervised.knearest", cls="Knearest"),
}


def configure_logger():
    handler = logging.StreamHandler(sys.stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


if __name__ == "__main__":
    configure_logger()
    parser = argparse.ArgumentParser()
    tasks = [TASKS[task].targ for task in TASKS]
    parser.add_argument("task", help="Task to run", type=str, choices=tasks)

    args = parser.parse_args()
    logger.info({
        "message": "Parsed arguments",
        "args": args
    })
    task: Task = TASKS[args.task]

    logger.info({
        "message": "Task will run",
        "task": task
    })
    module = importlib.import_module(task.pkg)
    task_class = getattr(module, task.cls)
    task_instance = task_class()
    task_instance.run()
