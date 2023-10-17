import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class LikesTypeResponseModel(enum.Enum):
    POST = "post"

    COMMENT = "comment"

    PHOTO = "photo"

    AUDIO = "audio"

    VIDEO = "video"

    NOTE = "note"

    MARKET = "market"

    PHOTO_COMMENT = "photo_comment"

    VIDEO_COMMENT = "video_comment"

    TOPIC_COMMENT = "topic_comment"

    MARKET_COMMENT = "market_comment"

    SITEPAGE = "sitepage"

    TEXTPOST = "textpost"

    COMMUNITY_REVIEW = "community_review"

    STORY = "story"

    GROUP_LIKE = "group_like"


class LikesTypeResponse(BaseResponse):
    response: "LikesTypeResponseModel"
