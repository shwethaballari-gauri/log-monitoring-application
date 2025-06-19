from log_parser import parse_log_file, generate_report

if __name__ == "__main__":
    log_file = "job_logs.csv"
    output_file = "output.log"

    jobs = parse_log_file(log_file)
    generate_report(jobs, output_file)
    print(f"Report generated in {output_file}")
