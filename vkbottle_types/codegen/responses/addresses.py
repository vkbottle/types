import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class AddressesFieldsResponseModel(enum.Enum):
    ID = "id"

    TITLE = "title"

    ADDRESS = "address"

    ADDITIONAL_ADDRESS = "additional_address"

    COUNTRY_ID = "country_id"

    CITY_ID = "city_id"

    METRO_STATION_ID = "metro_station_id"

    LATITUDE = "latitude"

    LONGITUDE = "longitude"

    DISTANCE = "distance"

    WORK_INFO_STATUS = "work_info_status"

    TIMETABLE = "timetable"

    PHONE = "phone"

    TIME_OFFSET = "time_offset"


class AddressesFieldsResponse(BaseResponse):
    response: "AddressesFieldsResponseModel"
