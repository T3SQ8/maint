import subprocess
from shutil import which

from colorama import Fore


class Command:
    def __init__(
        self,
        cmd: list,
        desc: str,
        default=False,
        required=None,
    ):
        self.cmd = cmd
        self.desc = desc
        self.default = default
        self.required = required

    def check_installed(self) -> bool:
        return bool(which(self.required)) if self.required else False

    def prompt(self):
        if self.required and not self.check_installed():
            print(Fore.RED + f"{self.required} is not installed" + Fore.RESET)
        show_default = "[Y/n]" if self.default else "[y/N]"
        decision = None
        while decision is None:
            cmd_str = " ".join(self.cmd)
            match input(
                f"Do you want to run `{cmd_str}` to {self.desc} {show_default}? "
            ).lower():
                case "y":
                    decision = True
                case "n":
                    decision = False
                case "":
                    decision = self.default
        if decision:
            self.run()

    def run(self):
        subprocess.run(self.cmd, check=False)


class Task:
    def __init__(self, instruct):
        self.instruct = instruct

    def prompt(self):
        completed = False
        while not completed:
            if (
                input(f'Go and {self.instruct}? When completed answer "YES": ').upper()
                == "YES"
            ):
                completed = True
