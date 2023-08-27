# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.23.2
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectionStatisticsSnapshotDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'predicted_millis_until_count_backpressure': 'int',
        'predicted_millis_until_bytes_backpressure': 'int',
        'predicted_count_at_next_interval': 'int',
        'predicted_bytes_at_next_interval': 'int',
        'predicted_percent_count': 'int',
        'predicted_percent_bytes': 'int',
        'prediction_interval_millis': 'int'
    }

    attribute_map = {
        'id': 'id',
        'predicted_millis_until_count_backpressure': 'predictedMillisUntilCountBackpressure',
        'predicted_millis_until_bytes_backpressure': 'predictedMillisUntilBytesBackpressure',
        'predicted_count_at_next_interval': 'predictedCountAtNextInterval',
        'predicted_bytes_at_next_interval': 'predictedBytesAtNextInterval',
        'predicted_percent_count': 'predictedPercentCount',
        'predicted_percent_bytes': 'predictedPercentBytes',
        'prediction_interval_millis': 'predictionIntervalMillis'
    }

    def __init__(self, id=None, predicted_millis_until_count_backpressure=None, predicted_millis_until_bytes_backpressure=None, predicted_count_at_next_interval=None, predicted_bytes_at_next_interval=None, predicted_percent_count=None, predicted_percent_bytes=None, prediction_interval_millis=None):
        """
        ConnectionStatisticsSnapshotDTO - a model defined in Swagger
        """

        self._id = None
        self._predicted_millis_until_count_backpressure = None
        self._predicted_millis_until_bytes_backpressure = None
        self._predicted_count_at_next_interval = None
        self._predicted_bytes_at_next_interval = None
        self._predicted_percent_count = None
        self._predicted_percent_bytes = None
        self._prediction_interval_millis = None

        if id is not None:
          self.id = id
        if predicted_millis_until_count_backpressure is not None:
          self.predicted_millis_until_count_backpressure = predicted_millis_until_count_backpressure
        if predicted_millis_until_bytes_backpressure is not None:
          self.predicted_millis_until_bytes_backpressure = predicted_millis_until_bytes_backpressure
        if predicted_count_at_next_interval is not None:
          self.predicted_count_at_next_interval = predicted_count_at_next_interval
        if predicted_bytes_at_next_interval is not None:
          self.predicted_bytes_at_next_interval = predicted_bytes_at_next_interval
        if predicted_percent_count is not None:
          self.predicted_percent_count = predicted_percent_count
        if predicted_percent_bytes is not None:
          self.predicted_percent_bytes = predicted_percent_bytes
        if prediction_interval_millis is not None:
          self.prediction_interval_millis = prediction_interval_millis

    @property
    def id(self):
        """
        Gets the id of this ConnectionStatisticsSnapshotDTO.
        The id of the connection.

        :return: The id of this ConnectionStatisticsSnapshotDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionStatisticsSnapshotDTO.
        The id of the connection.

        :param id: The id of this ConnectionStatisticsSnapshotDTO.
        :type: str
        """

        self._id = id

    @property
    def predicted_millis_until_count_backpressure(self):
        """
        Gets the predicted_millis_until_count_backpressure of this ConnectionStatisticsSnapshotDTO.
        The predicted number of milliseconds before the connection will have backpressure applied, based on the queued count.

        :return: The predicted_millis_until_count_backpressure of this ConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._predicted_millis_until_count_backpressure

    @predicted_millis_until_count_backpressure.setter
    def predicted_millis_until_count_backpressure(self, predicted_millis_until_count_backpressure):
        """
        Sets the predicted_millis_until_count_backpressure of this ConnectionStatisticsSnapshotDTO.
        The predicted number of milliseconds before the connection will have backpressure applied, based on the queued count.

        :param predicted_millis_until_count_backpressure: The predicted_millis_until_count_backpressure of this ConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._predicted_millis_until_count_backpressure = predicted_millis_until_count_backpressure

    @property
    def predicted_millis_until_bytes_backpressure(self):
        """
        Gets the predicted_millis_until_bytes_backpressure of this ConnectionStatisticsSnapshotDTO.
        The predicted number of milliseconds before the connection will have backpressure applied, based on the total number of bytes in the queue.

        :return: The predicted_millis_until_bytes_backpressure of this ConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._predicted_millis_until_bytes_backpressure

    @predicted_millis_until_bytes_backpressure.setter
    def predicted_millis_until_bytes_backpressure(self, predicted_millis_until_bytes_backpressure):
        """
        Sets the predicted_millis_until_bytes_backpressure of this ConnectionStatisticsSnapshotDTO.
        The predicted number of milliseconds before the connection will have backpressure applied, based on the total number of bytes in the queue.

        :param predicted_millis_until_bytes_backpressure: The predicted_millis_until_bytes_backpressure of this ConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._predicted_millis_until_bytes_backpressure = predicted_millis_until_bytes_backpressure

    @property
    def predicted_count_at_next_interval(self):
        """
        Gets the predicted_count_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        The predicted number of queued objects at the next configured interval.

        :return: The predicted_count_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._predicted_count_at_next_interval

    @predicted_count_at_next_interval.setter
    def predicted_count_at_next_interval(self, predicted_count_at_next_interval):
        """
        Sets the predicted_count_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        The predicted number of queued objects at the next configured interval.

        :param predicted_count_at_next_interval: The predicted_count_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._predicted_count_at_next_interval = predicted_count_at_next_interval

    @property
    def predicted_bytes_at_next_interval(self):
        """
        Gets the predicted_bytes_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        The predicted total number of bytes in the queue at the next configured interval.

        :return: The predicted_bytes_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._predicted_bytes_at_next_interval

    @predicted_bytes_at_next_interval.setter
    def predicted_bytes_at_next_interval(self, predicted_bytes_at_next_interval):
        """
        Sets the predicted_bytes_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        The predicted total number of bytes in the queue at the next configured interval.

        :param predicted_bytes_at_next_interval: The predicted_bytes_at_next_interval of this ConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._predicted_bytes_at_next_interval = predicted_bytes_at_next_interval

    @property
    def predicted_percent_count(self):
        """
        Gets the predicted_percent_count of this ConnectionStatisticsSnapshotDTO.
        The predicted percentage of queued objects at the next configured interval.

        :return: The predicted_percent_count of this ConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._predicted_percent_count

    @predicted_percent_count.setter
    def predicted_percent_count(self, predicted_percent_count):
        """
        Sets the predicted_percent_count of this ConnectionStatisticsSnapshotDTO.
        The predicted percentage of queued objects at the next configured interval.

        :param predicted_percent_count: The predicted_percent_count of this ConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._predicted_percent_count = predicted_percent_count

    @property
    def predicted_percent_bytes(self):
        """
        Gets the predicted_percent_bytes of this ConnectionStatisticsSnapshotDTO.
        The predicted percentage of bytes in the queue against current threshold at the next configured interval.

        :return: The predicted_percent_bytes of this ConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._predicted_percent_bytes

    @predicted_percent_bytes.setter
    def predicted_percent_bytes(self, predicted_percent_bytes):
        """
        Sets the predicted_percent_bytes of this ConnectionStatisticsSnapshotDTO.
        The predicted percentage of bytes in the queue against current threshold at the next configured interval.

        :param predicted_percent_bytes: The predicted_percent_bytes of this ConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._predicted_percent_bytes = predicted_percent_bytes

    @property
    def prediction_interval_millis(self):
        """
        Gets the prediction_interval_millis of this ConnectionStatisticsSnapshotDTO.
        The prediction interval in seconds

        :return: The prediction_interval_millis of this ConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._prediction_interval_millis

    @prediction_interval_millis.setter
    def prediction_interval_millis(self, prediction_interval_millis):
        """
        Sets the prediction_interval_millis of this ConnectionStatisticsSnapshotDTO.
        The prediction interval in seconds

        :param prediction_interval_millis: The prediction_interval_millis of this ConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._prediction_interval_millis = prediction_interval_millis

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ConnectionStatisticsSnapshotDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
