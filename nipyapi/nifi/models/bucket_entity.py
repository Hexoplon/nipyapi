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


class BucketEntity(object):
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
        'bucket': 'BucketDTO',
        'permissions': 'PermissionsDTO'
    }

    attribute_map = {
        'id': 'id',
        'bucket': 'bucket',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, bucket=None, permissions=None):
        """
        BucketEntity - a model defined in Swagger
        """

        self._id = None
        self._bucket = None
        self._permissions = None

        if id is not None:
          self.id = id
        if bucket is not None:
          self.bucket = bucket
        if permissions is not None:
          self.permissions = permissions

    @property
    def id(self):
        """
        Gets the id of this BucketEntity.

        :return: The id of this BucketEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BucketEntity.

        :param id: The id of this BucketEntity.
        :type: str
        """

        self._id = id

    @property
    def bucket(self):
        """
        Gets the bucket of this BucketEntity.

        :return: The bucket of this BucketEntity.
        :rtype: BucketDTO
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this BucketEntity.

        :param bucket: The bucket of this BucketEntity.
        :type: BucketDTO
        """

        self._bucket = bucket

    @property
    def permissions(self):
        """
        Gets the permissions of this BucketEntity.

        :return: The permissions of this BucketEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this BucketEntity.

        :param permissions: The permissions of this BucketEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

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
        if not isinstance(other, BucketEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
