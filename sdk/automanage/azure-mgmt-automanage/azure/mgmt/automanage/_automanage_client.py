# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AutomanageClientConfiguration
from .operations import AccountsOperations
from .operations import ConfigurationProfileAssignmentsOperations
from .operations import ConfigurationProfilePreferencesOperations
from .operations import Operations
from . import models


class AutomanageClient(SDKClient):
    """Automanage Client

    :ivar config: Configuration for client.
    :vartype config: AutomanageClientConfiguration

    :ivar accounts: Accounts operations
    :vartype accounts: azure.mgmt.automanage.operations.AccountsOperations
    :ivar configuration_profile_assignments: ConfigurationProfileAssignments operations
    :vartype configuration_profile_assignments: azure.mgmt.automanage.operations.ConfigurationProfileAssignmentsOperations
    :ivar configuration_profile_preferences: ConfigurationProfilePreferences operations
    :vartype configuration_profile_preferences: azure.mgmt.automanage.operations.ConfigurationProfilePreferencesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.automanage.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription ID which uniquely identify Microsoft
     Azure subscription. The subscription ID forms part of the URI for every
     service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AutomanageClientConfiguration(credentials, subscription_id, base_url)
        super(AutomanageClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-06-30-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.accounts = AccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.configuration_profile_assignments = ConfigurationProfileAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.configuration_profile_preferences = ConfigurationProfilePreferencesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
