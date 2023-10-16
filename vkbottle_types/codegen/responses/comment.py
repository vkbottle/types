import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import WallWallComment


class CommentThreadResponseModel(BaseModel):
    count: int = Field(
        description="Comments number",
    )

    items: typing.Optional[typing.List[WallWallComment]] = Field(
        default=None,
    )

    can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the post",
    )

    show_reply_button: typing.Optional[bool] = Field(
        default=None,
        description="Information whether recommended to display reply button",
    )

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether groups can comment the post",
    )


class CommentThreadResponse(BaseResponse):
    response: "CommentThreadResponseModel"
