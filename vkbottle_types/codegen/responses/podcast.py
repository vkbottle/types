import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import PodcastCover, PhotosPhotoSizes


class PodcastCoverResponseModel(BaseModel):
    sizes: typing.Optional[typing.List[PhotosPhotoSizes]] = Field(
        default=None,
    )


class PodcastCoverResponse(BaseResponse):
    response: "PodcastCoverResponseModel"


class PodcastExternalDataResponseModel(BaseModel):
    url: typing.Optional[str] = Field(
        default=None,
        description="Url of the podcast page",
    )

    owner_url: typing.Optional[str] = Field(
        default=None,
        description="Url of the podcasts owner community",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Podcast title",
    )

    owner_name: typing.Optional[str] = Field(
        default=None,
        description="Name of the podcasts owner community",
    )

    cover: typing.Optional["PodcastCover"] = Field(
        default=None,
        description="Podcast cover",
    )


class PodcastExternalDataResponse(BaseResponse):
    response: "PodcastExternalDataResponseModel"
