import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    BasePropertyExists,
    PhotosImageType,
    PhotosTagsSuggestionItemButton,
    BaseLikes,
    BaseRepostsInfo,
    BaseBoolInt,
    PhotosPhoto,
    PhotosPhotoSizesType,
    PhotosPhotoTag,
    PhotosImage,
    BaseObjectCount,
    PhotosPhotoSizes,
)


class PhotosImageResponseModel(BaseModel):
    height: typing.Optional[int] = Field(
        default=None,
        description="Height of the photo in px.",
    )

    type: typing.Optional["PhotosImageType"] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Photo URL.",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Width of the photo in px.",
    )


class PhotosImageResponse(BaseResponse):
    response: "PhotosImageResponseModel"


class PhotosImageTypeResponseModel(enum.Enum):
    S = "s"

    M = "m"

    X = "x"

    L = "l"

    O = "o"

    P = "p"

    Q = "q"

    R = "r"

    Y = "y"

    Z = "z"

    W = "w"

    BASE = "base"


class PhotosImageTypeResponse(BaseResponse):
    response: "PhotosImageTypeResponseModel"


class PhotosPhotoResponseModel(BaseModel):
    album_id: int = Field(
        description="Album ID",
    )

    date: int = Field(
        description="Date when uploaded",
    )

    id: int = Field(
        description="Photo ID",
    )

    owner_id: int = Field(
        description="Photo owner's ID",
    )

    has_tags: bool = Field(
        description="Whether photo has attached tag links",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the photo",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Original photo height",
    )

    images: typing.Optional[typing.List[PhotosImage]] = Field(
        default=None,
    )

    lat: typing.Optional[float] = Field(
        default=None,
        description="Latitude",
    )

    long: typing.Optional[float] = Field(
        default=None,
        description="Longitude",
    )

    photo_256: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 2560 px width",
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the photo",
    )

    place: typing.Optional[str] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )

    sizes: typing.Optional[typing.List[PhotosPhotoSizes]] = Field(
        default=None,
    )

    square_crop: typing.Optional[str] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Photo caption",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the user who have uploaded the photo",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Original photo width",
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )

    comments: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )

    tags: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    hidden: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Returns if the photo is hidden above the wall",
    )

    real_offset: typing.Optional[int] = Field(
        default=None,
        description="Real position of the photo",
    )

    vertical_align: typing.Optional[typing.Literal["top", "middle", "bottom"]] = Field(
        default=None,
        description="Sets vertical alignment of a photo",
    )


class PhotosPhotoResponse(BaseResponse):
    response: "PhotosPhotoResponseModel"


class PhotosPhotoAlbumResponseModel(BaseModel):
    created: int = Field(
        description="Date when the album has been created in Unixtime",
    )

    id: int = Field(
        description="Photo album ID",
    )

    owner_id: int = Field(
        description="Album owner's ID",
    )

    size: int = Field(
        description="Photos number",
    )

    title: str = Field(
        description="Photo album title",
    )

    updated: int = Field(
        description="Date when the album has been updated last time in Unixtime",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Photo album description",
    )

    thumb: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )


class PhotosPhotoAlbumResponse(BaseResponse):
    response: "PhotosPhotoAlbumResponseModel"


class PhotosPhotoAlbumFullResponseModel(BaseModel):
    id: int = Field(
        description="Photo album ID",
    )

    owner_id: int = Field(
        description="Album owner's ID",
    )

    size: int = Field(
        description="Photos number",
    )

    title: str = Field(
        description="Photo album title",
    )

    can_upload: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can upload photo to the album",
    )

    comments_disabled: typing.Optional[bool] = Field(
        default=None,
        description="Information whether album comments are disabled",
    )

    created: typing.Optional[int] = Field(
        default=None,
        description="Date when the album has been created in Unixtime, not set for system albums",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Photo album description",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="album can delete",
    )

    can_include_to_feed: typing.Optional[bool] = Field(
        default=None,
        description="album can be selected to feed",
    )

    sizes: typing.Optional[typing.List[PhotosPhotoSizes]] = Field(
        default=None,
    )

    thumb_id: typing.Optional[int] = Field(
        default=None,
        description="Thumb photo ID",
    )

    thumb_is_last: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the album thumb is last photo",
    )

    thumb_src: typing.Optional[str] = Field(
        default=None,
        description="URL of the thumb image",
    )

    updated: typing.Optional[int] = Field(
        default=None,
        description="Date when the album has been updated last time in Unixtime, not set for system albums",
    )

    upload_by_admins_only: typing.Optional[bool] = Field(
        default=None,
        description="Information whether only community administrators can upload photos",
    )


class PhotosPhotoAlbumFullResponse(BaseResponse):
    response: "PhotosPhotoAlbumFullResponseModel"


class PhotosPhotoFalseableResponseModel(BaseModel):
    pass


class PhotosPhotoFalseableResponse(BaseResponse):
    response: "PhotosPhotoFalseableResponseModel"


