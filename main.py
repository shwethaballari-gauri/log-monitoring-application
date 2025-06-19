import csv
from datetime import datetime
from collections import defaultdict

# Constants
WARNING_THRESHOLD = 300  # 5 minutes in seconds
ERROR_THRESHOLD = 600    # 10 minutes in seconds

# Format: HH:MM:SS
TIME_FORMAT = "%H:%M:%S"

class JobTracker:
    def __init__(self):
        self.jobs = defaultdict(dict)  # {pid: {'start': timestamp, 'end': timestamp, 'desc': str}}

    def process_log_line(self, line):
        # Example line: 12:01:01,Backup database,START,12345
        try:
            time_str, description, action, pid = [item.strip() for item in line.strip().split(',')]
            timestamp = datetime.strptime(time_str, TIME_FORMAT)
            pid = int(pid)

            if action == "START":
                self.jobs[pid]['start'] = timestamp
                self.jobs[pid]['desc'] = description
            elif action == "END":
                self.jobs[pid]['end'] = timestamp
                self.jobs[pid]['desc'] = description
        except Exception as e:
            print(f"Error parsing line: {line.strip()} -> {e}")

    def generate_report(self):
        with open("output.log", "w") as f:
            for pid, data in self.jobs.items():
                start = data.get('start')
                end = data.get('end')
                desc = data.get('desc', 'N/A')
                if start and end:
                    duration = (end - start).total_seconds()
                    if duration > ERROR_THRESHOLD:
                        level = "ERROR"
                    elif duration > WARNING_THRESHOLD:
                        level = "WARNING"
                    else:
                        level = "INFO"
                    message = f"[{level}] Job '{desc}' (PID: {pid}) took {int(duration)} seconds"
                    print(message)
                    f.write(message + "\n")
                else:
                    print(f"[MISSING] Job '{desc}' (PID: {pid}) missing start or end time.")

def main():
    tracker = JobTracker()
    with open("logs.log", "r") as file:
        for line in file:
            tracker.process_log_line(line)
    tracker.generate_report()

if __name__ == "__main__":
    main()
