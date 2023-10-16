"""Support for switches which integrates with other components."""
from __future__ import annotations

from typing import Any
import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
import os
import json

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the template switches."""

    _LOGGER.debug("call unicode converter setup2")
    _LOGGER.debug("config" + str(config.get("components")))

    for component in config.get("components"):
        filePath = "custom_components/" + component.get("name") + "/translations/"
        _LOGGER.debug("filePath : " + str(filePath))
        for file in os.listdir(filePath):
            data = None
            realPath = filePath + file
            if os.path.exists(realPath):
                with open(realPath, "r") as f:
                    _LOGGER.debug("load json")
                    data = json.load(f)
                if data != None:
                    with open(realPath, "w") as f:
                        json.dump(data, f, sort_keys=component.get("sort", False), indent=4)


    
    
    _LOGGER.debug("real path : " + str(os.listdir("custom_components")))


