import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    SearchHintSection,
    GroupsGroup,
    UsersUserMin,
    BaseBoolInt,
    BaseLink,
    SearchHintType,
    AppsApp,
)


class SearchHintResponseModel(BaseModel):
    description: str = Field(
        description="Object description",
    )

    type: "SearchHintType" = Field()

    app: typing.Optional["AppsApp"] = Field(
        default=None,
    )

    _global: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the object has been found globally",
        alias="global",
    )

    group: typing.Optional["GroupsGroup"] = Field(
        default=None,
    )

    profile: typing.Optional["UsersUserMin"] = Field(
        default=None,
    )

    section: typing.Optional["SearchHintSection"] = Field(
        default=None,
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )


class SearchHintResponse(BaseResponse):
    response: "SearchHintResponseModel"


class SearchHintSectionResponseModel(enum.Enum):
    GROUPS = "groups"

    EVENTS = "events"

    PUBLICS = "publics"

    CORRESPONDENTS = "correspondents"

    PEOPLE = "people"

    FRIENDS = "friends"

    MUTUAL_FRIENDS = "mutual_friends"

    PROMO = "promo"


class SearchHintSectionResponse(BaseResponse):
    response: "SearchHintSectionResponseModel"


class SearchHintTypeResponseModel(enum.Enum):
    GROUP = "group"

    PROFILE = "profile"

    VK_APP = "vk_app"

    APP = "app"

    HTML5_GAME = "html5_game"

    LINK = "link"


class SearchHintTypeResponse(BaseResponse):
    response: "SearchHintTypeResponseModel"
