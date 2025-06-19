import unittest
from datetime import datetime
from main import JobTracker

class TestJobTracker(unittest.TestCase):
    def test_duration_classification(self):
        jt = JobTracker()
        jt.jobs[1] = {
            'start': datetime.strptime("12:00:00", "%H:%M:%S"),
            'end': datetime.strptime("12:06:00", "%H:%M:%S"),
            'desc': "Test Job"
        }
        jt.generate_report()  # Manually check the output.log or mock file writing

if __name__ == "__main__":
    unittest.main()
