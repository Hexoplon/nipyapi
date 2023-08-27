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


class ProcessorStatusSnapshotEntity(object):
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
        'processor_status_snapshot': 'ProcessorStatusSnapshotDTO',
        'can_read': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'processor_status_snapshot': 'processorStatusSnapshot',
        'can_read': 'canRead'
    }

    def __init__(self, id=None, processor_status_snapshot=None, can_read=None):
        """
        ProcessorStatusSnapshotEntity - a model defined in Swagger
        """

        self._id = None
        self._processor_status_snapshot = None
        self._can_read = None

        if id is not None:
          self.id = id
        if processor_status_snapshot is not None:
          self.processor_status_snapshot = processor_status_snapshot
        if can_read is not None:
          self.can_read = can_read

    @property
    def id(self):
        """
        Gets the id of this ProcessorStatusSnapshotEntity.
        The id of the processor.

        :return: The id of this ProcessorStatusSnapshotEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessorStatusSnapshotEntity.
        The id of the processor.

        :param id: The id of this ProcessorStatusSnapshotEntity.
        :type: str
        """

        self._id = id

    @property
    def processor_status_snapshot(self):
        """
        Gets the processor_status_snapshot of this ProcessorStatusSnapshotEntity.

        :return: The processor_status_snapshot of this ProcessorStatusSnapshotEntity.
        :rtype: ProcessorStatusSnapshotDTO
        """
        return self._processor_status_snapshot

    @processor_status_snapshot.setter
    def processor_status_snapshot(self, processor_status_snapshot):
        """
        Sets the processor_status_snapshot of this ProcessorStatusSnapshotEntity.

        :param processor_status_snapshot: The processor_status_snapshot of this ProcessorStatusSnapshotEntity.
        :type: ProcessorStatusSnapshotDTO
        """

        self._processor_status_snapshot = processor_status_snapshot

    @property
    def can_read(self):
        """
        Gets the can_read of this ProcessorStatusSnapshotEntity.
        Indicates whether the user can read a given resource.

        :return: The can_read of this ProcessorStatusSnapshotEntity.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        """
        Sets the can_read of this ProcessorStatusSnapshotEntity.
        Indicates whether the user can read a given resource.

        :param can_read: The can_read of this ProcessorStatusSnapshotEntity.
        :type: bool
        """

        self._can_read = can_read

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
        if not isinstance(other, ProcessorStatusSnapshotEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
