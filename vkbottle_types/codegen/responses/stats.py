import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    StatsActivity,
    StatsCountry,
    StatsPeriodFromOneOf,
    StatsPeriodToOneOf,
    StatsVisitorsOneOf,
    StatsReachOneOf,
    StatsSexAge,
    StatsCity,
)


class StatsActivityResponseModel(BaseModel):
    comments: typing.Optional[int] = Field(
        default=None,
        description="Comments number",
    )

    copies: typing.Optional[int] = Field(
        default=None,
        description="Reposts number",
    )

    hidden: typing.Optional[int] = Field(
        default=None,
        description="Hidden from news count",
    )

    likes: typing.Optional[int] = Field(
        default=None,
        description="Likes number",
    )

    subscribed: typing.Optional[int] = Field(
        default=None,
        description="New subscribers count",
    )

    unsubscribed: typing.Optional[int] = Field(
        default=None,
        description="Unsubscribed count",
    )


class StatsActivityResponse(BaseResponse):
    response: "StatsActivityResponseModel"


class StatsCityResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="City name",
    )

    value: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )


class StatsCityResponse(BaseResponse):
    response: "StatsCityResponseModel"


class StatsCountryResponseModel(BaseModel):
    code: typing.Optional[str] = Field(
        default=None,
        description="Country code",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Country name",
    )

    value: typing.Optional[int] = Field(
        default=None,
        description="Country ID",
    )


class StatsCountryResponse(BaseResponse):
    response: "StatsCountryResponseModel"


class StatsPeriodResponseModel(BaseModel):
    activity: typing.Optional["StatsActivity"] = Field(
        default=None,
    )

    period_from: typing.Optional["StatsPeriodFromOneOf"] = Field(
        default=None,
    )

    period_to: typing.Optional["StatsPeriodToOneOf"] = Field(
        default=None,
    )

    reach: typing.Optional["StatsReachOneOf"] = Field(
        default=None,
    )

    visitors: typing.Optional["StatsVisitorsOneOf"] = Field(
        default=None,
    )


class StatsPeriodResponse(BaseResponse):
    response: "StatsPeriodResponseModel"


StatsPeriodFromOneOfResponseModel = int


class StatsPeriodFromOneOfResponse(BaseResponse):
    response: "StatsPeriodFromOneOfResponseModel"


StatsPeriodToOneOfResponseModel = int


class StatsPeriodToOneOfResponse(BaseResponse):
    response: "StatsPeriodToOneOfResponseModel"


class StatsReachResponseModel(BaseModel):
    age: typing.Optional[typing.List[StatsSexAge]] = Field(
        default=None,
    )

    cities: typing.Optional[typing.List[StatsCity]] = Field(
        default=None,
    )

    countries: typing.Optional[typing.List[StatsCountry]] = Field(
        default=None,
    )

    mobile_reach: typing.Optional[int] = Field(
        default=None,
        description="Reach count from mobile devices",
    )

    reach: typing.Optional[int] = Field(
        default=None,
        description="Reach count",
    )

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
        description="Subscribers reach count",
    )

    sex: typing.Optional[typing.List[StatsSexAge]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List[StatsSexAge]] = Field(
        default=None,
    )


class StatsReachResponse(BaseResponse):
    response: "StatsReachResponseModel"


class StatsReachOneOfResponseModel(BaseModel):
    pass


class StatsReachOneOfResponse(BaseResponse):
    response: "StatsReachOneOfResponseModel"


class StatsSexAgeResponseModel(BaseModel):
    value: str = Field(
        description="Sex/age value",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )

    reach: typing.Optional[int] = Field(
        default=None,
    )

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
    )

    count_subscribers: typing.Optional[int] = Field(
        default=None,
    )


class StatsSexAgeResponse(BaseResponse):
    response: "StatsSexAgeResponseModel"


class StatsViewsResponseModel(BaseModel):
    age: typing.Optional[typing.List[StatsSexAge]] = Field(
        default=None,
    )

    cities: typing.Optional[typing.List[StatsCity]] = Field(
        default=None,
    )

    countries: typing.Optional[typing.List[StatsCountry]] = Field(
        default=None,
    )

    mobile_views: typing.Optional[int] = Field(
        default=None,
        description="Number of views from mobile devices",
    )

    sex: typing.Optional[typing.List[StatsSexAge]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List[StatsSexAge]] = Field(
        default=None,
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number",
    )

    visitors: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )


class StatsViewsResponse(BaseResponse):
    response: "StatsViewsResponseModel"


class StatsVisitorsOneOfResponseModel(BaseModel):
    pass


class StatsVisitorsOneOfResponse(BaseResponse):
    response: "StatsVisitorsOneOfResponseModel"


class StatsWallpostStatResponseModel(BaseModel):
    post_id: typing.Optional[int] = Field(
        default=None,
    )

    hide: typing.Optional[int] = Field(
        default=None,
        description="Hidings number",
    )

    join_group: typing.Optional[int] = Field(
        default=None,
        description="People have joined the group",
    )

    links: typing.Optional[int] = Field(
        default=None,
        description="Link clickthrough",
    )

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
        description="Subscribers reach",
    )

    reach_subscribers_count: typing.Optional[int] = Field(
        default=None,
    )

    reach_total: typing.Optional[int] = Field(
        default=None,
        description="Total reach",
    )

    reach_total_count: typing.Optional[int] = Field(
        default=None,
    )

    reach_viral: typing.Optional[int] = Field(
        default=None,
    )

    reach_ads: typing.Optional[int] = Field(
        default=None,
    )

    report: typing.Optional[int] = Field(
        default=None,
        description="Reports number",
    )

    to_group: typing.Optional[int] = Field(
        default=None,
        description="Clickthrough to community",
    )

    unsubscribe: typing.Optional[int] = Field(
        default=None,
        description="Unsubscribed members",
    )

    sex_age: typing.Optional[typing.List[StatsSexAge]] = Field(
        default=None,
    )


class StatsWallpostStatResponse(BaseResponse):
    response: "StatsWallpostStatResponseModel"
