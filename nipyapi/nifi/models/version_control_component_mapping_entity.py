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


class VersionControlComponentMappingEntity(object):
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
        'version_control_component_mapping': 'dict(str, str)',
        'process_group_revision': 'RevisionDTO',
        'version_control_information': 'VersionControlInformationDTO'
    }

    attribute_map = {
        'version_control_component_mapping': 'versionControlComponentMapping',
        'process_group_revision': 'processGroupRevision',
        'version_control_information': 'versionControlInformation'
    }

    def __init__(self, version_control_component_mapping=None, process_group_revision=None, version_control_information=None):
        """
        VersionControlComponentMappingEntity - a model defined in Swagger
        """

        self._version_control_component_mapping = None
        self._process_group_revision = None
        self._version_control_information = None

        if version_control_component_mapping is not None:
          self.version_control_component_mapping = version_control_component_mapping
        if process_group_revision is not None:
          self.process_group_revision = process_group_revision
        if version_control_information is not None:
          self.version_control_information = version_control_information

    @property
    def version_control_component_mapping(self):
        """
        Gets the version_control_component_mapping of this VersionControlComponentMappingEntity.
        The mapping of Versioned Component Identifiers to instance ID's

        :return: The version_control_component_mapping of this VersionControlComponentMappingEntity.
        :rtype: dict(str, str)
        """
        return self._version_control_component_mapping

    @version_control_component_mapping.setter
    def version_control_component_mapping(self, version_control_component_mapping):
        """
        Sets the version_control_component_mapping of this VersionControlComponentMappingEntity.
        The mapping of Versioned Component Identifiers to instance ID's

        :param version_control_component_mapping: The version_control_component_mapping of this VersionControlComponentMappingEntity.
        :type: dict(str, str)
        """

        self._version_control_component_mapping = version_control_component_mapping

    @property
    def process_group_revision(self):
        """
        Gets the process_group_revision of this VersionControlComponentMappingEntity.
        The revision of the Process Group

        :return: The process_group_revision of this VersionControlComponentMappingEntity.
        :rtype: RevisionDTO
        """
        return self._process_group_revision

    @process_group_revision.setter
    def process_group_revision(self, process_group_revision):
        """
        Sets the process_group_revision of this VersionControlComponentMappingEntity.
        The revision of the Process Group

        :param process_group_revision: The process_group_revision of this VersionControlComponentMappingEntity.
        :type: RevisionDTO
        """

        self._process_group_revision = process_group_revision

    @property
    def version_control_information(self):
        """
        Gets the version_control_information of this VersionControlComponentMappingEntity.
        The Version Control information

        :return: The version_control_information of this VersionControlComponentMappingEntity.
        :rtype: VersionControlInformationDTO
        """
        return self._version_control_information

    @version_control_information.setter
    def version_control_information(self, version_control_information):
        """
        Sets the version_control_information of this VersionControlComponentMappingEntity.
        The Version Control information

        :param version_control_information: The version_control_information of this VersionControlComponentMappingEntity.
        :type: VersionControlInformationDTO
        """

        self._version_control_information = version_control_information

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
        if not isinstance(other, VersionControlComponentMappingEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
