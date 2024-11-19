# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ansible_collections.flightctl.edge.plugins.module_utils.api_client.models.application_spec import ApplicationSpec
from ansible_collections.flightctl.edge.plugins.module_utils.api_client.models.config_provider_spec import ConfigProviderSpec
from ansible_collections.flightctl.edge.plugins.module_utils.api_client.models.device_hooks_spec import DeviceHooksSpec
from ansible_collections.flightctl.edge.plugins.module_utils.api_client.models.device_os_spec import DeviceOSSpec
from ansible_collections.flightctl.edge.plugins.module_utils.api_client.models.device_spec_systemd import DeviceSpecSystemd
from ansible_collections.flightctl.edge.plugins.module_utils.api_client.models.resource_monitor import ResourceMonitor
from typing import Optional, Set
from typing_extensions import Self

class DeviceSpec(BaseModel):
    """
    DeviceSpec
    """ # noqa: E501
    os: Optional[DeviceOSSpec] = None
    config: Optional[List[ConfigProviderSpec]] = Field(default=None, description="List of config providers.")
    hooks: Optional[DeviceHooksSpec] = None
    applications: Optional[List[ApplicationSpec]] = Field(default=None, description="List of applications.")
    systemd: Optional[DeviceSpecSystemd] = None
    resources: Optional[List[ResourceMonitor]] = Field(default=None, description="Array of resource monitor configurations.")
    __properties: ClassVar[List[str]] = ["os", "config", "hooks", "applications", "systemd", "resources"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DeviceSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of os
        if self.os:
            _dict['os'] = self.os.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in config (list)
        _items = []
        if self.config:
            for _item_config in self.config:
                if _item_config:
                    _items.append(_item_config.to_dict())
            _dict['config'] = _items
        # override the default output from pydantic by calling `to_dict()` of hooks
        if self.hooks:
            _dict['hooks'] = self.hooks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in applications (list)
        _items = []
        if self.applications:
            for _item_applications in self.applications:
                if _item_applications:
                    _items.append(_item_applications.to_dict())
            _dict['applications'] = _items
        # override the default output from pydantic by calling `to_dict()` of systemd
        if self.systemd:
            _dict['systemd'] = self.systemd.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item_resources in self.resources:
                if _item_resources:
                    _items.append(_item_resources.to_dict())
            _dict['resources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "os": DeviceOSSpec.from_dict(obj["os"]) if obj.get("os") is not None else None,
            "config": [ConfigProviderSpec.from_dict(_item) for _item in obj["config"]] if obj.get("config") is not None else None,
            "hooks": DeviceHooksSpec.from_dict(obj["hooks"]) if obj.get("hooks") is not None else None,
            "applications": [ApplicationSpec.from_dict(_item) for _item in obj["applications"]] if obj.get("applications") is not None else None,
            "systemd": DeviceSpecSystemd.from_dict(obj["systemd"]) if obj.get("systemd") is not None else None,
            "resources": [ResourceMonitor.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None
        })
        return _obj


