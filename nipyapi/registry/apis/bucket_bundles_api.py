# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.17.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BucketBundlesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_extension_bundle_version(self, bucket_id, bundle_type, **kwargs):
        """
        Create extension bundle version
        Creates a version of an extension bundle by uploading a binary artifact. If an extension bundle already exists in the given bucket with the same group id and artifact id as that of the bundle being uploaded, then it will be added as a new version to the existing bundle. If an extension bundle does not already exist in the given bucket with the same group id and artifact id, then a new extension bundle will be created and this version will be added to the new bundle. Client's may optionally supply a SHA-256 in hex format through the multi-part form field 'sha256'. If supplied, then this value will be compared against the SHA-256 computed by the server, and the bundle will be rejected if the values do not match. If not supplied, the bundle will be accepted, but will be marked to indicate that the client did not supply a SHA-256 during creation.   NOTE: This endpoint is subject to change as NiFi Registry and its REST API evolve.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_extension_bundle_version(bucket_id, bundle_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :param str bundle_type: The type of the bundle (required)
        :return: BundleVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_extension_bundle_version_with_http_info(bucket_id, bundle_type, **kwargs)
        else:
            (data) = self.create_extension_bundle_version_with_http_info(bucket_id, bundle_type, **kwargs)
            return data

    def create_extension_bundle_version_with_http_info(self, bucket_id, bundle_type, **kwargs):
        """
        Create extension bundle version
        Creates a version of an extension bundle by uploading a binary artifact. If an extension bundle already exists in the given bucket with the same group id and artifact id as that of the bundle being uploaded, then it will be added as a new version to the existing bundle. If an extension bundle does not already exist in the given bucket with the same group id and artifact id, then a new extension bundle will be created and this version will be added to the new bundle. Client's may optionally supply a SHA-256 in hex format through the multi-part form field 'sha256'. If supplied, then this value will be compared against the SHA-256 computed by the server, and the bundle will be rejected if the values do not match. If not supplied, the bundle will be accepted, but will be marked to indicate that the client did not supply a SHA-256 during creation.   NOTE: This endpoint is subject to change as NiFi Registry and its REST API evolve.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_extension_bundle_version_with_http_info(bucket_id, bundle_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :param str bundle_type: The type of the bundle (required)
        :return: BundleVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_id', 'bundle_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_extension_bundle_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in params) or (params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `create_extension_bundle_version`")
        # verify the required parameter 'bundle_type' is set
        if ('bundle_type' not in params) or (params['bundle_type'] is None):
            raise ValueError("Missing the required parameter `bundle_type` when calling `create_extension_bundle_version`")


        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucketId'] = params['bucket_id']
        if 'bundle_type' in params:
            path_params['bundleType'] = params['bundle_type']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets/{bucketId}/bundles/{bundleType}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BundleVersion',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_extension_bundles(self, bucket_id, **kwargs):
        """
        Get extension bundles by bucket
          NOTE: This endpoint is subject to change as NiFi Registry and its REST API evolve.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_extension_bundles(bucket_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :return: list[ExtensionBundle]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_extension_bundles_with_http_info(bucket_id, **kwargs)
        else:
            (data) = self.get_extension_bundles_with_http_info(bucket_id, **kwargs)
            return data

    def get_extension_bundles_with_http_info(self, bucket_id, **kwargs):
        """
        Get extension bundles by bucket
          NOTE: This endpoint is subject to change as NiFi Registry and its REST API evolve.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_extension_bundles_with_http_info(bucket_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bucket_id: The bucket identifier (required)
        :return: list[ExtensionBundle]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extension_bundles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in params) or (params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `get_extension_bundles`")


        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucketId'] = params['bucket_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth', 'Authorization']

        return self.api_client.call_api('/buckets/{bucketId}/bundles', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ExtensionBundle]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
