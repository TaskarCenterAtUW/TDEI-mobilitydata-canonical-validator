import unittest
import requests
from unittest.mock import patch, Mock, mock_open
from src.gtfs_canonical_validator.gtfs_validator import GTFSValidator


class TestGTFSValidatorData(unittest.TestCase):

    @patch('requests.post')
    def test_get_info_success(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {'jobId': 'mock_job_id', 'url': 'mock_url'}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value.__enter__.return_value = mock_response

        job_id, url, error = GTFSValidator.get_info()

        self.assertEqual(job_id, 'mock_job_id')
        self.assertEqual(url, 'mock_url')
        self.assertIsNone(error)

    @patch('requests.post')
    def test_get_info_failure(self, mock_post):
        mock_post.side_effect = requests.exceptions.RequestException("Mock exception")

        job_id, url, error = GTFSValidator.get_info()

        self.assertIsNone(job_id)
        self.assertIsNone(url)
        self.assertEqual(error, 'Error: Mock exception')

    @patch('requests.put')
    def test_upload_success(self, mock_put):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_put.return_value.__enter__.return_value = mock_response

        mobility_data = GTFSValidator(Mock())
        mobility_data.url = 'mock_upload_url'

        # Ensure the provided file path exists
        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.return_value.__enter__.return_value.read.return_value = b'mock_file_content'
            result, error = mobility_data.upload('mock_file_path')

        # Verify the URL and file path
        self.assertTrue(mock_put.called)
        self.assertTrue(result)
        self.assertIsNone(error)

    @patch('requests.put')
    def test_upload_failure(self, mock_put):
        mock_put.side_effect = requests.exceptions.RequestException("Mock exception")

        mobility_data = GTFSValidator(Mock())
        mobility_data.url = 'mock_upload_url'

        with patch('builtins.open', mock_open()) as mock_file:
            # Ensure that read method of the mock file object returns b''
            mock_file.return_value.__enter__.return_value.read.return_value = b''

            result, error = mobility_data.upload('mock_file_path')

        self.assertFalse(result)
        self.assertEqual(error, 'Error uploading file: Mock exception')

    @patch('requests.get')
    def test_get_mobility_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'mock_data': 'mock_value'}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value.__enter__.return_value = mock_response

        mobility_data = GTFSValidator(Mock())
        result = mobility_data.get_mobility_data('mock_url')

        self.assertEqual(result, {'mock_data': 'mock_value'})

    @patch('requests.get')
    def test_get_mobility_data_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Mock exception")

        mobility_data = GTFSValidator(Mock())
        result = mobility_data.get_mobility_data('mock_url')

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
