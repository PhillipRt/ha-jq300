#  Copyright (c) 2020-2021, Andrey "Limych" Khrolenok <andrey@khrolenok.ru>
#  Creative Commons BY-NC-SA 4.0 International Public License
#  (see LICENSE.md or https://creativecommons.org/licenses/by-nc-sa/4.0/)

"""
Integration of the JQ-300/200/100 indoor air quality meter.

For more details about this component, please refer to
https://github.com/Limych/ha-jq300
"""

from datetime import timedelta
from typing import Final

from homeassistant.components.binary_sensor import DEVICE_CLASS_PROBLEM
from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR
from homeassistant.components.sensor import DOMAIN as SENSOR
from homeassistant.const import (
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
    CONCENTRATION_PARTS_PER_MILLION,
    CONF_DEVICE_CLASS,
    CONF_ENTITY_ID,
    CONF_ICON,
    CONF_NAME,
    CONF_UNIT_OF_MEASUREMENT,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_TEMPERATURE,
    PERCENTAGE,
    TEMP_CELSIUS,
)

# Base component constants
NAME: Final = "JQ-300/200/100 Indoor Air Quality Meter"
DOMAIN: Final = "jq300"
VERSION: Final = "0.10.2"
ATTRIBUTION: Final = "Data provided by JQ-300 Cloud"
ISSUE_URL: Final = "https://github.com/Limych/ha-jq300/issues"

STARTUP_MESSAGE: Final = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have ANY issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

# Icons

# Device classes

# Platforms
PLATFORMS: Final = [BINARY_SENSOR, SENSOR]

# Configuration and options
CONF_RECEIVE_TVOC_IN_PPB: Final = "receive_tvoc_in_ppb"
CONF_RECEIVE_HCHO_IN_PPB: Final = "receive_hcho_in_ppb"
CONF_ACCOUNT_CONTROLLER: Final = "account_controller"
CONF_YAML: Final = "_yaml"
CONF_PRECISION: Final = "precision"

# Defaults

# Attributes
ATTR_DEVICE_ID: Final = "device_id"
ATTR_DEVICE_BRAND: Final = "device_brand"
ATTR_DEVICE_MODEL: Final = "device_model"
ATTR_RAW_STATE: Final = "raw_state"

SENSORS_FILTER_FRAME: Final = timedelta(minutes=5)

QUERY_TIMEOUT: Final = 7  # seconds
UPDATE_TIMEOUT: Final = 12  # seconds
AVAILABLE_TIMEOUT: Final = 30  # seconds

MWEIGTH_TVOC: Final = 100  # g/mol
MWEIGTH_HCHO: Final = 30.0260  # g/mol

BINARY_SENSORS: Final = {
    1: {
        CONF_NAME: "Air Quality Alert",
        CONF_ICON: "mdi:alert",
        CONF_DEVICE_CLASS: DEVICE_CLASS_PROBLEM,
    },
}

SENSORS: Final = {
    4: {
        CONF_NAME: "Internal Temperature",
        CONF_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
        CONF_ICON: "mdi:thermometer",
        CONF_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        CONF_PRECISION: 1,
    },
    5: {
        CONF_NAME: "Humidity",
        CONF_UNIT_OF_MEASUREMENT: PERCENTAGE,
        CONF_ICON: "mdi:water-percent",
        CONF_DEVICE_CLASS: DEVICE_CLASS_HUMIDITY,
        CONF_PRECISION: 1,
    },
    6: {
        CONF_NAME: "PM 2.5",
        CONF_UNIT_OF_MEASUREMENT: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        CONF_ICON: "mdi:air-filter",
        CONF_ENTITY_ID: "pm25",
    },
    7: {
        CONF_NAME: "HCHO",
        CONF_UNIT_OF_MEASUREMENT: CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        CONF_ICON: "mdi:cloud",
        CONF_PRECISION: 3,
    },
    8: {
        CONF_NAME: "TVOC",
        CONF_UNIT_OF_MEASUREMENT: CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        CONF_ICON: "mdi:radiator",
        CONF_PRECISION: 3,
    },
    9: {
        CONF_NAME: "eCO2",
        CONF_UNIT_OF_MEASUREMENT: CONCENTRATION_PARTS_PER_MILLION,
        CONF_ICON: "mdi:molecule-co2",
    },
}
