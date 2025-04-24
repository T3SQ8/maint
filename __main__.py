from .helper import convert_size, used_storage
from .steps import steps

if __name__ == "__main__":

    hdd_before = used_storage()
    total_steps = len(steps)
    current_step = 1
    for s in steps:
        print(f"[{current_step}/{total_steps}]", end=" ")
        s.prompt()
        current_step += 1
    hdd_after = used_storage()

    b = convert_size(hdd_before)
    a = convert_size(hdd_after)
    d = convert_size(hdd_before - hdd_after)

    MESSAGE = f"{b} -> {a} ({d})"
    print("\n" * 3, "-" * len(MESSAGE))
    print(MESSAGE)
