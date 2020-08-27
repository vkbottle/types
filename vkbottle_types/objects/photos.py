from .base_model import BaseObject
from . import base, comment, wall, media
from typing import Optional, Union, Any, List
import typing
import enum


class CommentXtrPid(BaseObject):
    """VK Object photos/CommentXtrPid

    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    pid - Photo ID
    reply_to_comment - Replied comment ID
    reply_to_user - Replied user ID
    text - Comment text
    """

    attachments: Optional[List[wall.CommentAttachment]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional[base.LikesInfo] = None
    pid: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: Optional[str] = None
    parents_stack: Optional[List[int]] = None
    thread: Optional[comment.Thread] = None


class Image(BaseObject):
    """VK Object photos/Image"""

    height: Optional[int] = None
    type: Optional["ImageType"]
    url: Optional[str] = None
    width: Optional[int] = None


class ImageType(enum.Enum):
    """ Photo's type. """

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


class MarketAlbumUploadResponse(BaseObject):
    """VK Object photos/MarketAlbumUploadResponse

    gid - Community ID
    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    gid: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class MarketUploadResponse(BaseObject):
    """VK Object photos/MarketUploadResponse

    crop_data - Crop data
    crop_hash - Crop hash
    group_id - Community ID
    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    crop_data: Optional[str] = None
    crop_hash: Optional[str] = None
    group_id: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class MessageUploadResponse(BaseObject):
    """VK Object photos/MessageUploadResponse

    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class OwnerUploadResponse(BaseObject):
    """VK Object photos/OwnerUploadResponse

    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class Photo(BaseObject):
    """VK Object photos/Photo

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_256 - URL of image with 2560 px width
    can_comment - Information whether current user can comment the photo
    post_id - Post ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    has_tags - Whether photo has attached tag links
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["Image"]]
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_256: Optional[str] = None
    can_comment: Optional[base.BoolInt] = None
    place: Optional[str] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
    has_tags: Optional[bool] = None
    restrictions: Optional[media.Restriction] = None


class PhotoAlbum(BaseObject):
    """VK Object photos/PhotoAlbum

    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    """

    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    thumb: Optional["Photo"]
    title: Optional[str] = None
    updated: Optional[int] = None


class PhotoAlbumFull(BaseObject):
    """VK Object photos/PhotoAlbumFull

    can_upload - Information whether current user can upload photo to the album
    comments_disabled - Information whether album comments are disabled
    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    thumb_id - Thumb photo ID
    thumb_is_last - Information whether the album thumb is last photo
    thumb_src - URL of the thumb image
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    upload_by_admins_only - Information whether only community administrators can upload photos
    """

    can_upload: Optional[base.BoolInt] = None
    comments_disabled: Optional[base.BoolInt] = None
    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    thumb_id: Optional[int] = None
    thumb_is_last: Optional[base.BoolInt] = None
    thumb_src: Optional[str] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    upload_by_admins_only: Optional[base.BoolInt] = None


class PhotoFull(BaseObject):
    """VK Object photos/PhotoFull

    access_key - Access key for the photo
    album_id - Album ID
    can_comment - Information whether current user can comment the photo
    date - Date when uploaded
    height - Original photo height
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    post_id - Post ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional[base.BoolInt] = None
    comments: Optional[base.ObjectCount] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["Image"]]
    lat: Optional[float] = None
    likes: Optional[base.Likes] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    post_id: Optional[int] = None
    reposts: Optional[base.ObjectCount] = None
    tags: Optional[base.ObjectCount] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotoFullXtrRealOffset(BaseObject):
    """VK Object photos/PhotoFullXtrRealOffset

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    hidden - Returns if the photo is hidden above the wall
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_1280 - URL of image with 1280 px width
    photo_130 - URL of image with 130 px width
    photo_2560 - URL of image with 2560 px width
    photo_604 - URL of image with 604 px width
    photo_75 - URL of image with 75 px width
    photo_807 - URL of image with 807 px width
    post_id - Post ID
    real_offset - Real position of the photo
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional[base.BoolInt] = None
    comments: Optional[base.ObjectCount] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional[base.PropertyExists] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    likes: Optional[base.Likes] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    reposts: Optional[base.ObjectCount] = None
    sizes: Optional[List["PhotoSizes"]]
    tags: Optional[base.ObjectCount] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotoSizes(BaseObject):
    """VK Object photos/PhotoSizes"""

    height: Optional[int] = None
    url: Optional[str] = None
    src: Optional[str] = None
    type: Optional["PhotoSizesType"]
    width: Optional[int] = None


class PhotoSizesType(enum.Enum):
    """ Size type """

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


class PhotoTag(BaseObject):
    """VK Object photos/PhotoTag

    date - Date when tag has been added in Unixtime
    id - Tag ID
    placer_id - ID of the tag creator
    tagged_name - Tag description
    user_id - Tagged user ID
    viewed - Information whether the tag is reviewed
    x - Coordinate X of the left upper corner
    x2 - Coordinate X of the right lower corner
    y - Coordinate Y of the left upper corner
    y2 - Coordinate Y of the right lower corner
    """

    date: Optional[int] = None
    id: Optional[int] = None
    placer_id: Optional[int] = None
    tagged_name: Optional[str] = None
    user_id: Optional[int] = None
    viewed: Optional[base.BoolInt] = None
    x: Optional[float] = None
    x2: Optional[float] = None
    y: Optional[float] = None
    y2: Optional[float] = None


class PhotoUpload(BaseObject):
    """VK Object photos/PhotoUpload

    album_id - Album ID
    upload_url - URL to upload photo
    fallback_upload_url - Fallback URL if upload_url returned error
    user_id - User ID
    group_id - Group ID
    """

    album_id: Optional[int] = None
    upload_url: Optional[str] = None
    fallback_upload_url: Optional[str] = None
    user_id: Optional[int] = None
    group_id: Optional[int] = None


class PhotoUploadResponse(BaseObject):
    """VK Object photos/PhotoUploadResponse

    aid - Album ID
    hash - Uploading hash
    photos_list - Uploaded photos data
    server - Upload server number
    """

    aid: Optional[int] = None
    hash: Optional[str] = None
    photos_list: Optional[str] = None
    server: Optional[int] = None


class PhotoXtrRealOffset(BaseObject):
    """VK Object photos/PhotoXtrRealOffset

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    hidden - Returns if the photo is hidden above the wall
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_1280 - URL of image with 1280 px width
    photo_130 - URL of image with 130 px width
    photo_2560 - URL of image with 2560 px width
    photo_604 - URL of image with 604 px width
    photo_75 - URL of image with 75 px width
    photo_807 - URL of image with 807 px width
    post_id - Post ID
    real_offset - Real position of the photo
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional[base.PropertyExists] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotoXtrTagInfo(BaseObject):
    """VK Object photos/PhotoXtrTagInfo

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_1280 - URL of image with 1280 px width
    photo_130 - URL of image with 130 px width
    photo_2560 - URL of image with 2560 px width
    photo_604 - URL of image with 604 px width
    photo_75 - URL of image with 75 px width
    photo_807 - URL of image with 807 px width
    placer_id - ID of the tag creator
    post_id - Post ID
    tag_created - Date when tag has been added in Unixtime
    tag_id - Tag ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    placer_id: Optional[int] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    tag_created: Optional[int] = None
    tag_id: Optional[int] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class TagsSuggestionItem(BaseObject):
    """VK Object photos/TagsSuggestionItem"""

    title: Optional[str] = None
    type: Optional[str] = None
    buttons: Optional[List["TagsSuggestionItemButton"]]
    photo: Optional["Photo"]
    tags: Optional[List["PhotoTag"]]


class TagsSuggestionItemButton(BaseObject):
    """VK Object photos/TagsSuggestionItemButton"""

    title: Optional[str] = None
    action: Optional[str] = None
    style: Optional[str] = None


class WallUploadResponse(BaseObject):
    """VK Object photos/WallUploadResponse

    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None
