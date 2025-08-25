import typing

from typing_extensions import Literal

from vkbottle_types.codegen.methods.video import VideoCategory as _VideoCategory  # type: ignore
from vkbottle_types.codegen.responses.base import BaseOkResponse, BaseOkResponseModel
from vkbottle_types.codegen.responses.video import VideoChangeVideoAlbumsResponse

if typing.TYPE_CHECKING:
    from vkbottle import ABCAPI  # type: ignore


class VideoCategory(_VideoCategory):  # type: ignore
    def __init__(self, api: "ABCAPI") -> None:
        super().__init__(api)

    @typing.overload  # type: ignore
    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = ...,
        album_ids: typing.Optional[Literal[None]] = None,
        **kwargs,
    ) -> BaseOkResponseModel: ...

    @typing.overload
    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[Literal[None]] = None,
        album_ids: typing.Optional[typing.List[int]] = ...,
        **kwargs,
    ) -> typing.List[int]: ...

    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> typing.Union[BaseOkResponseModel, typing.List[int]]:
        """video.addToAlbum method

        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.addToAlbum", params)
        model = self.get_model(
            ((("album_ids",), VideoChangeVideoAlbumsResponse),),
            default=BaseOkResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload  # type: ignore
    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = ...,
        album_ids: typing.Optional[Literal[None]] = None,
        **kwargs,
    ) -> BaseOkResponseModel: ...

    @typing.overload
    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[Literal[None]] = None,
        album_ids: typing.Optional[typing.List[int]] = ...,
        **kwargs,
    ) -> typing.List[int]: ...

    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> typing.Union[BaseOkResponseModel, typing.List[int]]:
        """video.removeFromAlbum method

        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.removeFromAlbum", params)
        model = self.get_model(
            ((("album_ids",), VideoChangeVideoAlbumsResponse),),
            default=BaseOkResponse,
            params=params,
        )
        return model(**response).response


__all__ = ("VideoCategory",)
