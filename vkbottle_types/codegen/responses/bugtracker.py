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
    errors: list["BugtrackerAddCompanyGroupsMembersError"] = Field()


class BugtrackerAddCompanyGroupsMembersResponse(BaseResponse):
    response: "BugtrackerAddCompanyGroupsMembersResponseModel" = Field()


class BugtrackerAddCompanyMembersResponseModel(BaseModel):
    errors: list[str] = Field()


class BugtrackerAddCompanyMembersResponse(BaseResponse):
    response: "BugtrackerAddCompanyMembersResponseModel" = Field()


class BugtrackerCreateCommentResponseModel(BaseModel):
    comment: "BugtrackerComment" = Field()
    comment_flood: bool | None = Field(
        default=None,
    )
    subscribe_state: "BugtrackerBugreportSubscribeState | None" = Field(
        default=None,
    )


class BugtrackerCreateCommentResponse(BaseResponse):
    response: "BugtrackerCreateCommentResponseModel" = Field()


class BugtrackerGetBugreportByIdResponseModel(BaseModel):
    bugreport: "BugtrackerBugreport | None" = Field(
        default=None,
    )
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )


class BugtrackerGetBugreportByIdResponse(BaseResponse):
    response: "BugtrackerGetBugreportByIdResponseModel" = Field()


class BugtrackerGetCompanyGroupMembersResponseModel(BaseModel):
    user_ids: list[int] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )


class BugtrackerGetCompanyGroupMembersResponse(BaseResponse):
    response: "BugtrackerGetCompanyGroupMembersResponseModel" = Field()


class BugtrackerGetCompanyMembersResponseModel(BaseModel):
    company_members: list["BugtrackerCompanyMember"] = Field()
    count: int = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )


class BugtrackerGetCompanyMembersResponse(BaseResponse):
    response: "BugtrackerGetCompanyMembersResponseModel" = Field()


class BugtrackerGetDownloadVersionUrlResponseModel(BaseModel):
    url: str = Field()
    app_title: str | None = Field(
        default=None,
    )
    bundle_name: str | None = Field(
        default=None,
    )
    build_id: int | None = Field(
        default=None,
    )
    build_name: str | None = Field(
        default=None,
    )
    build_title: str | None = Field(
        default=None,
    )


class BugtrackerGetDownloadVersionUrlResponse(BaseResponse):
    response: "BugtrackerGetDownloadVersionUrlResponseModel" = Field()
