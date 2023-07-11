import argparse

from dataclasses import dataclass
from functools import lru_cache


@dataclass
class AttendanceData:
    valid_classes: int
    days_missed_ceremony: int

    def update_counts(self, other_data):
        self.valid_classes += other_data.valid_classes
        self.days_missed_ceremony += other_data.days_missed_ceremony


@lru_cache(maxsize=1000)
def attendance(consecutive_absent, nth_class, total_days) -> AttendanceData:
    attendance_data = AttendanceData(valid_classes=0, days_missed_ceremony=0)

    if consecutive_absent == 4:
        return AttendanceData(valid_classes=0, days_missed_ceremony=0)
    if nth_class == total_days:
        if consecutive_absent != 0:
            return AttendanceData(valid_classes=1, days_missed_ceremony=1)
        return AttendanceData(valid_classes=1, days_missed_ceremony=0)

    # Recursion call for absent (increasing absence count)
    attendance_data.update_counts(attendance(consecutive_absent + 1, nth_class + 1, total_days))

    # Recursion call for present (resetting absence count to 0)
    attendance_data.update_counts(attendance(0, nth_class + 1, total_days))

    return attendance_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Probability of Attending Graduation Ceremony Finder")
    parser.add_argument("-n", help="Number of days for Finding the probability.", required=True, type=int)

    args = parser.parse_args()
    number_of_days = args.n
    if not(0 < number_of_days < 498):
        print(f"Number of days should be between 1 - 497, {number_of_days} ")
        exit(-1)
    data = attendance(0, 0, number_of_days)
    print(f"{data.days_missed_ceremony}/{data.valid_classes}")
