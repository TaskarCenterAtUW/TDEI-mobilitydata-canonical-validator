import unittest
from src.mobility_canonical_validator.constants import Constants


class TestConstants(unittest.TestCase):

    def setUp(self):
        self.constants = Constants()
        self.mock_job_id = 'mock_job_id'

    def test_get_result_url(self):
        expected_result = "https://gtfs-validator-results.mobilitydata.org/mock_job_id/report.json"
        result_url = self.constants.get_result_url(self.mock_job_id)
        self.assertEqual(result_url, expected_result)


if __name__ == '__main__':
    unittest.main()
