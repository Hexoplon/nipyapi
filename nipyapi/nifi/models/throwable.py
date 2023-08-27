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


class Throwable(object):
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
        'cause': 'Throwable',
        'stack_trace': 'list[StackTraceElement]',
        'message': 'str',
        'suppressed': 'list[Throwable]',
        'localized_message': 'str'
    }

    attribute_map = {
        'cause': 'cause',
        'stack_trace': 'stackTrace',
        'message': 'message',
        'suppressed': 'suppressed',
        'localized_message': 'localizedMessage'
    }

    def __init__(self, cause=None, stack_trace=None, message=None, suppressed=None, localized_message=None):
        """
        Throwable - a model defined in Swagger
        """

        self._cause = None
        self._stack_trace = None
        self._message = None
        self._suppressed = None
        self._localized_message = None

        if cause is not None:
          self.cause = cause
        if stack_trace is not None:
          self.stack_trace = stack_trace
        if message is not None:
          self.message = message
        if suppressed is not None:
          self.suppressed = suppressed
        if localized_message is not None:
          self.localized_message = localized_message

    @property
    def cause(self):
        """
        Gets the cause of this Throwable.

        :return: The cause of this Throwable.
        :rtype: Throwable
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """
        Sets the cause of this Throwable.

        :param cause: The cause of this Throwable.
        :type: Throwable
        """

        self._cause = cause

    @property
    def stack_trace(self):
        """
        Gets the stack_trace of this Throwable.

        :return: The stack_trace of this Throwable.
        :rtype: list[StackTraceElement]
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """
        Sets the stack_trace of this Throwable.

        :param stack_trace: The stack_trace of this Throwable.
        :type: list[StackTraceElement]
        """

        self._stack_trace = stack_trace

    @property
    def message(self):
        """
        Gets the message of this Throwable.

        :return: The message of this Throwable.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Throwable.

        :param message: The message of this Throwable.
        :type: str
        """

        self._message = message

    @property
    def suppressed(self):
        """
        Gets the suppressed of this Throwable.

        :return: The suppressed of this Throwable.
        :rtype: list[Throwable]
        """
        return self._suppressed

    @suppressed.setter
    def suppressed(self, suppressed):
        """
        Sets the suppressed of this Throwable.

        :param suppressed: The suppressed of this Throwable.
        :type: list[Throwable]
        """

        self._suppressed = suppressed

    @property
    def localized_message(self):
        """
        Gets the localized_message of this Throwable.

        :return: The localized_message of this Throwable.
        :rtype: str
        """
        return self._localized_message

    @localized_message.setter
    def localized_message(self, localized_message):
        """
        Sets the localized_message of this Throwable.

        :param localized_message: The localized_message of this Throwable.
        :type: str
        """

        self._localized_message = localized_message

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
        if not isinstance(other, Throwable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
