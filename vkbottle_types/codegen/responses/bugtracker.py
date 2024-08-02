import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    BugtrackerAddCompanyGroupsMembersError,
    BugtrackerBugreport,
    BugtrackerBugreportSubscribeState,
    BugtrackerComment,
    BugtrackerCompanyMember,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class BugtrackerAddCompanyGroupsMembersResponseModel(BaseModel):
    errors: typing.List["BugtrackerAddCompanyGroupsMembersError"] = Field()


class BugtrackerAddCompanyGroupsMembersResponse(BaseResponse):
    response: "BugtrackerAddCompanyGroupsMembersResponseModel" = Field()


class BugtrackerAddCompanyMembersResponseModel(BaseModel):
    errors: typing.List[str] = Field()


class BugtrackerAddCompanyMembersResponse(BaseResponse):
    response: "BugtrackerAddCompanyMembersResponseModel" = Field()


class BugtrackerCreateCommentResponseModel(BaseModel):
    comment: "BugtrackerComment" = Field()
    comment_flood: typing.Optional[bool] = Field(
        default=None,
    )
    subscribe_state: typing.Optional["BugtrackerBugreportSubscribeState"] = Field(
        default=None,
    )


class BugtrackerCreateCommentResponse(BaseResponse):
    response: "BugtrackerCreateCommentResponseModel" = Field()


class BugtrackerGetBugreportByIdResponseModel(BaseModel):
    bugreport: typing.Optional["BugtrackerBugreport"] = Field(
        default=None,
    )
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )


class BugtrackerGetBugreportByIdResponse(BaseResponse):
    response: "BugtrackerGetBugreportByIdResponseModel" = Field()


class BugtrackerGetCompanyGroupMembersResponseModel(BaseModel):
    user_ids: typing.List[int] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )


class BugtrackerGetCompanyGroupMembersResponse(BaseResponse):
    response: "BugtrackerGetCompanyGroupMembersResponseModel" = Field()


class BugtrackerGetCompanyMembersResponseModel(BaseModel):
    company_members: typing.List["BugtrackerCompanyMember"] = Field()
    count: int = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )


class BugtrackerGetCompanyMembersResponse(BaseResponse):
    response: "BugtrackerGetCompanyMembersResponseModel" = Field()


class BugtrackerGetDownloadVersionUrlResponseModel(BaseModel):
    url: str = Field()
    app_title: typing.Optional[str] = Field(
        default=None,
    )
    bundle_name: typing.Optional[str] = Field(
        default=None,
    )
    build_id: typing.Optional[int] = Field(
        default=None,
    )
    build_name: typing.Optional[str] = Field(
        default=None,
    )
    build_title: typing.Optional[str] = Field(
        default=None,
    )


class BugtrackerGetDownloadVersionUrlResponse(BaseResponse):
    response: "BugtrackerGetDownloadVersionUrlResponseModel" = Field()
