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

    size_before = convert_size(hdd_before)
    size_after = convert_size(hdd_after)
    if hdd_after < hdd_before:
        size_diff = convert_size(hdd_before - hdd_after)
    else:
        size_diff = "-" + convert_size(abs(hdd_before - hdd_after))

    MESSAGE = f"{size_before} -> {size_after} ({size_diff})"
    print("\n" * 3, "-" * len(MESSAGE))
    print(MESSAGE)
