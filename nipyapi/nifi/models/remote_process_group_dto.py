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


class RemoteProcessGroupDTO(object):
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
        'target_uri': 'str',
        'target_uris': 'str',
        'target_secure': 'bool',
        'name': 'str',
        'comments': 'str',
        'communications_timeout': 'str',
        'yield_duration': 'str',
        'transport_protocol': 'str',
        'local_network_interface': 'str',
        'proxy_host': 'str',
        'proxy_port': 'int',
        'proxy_user': 'str',
        'proxy_password': 'str',
        'authorization_issues': 'list[str]',
        'validation_errors': 'list[str]',
        'transmitting': 'bool',
        'input_port_count': 'int',
        'output_port_count': 'int',
        'active_remote_input_port_count': 'int',
        'inactive_remote_input_port_count': 'int',
        'active_remote_output_port_count': 'int',
        'inactive_remote_output_port_count': 'int',
        'flow_refreshed': 'str',
        'contents': 'RemoteProcessGroupContentsDTO'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'target_uri': 'targetUri',
        'target_uris': 'targetUris',
        'target_secure': 'targetSecure',
        'name': 'name',
        'comments': 'comments',
        'communications_timeout': 'communicationsTimeout',
        'yield_duration': 'yieldDuration',
        'transport_protocol': 'transportProtocol',
        'local_network_interface': 'localNetworkInterface',
        'proxy_host': 'proxyHost',
        'proxy_port': 'proxyPort',
        'proxy_user': 'proxyUser',
        'proxy_password': 'proxyPassword',
        'authorization_issues': 'authorizationIssues',
        'validation_errors': 'validationErrors',
        'transmitting': 'transmitting',
        'input_port_count': 'inputPortCount',
        'output_port_count': 'outputPortCount',
        'active_remote_input_port_count': 'activeRemoteInputPortCount',
        'inactive_remote_input_port_count': 'inactiveRemoteInputPortCount',
        'active_remote_output_port_count': 'activeRemoteOutputPortCount',
        'inactive_remote_output_port_count': 'inactiveRemoteOutputPortCount',
        'flow_refreshed': 'flowRefreshed',
        'contents': 'contents'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, target_uri=None, target_uris=None, target_secure=None, name=None, comments=None, communications_timeout=None, yield_duration=None, transport_protocol=None, local_network_interface=None, proxy_host=None, proxy_port=None, proxy_user=None, proxy_password=None, authorization_issues=None, validation_errors=None, transmitting=None, input_port_count=None, output_port_count=None, active_remote_input_port_count=None, inactive_remote_input_port_count=None, active_remote_output_port_count=None, inactive_remote_output_port_count=None, flow_refreshed=None, contents=None):
        """
        RemoteProcessGroupDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._target_uri = None
        self._target_uris = None
        self._target_secure = None
        self._name = None
        self._comments = None
        self._communications_timeout = None
        self._yield_duration = None
        self._transport_protocol = None
        self._local_network_interface = None
        self._proxy_host = None
        self._proxy_port = None
        self._proxy_user = None
        self._proxy_password = None
        self._authorization_issues = None
        self._validation_errors = None
        self._transmitting = None
        self._input_port_count = None
        self._output_port_count = None
        self._active_remote_input_port_count = None
        self._inactive_remote_input_port_count = None
        self._active_remote_output_port_count = None
        self._inactive_remote_output_port_count = None
        self._flow_refreshed = None
        self._contents = None

        if id is not None:
          self.id = id
        if versioned_component_id is not None:
          self.versioned_component_id = versioned_component_id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if target_uri is not None:
          self.target_uri = target_uri
        if target_uris is not None:
          self.target_uris = target_uris
        if target_secure is not None:
          self.target_secure = target_secure
        if name is not None:
          self.name = name
        if comments is not None:
          self.comments = comments
        if communications_timeout is not None:
          self.communications_timeout = communications_timeout
        if yield_duration is not None:
          self.yield_duration = yield_duration
        if transport_protocol is not None:
          self.transport_protocol = transport_protocol
        if local_network_interface is not None:
          self.local_network_interface = local_network_interface
        if proxy_host is not None:
          self.proxy_host = proxy_host
        if proxy_port is not None:
          self.proxy_port = proxy_port
        if proxy_user is not None:
          self.proxy_user = proxy_user
        if proxy_password is not None:
          self.proxy_password = proxy_password
        if authorization_issues is not None:
          self.authorization_issues = authorization_issues
        if validation_errors is not None:
          self.validation_errors = validation_errors
        if transmitting is not None:
          self.transmitting = transmitting
        if input_port_count is not None:
          self.input_port_count = input_port_count
        if output_port_count is not None:
          self.output_port_count = output_port_count
        if active_remote_input_port_count is not None:
          self.active_remote_input_port_count = active_remote_input_port_count
        if inactive_remote_input_port_count is not None:
          self.inactive_remote_input_port_count = inactive_remote_input_port_count
        if active_remote_output_port_count is not None:
          self.active_remote_output_port_count = active_remote_output_port_count
        if inactive_remote_output_port_count is not None:
          self.inactive_remote_output_port_count = inactive_remote_output_port_count
        if flow_refreshed is not None:
          self.flow_refreshed = flow_refreshed
        if contents is not None:
          self.contents = contents

    @property
    def id(self):
        """
        Gets the id of this RemoteProcessGroupDTO.
        The id of the component.

        :return: The id of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RemoteProcessGroupDTO.
        The id of the component.

        :param id: The id of this RemoteProcessGroupDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this RemoteProcessGroupDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this RemoteProcessGroupDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this RemoteProcessGroupDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this RemoteProcessGroupDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this RemoteProcessGroupDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this RemoteProcessGroupDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this RemoteProcessGroupDTO.
        The position of this component in the UI if applicable.

        :return: The position of this RemoteProcessGroupDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this RemoteProcessGroupDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this RemoteProcessGroupDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def target_uri(self):
        """
        Gets the target_uri of this RemoteProcessGroupDTO.
        The target URI of the remote process group. If target uri is not set, but uris are set, then returns the first url in the urls. If neither target uri nor uris are set, then returns null.

        :return: The target_uri of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._target_uri

    @target_uri.setter
    def target_uri(self, target_uri):
        """
        Sets the target_uri of this RemoteProcessGroupDTO.
        The target URI of the remote process group. If target uri is not set, but uris are set, then returns the first url in the urls. If neither target uri nor uris are set, then returns null.

        :param target_uri: The target_uri of this RemoteProcessGroupDTO.
        :type: str
        """

        self._target_uri = target_uri

    @property
    def target_uris(self):
        """
        Gets the target_uris of this RemoteProcessGroupDTO.
        The target URI of the remote process group. If target uris is not set but target uri is set, then returns a collection containing the single target uri. If neither target uris nor uris are set, then returns null.

        :return: The target_uris of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._target_uris

    @target_uris.setter
    def target_uris(self, target_uris):
        """
        Sets the target_uris of this RemoteProcessGroupDTO.
        The target URI of the remote process group. If target uris is not set but target uri is set, then returns a collection containing the single target uri. If neither target uris nor uris are set, then returns null.

        :param target_uris: The target_uris of this RemoteProcessGroupDTO.
        :type: str
        """

        self._target_uris = target_uris

    @property
    def target_secure(self):
        """
        Gets the target_secure of this RemoteProcessGroupDTO.
        Whether the target is running securely.

        :return: The target_secure of this RemoteProcessGroupDTO.
        :rtype: bool
        """
        return self._target_secure

    @target_secure.setter
    def target_secure(self, target_secure):
        """
        Sets the target_secure of this RemoteProcessGroupDTO.
        Whether the target is running securely.

        :param target_secure: The target_secure of this RemoteProcessGroupDTO.
        :type: bool
        """

        self._target_secure = target_secure

    @property
    def name(self):
        """
        Gets the name of this RemoteProcessGroupDTO.
        The name of the remote process group.

        :return: The name of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RemoteProcessGroupDTO.
        The name of the remote process group.

        :param name: The name of this RemoteProcessGroupDTO.
        :type: str
        """

        self._name = name

    @property
    def comments(self):
        """
        Gets the comments of this RemoteProcessGroupDTO.
        The comments for the remote process group.

        :return: The comments of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this RemoteProcessGroupDTO.
        The comments for the remote process group.

        :param comments: The comments of this RemoteProcessGroupDTO.
        :type: str
        """

        self._comments = comments

    @property
    def communications_timeout(self):
        """
        Gets the communications_timeout of this RemoteProcessGroupDTO.
        The time period used for the timeout when communicating with the target.

        :return: The communications_timeout of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._communications_timeout

    @communications_timeout.setter
    def communications_timeout(self, communications_timeout):
        """
        Sets the communications_timeout of this RemoteProcessGroupDTO.
        The time period used for the timeout when communicating with the target.

        :param communications_timeout: The communications_timeout of this RemoteProcessGroupDTO.
        :type: str
        """

        self._communications_timeout = communications_timeout

    @property
    def yield_duration(self):
        """
        Gets the yield_duration of this RemoteProcessGroupDTO.
        When yielding, this amount of time must elapse before the remote process group is scheduled again.

        :return: The yield_duration of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._yield_duration

    @yield_duration.setter
    def yield_duration(self, yield_duration):
        """
        Sets the yield_duration of this RemoteProcessGroupDTO.
        When yielding, this amount of time must elapse before the remote process group is scheduled again.

        :param yield_duration: The yield_duration of this RemoteProcessGroupDTO.
        :type: str
        """

        self._yield_duration = yield_duration

    @property
    def transport_protocol(self):
        """
        Gets the transport_protocol of this RemoteProcessGroupDTO.

        :return: The transport_protocol of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._transport_protocol

    @transport_protocol.setter
    def transport_protocol(self, transport_protocol):
        """
        Sets the transport_protocol of this RemoteProcessGroupDTO.

        :param transport_protocol: The transport_protocol of this RemoteProcessGroupDTO.
        :type: str
        """

        self._transport_protocol = transport_protocol

    @property
    def local_network_interface(self):
        """
        Gets the local_network_interface of this RemoteProcessGroupDTO.
        The local network interface to send/receive data. If not specified, any local address is used. If clustered, all nodes must have an interface with this identifier.

        :return: The local_network_interface of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._local_network_interface

    @local_network_interface.setter
    def local_network_interface(self, local_network_interface):
        """
        Sets the local_network_interface of this RemoteProcessGroupDTO.
        The local network interface to send/receive data. If not specified, any local address is used. If clustered, all nodes must have an interface with this identifier.

        :param local_network_interface: The local_network_interface of this RemoteProcessGroupDTO.
        :type: str
        """

        self._local_network_interface = local_network_interface

    @property
    def proxy_host(self):
        """
        Gets the proxy_host of this RemoteProcessGroupDTO.

        :return: The proxy_host of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        """
        Sets the proxy_host of this RemoteProcessGroupDTO.

        :param proxy_host: The proxy_host of this RemoteProcessGroupDTO.
        :type: str
        """

        self._proxy_host = proxy_host

    @property
    def proxy_port(self):
        """
        Gets the proxy_port of this RemoteProcessGroupDTO.

        :return: The proxy_port of this RemoteProcessGroupDTO.
        :rtype: int
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        """
        Sets the proxy_port of this RemoteProcessGroupDTO.

        :param proxy_port: The proxy_port of this RemoteProcessGroupDTO.
        :type: int
        """

        self._proxy_port = proxy_port

    @property
    def proxy_user(self):
        """
        Gets the proxy_user of this RemoteProcessGroupDTO.

        :return: The proxy_user of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        """
        Sets the proxy_user of this RemoteProcessGroupDTO.

        :param proxy_user: The proxy_user of this RemoteProcessGroupDTO.
        :type: str
        """

        self._proxy_user = proxy_user

    @property
    def proxy_password(self):
        """
        Gets the proxy_password of this RemoteProcessGroupDTO.

        :return: The proxy_password of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, proxy_password):
        """
        Sets the proxy_password of this RemoteProcessGroupDTO.

        :param proxy_password: The proxy_password of this RemoteProcessGroupDTO.
        :type: str
        """

        self._proxy_password = proxy_password

    @property
    def authorization_issues(self):
        """
        Gets the authorization_issues of this RemoteProcessGroupDTO.
        Any remote authorization issues for the remote process group.

        :return: The authorization_issues of this RemoteProcessGroupDTO.
        :rtype: list[str]
        """
        return self._authorization_issues

    @authorization_issues.setter
    def authorization_issues(self, authorization_issues):
        """
        Sets the authorization_issues of this RemoteProcessGroupDTO.
        Any remote authorization issues for the remote process group.

        :param authorization_issues: The authorization_issues of this RemoteProcessGroupDTO.
        :type: list[str]
        """

        self._authorization_issues = authorization_issues

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this RemoteProcessGroupDTO.
        The validation errors for the remote process group. These validation errors represent the problems with the remote process group that must be resolved before it can transmit.

        :return: The validation_errors of this RemoteProcessGroupDTO.
        :rtype: list[str]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this RemoteProcessGroupDTO.
        The validation errors for the remote process group. These validation errors represent the problems with the remote process group that must be resolved before it can transmit.

        :param validation_errors: The validation_errors of this RemoteProcessGroupDTO.
        :type: list[str]
        """

        self._validation_errors = validation_errors

    @property
    def transmitting(self):
        """
        Gets the transmitting of this RemoteProcessGroupDTO.
        Whether the remote process group is actively transmitting.

        :return: The transmitting of this RemoteProcessGroupDTO.
        :rtype: bool
        """
        return self._transmitting

    @transmitting.setter
    def transmitting(self, transmitting):
        """
        Sets the transmitting of this RemoteProcessGroupDTO.
        Whether the remote process group is actively transmitting.

        :param transmitting: The transmitting of this RemoteProcessGroupDTO.
        :type: bool
        """

        self._transmitting = transmitting

    @property
    def input_port_count(self):
        """
        Gets the input_port_count of this RemoteProcessGroupDTO.
        The number of remote input ports currently available on the target.

        :return: The input_port_count of this RemoteProcessGroupDTO.
        :rtype: int
        """
        return self._input_port_count

    @input_port_count.setter
    def input_port_count(self, input_port_count):
        """
        Sets the input_port_count of this RemoteProcessGroupDTO.
        The number of remote input ports currently available on the target.

        :param input_port_count: The input_port_count of this RemoteProcessGroupDTO.
        :type: int
        """

        self._input_port_count = input_port_count

    @property
    def output_port_count(self):
        """
        Gets the output_port_count of this RemoteProcessGroupDTO.
        The number of remote output ports currently available on the target.

        :return: The output_port_count of this RemoteProcessGroupDTO.
        :rtype: int
        """
        return self._output_port_count

    @output_port_count.setter
    def output_port_count(self, output_port_count):
        """
        Sets the output_port_count of this RemoteProcessGroupDTO.
        The number of remote output ports currently available on the target.

        :param output_port_count: The output_port_count of this RemoteProcessGroupDTO.
        :type: int
        """

        self._output_port_count = output_port_count

    @property
    def active_remote_input_port_count(self):
        """
        Gets the active_remote_input_port_count of this RemoteProcessGroupDTO.
        The number of active remote input ports.

        :return: The active_remote_input_port_count of this RemoteProcessGroupDTO.
        :rtype: int
        """
        return self._active_remote_input_port_count

    @active_remote_input_port_count.setter
    def active_remote_input_port_count(self, active_remote_input_port_count):
        """
        Sets the active_remote_input_port_count of this RemoteProcessGroupDTO.
        The number of active remote input ports.

        :param active_remote_input_port_count: The active_remote_input_port_count of this RemoteProcessGroupDTO.
        :type: int
        """

        self._active_remote_input_port_count = active_remote_input_port_count

    @property
    def inactive_remote_input_port_count(self):
        """
        Gets the inactive_remote_input_port_count of this RemoteProcessGroupDTO.
        The number of inactive remote input ports.

        :return: The inactive_remote_input_port_count of this RemoteProcessGroupDTO.
        :rtype: int
        """
        return self._inactive_remote_input_port_count

    @inactive_remote_input_port_count.setter
    def inactive_remote_input_port_count(self, inactive_remote_input_port_count):
        """
        Sets the inactive_remote_input_port_count of this RemoteProcessGroupDTO.
        The number of inactive remote input ports.

        :param inactive_remote_input_port_count: The inactive_remote_input_port_count of this RemoteProcessGroupDTO.
        :type: int
        """

        self._inactive_remote_input_port_count = inactive_remote_input_port_count

    @property
    def active_remote_output_port_count(self):
        """
        Gets the active_remote_output_port_count of this RemoteProcessGroupDTO.
        The number of active remote output ports.

        :return: The active_remote_output_port_count of this RemoteProcessGroupDTO.
        :rtype: int
        """
        return self._active_remote_output_port_count

    @active_remote_output_port_count.setter
    def active_remote_output_port_count(self, active_remote_output_port_count):
        """
        Sets the active_remote_output_port_count of this RemoteProcessGroupDTO.
        The number of active remote output ports.

        :param active_remote_output_port_count: The active_remote_output_port_count of this RemoteProcessGroupDTO.
        :type: int
        """

        self._active_remote_output_port_count = active_remote_output_port_count

    @property
    def inactive_remote_output_port_count(self):
        """
        Gets the inactive_remote_output_port_count of this RemoteProcessGroupDTO.
        The number of inactive remote output ports.

        :return: The inactive_remote_output_port_count of this RemoteProcessGroupDTO.
        :rtype: int
        """
        return self._inactive_remote_output_port_count

    @inactive_remote_output_port_count.setter
    def inactive_remote_output_port_count(self, inactive_remote_output_port_count):
        """
        Sets the inactive_remote_output_port_count of this RemoteProcessGroupDTO.
        The number of inactive remote output ports.

        :param inactive_remote_output_port_count: The inactive_remote_output_port_count of this RemoteProcessGroupDTO.
        :type: int
        """

        self._inactive_remote_output_port_count = inactive_remote_output_port_count

    @property
    def flow_refreshed(self):
        """
        Gets the flow_refreshed of this RemoteProcessGroupDTO.
        The timestamp when this remote process group was last refreshed.

        :return: The flow_refreshed of this RemoteProcessGroupDTO.
        :rtype: str
        """
        return self._flow_refreshed

    @flow_refreshed.setter
    def flow_refreshed(self, flow_refreshed):
        """
        Sets the flow_refreshed of this RemoteProcessGroupDTO.
        The timestamp when this remote process group was last refreshed.

        :param flow_refreshed: The flow_refreshed of this RemoteProcessGroupDTO.
        :type: str
        """

        self._flow_refreshed = flow_refreshed

    @property
    def contents(self):
        """
        Gets the contents of this RemoteProcessGroupDTO.
        The contents of the remote process group. Will contain available input/output ports.

        :return: The contents of this RemoteProcessGroupDTO.
        :rtype: RemoteProcessGroupContentsDTO
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """
        Sets the contents of this RemoteProcessGroupDTO.
        The contents of the remote process group. Will contain available input/output ports.

        :param contents: The contents of this RemoteProcessGroupDTO.
        :type: RemoteProcessGroupContentsDTO
        """

        self._contents = contents

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
        if not isinstance(other, RemoteProcessGroupDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
