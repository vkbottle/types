from vkbottle_types.codegen.responses.wall import *  # noqa: F403,F401

from .base_response import BaseResponse


class WallGetByIdExtendedResponseModel(WallGetByIdExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallGetByIdExtendedResponse(WallGetByIdExtendedResponse):  # type: ignore[no-redef]
    response: "WallGetByIdExtendedResponseModel" = Field()


class WallGetByIdResponseModel(WallGetByIdResponseModel):  # type: ignore[no-redef]
    items: typing.Optional[typing.List["WallWallpostFull"]] = Field(
        default=None,
    )


class WallGetByIdResponse(WallGetByIdResponse):  # type: ignore[no-redef]
    response: "WallGetByIdResponseModel" = Field()


class WallGetExtendedResponseModel(WallGetExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallGetExtendedResponse(WallGetExtendedResponse):  # type: ignore[no-redef]
    response: "WallGetExtendedResponseModel" = Field()


class WallGetResponseModel(WallGetResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallGetResponse(WallGetResponse):  # type: ignore[no-redef]
    response: "WallGetResponseModel" = Field()


class WallSearchExtendedResponseModel(WallSearchExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallSearchExtendedResponse(WallSearchExtendedResponse):  # type: ignore[no-redef]
    response: "WallSearchExtendedResponseModel" = Field()


class WallSearchResponseModel(WallSearchResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallSearchResponse(WallSearchResponse):  # type: ignore[no-redef]
    response: "WallSearchResponseModel" = Field()


localns = locals().copy()
for item in localns.values():
    if not (isinstance(item, type) and issubclass(item, BaseResponse)):
        continue
    
    for base in item.__bases__:
        if base is not BaseResponse and issubclass(base, BaseResponse):
            item.model_rebuild(force=True)

    item.model_rebuild(force=True, _types_namespace=localns)
