from vkbottle_types.codegen.responses.wall import *  # noqa: F403,F401  # type: ignore


class WallGetByIdExtendedResponseModel(WallGetByIdExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()  # type: ignore


class WallGetByIdExtendedResponse(WallGetByIdExtendedResponse):  # type: ignore[no-redef]
    response: "WallGetByIdExtendedResponseModel" = Field()


class WallGetByIdResponseModel(WallGetByIdResponseModel):  # type: ignore[no-redef]
    items: typing.Optional[typing.List["WallWallpostFull"]] = Field(  # type: ignore
        default=None,
    )


class WallGetByIdResponse(WallGetByIdResponse):  # type: ignore[no-redef]
    response: "WallGetByIdResponseModel" = Field()


class WallGetExtendedResponseModel(WallGetExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()  # type: ignore


class WallGetExtendedResponse(WallGetExtendedResponse):  # type: ignore[no-redef]
    response: "WallGetExtendedResponseModel" = Field()


class WallGetResponseModel(WallGetResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()  # type: ignore


class WallGetResponse(WallGetResponse):  # type: ignore[no-redef]
    response: "WallGetResponseModel" = Field()


class WallSearchExtendedResponseModel(WallSearchExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()  # type: ignore


class WallSearchExtendedResponse(WallSearchExtendedResponse):  # type: ignore[no-redef]
    response: "WallSearchExtendedResponseModel" = Field()


class WallSearchResponseModel(WallSearchResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()  # type: ignore


class WallSearchResponse(WallSearchResponse):  # type: ignore[no-redef]
    response: "WallSearchResponseModel" = Field()
