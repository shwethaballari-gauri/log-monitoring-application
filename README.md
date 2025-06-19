# log-monitoring-application

This app parses a CSV log of job executions, tracks durations, and logs warnings/errors based on thresholds.

## Features
- Track job start and end
- Compute duration
- Log warnings (5+ mins) and errors (10+ mins)
- Output saved to `output.log`

## How to Run
```bash
python main.py
