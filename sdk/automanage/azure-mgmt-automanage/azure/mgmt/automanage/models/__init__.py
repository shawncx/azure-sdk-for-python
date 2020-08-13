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

try:
    from ._models_py3 import Account
    from ._models_py3 import AccountIdentity
    from ._models_py3 import ConfigurationProfileAssignment
    from ._models_py3 import ConfigurationProfileAssignmentCompliance
    from ._models_py3 import ConfigurationProfileAssignmentProperties
    from ._models_py3 import ConfigurationProfilePreference
    from ._models_py3 import ConfigurationProfilePreferenceAntiMalware
    from ._models_py3 import ConfigurationProfilePreferenceProperties
    from ._models_py3 import ConfigurationProfilePreferenceVmBackup
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import ErrorResponseBody
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import Account
    from ._models import AccountIdentity
    from ._models import ConfigurationProfileAssignment
    from ._models import ConfigurationProfileAssignmentCompliance
    from ._models import ConfigurationProfileAssignmentProperties
    from ._models import ConfigurationProfilePreference
    from ._models import ConfigurationProfilePreferenceAntiMalware
    from ._models import ConfigurationProfilePreferenceProperties
    from ._models import ConfigurationProfilePreferenceVmBackup
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import ErrorResponseBody
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import ProxyResource
    from ._models import Resource
    from ._models import TrackedResource
from ._paged_models import AccountPaged
from ._paged_models import ConfigurationProfileAssignmentPaged
from ._paged_models import ConfigurationProfilePreferencePaged
from ._paged_models import OperationPaged
from ._automanage_client_enums import (
    ResourceIdentityType,
    ConfigurationProfile,
    ProvisioningStatus,
    UpdateStatus,
    EnableRealTimeProtection,
    RunScheduledScan,
    ScanType,
)

__all__ = [
    'Account',
    'AccountIdentity',
    'ConfigurationProfileAssignment',
    'ConfigurationProfileAssignmentCompliance',
    'ConfigurationProfileAssignmentProperties',
    'ConfigurationProfilePreference',
    'ConfigurationProfilePreferenceAntiMalware',
    'ConfigurationProfilePreferenceProperties',
    'ConfigurationProfilePreferenceVmBackup',
    'ErrorResponse', 'ErrorResponseException',
    'ErrorResponseBody',
    'Operation',
    'OperationDisplay',
    'ProxyResource',
    'Resource',
    'TrackedResource',
    'AccountPaged',
    'ConfigurationProfileAssignmentPaged',
    'ConfigurationProfilePreferencePaged',
    'OperationPaged',
    'ResourceIdentityType',
    'ConfigurationProfile',
    'ProvisioningStatus',
    'UpdateStatus',
    'EnableRealTimeProtection',
    'RunScheduledScan',
    'ScanType',
]