class PhotosPhotoSizesResponseModel(BaseModel):
    height: int = Field(
        description="Height in px",
    )

    type: "PhotosPhotoSizesType" = Field()

    width: int = Field(
        description="Width in px",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL of the image",
    )

    src: typing.Optional[str] = Field(
        default=None,
        description="URL of the image",
    )


class PhotosPhotoSizesResponse(BaseResponse):
    response: "PhotosPhotoSizesResponseModel"


class PhotosPhotoSizesTypeResponseModel(enum.Enum):
    T = "t"

    S = "s"

    M = "m"

    X = "x"

    O = "o"

    P = "p"

    Q = "q"

    R = "r"

    K = "k"

    L = "l"

    Y = "y"

    Z = "z"

    C = "c"

    W = "w"

    A = "a"

    B = "b"

    E = "e"

    I = "i"

    D = "d"

    J = "j"

    TEMP = "temp"

    H = "h"

    G = "g"

    N = "n"

    F = "f"

    MAX = "max"

    BASE = "base"

    U = "u"

    V = "v"


class PhotosPhotoSizesTypeResponse(BaseResponse):
    response: "PhotosPhotoSizesTypeResponseModel"


class PhotosPhotoTagResponseModel(BaseModel):
    date: int = Field(
        description="Date when tag has been added in Unixtime",
    )

    id: int = Field(
        description="Tag ID",
    )

    placer_id: int = Field(
        description="ID of the tag creator",
    )

    tagged_name: str = Field(
        description="Tag description",
    )

    user_id: int = Field(
        description="Tagged user ID",
    )

    viewed: bool = Field(
        description="Information whether the tag is reviewed",
    )

    x: float = Field(
        description="Coordinate X of the left upper corner",
    )

    x2: float = Field(
        description="Coordinate X of the right lower corner",
    )

    y: float = Field(
        description="Coordinate Y of the left upper corner",
    )

    y2: float = Field(
        description="Coordinate Y of the right lower corner",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Tagged description.",
    )


class PhotosPhotoTagResponse(BaseResponse):
    response: "PhotosPhotoTagResponseModel"


class PhotosPhotoUploadResponseModel(BaseModel):
    album_id: int = Field(
        description="Album ID",
    )

    upload_url: str = Field(
        description="URL to upload photo",
    )

    user_id: int = Field(
        description="User ID",
    )

    fallback_upload_url: typing.Optional[str] = Field(
        default=None,
        description="Fallback URL if upload_url returned error",
    )

    group_id: typing.Optional[int] = Field(
        default=None,
        description="Group ID",
    )


class PhotosPhotoUploadResponse(BaseResponse):
    response: "PhotosPhotoUploadResponseModel"


class PhotosPhotoXtrTagInfoResponseModel(BaseModel):
    album_id: int = Field(
        description="Album ID",
    )

    date: int = Field(
        description="Date when uploaded",
    )

    id: int = Field(
        description="Photo ID",
    )

    owner_id: int = Field(
        description="Photo owner's ID",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the photo",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Original photo height",
    )

    lat: typing.Optional[float] = Field(
        default=None,
        description="Latitude",
    )

    long: typing.Optional[float] = Field(
        default=None,
        description="Longitude",
    )

    photo_1280: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 1280 px width",
    )

    photo_130: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 130 px width",
    )

    photo_2560: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 2560 px width",
    )

    photo_604: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 604 px width",
    )

    photo_75: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 75 px width",
    )

    photo_807: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 807 px width",
    )

    placer_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the tag creator",
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )

    sizes: typing.Optional[typing.List[PhotosPhotoSizes]] = Field(
        default=None,
    )

    tag_created: typing.Optional[int] = Field(
        default=None,
        description="Date when tag has been added in Unixtime",
    )

    tag_id: typing.Optional[int] = Field(
        default=None,
        description="Tag ID",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Photo caption",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the user who have uploaded the photo",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Original photo width",
    )

    has_tags: typing.Optional[bool] = Field(
        default=None,
        description="Whether photo has attached tag links",
    )


class PhotosPhotoXtrTagInfoResponse(BaseResponse):
    response: "PhotosPhotoXtrTagInfoResponseModel"


class PhotosTagsSuggestionItemResponseModel(BaseModel):
    title: typing.Optional[str] = Field(
        default=None,
    )

    caption: typing.Optional[str] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
    )

    buttons: typing.Optional[typing.List[PhotosTagsSuggestionItemButton]] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    tags: typing.Optional[typing.List[PhotosPhotoTag]] = Field(
        default=None,
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )


class PhotosTagsSuggestionItemResponse(BaseResponse):
    response: "PhotosTagsSuggestionItemResponseModel"


class PhotosTagsSuggestionItemButtonResponseModel(BaseModel):
    title: typing.Optional[str] = Field(
        default=None,
    )

    action: typing.Optional[typing.Literal["confirm", "decline", "show_tags"]] = Field(
        default=None,
    )

    style: typing.Optional[typing.Literal["primary", "secondary"]] = Field(
        default=None,
    )


class PhotosTagsSuggestionItemButtonResponse(BaseResponse):
    response: "PhotosTagsSuggestionItemButtonResponseModel"
