import logging
from .version import __version__
from .constants import Constants
from .mobility_data import MobilityData

logging.basicConfig()


class CanonicalValidator:
    def __init__(self, zip_file):
        self.file = zip_file
        self.logger = logging.getLogger('CANONICAL_VALIDATOR')
        self.logger.setLevel(logging.INFO)
        self.uploader = MobilityData(logger=self.logger)

    def validate(self):
        uploader_status, uploader_error = self.uploader.upload(file_path=self.file)
        if uploader_status:
            self.logger.info(f'File uploaded with JOB ID: {self.uploader.job_id}')
            report_url = Constants().get_result_url(job_id=self.uploader.job_id)
            report = self.uploader.get_mobility_data(url=report_url)
            self.logger.info('Got Success Response From Mobility')
            return report['notices']
        else:
            return {'error': uploader_error}
