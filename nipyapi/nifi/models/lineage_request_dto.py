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


class LineageRequestDTO(object):
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
        'event_id': 'int',
        'lineage_request_type': 'str',
        'uuid': 'str',
        'cluster_node_id': 'str'
    }

    attribute_map = {
        'event_id': 'eventId',
        'lineage_request_type': 'lineageRequestType',
        'uuid': 'uuid',
        'cluster_node_id': 'clusterNodeId'
    }

    def __init__(self, event_id=None, lineage_request_type=None, uuid=None, cluster_node_id=None):
        """
        LineageRequestDTO - a model defined in Swagger
        """

        self._event_id = None
        self._lineage_request_type = None
        self._uuid = None
        self._cluster_node_id = None

        if event_id is not None:
          self.event_id = event_id
        if lineage_request_type is not None:
          self.lineage_request_type = lineage_request_type
        if uuid is not None:
          self.uuid = uuid
        if cluster_node_id is not None:
          self.cluster_node_id = cluster_node_id

    @property
    def event_id(self):
        """
        Gets the event_id of this LineageRequestDTO.
        The event id that was used to generate this lineage, if applicable. The event id is allowed for any type of lineageRequestType. If the lineageRequestType is FLOWFILE and the flowfile uuid is also included in the request, the event id will be ignored.

        :return: The event_id of this LineageRequestDTO.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this LineageRequestDTO.
        The event id that was used to generate this lineage, if applicable. The event id is allowed for any type of lineageRequestType. If the lineageRequestType is FLOWFILE and the flowfile uuid is also included in the request, the event id will be ignored.

        :param event_id: The event_id of this LineageRequestDTO.
        :type: int
        """

        self._event_id = event_id

    @property
    def lineage_request_type(self):
        """
        Gets the lineage_request_type of this LineageRequestDTO.
        The type of lineage request. PARENTS will return the lineage for the flowfiles that are parents of the specified event. CHILDREN will return the lineage for the flowfiles that are children of the specified event. FLOWFILE will return the lineage for the specified flowfile.

        :return: The lineage_request_type of this LineageRequestDTO.
        :rtype: str
        """
        return self._lineage_request_type

    @lineage_request_type.setter
    def lineage_request_type(self, lineage_request_type):
        """
        Sets the lineage_request_type of this LineageRequestDTO.
        The type of lineage request. PARENTS will return the lineage for the flowfiles that are parents of the specified event. CHILDREN will return the lineage for the flowfiles that are children of the specified event. FLOWFILE will return the lineage for the specified flowfile.

        :param lineage_request_type: The lineage_request_type of this LineageRequestDTO.
        :type: str
        """
        allowed_values = ["PARENTS", "CHILDREN", "and FLOWFILE"]
        if lineage_request_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lineage_request_type` ({0}), must be one of {1}"
                .format(lineage_request_type, allowed_values)
            )

        self._lineage_request_type = lineage_request_type

    @property
    def uuid(self):
        """
        Gets the uuid of this LineageRequestDTO.
        The flowfile uuid that was used to generate the lineage. The flowfile uuid is only allowed when the lineageRequestType is FLOWFILE and will take precedence over event id.

        :return: The uuid of this LineageRequestDTO.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this LineageRequestDTO.
        The flowfile uuid that was used to generate the lineage. The flowfile uuid is only allowed when the lineageRequestType is FLOWFILE and will take precedence over event id.

        :param uuid: The uuid of this LineageRequestDTO.
        :type: str
        """

        self._uuid = uuid

    @property
    def cluster_node_id(self):
        """
        Gets the cluster_node_id of this LineageRequestDTO.
        The id of the node where this lineage originated if clustered.

        :return: The cluster_node_id of this LineageRequestDTO.
        :rtype: str
        """
        return self._cluster_node_id

    @cluster_node_id.setter
    def cluster_node_id(self, cluster_node_id):
        """
        Sets the cluster_node_id of this LineageRequestDTO.
        The id of the node where this lineage originated if clustered.

        :param cluster_node_id: The cluster_node_id of this LineageRequestDTO.
        :type: str
        """

        self._cluster_node_id = cluster_node_id

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
        if not isinstance(other, LineageRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
