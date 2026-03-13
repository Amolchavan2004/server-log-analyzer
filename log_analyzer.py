"""
Server Log Analyzer
Author: Amol Chavan

Description:
This script analyzes server log files and provides insights such as:
- Log level counts
- Most recent log entry
- Filtering logs by date range

Engineering Decisions:
- Invalid log lines are skipped.
- Unknown log levels are ignored.
- Logs are stored as dictionaries for easier processing.
"""

from datetime import datetime
from collections import Counter


def parse_log_line(line):
    """
    Parse a single log line and return a dictionary containing
    timestamp, log level, and message.
    """

    parts = line.strip().split(" ", 3)

    # Engineering decision: skip malformed lines
    if len(parts) < 4:
        print(f"Warning: Invalid log skipped -> {line.strip()}")
        return None

    date, time, level, message = parts
    timestamp_str = f"{date} {time}"

    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(f"Warning: Invalid timestamp -> {timestamp_str}")
        return None

    valid_levels = {"INFO", "WARNING", "ERROR", "DEBUG"}

    if level not in valid_levels:
        print(f"Warning: Unknown log level -> {level}")
        return None

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }


def read_logs(file_path):
    """
    Reads the log file and returns a list of parsed log entries.
    """

    logs = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)

    except FileNotFoundError:
        print("Error: Log file not found.")

    if not logs:
        print("Warning: No valid logs found.")

    return logs


def count_log_levels(logs):
    """
    Count occurrences of each log level.
    """

    levels = [log["level"] for log in logs]
    counts = Counter(levels)

    print("\n====== Log Level Counts ======")
    for level, count in counts.items():
        print(f"{level:<10} : {count}")
    print("==============================")

    return counts


def find_most_recent_log(logs, level):
    """
    Find the most recent log entry for the given log level.
    """

    filtered = [log for log in logs if log["level"] == level]

    if not filtered:
        print(f"No logs found for level: {level}")
        return None

    recent_log = max(filtered, key=lambda x: x["timestamp"])

    print("\nMost Recent Log Entry:")
    print(f"{recent_log['timestamp']} {recent_log['level']} {recent_log['message']}")

    return recent_log


def filter_logs_by_date(logs, start_date, end_date):
    """
    Filter logs between the given date range.
    """

    filtered = []

    for log in logs:
        log_date = log["timestamp"].date()

        if start_date <= log_date <= end_date:
            filtered.append(log)

    return filtered


def save_filtered_logs(logs, file_name):
    """
    Save filtered logs into a file.
    """

    with open(file_name, "w") as file:
        for log in logs:
            line = f"{log['timestamp']} {log['level']} {log['message']}\n"
            file.write(line)

    print(f"\nFiltered logs saved to {file_name}")


def main():
    """
    Main function to run the log analyzer.
    """

    print("\n===== SERVER LOG ANALYZER =====")

    file_path = "logs.txt"

    logs = read_logs(file_path)

    if not logs:
        return

    # Count log levels
    count_log_levels(logs)

    # Valid log levels
    valid_levels = {"INFO", "WARNING", "ERROR", "DEBUG"}

    level = input("\nEnter log level to find most recent entry (INFO/WARNING/ERROR/DEBUG): ").upper()

    if level not in valid_levels:
        print("Invalid log level entered.")
        return

    find_most_recent_log(logs, level)

    # Date range input
    start_input = input("\nEnter start date (YYYY-MM-DD): ")
    end_input = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_input, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered_logs = filter_logs_by_date(logs, start_date, end_date)

    if not filtered_logs:
        print("No logs found in given date range.")
    else:
        save_filtered_logs(filtered_logs, "filtered_logs.txt")


if __name__ == "__main__":
    main()