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


class AccessPolicyDTO(object):
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
        'versioned_component_id': 'str',
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'resource': 'str',
        'action': 'str',
        'component_reference': 'ComponentReferenceEntity',
        'configurable': 'bool',
        'users': 'list[TenantEntity]',
        'user_groups': 'list[TenantEntity]'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'resource': 'resource',
        'action': 'action',
        'component_reference': 'componentReference',
        'configurable': 'configurable',
        'users': 'users',
        'user_groups': 'userGroups'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, resource=None, action=None, component_reference=None, configurable=None, users=None, user_groups=None):
        """
        AccessPolicyDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._resource = None
        self._action = None
        self._component_reference = None
        self._configurable = None
        self._users = None
        self._user_groups = None

        if id is not None:
          self.id = id
        if versioned_component_id is not None:
          self.versioned_component_id = versioned_component_id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if resource is not None:
          self.resource = resource
        if action is not None:
          self.action = action
        if component_reference is not None:
          self.component_reference = component_reference
        if configurable is not None:
          self.configurable = configurable
        if users is not None:
          self.users = users
        if user_groups is not None:
          self.user_groups = user_groups

    @property
    def id(self):
        """
        Gets the id of this AccessPolicyDTO.
        The id of the component.

        :return: The id of this AccessPolicyDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccessPolicyDTO.
        The id of the component.

        :param id: The id of this AccessPolicyDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this AccessPolicyDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this AccessPolicyDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this AccessPolicyDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this AccessPolicyDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this AccessPolicyDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this AccessPolicyDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this AccessPolicyDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this AccessPolicyDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this AccessPolicyDTO.
        The position of this component in the UI if applicable.

        :return: The position of this AccessPolicyDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this AccessPolicyDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this AccessPolicyDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def resource(self):
        """
        Gets the resource of this AccessPolicyDTO.
        The resource for this access policy.

        :return: The resource of this AccessPolicyDTO.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this AccessPolicyDTO.
        The resource for this access policy.

        :param resource: The resource of this AccessPolicyDTO.
        :type: str
        """

        self._resource = resource

    @property
    def action(self):
        """
        Gets the action of this AccessPolicyDTO.
        The action associated with this access policy.

        :return: The action of this AccessPolicyDTO.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AccessPolicyDTO.
        The action associated with this access policy.

        :param action: The action of this AccessPolicyDTO.
        :type: str
        """
        allowed_values = ["read", "write"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def component_reference(self):
        """
        Gets the component_reference of this AccessPolicyDTO.
        Component this policy references if applicable.

        :return: The component_reference of this AccessPolicyDTO.
        :rtype: ComponentReferenceEntity
        """
        return self._component_reference

    @component_reference.setter
    def component_reference(self, component_reference):
        """
        Sets the component_reference of this AccessPolicyDTO.
        Component this policy references if applicable.

        :param component_reference: The component_reference of this AccessPolicyDTO.
        :type: ComponentReferenceEntity
        """

        self._component_reference = component_reference

    @property
    def configurable(self):
        """
        Gets the configurable of this AccessPolicyDTO.
        Whether this policy is configurable.

        :return: The configurable of this AccessPolicyDTO.
        :rtype: bool
        """
        return self._configurable

    @configurable.setter
    def configurable(self, configurable):
        """
        Sets the configurable of this AccessPolicyDTO.
        Whether this policy is configurable.

        :param configurable: The configurable of this AccessPolicyDTO.
        :type: bool
        """

        self._configurable = configurable

    @property
    def users(self):
        """
        Gets the users of this AccessPolicyDTO.
        The set of user IDs associated with this access policy.

        :return: The users of this AccessPolicyDTO.
        :rtype: list[TenantEntity]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this AccessPolicyDTO.
        The set of user IDs associated with this access policy.

        :param users: The users of this AccessPolicyDTO.
        :type: list[TenantEntity]
        """

        self._users = users

    @property
    def user_groups(self):
        """
        Gets the user_groups of this AccessPolicyDTO.
        The set of user group IDs associated with this access policy.

        :return: The user_groups of this AccessPolicyDTO.
        :rtype: list[TenantEntity]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """
        Sets the user_groups of this AccessPolicyDTO.
        The set of user group IDs associated with this access policy.

        :param user_groups: The user_groups of this AccessPolicyDTO.
        :type: list[TenantEntity]
        """

        self._user_groups = user_groups

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
        if not isinstance(other, AccessPolicyDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
