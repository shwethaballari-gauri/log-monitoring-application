import unittest
from log_parser import parse_log_file

class TestLogParser(unittest.TestCase):
    def test_parse_log_file(self):
        jobs = parse_log_file("job_logs.csv")
        self.assertEqual(len(jobs), 3)
        self.assertIn("1234", jobs)
        self.assertEqual(jobs["1234"]["job_name"], "backup-database")

if __name__ == '__main__':
    unittest.main()
