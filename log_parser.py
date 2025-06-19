import csv
from datetime import datetime
from collections import defaultdict

def parse_log_file(filename):
    jobs = defaultdict(dict)  # pid -> {job_name, start, end}

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pid = row['pid']
            job_name = row['job_name']
            timestamp = datetime.strptime(row['timestamp'], "%Y-%m-%d %H:%M:%S")
            action = row['action']

            if pid not in jobs:
                jobs[pid] = {"job_name": job_name}

            jobs[pid][action.lower()] = timestamp  # jobs[pid]['start'] or ['end']

    return jobs

def generate_report(jobs, output_file):
    with open(output_file, 'w') as f:
        for pid, data in jobs.items():
            job_name = data['job_name']
            start = data.get('start')
            end = data.get('end')

            if not start or not end:
                f.write(f"ERROR: Missing start or end for job '{job_name}' with PID {pid}\n")
                continue

            duration = (end - start).total_seconds() / 60  # duration in minutes
            f.write(f"Job: {job_name}, PID: {pid}, Duration: {duration:.2f} minutes\n")

            if duration > 10:
                f.write(f"ERROR: Job '{job_name}' (PID: {pid}) exceeded 10 minutes.\n")
            elif duration > 5:
                f.write(f"WARNING: Job '{job_name}' (PID: {pid}) took longer than 5 minutes.\n")
