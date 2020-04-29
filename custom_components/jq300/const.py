"""
Integration of the JQ-300/200/100 indoor air quality meter.

For more details about this component, please refer to
https://github.com/Limych/ha-jq300
"""

#
#  Copyright (c) 2020, Andrey "Limych" Khrolenok <andrey@khrolenok.ru>
#  Creative Commons BY-NC-SA 4.0 International Public License
#  (see LICENSE.md or https://creativecommons.org/licenses/by-nc-sa/4.0/)
#

from homeassistant.const import TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE, \
    DEVICE_CLASS_HUMIDITY, UNIT_PERCENTAGE, \
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, \
    CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION

# Base component constants
DOMAIN = "jq300"
VERSION = "0.7.3"
ISSUE_URL = "https://github.com/Limych/ha-jq300/issues"
ATTRIBUTION = None
DATA_JQ300 = 'jq300'

SUPPORT_LIB_URL = "https://github.com/Limych/jq300/issues/new/choose"

CONF_RECEIVE_TVOC_IN_PPB = 'receive_tvoc_in_ppb'
CONF_RECEIVE_HCHO_IN_PPB = 'receive_hcho_in_ppb'

# Error strings
MSG_GENERIC_FAIL = 'Sorry.. Something went wrong...'
MSG_LOGIN_FAIL = 'Account name or password is wrong, please try again'
MSG_BUSY = 'The system is busy'

QUERY_TYPE_API = 'API'
QUERY_TYPE_DEVICE = 'DEVICE'

QUERY_METHOD_GET = 'GET'
QUERY_METHOD_POST = 'POST'

BASE_URL_API = "http://www.youpinyuntai.com:32086/ypyt-api/api/app/"
BASE_URL_DEVICE = "https://www.youpinyuntai.com:31447/device/"

_USERAGENT_SYSTEM = "Android 6.0.1; RedMi Note 5 Build/RB3N5C"
USERAGENT_API = f"Dalvik/2.1.0 (Linux; U; {_USERAGENT_SYSTEM})"
USERAGENT_DEVICE = f"Mozilla/5.0 (Linux; {_USERAGENT_SYSTEM}; wv) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 " \
                   "Chrome/68.0.3440.91 Mobile Safari/537.36"

QUERY_TIMEOUT = 12

SENSORS = {
    4: [
        'Internal Temperature',
        TEMP_CELSIUS,
        'mdi:thermometer',
        DEVICE_CLASS_TEMPERATURE,
        None,
    ],
    5: [
        'Humidity',
        UNIT_PERCENTAGE,
        'mdi:water-percent',
        DEVICE_CLASS_HUMIDITY,
        None,
    ],
    6: [
        'PM 2.5',
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        'mdi:air-filter',
        None,
        'pm25',
    ],
    7: [
        'HCHO',
        CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        'mdi:cloud',
        None,
        None,
    ],
    8: [
        'TVOC',
        CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        'mdi:radiator',
        None,
        None,
    ],
    9: [
        'eCO2',
        CONCENTRATION_PARTS_PER_MILLION,
        'mdi:periodic-table-co2',
        None,
        None,
    ],
}

ATTR_DEVICE_ID = 'device_id'
ATTR_DEVICE_BRAND = "device_brand"
ATTR_DEVICE_MODEL = "device_model"
ATTR_RAW_STATE = 'raw_state'

UPDATE_MIN_TIME = 20  # seconds
SENSORS_FILTER_TIME = 600  # seconds

MWEIGTH_TVOC = 56.1060      # g/mol
MWEIGTH_HCHO = 30.0260      # g/mol
