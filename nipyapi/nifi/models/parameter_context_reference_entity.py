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


class ParameterContextReferenceEntity(object):
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
        'permissions': 'PermissionsDTO',
        'component': 'ParameterContextReferenceDTO'
    }

    attribute_map = {
        'id': 'id',
        'permissions': 'permissions',
        'component': 'component'
    }

    def __init__(self, id=None, permissions=None, component=None):
        """
        ParameterContextReferenceEntity - a model defined in Swagger
        """

        self._id = None
        self._permissions = None
        self._component = None

        if id is not None:
          self.id = id
        if permissions is not None:
          self.permissions = permissions
        if component is not None:
          self.component = component

    @property
    def id(self):
        """
        Gets the id of this ParameterContextReferenceEntity.
        The id of the component.

        :return: The id of this ParameterContextReferenceEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ParameterContextReferenceEntity.
        The id of the component.

        :param id: The id of this ParameterContextReferenceEntity.
        :type: str
        """

        self._id = id

    @property
    def permissions(self):
        """
        Gets the permissions of this ParameterContextReferenceEntity.
        The permissions for this component.

        :return: The permissions of this ParameterContextReferenceEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this ParameterContextReferenceEntity.
        The permissions for this component.

        :param permissions: The permissions of this ParameterContextReferenceEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def component(self):
        """
        Gets the component of this ParameterContextReferenceEntity.

        :return: The component of this ParameterContextReferenceEntity.
        :rtype: ParameterContextReferenceDTO
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this ParameterContextReferenceEntity.

        :param component: The component of this ParameterContextReferenceEntity.
        :type: ParameterContextReferenceDTO
        """

        self._component = component

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
        if not isinstance(other, ParameterContextReferenceEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
