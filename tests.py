# Basic unit tests for the application.

import unittest
from data_collector import collect_data
from config import DUMMY_DATA_SOURCE

class TestOSINTShark(unittest.TestCase):
    def test_data_collection(self):
        try:
            data = collect_data()
            assert len(data) > 0, "Data collection failed"
        except Exception:
            assert False, "Exception in data collection"

if __name__ == '__main__':
    unittest.main()
