from functools import lru_cache


@lru_cache(maxsize=1000)
def attendance(consecutive_absent, nth_class, total_days) -> tuple[int, int]:
    valid_classes, days_missed_ceremony = 0, 0

    if consecutive_absent == 4:
        return 0, 0  # valid_classes=0, days_missed_ceremony=0
    if nth_class == total_days:
        if consecutive_absent != 0:
            return 1, 1  # valid_classes=1, days_missed_ceremony=1
        return 1, 0  # valid_classes=1, days_missed_ceremony=0

    # Recursion call for absent (increasing absence count)
    data = attendance(consecutive_absent + 1, nth_class + 1, total_days)
    valid_classes += data[0]
    days_missed_ceremony += data[1]

    # Recursion call for present (resetting absence count to 0)
    data = attendance(0, nth_class + 1, total_days)
    valid_classes += data[0]
    days_missed_ceremony += data[1]

    return valid_classes, days_missed_ceremony


number_of_days = 10
res = attendance(0, 0, number_of_days)
print(f"{res[1]}/{res[0]}")
