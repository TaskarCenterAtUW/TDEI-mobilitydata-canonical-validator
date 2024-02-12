class Constants:
    JOB_URL = 'https://gtfs-validator-web-mbzoxaljzq-ue.a.run.app/create-job'
    RESULT_BASE_URL = 'https://gtfs-validator-results.mobilitydata.org'

    def get_result_url(self, job_id):
        return f'{self.RESULT_BASE_URL}/{job_id}/report.json'.format(job_id=job_id)

