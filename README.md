# Server Log Analyzer

## Author
Amol Chavan

---

## Description

This project is a Python-based Server Log Analyzer that reads and analyzes server log files.

The program processes log entries from a log file and performs several operations such as:

- Parsing log entries
- Counting log levels
- Finding the most recent log entry for a specific level
- Filtering logs within a given date range

The goal of this project is to demonstrate log parsing and basic log analysis using Python.

---

# Log File Format

Each log entry follows this format:

<timestamp> <log_level> <message>

Example:

2025-01-10 09:23:45 INFO Application started

Explanation:

timestamp → Date and time of the event  
log_level → Severity level (INFO, WARNING, ERROR, DEBUG)  
message → Description of the event  

---

# Features

### 1. Read and Parse Logs
The program reads log entries from a file named `logs.txt` and parses each entry into timestamp, log level, and message.

### 2. Count Log Levels
The program counts the occurrences of each log level.

Example:

INFO: 2  
WARNING: 2  
ERROR: 2  
DEBUG: 1  

### 3. Find Most Recent Log Entry
The user provides a log level and the program displays the most recent log entry for that level.

### 4. Filter Logs by Date Range
The user enters a start date and end date, and the program filters logs within that date range.

### 5. Save Filtered Logs
Filtered logs are saved into a file named:

filtered_logs.txt

---

# How to Run the Program

Run the following command in the terminal:

```bash
python log_analyzer.py
```

Then follow the prompts in the terminal:

- Enter log level
- Enter start date
- Enter end date

---

# Sample Input (logs.txt)

```
2025-01-10 09:23:45 INFO Application started
2025-01-10 09:25:00 WARNING Disk space low
2025-01-10 09:26:30 ERROR Unable to connect to database
2025-01-10 09:30:15 INFO User logged in
2025-01-10 09:35:20 ERROR Timeout occurred
2025-01-10 09:40:05 WARNING CPU usage high
2025-01-11 10:15:45 DEBUG Debugging started
```

---

# Expected Output

Example output when running the program:

```
===== SERVER LOG ANALYZER =====

====== Log Level Counts ======
INFO : 2
WARNING : 2
ERROR : 2
DEBUG : 1
==============================

Enter log level to find most recent entry (INFO/WARNING/ERROR/DEBUG): ERROR

Most Recent Log Entry:
2025-01-10 09:35:20 ERROR Timeout occurred

Enter start date (YYYY-MM-DD): 2025-01-10
Enter end date (YYYY-MM-DD): 2025-01-10

Filtered logs saved to filtered_logs.txt
```

---

# Assumptions and Engineering Decisions

- Invalid or malformed log lines are skipped.
- Unknown log levels are ignored.
- Logs are stored as dictionaries for easier processing.
- Timestamps are converted into Python `datetime` objects for accurate comparisons.

---

# Project Structure

```
log_analyzer
│
├── log_analyzer.py
├── logs.txt
├── filtered_logs.txt
└── README.md
```

---

# Future Improvements

Possible improvements:

- Add command-line argument support using argparse
- Implement automated testing using pytest
- Use Python logging module for better log management
