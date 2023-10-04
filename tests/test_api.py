import os
import sys
import mock
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tinarm

NODE_ID = "testnode"
ROOT_URL = "http://example.com"
API_KEY = "1234"
JOB_ID = "4568"
JOB_STATUS = 20
JOB_ARTIFACT_ID = "6544"
JOB_ARTIFACT_TYPE = "TEST_PLOT"
JOB_ARTIFACT_FILE_PATH = "/lala/test_plot.png"
JOB_ARTIFACT_FILE_URL = "file://testnode/" + JOB_ARTIFACT_FILE_PATH
JOB_ARTIFACT_REMOTE_URL = "http://example.com/test_plot.png"


class ApiTestCase(unittest.TestCase):

    @mock.patch("tinarm.api.requests")
    def test_all(self, mock_requests):
        a = tinarm.Api(NODE_ID, ROOT_URL, API_KEY)

        a.get_job(JOB_ID)
        mock_requests.get.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}?apikey={API_KEY}",
        )

        a.update_job_status(JOB_ID, JOB_STATUS)
        mock_requests.put.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}/status/{JOB_STATUS}?apikey={API_KEY}"
        )

        a.get_job_artifact(JOB_ID, JOB_ARTIFACT_ID)
        mock_requests.get.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}?apikey={API_KEY}",
        )

        a.create_job_artifact(JOB_ID, JOB_ARTIFACT_TYPE, JOB_ARTIFACT_REMOTE_URL)
        mock_requests.post.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}/artifacts?promote=False&apikey={API_KEY}",
            json={
                "type": JOB_ARTIFACT_TYPE,
                "url": JOB_ARTIFACT_REMOTE_URL,
            },
        )

        a.create_job_artifact_from_file(JOB_ID, JOB_ARTIFACT_TYPE, JOB_ARTIFACT_FILE_PATH)
        mock_requests.post.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}/artifacts?promote=False&apikey={API_KEY}",
            json={
                "type": JOB_ARTIFACT_TYPE,
                "url": JOB_ARTIFACT_FILE_URL,
            },
        )

        a.create_job_artifact_from_file(JOB_ID, JOB_ARTIFACT_TYPE, JOB_ARTIFACT_FILE_PATH, True)
        mock_requests.post.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}/artifacts?promote=True&apikey={API_KEY}",
            json={
                "type": JOB_ARTIFACT_TYPE,
                "url": JOB_ARTIFACT_FILE_URL,
            },
        )

        a.update_job_artifact(JOB_ID, JOB_ARTIFACT_ID, {"type": JOB_ARTIFACT_TYPE, "url": JOB_ARTIFACT_REMOTE_URL} )
        mock_requests.put.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}/artifacts/{JOB_ARTIFACT_ID}?apikey={API_KEY}",
            json={
                "type": JOB_ARTIFACT_TYPE,
                "url": JOB_ARTIFACT_REMOTE_URL,
            },
        )

        a.promote_job_artifact(JOB_ID, JOB_ARTIFACT_ID)
        mock_requests.put.assert_called_with(
            url=f"{ROOT_URL}/jobs/{JOB_ID}/artifacts/{JOB_ARTIFACT_ID}/promote?apikey={API_KEY}",
        )

    
if __name__ == "__main__":
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)