# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class AnalysisResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, sentiment_score: float=None, suggested_response: str=None, suggested_response_score: float=None):
        """
        AnalysisResponse - a model defined in Swagger

        :param sentiment_score: The sentiment_score of this AnalysisResponse.
        :type sentiment_score: float
        :param suggested_response: The suggested_response of this AnalysisResponse.
        :type suggested_response: str
        :param suggested_response_score: The suggested_response_score of this AnalysisResponse.
        :type suggested_response_score: float
        """
        self.swagger_types = {
            'sentiment_score': float,
            'suggested_response': str,
            'suggested_response_score': float
        }

        self.attribute_map = {
            'sentiment_score': 'sentiment-score',
            'suggested_response': 'suggested-response',
            'suggested_response_score': 'suggested-response-score'
        }

        self._sentiment_score = sentiment_score
        self._suggested_response = suggested_response
        self._suggested_response_score = suggested_response_score

    @classmethod
    def from_dict(cls, dikt) -> 'AnalysisResponse':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnalysisResponse of this AnalysisResponse.
        :rtype: AnalysisResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def sentiment_score(self) -> float:
        """
        Gets the sentiment_score of this AnalysisResponse.
        A sentiment analysis of the input text on a scale from 0 to 1, with 0 being very unhappy and 1 being very happy.

        :return: The sentiment_score of this AnalysisResponse.
        :rtype: float
        """
        return self._sentiment_score

    @sentiment_score.setter
    def sentiment_score(self, sentiment_score: float):
        """
        Sets the sentiment_score of this AnalysisResponse.
        A sentiment analysis of the input text on a scale from 0 to 1, with 0 being very unhappy and 1 being very happy.

        :param sentiment_score: The sentiment_score of this AnalysisResponse.
        :type sentiment_score: float
        """

        self._sentiment_score = sentiment_score

    @property
    def suggested_response(self) -> str:
        """
        Gets the suggested_response of this AnalysisResponse.
        Suggested response to the customer service text.

        :return: The suggested_response of this AnalysisResponse.
        :rtype: str
        """
        return self._suggested_response

    @suggested_response.setter
    def suggested_response(self, suggested_response: str):
        """
        Sets the suggested_response of this AnalysisResponse.
        Suggested response to the customer service text.

        :param suggested_response: The suggested_response of this AnalysisResponse.
        :type suggested_response: str
        """

        self._suggested_response = suggested_response

    @property
    def suggested_response_score(self) -> float:
        """
        Gets the suggested_response_score of this AnalysisResponse.
        The confidence score of the suggested response.

        :return: The suggested_response_score of this AnalysisResponse.
        :rtype: float
        """
        return self._suggested_response_score

    @suggested_response_score.setter
    def suggested_response_score(self, suggested_response_score: float):
        """
        Sets the suggested_response_score of this AnalysisResponse.
        The confidence score of the suggested response.

        :param suggested_response_score: The suggested_response_score of this AnalysisResponse.
        :type suggested_response_score: float
        """

        self._suggested_response_score = suggested_response_score

