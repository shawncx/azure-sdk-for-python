# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class EventSourcesOperations(object):
    """EventSourcesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.timeseriesinsights.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def create_or_update(
        self,
        resource_group_name,  # type: str
        environment_name,  # type: str
        event_source_name,  # type: str
        parameters,  # type: "models.EventSourceCreateOrUpdateParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.EventSourceResource"
        """Create or update an event source under the specified environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param event_source_name: Name of the event source.
        :type event_source_name: str
        :param parameters: Parameters for creating an event source resource.
        :type parameters: ~azure.mgmt.timeseriesinsights.models.EventSourceCreateOrUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EventSourceResource or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.EventSourceResource or ~azure.mgmt.timeseriesinsights.models.EventSourceResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EventSourceResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-08-15-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'eventSourceName': self._serialize.url("event_source_name", event_source_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'EventSourceCreateOrUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('EventSourceResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('EventSourceResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName}'}

    def get(
        self,
        resource_group_name,  # type: str
        environment_name,  # type: str
        event_source_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.EventSourceResource"
        """Gets the event source with the specified name in the specified environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param event_source_name: The name of the Time Series Insights event source associated with the
         specified environment.
        :type event_source_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EventSourceResource or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.EventSourceResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EventSourceResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-08-15-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'eventSourceName': self._serialize.url("event_source_name", event_source_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EventSourceResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName}'}

    def update(
        self,
        resource_group_name,  # type: str
        environment_name,  # type: str
        event_source_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.EventSourceResource"
        """Updates the event source with the specified name in the specified subscription, resource group, and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param event_source_name: The name of the Time Series Insights event source associated with the
         specified environment.
        :type event_source_name: str
        :param tags: Key-value pairs of additional properties for the event source.
        :type tags: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EventSourceResource or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.EventSourceResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EventSourceResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _event_source_update_parameters = models.EventSourceUpdateParameters(tags=tags)
        api_version = "2018-08-15-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'eventSourceName': self._serialize.url("event_source_name", event_source_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_event_source_update_parameters, 'EventSourceUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EventSourceResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName}'}

    def delete(
        self,
        resource_group_name,  # type: str
        environment_name,  # type: str
        event_source_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes the event source with the specified name in the specified subscription, resource group, and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param event_source_name: The name of the Time Series Insights event source associated with the
         specified environment.
        :type event_source_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-08-15-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'eventSourceName': self._serialize.url("event_source_name", event_source_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName}'}

    def list_by_environment(
        self,
        resource_group_name,  # type: str
        environment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.EventSourceListResponse"
        """Lists all the available event sources associated with the subscription and within the specified resource group and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EventSourceListResponse or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.EventSourceListResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EventSourceListResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-08-15-preview"

        # Construct URL
        url = self.list_by_environment.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EventSourceListResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_by_environment.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources'}
