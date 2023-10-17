import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import PagesPrivacySettings, BaseBoolInt


class PagesPrivacySettingsResponseModel(enum.IntEnum):
    COMMUNITY_MANAGERS_ONLY = 0

    COMMUNITY_MEMBERS_ONLY = 1

    EVERYONE = 2


class PagesPrivacySettingsResponse(BaseResponse):
    response: "PagesPrivacySettingsResponseModel"


class PagesWikipageResponseModel(BaseModel):
    group_id: int = Field(
        description="Community ID",
    )

    id: int = Field(
        description="Page ID",
    )

    title: str = Field(
        description="Page title",
    )

    views: int = Field(
        description="Views number",
    )

    who_can_edit: "PagesPrivacySettings" = Field(
        description="Edit settings of the page",
    )

    who_can_view: "PagesPrivacySettings" = Field(
        description="View settings of the page",
    )

    creator_id: typing.Optional[int] = Field(
        default=None,
        description="Page creator ID",
    )

    creator_name: typing.Optional[str] = Field(
        default=None,
        description="Page creator name",
    )

    editor_id: typing.Optional[int] = Field(
        default=None,
        description="Last editor ID",
    )

    editor_name: typing.Optional[str] = Field(
        default=None,
        description="Last editor name",
    )


class PagesWikipageResponse(BaseResponse):
    response: "PagesWikipageResponseModel"


class PagesWikipageFullResponseModel(BaseModel):
    created: int = Field(
        description="Date when the page has been created in Unixtime",
    )

    edited: int = Field(
        description="Date when the page has been edited in Unixtime",
    )

    group_id: int = Field(
        description="Community ID",
    )

    id: int = Field(
        description="Page ID",
    )

    title: str = Field(
        description="Page title",
    )

    view_url: str = Field(
        description="URL of the page preview",
    )

    views: int = Field(
        description="Views number",
    )

    who_can_edit: "PagesPrivacySettings" = Field(
        description="Edit settings of the page",
    )

    who_can_view: "PagesPrivacySettings" = Field(
        description="View settings of the page",
    )

    creator_id: typing.Optional[int] = Field(
        default=None,
        description="Page creator ID",
    )

    current_user_can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the page",
    )

    current_user_can_edit_access: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the page access settings",
    )

    editor_id: typing.Optional[int] = Field(
        default=None,
        description="Last editor ID",
    )

    html: typing.Optional[str] = Field(
        default=None,
        description="Page content, HTML",
    )

    source: typing.Optional[str] = Field(
        default=None,
        description="Page content, wiki",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL",
    )

    parent: typing.Optional[str] = Field(
        default=None,
        description="Parent",
    )

    parent2: typing.Optional[str] = Field(
        default=None,
        description="Parent2",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Owner ID",
    )


class PagesWikipageFullResponse(BaseResponse):
    response: "PagesWikipageFullResponseModel"


class PagesWikipageHistoryResponseModel(BaseModel):
    id: int = Field(
        description="Version ID",
    )

    length: int = Field(
        description="Page size in bytes",
    )

    date: int = Field(
        description="Date when the page has been edited in Unixtime",
    )

    editor_id: int = Field(
        description="Last editor ID",
    )

    editor_name: str = Field(
        description="Last editor name",
    )


class PagesWikipageHistoryResponse(BaseResponse):
    response: "PagesWikipageHistoryResponseModel"
