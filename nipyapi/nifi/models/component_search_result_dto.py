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


class ComponentSearchResultDTO(object):
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
        'group_id': 'str',
        'parent_group': 'SearchResultGroupDTO',
        'versioned_group': 'SearchResultGroupDTO',
        'name': 'str',
        'matches': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'parent_group': 'parentGroup',
        'versioned_group': 'versionedGroup',
        'name': 'name',
        'matches': 'matches'
    }

    def __init__(self, id=None, group_id=None, parent_group=None, versioned_group=None, name=None, matches=None):
        """
        ComponentSearchResultDTO - a model defined in Swagger
        """

        self._id = None
        self._group_id = None
        self._parent_group = None
        self._versioned_group = None
        self._name = None
        self._matches = None

        if id is not None:
          self.id = id
        if group_id is not None:
          self.group_id = group_id
        if parent_group is not None:
          self.parent_group = parent_group
        if versioned_group is not None:
          self.versioned_group = versioned_group
        if name is not None:
          self.name = name
        if matches is not None:
          self.matches = matches

    @property
    def id(self):
        """
        Gets the id of this ComponentSearchResultDTO.
        The id of the component that matched the search.

        :return: The id of this ComponentSearchResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComponentSearchResultDTO.
        The id of the component that matched the search.

        :param id: The id of this ComponentSearchResultDTO.
        :type: str
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this ComponentSearchResultDTO.
        The group id of the component that matched the search.

        :return: The group_id of this ComponentSearchResultDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this ComponentSearchResultDTO.
        The group id of the component that matched the search.

        :param group_id: The group_id of this ComponentSearchResultDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def parent_group(self):
        """
        Gets the parent_group of this ComponentSearchResultDTO.
        The parent group of the component that matched the search.

        :return: The parent_group of this ComponentSearchResultDTO.
        :rtype: SearchResultGroupDTO
        """
        return self._parent_group

    @parent_group.setter
    def parent_group(self, parent_group):
        """
        Sets the parent_group of this ComponentSearchResultDTO.
        The parent group of the component that matched the search.

        :param parent_group: The parent_group of this ComponentSearchResultDTO.
        :type: SearchResultGroupDTO
        """

        self._parent_group = parent_group

    @property
    def versioned_group(self):
        """
        Gets the versioned_group of this ComponentSearchResultDTO.
        The nearest versioned ancestor group of the component that matched the search.

        :return: The versioned_group of this ComponentSearchResultDTO.
        :rtype: SearchResultGroupDTO
        """
        return self._versioned_group

    @versioned_group.setter
    def versioned_group(self, versioned_group):
        """
        Sets the versioned_group of this ComponentSearchResultDTO.
        The nearest versioned ancestor group of the component that matched the search.

        :param versioned_group: The versioned_group of this ComponentSearchResultDTO.
        :type: SearchResultGroupDTO
        """

        self._versioned_group = versioned_group

    @property
    def name(self):
        """
        Gets the name of this ComponentSearchResultDTO.
        The name of the component that matched the search.

        :return: The name of this ComponentSearchResultDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ComponentSearchResultDTO.
        The name of the component that matched the search.

        :param name: The name of this ComponentSearchResultDTO.
        :type: str
        """

        self._name = name

    @property
    def matches(self):
        """
        Gets the matches of this ComponentSearchResultDTO.
        What matched the search from the component.

        :return: The matches of this ComponentSearchResultDTO.
        :rtype: list[str]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """
        Sets the matches of this ComponentSearchResultDTO.
        What matched the search from the component.

        :param matches: The matches of this ComponentSearchResultDTO.
        :type: list[str]
        """

        self._matches = matches

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
        if not isinstance(other, ComponentSearchResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
