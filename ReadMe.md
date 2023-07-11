# Attendance Calculator

This script calculates the probability of attending a graduation ceremony based on attendance records. It uses a recursive function to calculate the probability by considering consecutive absences.

## Requirements

- Python 3.7+ 

## Usage

To use this script, follow the instructions below:

1. Make sure you have Python 3.7 or higher installed on your system.
2. Open a terminal or command prompt.
3. Clone or download the script to your local machine.
4. Navigate to the directory where the script is located.
5. Run the script using the following command:

```commandline
python script.py -n <number_of_days>
```


Replace `<number_of_days>` with the actual number of days for which you want to find the probability of attending the graduation ceremony.

For example, to find the probability for 100 days, run the command:

```commandline
python script.py -n 100
```


The script will calculate the probability and display the result in the format `days_missed_ceremony/valid_classes`.

**Note:** The number of days should be between 1 and 497.

## Code Explanation

The script uses the following main components:
- `lru_cache` decorator: this decorator is used to cache the `attendance` function's output which reduces the time complexity of the solution from `2^N` to `N` where `N` is `the number of days`

- `AttendanceData` class: A data class that represents the attendance data. It has two attributes: `valid_classes` (number of ways to attend classes over n days without being ineligible) and `days_missed_ceremony` (number of ways in which missed the ceremony on the last Day).

- `attendance` function: A recursive function that calculates the probability of attending the graduation ceremony. It takes three parameters: `consecutive_absent` (number of consecutive absences), `nth_class` (current class day), and `total_days` (total number of days). The function returns an instance of `AttendanceData` with the calculated values.

- `if __name__ == '__main__'` block: The main entry point of the script. It parses the command-line arguments, validates the input, calls the `attendance` function, and displays the result.

## Complexity

### Time Complexity:
For memoization of the `attendance` function, the time complexity of the solution is `O(N)` where `N` is the `number of days` 

### Space Complexity:
Since we are caching the `attendance` function, `4 * N` space would be needed for cache, makes the space complexity as `O(N)`



## License

This script is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.
