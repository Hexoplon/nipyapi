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


class StartVersionControlRequestEntity(object):
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
        'versioned_flow': 'VersionedFlowDTO',
        'process_group_revision': 'RevisionDTO'
    }

    attribute_map = {
        'versioned_flow': 'versionedFlow',
        'process_group_revision': 'processGroupRevision'
    }

    def __init__(self, versioned_flow=None, process_group_revision=None):
        """
        StartVersionControlRequestEntity - a model defined in Swagger
        """

        self._versioned_flow = None
        self._process_group_revision = None

        if versioned_flow is not None:
          self.versioned_flow = versioned_flow
        if process_group_revision is not None:
          self.process_group_revision = process_group_revision

    @property
    def versioned_flow(self):
        """
        Gets the versioned_flow of this StartVersionControlRequestEntity.
        The versioned flow

        :return: The versioned_flow of this StartVersionControlRequestEntity.
        :rtype: VersionedFlowDTO
        """
        return self._versioned_flow

    @versioned_flow.setter
    def versioned_flow(self, versioned_flow):
        """
        Sets the versioned_flow of this StartVersionControlRequestEntity.
        The versioned flow

        :param versioned_flow: The versioned_flow of this StartVersionControlRequestEntity.
        :type: VersionedFlowDTO
        """

        self._versioned_flow = versioned_flow

    @property
    def process_group_revision(self):
        """
        Gets the process_group_revision of this StartVersionControlRequestEntity.
        The Revision of the Process Group under Version Control

        :return: The process_group_revision of this StartVersionControlRequestEntity.
        :rtype: RevisionDTO
        """
        return self._process_group_revision

    @process_group_revision.setter
    def process_group_revision(self, process_group_revision):
        """
        Sets the process_group_revision of this StartVersionControlRequestEntity.
        The Revision of the Process Group under Version Control

        :param process_group_revision: The process_group_revision of this StartVersionControlRequestEntity.
        :type: RevisionDTO
        """

        self._process_group_revision = process_group_revision

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
        if not isinstance(other, StartVersionControlRequestEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
