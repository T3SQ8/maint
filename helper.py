import math
import shutil


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    unit_index = int(math.floor(math.log(size_bytes, 1024)))
    divisor = math.pow(1024, unit_index)
    converted_size = round(size_bytes / divisor, 2)
    return f"{converted_size} {size_units[unit_index]}"


def used_storage():
    return shutil.disk_usage("/").used
