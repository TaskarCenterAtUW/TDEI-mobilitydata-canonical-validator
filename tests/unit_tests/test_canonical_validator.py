import os
import unittest
from unittest.mock import Mock
from src.gtfs_canonical_validator import CanonicalValidator

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_FILES = os.path.join(PARENT_DIR, 'test_files')


class TestCanonicalValidator(unittest.TestCase):

    def setUp(self):
        self.mock_zip_file = 'mock_zip_file.zip'
        self.validator = CanonicalValidator(self.mock_zip_file)

    def test_validate_successful_upload(self):
        mock_report = {'notices': [{
            'code': 'feed_expiration_date7_days',
            'severity': 'WARNING',
            'totalNotices': 1,
            'sampleNotices': [
                {
                    'csvRowNumber': 2,
                    'currentDate': '20240228',
                    'feedEndDate': '20230625',
                    'suggestedExpirationDate': '20240306'
                }
            ]
        }]}
        self.validator.uploader.upload = Mock(return_value=(True, None))
        self.validator.uploader.job_id = 'mock_job_id'
        self.validator.uploader.get_mobility_data = Mock(return_value=mock_report)

        result = self.validator.validate()

        self.assertTrue(result.status)
        self.validator.uploader.upload.assert_called_once_with(file_path=self.mock_zip_file)
        self.validator.uploader.get_mobility_data.assert_called_once()

    def test_validate_failed_upload(self):
        mock_error = 'Mock upload error'
        self.validator.uploader.upload = Mock(return_value=(False, mock_error))
        self.validator.uploader.get_mobility_data = Mock()

        result = self.validator.validate()

        self.assertEqual(result.error, mock_error)
        self.validator.uploader.upload.assert_called_once_with(file_path=self.mock_zip_file)
        self.assertFalse(self.validator.uploader.get_mobility_data.called)


class TestCanonicalValidatorSuccessWithDatasets(unittest.TestCase):

    def setUp(self):
        self.valid_file = os.path.join(TEST_FILES, 'valid.zip')

    def test_validate_successful_upload(self):
        self.validator = CanonicalValidator(zip_file=self.valid_file)
        report = self.validator.validate()
        # Make sure report.error is None
        self.assertIsNone(report.error)
        self.assertGreaterEqual(len(report.info), 0)
        self.assertTrue(report.status)


class TestCanonicalValidatorFailureWithDatasets(unittest.TestCase):

    def setUp(self):
        self.valid_file = os.path.join(TEST_FILES, 'failure.zip')

    def test_validate_failure_dataset_upload(self):
        self.validator = CanonicalValidator(zip_file=self.valid_file)
        report = self.validator.validate()
        self.assertFalse(report.status)


if __name__ == '__main__':
    unittest.main()
