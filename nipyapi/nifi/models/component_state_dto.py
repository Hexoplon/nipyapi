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


class ComponentStateDTO(object):
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
        'state_description': 'str',
        'cluster_state': 'StateMapDTO',
        'local_state': 'StateMapDTO'
    }

    attribute_map = {
        'component_id': 'componentId',
        'state_description': 'stateDescription',
        'cluster_state': 'clusterState',
        'local_state': 'localState'
    }

    def __init__(self, component_id=None, state_description=None, cluster_state=None, local_state=None):
        """
        ComponentStateDTO - a model defined in Swagger
        """

        self._component_id = None
        self._state_description = None
        self._cluster_state = None
        self._local_state = None

        if component_id is not None:
          self.component_id = component_id
        if state_description is not None:
          self.state_description = state_description
        if cluster_state is not None:
          self.cluster_state = cluster_state
        if local_state is not None:
          self.local_state = local_state

    @property
    def component_id(self):
        """
        Gets the component_id of this ComponentStateDTO.
        The component identifier.

        :return: The component_id of this ComponentStateDTO.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """
        Sets the component_id of this ComponentStateDTO.
        The component identifier.

        :param component_id: The component_id of this ComponentStateDTO.
        :type: str
        """

        self._component_id = component_id

    @property
    def state_description(self):
        """
        Gets the state_description of this ComponentStateDTO.
        Description of the state this component persists.

        :return: The state_description of this ComponentStateDTO.
        :rtype: str
        """
        return self._state_description

    @state_description.setter
    def state_description(self, state_description):
        """
        Sets the state_description of this ComponentStateDTO.
        Description of the state this component persists.

        :param state_description: The state_description of this ComponentStateDTO.
        :type: str
        """

        self._state_description = state_description

    @property
    def cluster_state(self):
        """
        Gets the cluster_state of this ComponentStateDTO.
        The cluster state for this component, or null if this NiFi is a standalone instance.

        :return: The cluster_state of this ComponentStateDTO.
        :rtype: StateMapDTO
        """
        return self._cluster_state

    @cluster_state.setter
    def cluster_state(self, cluster_state):
        """
        Sets the cluster_state of this ComponentStateDTO.
        The cluster state for this component, or null if this NiFi is a standalone instance.

        :param cluster_state: The cluster_state of this ComponentStateDTO.
        :type: StateMapDTO
        """

        self._cluster_state = cluster_state

    @property
    def local_state(self):
        """
        Gets the local_state of this ComponentStateDTO.
        The local state for this component.

        :return: The local_state of this ComponentStateDTO.
        :rtype: StateMapDTO
        """
        return self._local_state

    @local_state.setter
    def local_state(self, local_state):
        """
        Sets the local_state of this ComponentStateDTO.
        The local state for this component.

        :param local_state: The local_state of this ComponentStateDTO.
        :type: StateMapDTO
        """

        self._local_state = local_state

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
        if not isinstance(other, ComponentStateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
