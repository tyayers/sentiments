import sys
import connexion
from swagger_server.models.analysis_request import AnalysisRequest
from swagger_server.models.analysis_response import AnalysisResponse
from swagger_server.models.error import Error
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from textblob_de import TextBlobDE
from textblob import TextBlob

def text_analytics(analysis_request):
    """
    Customer Service Text Analytics
    The Analytics endpoint returns both the sentiment and suggested response for a customer service text. 
    :param analysis_request: The customer&#39;s serve text in base64 encoding
    :type analysis_request: dict | bytes

    :rtype: AnalysisResponse
    """
    if connexion.request.is_json:
        analysis_request = AnalysisRequest.from_dict(connexion.request.get_json())
        response = AnalysisResponse()

        if analysis_request.language_code.upper() == "DE":
            blob = TextBlobDE(analysis_request.customer_text)
            response.sentiment_score = (blob.sentiment.polarity + 1) / 2
        else:
            blob = TextBlob(analysis_request.customer_text)
            response.sentiment_score = (blob.sentiment.polarity + 1) / 2            

    return response
