from .helper import *
from .tasks import Command, Task


class Routine:
    def __init__(self):
        self.steps = []

    def add_command(self, *args, **kwargs):
        self.steps.append(Command(*args, **kwargs))

    def add_task(self, *args, **kwargs):
        self.steps.append(Task(*args, **kwargs))

    def run(self):
        hdd_before = used_storage()
        total_steps = len(self.steps)
        current_step = 1
        for step in self.steps:
            print(f"[{current_step}/{total_steps}]", end=" ")
            step.prompt()
            current_step += 1
        hdd_after = used_storage()

        size_before = convert_size(hdd_before)
        size_after = convert_size(hdd_after)
        if hdd_after < hdd_before:
            size_diff = convert_size(hdd_before - hdd_after)
        else:
            size_diff = "-" + convert_size(abs(hdd_before - hdd_after))

        MESSAGE = f"{size_before} -> {size_after} ({size_diff})"
        print("\n" * 3, "-" * len(MESSAGE))
        print(MESSAGE)


