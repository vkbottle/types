import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    AppsAppType,
    AppsAppLeaderboardType,
    BaseBoolInt,
    AppsApp,
    UsersUserMin,
)


class AppsAppResponseModel(AppsAppMin):
    author_url: typing.Optional[str] = Field(
        default=None,
        description="Application author's URL",
    )

    banner_1120: typing.Optional[str] = Field(
        default=None,
        description="URL of the app banner with 1120 px in width",
    )

    banner_560: typing.Optional[str] = Field(
        default=None,
        description="URL of the app banner with 560 px in width",
    )

    icon_16: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 16 px in width",
    )

    is_new: typing.Optional[bool] = Field(
        default=None,
        description="Is new flag",
    )

    push_enabled: typing.Optional[bool] = Field(
        default=None,
        description="Is push enabled",
    )

    friends: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    catalog_position: typing.Optional[int] = Field(
        default=None,
        description="Catalog position",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Application description",
    )

    genre: typing.Optional[str] = Field(
        default=None,
        description="Genre name",
    )

    genre_id: typing.Optional[int] = Field(
        default=None,
        description="Genre ID",
    )

    international: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the application is multilanguage",
    )

    is_in_catalog: typing.Optional[int] = Field(
        default=None,
        description="Information whether application is in mobile catalog",
    )

    leaderboard_type: typing.Optional["AppsAppLeaderboardType"] = Field(
        default=None,
    )

    members_count: typing.Optional[int] = Field(
        default=None,
        description="Members number",
    )

    platform_id: typing.Optional[str] = Field(
        default=None,
        description="Application ID in store",
    )

    published_date: typing.Optional[int] = Field(
        default=None,
        description="Date when the application has been published in Unixtime",
    )

    screen_name: typing.Optional[str] = Field(
        default=None,
        description="Screen name",
    )

    section: typing.Optional[str] = Field(
        default=None,
        description="Application section name",
    )


class AppsAppResponse(BaseResponse):
    response: "AppsAppResponseModel"


class AppsAppFieldsResponseModel(enum.Enum):
    AUTHOR_GROUP = "author_group"

    AUTHOR_ID = "author_id"

    AUTHOR_URL = "author_url"

    BANNER_1120 = "banner_1120"

    BANNER_560 = "banner_560"

    BANNER_186 = "banner_186"

    BANNER_896 = "banner_896"

    ICON_16 = "icon_16"

    ICON_25 = "icon_25"

    ICON_50 = "icon_50"

    ICON_100 = "icon_100"

    ICON_200 = "icon_200"

    ICON_128 = "icon_128"

    ICON_256 = "icon_256"

    IS_NEW = "is_new"

    NEW = "new"

    IS_HTML5_APP = "is_html5_app"

    PUSH_ENABLED = "push_enabled"

    CATALOG_BANNER = "catalog_banner"

    FRIENDS = "friends"

    CATALOG_POSITION = "catalog_position"

    DESCRIPTION = "description"

    GENRE = "genre"

    GENRE_ID = "genre_id"

    INTERNATIONAL = "international"

    IS_IN_CATALOG = "is_in_catalog"

    INSTALLED = "installed"

    LEADERBOARD_TYPE = "leaderboard_type"

    MEMBERS_COUNT = "members_count"

    PLATFORM_ID = "platform_id"

    PUBLISHED_DATE = "published_date"

    SCREEN_NAME = "screen_name"

    SECTION = "section"

    TYPE = "type"

    ID = "id"

    TITLE = "title"

    AUTHOR_OWNER_ID = "author_owner_id"

    IS_INSTALLED = "is_installed"

    ICON_139 = "icon_139"

    ICON_150 = "icon_150"

    ICON_278 = "icon_278"

    ICON_576 = "icon_576"

    BACKGROUND_LOADER_COLOR = "background_loader_color"

    LOADER_ICON = "loader_icon"

    ICON_75 = "icon_75"

    OPEN_IN_EXTERNAL_BROWSER = "open_in_external_browser"

    AD_CONFIG = "ad_config"

    SCREEN_ORIENTATION = "screen_orientation"


