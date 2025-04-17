from os.path import expanduser

from .prompts import Command, Task

docker = [
    Command(
        "docker system prune -a".split(),
        "remove unused docker images, containers and networks",
        required="docker",
    ),
    Command(
        "docker volume ls".split(),
        "list docker volumes",
        default=True,
        required="docker",
    ),
]

storage = [
    Command(
        expanduser("~/.local/bin/xdg-dirs-size.sh").split(),
        "view storage used by XDG dirs",
    ),
]

phone = [Task("organize phone gallery")]

steps = docker + storage + phone
