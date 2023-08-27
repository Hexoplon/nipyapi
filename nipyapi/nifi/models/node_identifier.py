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


class NodeIdentifier(object):
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
        'api_address': 'str',
        'api_port': 'int',
        'socket_address': 'str',
        'socket_port': 'int',
        'load_balance_address': 'str',
        'load_balance_port': 'int',
        'site_to_site_address': 'str',
        'site_to_site_port': 'int',
        'site_to_site_http_api_port': 'int',
        'site_to_site_secure': 'bool',
        'node_identities': 'list[str]',
        'full_description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'api_address': 'apiAddress',
        'api_port': 'apiPort',
        'socket_address': 'socketAddress',
        'socket_port': 'socketPort',
        'load_balance_address': 'loadBalanceAddress',
        'load_balance_port': 'loadBalancePort',
        'site_to_site_address': 'siteToSiteAddress',
        'site_to_site_port': 'siteToSitePort',
        'site_to_site_http_api_port': 'siteToSiteHttpApiPort',
        'site_to_site_secure': 'siteToSiteSecure',
        'node_identities': 'nodeIdentities',
        'full_description': 'fullDescription'
    }

    def __init__(self, id=None, api_address=None, api_port=None, socket_address=None, socket_port=None, load_balance_address=None, load_balance_port=None, site_to_site_address=None, site_to_site_port=None, site_to_site_http_api_port=None, site_to_site_secure=None, node_identities=None, full_description=None):
        """
        NodeIdentifier - a model defined in Swagger
        """

        self._id = None
        self._api_address = None
        self._api_port = None
        self._socket_address = None
        self._socket_port = None
        self._load_balance_address = None
        self._load_balance_port = None
        self._site_to_site_address = None
        self._site_to_site_port = None
        self._site_to_site_http_api_port = None
        self._site_to_site_secure = None
        self._node_identities = None
        self._full_description = None

        if id is not None:
          self.id = id
        if api_address is not None:
          self.api_address = api_address
        if api_port is not None:
          self.api_port = api_port
        if socket_address is not None:
          self.socket_address = socket_address
        if socket_port is not None:
          self.socket_port = socket_port
        if load_balance_address is not None:
          self.load_balance_address = load_balance_address
        if load_balance_port is not None:
          self.load_balance_port = load_balance_port
        if site_to_site_address is not None:
          self.site_to_site_address = site_to_site_address
        if site_to_site_port is not None:
          self.site_to_site_port = site_to_site_port
        if site_to_site_http_api_port is not None:
          self.site_to_site_http_api_port = site_to_site_http_api_port
        if site_to_site_secure is not None:
          self.site_to_site_secure = site_to_site_secure
        if node_identities is not None:
          self.node_identities = node_identities
        if full_description is not None:
          self.full_description = full_description

    @property
    def id(self):
        """
        Gets the id of this NodeIdentifier.

        :return: The id of this NodeIdentifier.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NodeIdentifier.

        :param id: The id of this NodeIdentifier.
        :type: str
        """

        self._id = id

    @property
    def api_address(self):
        """
        Gets the api_address of this NodeIdentifier.

        :return: The api_address of this NodeIdentifier.
        :rtype: str
        """
        return self._api_address

    @api_address.setter
    def api_address(self, api_address):
        """
        Sets the api_address of this NodeIdentifier.

        :param api_address: The api_address of this NodeIdentifier.
        :type: str
        """

        self._api_address = api_address

    @property
    def api_port(self):
        """
        Gets the api_port of this NodeIdentifier.

        :return: The api_port of this NodeIdentifier.
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """
        Sets the api_port of this NodeIdentifier.

        :param api_port: The api_port of this NodeIdentifier.
        :type: int
        """

        self._api_port = api_port

    @property
    def socket_address(self):
        """
        Gets the socket_address of this NodeIdentifier.

        :return: The socket_address of this NodeIdentifier.
        :rtype: str
        """
        return self._socket_address

    @socket_address.setter
    def socket_address(self, socket_address):
        """
        Sets the socket_address of this NodeIdentifier.

        :param socket_address: The socket_address of this NodeIdentifier.
        :type: str
        """

        self._socket_address = socket_address

    @property
    def socket_port(self):
        """
        Gets the socket_port of this NodeIdentifier.

        :return: The socket_port of this NodeIdentifier.
        :rtype: int
        """
        return self._socket_port

    @socket_port.setter
    def socket_port(self, socket_port):
        """
        Sets the socket_port of this NodeIdentifier.

        :param socket_port: The socket_port of this NodeIdentifier.
        :type: int
        """

        self._socket_port = socket_port

    @property
    def load_balance_address(self):
        """
        Gets the load_balance_address of this NodeIdentifier.

        :return: The load_balance_address of this NodeIdentifier.
        :rtype: str
        """
        return self._load_balance_address

    @load_balance_address.setter
    def load_balance_address(self, load_balance_address):
        """
        Sets the load_balance_address of this NodeIdentifier.

        :param load_balance_address: The load_balance_address of this NodeIdentifier.
        :type: str
        """

        self._load_balance_address = load_balance_address

    @property
    def load_balance_port(self):
        """
        Gets the load_balance_port of this NodeIdentifier.

        :return: The load_balance_port of this NodeIdentifier.
        :rtype: int
        """
        return self._load_balance_port

    @load_balance_port.setter
    def load_balance_port(self, load_balance_port):
        """
        Sets the load_balance_port of this NodeIdentifier.

        :param load_balance_port: The load_balance_port of this NodeIdentifier.
        :type: int
        """

        self._load_balance_port = load_balance_port

    @property
    def site_to_site_address(self):
        """
        Gets the site_to_site_address of this NodeIdentifier.

        :return: The site_to_site_address of this NodeIdentifier.
        :rtype: str
        """
        return self._site_to_site_address

    @site_to_site_address.setter
    def site_to_site_address(self, site_to_site_address):
        """
        Sets the site_to_site_address of this NodeIdentifier.

        :param site_to_site_address: The site_to_site_address of this NodeIdentifier.
        :type: str
        """

        self._site_to_site_address = site_to_site_address

    @property
    def site_to_site_port(self):
        """
        Gets the site_to_site_port of this NodeIdentifier.

        :return: The site_to_site_port of this NodeIdentifier.
        :rtype: int
        """
        return self._site_to_site_port

    @site_to_site_port.setter
    def site_to_site_port(self, site_to_site_port):
        """
        Sets the site_to_site_port of this NodeIdentifier.

        :param site_to_site_port: The site_to_site_port of this NodeIdentifier.
        :type: int
        """

        self._site_to_site_port = site_to_site_port

    @property
    def site_to_site_http_api_port(self):
        """
        Gets the site_to_site_http_api_port of this NodeIdentifier.

        :return: The site_to_site_http_api_port of this NodeIdentifier.
        :rtype: int
        """
        return self._site_to_site_http_api_port

    @site_to_site_http_api_port.setter
    def site_to_site_http_api_port(self, site_to_site_http_api_port):
        """
        Sets the site_to_site_http_api_port of this NodeIdentifier.

        :param site_to_site_http_api_port: The site_to_site_http_api_port of this NodeIdentifier.
        :type: int
        """

        self._site_to_site_http_api_port = site_to_site_http_api_port

    @property
    def site_to_site_secure(self):
        """
        Gets the site_to_site_secure of this NodeIdentifier.

        :return: The site_to_site_secure of this NodeIdentifier.
        :rtype: bool
        """
        return self._site_to_site_secure

    @site_to_site_secure.setter
    def site_to_site_secure(self, site_to_site_secure):
        """
        Sets the site_to_site_secure of this NodeIdentifier.

        :param site_to_site_secure: The site_to_site_secure of this NodeIdentifier.
        :type: bool
        """

        self._site_to_site_secure = site_to_site_secure

    @property
    def node_identities(self):
        """
        Gets the node_identities of this NodeIdentifier.

        :return: The node_identities of this NodeIdentifier.
        :rtype: list[str]
        """
        return self._node_identities

    @node_identities.setter
    def node_identities(self, node_identities):
        """
        Sets the node_identities of this NodeIdentifier.

        :param node_identities: The node_identities of this NodeIdentifier.
        :type: list[str]
        """

        self._node_identities = node_identities

    @property
    def full_description(self):
        """
        Gets the full_description of this NodeIdentifier.

        :return: The full_description of this NodeIdentifier.
        :rtype: str
        """
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        """
        Sets the full_description of this NodeIdentifier.

        :param full_description: The full_description of this NodeIdentifier.
        :type: str
        """

        self._full_description = full_description

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
        if not isinstance(other, NodeIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