class AppsAppFieldsResponse(BaseResponse):
    response: "AppsAppFieldsResponseModel"


class AppsAppLeaderboardTypeResponseModel(enum.IntEnum):
    NOT_SUPPORTED = 0

    LEVELS = 1

    POINTS = 2


class AppsAppLeaderboardTypeResponse(BaseResponse):
    response: "AppsAppLeaderboardTypeResponseModel"


class AppsAppMinResponseModel(BaseModel):
    type: "AppsAppType" = Field()

    id: int = Field(
        description="Application ID",
    )

    title: str = Field(
        description="Application title",
    )

    author_owner_id: typing.Optional[int] = Field(
        default=None,
        description="Application author's ID",
    )

    is_installed: typing.Optional[bool] = Field(
        default=None,
        description="Is application installed",
    )

    icon_139: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 139 px in width",
    )

    icon_150: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 150 px in width",
    )

    icon_278: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 278 px in width",
    )

    icon_576: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 576 px in width",
    )

    background_loader_color: typing.Optional[str] = Field(
        default=None,
        description="Hex color code without hash sign",
    )

    loader_icon: typing.Optional[str] = Field(
        default=None,
        description="SVG data",
    )

    icon_75: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 75 px in width",
    )

    screen_orientation: typing.Optional[int] = Field(
        default=None,
        description="Screen orientation",
    )


class AppsAppMinResponse(BaseResponse):
    response: "AppsAppMinResponseModel"


class AppsAppTypeResponseModel(enum.Enum):
    APP = "app"

    GAME = "game"

    SITE = "site"

    STANDALONE = "standalone"

    VK_APP = "vk_app"

    COMMUNITY_APP = "community_app"

    HTML5_GAME = "html5_game"

    MINI_APP = "mini_app"


class AppsAppTypeResponse(BaseResponse):
    response: "AppsAppTypeResponseModel"


class AppsCatalogListResponseModel(BaseModel):
    count: int = Field(
        description="Total number",
    )

    items: typing.List[AppsApp] = Field()

    profiles: typing.Optional[typing.List[UsersUserMin]] = Field(
        default=None,
    )


class AppsCatalogListResponse(BaseResponse):
    response: "AppsCatalogListResponseModel"


class AppsLeaderboardResponseModel(BaseModel):
    user_id: int = Field(
        description="User ID",
    )

    level: typing.Optional[int] = Field(
        default=None,
        description="Level",
    )

    points: typing.Optional[int] = Field(
        default=None,
        description="Points number",
    )

    score: typing.Optional[int] = Field(
        default=None,
        description="Score number",
    )


class AppsLeaderboardResponse(BaseResponse):
    response: "AppsLeaderboardResponseModel"


class AppsScopeResponseModel(BaseModel):
    name: typing.Literal[
        "friends",
        "photos",
        "video",
        "pages",
        "status",
        "notes",
        "wall",
        "docs",
        "groups",
        "stats",
        "market",
        "stories",
        "app_widget",
        "messages",
        "manage",
        "notify",
        "audio",
        "support",
        "menu",
        "wallmenu",
        "ads",
        "offline",
        "notifications",
        "email",
        "adsweb",
        "leads",
        "group_messages",
        "exchange",
        "phone",
    ] = Field(
        description="Scope name",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Scope title",
    )


class AppsScopeResponse(BaseResponse):
    response: "AppsScopeResponseModel"


class AppsTestingGroupResponseModel(BaseModel):
    user_ids: typing.List[int] = Field()

    group_id: int = Field()

    name: typing.Optional[str] = Field(
        default=None,
    )

    webview: typing.Optional[str] = Field(
        default=None,
    )

    platforms: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class AppsTestingGroupResponse(BaseResponse):
    response: "AppsTestingGroupResponseModel"
