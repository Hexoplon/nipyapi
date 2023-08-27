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


class JVMDiagnosticsSnapshotDTO(object):
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
        'system_diagnostics_dto': 'JVMSystemDiagnosticsSnapshotDTO',
        'flow_diagnostics_dto': 'JVMFlowDiagnosticsSnapshotDTO',
        'controller_diagnostics': 'JVMControllerDiagnosticsSnapshotDTO'
    }

    attribute_map = {
        'system_diagnostics_dto': 'systemDiagnosticsDto',
        'flow_diagnostics_dto': 'flowDiagnosticsDto',
        'controller_diagnostics': 'controllerDiagnostics'
    }

    def __init__(self, system_diagnostics_dto=None, flow_diagnostics_dto=None, controller_diagnostics=None):
        """
        JVMDiagnosticsSnapshotDTO - a model defined in Swagger
        """

        self._system_diagnostics_dto = None
        self._flow_diagnostics_dto = None
        self._controller_diagnostics = None

        if system_diagnostics_dto is not None:
          self.system_diagnostics_dto = system_diagnostics_dto
        if flow_diagnostics_dto is not None:
          self.flow_diagnostics_dto = flow_diagnostics_dto
        if controller_diagnostics is not None:
          self.controller_diagnostics = controller_diagnostics

    @property
    def system_diagnostics_dto(self):
        """
        Gets the system_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        System-related diagnostics information

        :return: The system_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        :rtype: JVMSystemDiagnosticsSnapshotDTO
        """
        return self._system_diagnostics_dto

    @system_diagnostics_dto.setter
    def system_diagnostics_dto(self, system_diagnostics_dto):
        """
        Sets the system_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        System-related diagnostics information

        :param system_diagnostics_dto: The system_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        :type: JVMSystemDiagnosticsSnapshotDTO
        """

        self._system_diagnostics_dto = system_diagnostics_dto

    @property
    def flow_diagnostics_dto(self):
        """
        Gets the flow_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        Flow-related diagnostics information

        :return: The flow_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        :rtype: JVMFlowDiagnosticsSnapshotDTO
        """
        return self._flow_diagnostics_dto

    @flow_diagnostics_dto.setter
    def flow_diagnostics_dto(self, flow_diagnostics_dto):
        """
        Sets the flow_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        Flow-related diagnostics information

        :param flow_diagnostics_dto: The flow_diagnostics_dto of this JVMDiagnosticsSnapshotDTO.
        :type: JVMFlowDiagnosticsSnapshotDTO
        """

        self._flow_diagnostics_dto = flow_diagnostics_dto

    @property
    def controller_diagnostics(self):
        """
        Gets the controller_diagnostics of this JVMDiagnosticsSnapshotDTO.
        Controller-related diagnostics information

        :return: The controller_diagnostics of this JVMDiagnosticsSnapshotDTO.
        :rtype: JVMControllerDiagnosticsSnapshotDTO
        """
        return self._controller_diagnostics

    @controller_diagnostics.setter
    def controller_diagnostics(self, controller_diagnostics):
        """
        Sets the controller_diagnostics of this JVMDiagnosticsSnapshotDTO.
        Controller-related diagnostics information

        :param controller_diagnostics: The controller_diagnostics of this JVMDiagnosticsSnapshotDTO.
        :type: JVMControllerDiagnosticsSnapshotDTO
        """

        self._controller_diagnostics = controller_diagnostics

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
        if not isinstance(other, JVMDiagnosticsSnapshotDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
