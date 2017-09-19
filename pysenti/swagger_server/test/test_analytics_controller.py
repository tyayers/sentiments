# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.analysis_request import AnalysisRequest
from swagger_server.models.analysis_response import AnalysisResponse
from swagger_server.models.error import Error
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAnalyticsController(BaseTestCase):
    """ AnalyticsController integration test stubs """

    def test_text_analytics(self):
        """
        Test case for text_analytics

        Customer Service Text Analytics
        """
        analysis_request = AnalysisRequest()
        response = self.client.open('/v1/analytics',
                                    method='POST',
                                    data=json.dumps(analysis_request),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
