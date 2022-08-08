# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.17.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VersionedFlowSnapshotMetadataEntity(object):
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
        'versioned_flow_snapshot_metadata': 'VersionedFlowSnapshotMetadata',
        'registry_id': 'str'
    }

    attribute_map = {
        'versioned_flow_snapshot_metadata': 'versionedFlowSnapshotMetadata',
        'registry_id': 'registryId'
    }

    def __init__(self, versioned_flow_snapshot_metadata=None, registry_id=None):
        """
        VersionedFlowSnapshotMetadataEntity - a model defined in Swagger
        """

        self._versioned_flow_snapshot_metadata = None
        self._registry_id = None

        if versioned_flow_snapshot_metadata is not None:
          self.versioned_flow_snapshot_metadata = versioned_flow_snapshot_metadata
        if registry_id is not None:
          self.registry_id = registry_id

    @property
    def versioned_flow_snapshot_metadata(self):
        """
        Gets the versioned_flow_snapshot_metadata of this VersionedFlowSnapshotMetadataEntity.
        The collection of versioned flow snapshot metadata

        :return: The versioned_flow_snapshot_metadata of this VersionedFlowSnapshotMetadataEntity.
        :rtype: VersionedFlowSnapshotMetadata
        """
        return self._versioned_flow_snapshot_metadata

    @versioned_flow_snapshot_metadata.setter
    def versioned_flow_snapshot_metadata(self, versioned_flow_snapshot_metadata):
        """
        Sets the versioned_flow_snapshot_metadata of this VersionedFlowSnapshotMetadataEntity.
        The collection of versioned flow snapshot metadata

        :param versioned_flow_snapshot_metadata: The versioned_flow_snapshot_metadata of this VersionedFlowSnapshotMetadataEntity.
        :type: VersionedFlowSnapshotMetadata
        """

        self._versioned_flow_snapshot_metadata = versioned_flow_snapshot_metadata

    @property
    def registry_id(self):
        """
        Gets the registry_id of this VersionedFlowSnapshotMetadataEntity.
        The ID of the Registry that this flow belongs to

        :return: The registry_id of this VersionedFlowSnapshotMetadataEntity.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        """
        Sets the registry_id of this VersionedFlowSnapshotMetadataEntity.
        The ID of the Registry that this flow belongs to

        :param registry_id: The registry_id of this VersionedFlowSnapshotMetadataEntity.
        :type: str
        """

        self._registry_id = registry_id

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
        if not isinstance(other, VersionedFlowSnapshotMetadataEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
