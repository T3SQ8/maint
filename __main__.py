from .helper import convert_size, used_storage
from .steps import steps

if __name__ == "__main__":

    hdd_before = used_storage()
    for s in steps:
        s.prompt()
    hdd_after = used_storage()

    b = convert_size(hdd_before)
    a = convert_size(hdd_after)
    d = convert_size(hdd_before - hdd_after)

    MESSAGE = f"{b} -> {a} ({d})"
    print("\n" * 3, "-" * len(MESSAGE))
    print(MESSAGE)
