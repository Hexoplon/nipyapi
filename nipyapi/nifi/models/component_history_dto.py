# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.6.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ComponentHistoryDTO(object):
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
        'component_id': 'str',
        'property_history': 'dict(str, PropertyHistoryDTO)'
    }

    attribute_map = {
        'component_id': 'componentId',
        'property_history': 'propertyHistory'
    }

    def __init__(self, component_id=None, property_history=None):
        """
        ComponentHistoryDTO - a model defined in Swagger
        """

        self._component_id = None
        self._property_history = None

        if component_id is not None:
          self.component_id = component_id
        if property_history is not None:
          self.property_history = property_history

    @property
    def component_id(self):
        """
        Gets the component_id of this ComponentHistoryDTO.
        The component id.

        :return: The component_id of this ComponentHistoryDTO.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """
        Sets the component_id of this ComponentHistoryDTO.
        The component id.

        :param component_id: The component_id of this ComponentHistoryDTO.
        :type: str
        """

        self._component_id = component_id

    @property
    def property_history(self):
        """
        Gets the property_history of this ComponentHistoryDTO.
        The history for the properties of the component.

        :return: The property_history of this ComponentHistoryDTO.
        :rtype: dict(str, PropertyHistoryDTO)
        """
        return self._property_history

    @property_history.setter
    def property_history(self, property_history):
        """
        Sets the property_history of this ComponentHistoryDTO.
        The history for the properties of the component.

        :param property_history: The property_history of this ComponentHistoryDTO.
        :type: dict(str, PropertyHistoryDTO)
        """

        self._property_history = property_history

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
        if not isinstance(other, ComponentHistoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
