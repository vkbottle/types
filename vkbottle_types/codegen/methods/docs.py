import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUploadServer, DocsDoc
from vkbottle_types.responses.base import (
    BaseGetUploadServerResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.docs import *  # noqa: F401,F403  # type: ignore


class DocsCategory(BaseCategory):
    async def add(
        self,
        doc_id: int,
        owner_id: int,
        access_key: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `docs.add()`

        :param doc_id: Document ID.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.add", params)
        model = DocsAddResponse
        return model(**response).response

    async def delete(
        self,
        doc_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `docs.delete()`

        :param doc_id: Document ID.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.delete", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit(
        self,
        doc_id: int,
        title: str,
        owner_id: typing.Optional[int] = None,
        tags: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `docs.edit()`

        :param doc_id: Document ID.
        :param title: Document title.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param tags: Document tags.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.edit", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        return_tags: typing.Optional[bool] = None,
        type: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DocsGetResponseModel:
        """Method `docs.get()`

        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_tags:
        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.get", params)
        model = DocsGetResponse
        return model(**response).response

    async def get_by_id(
        self,
        docs: typing.List[str],
        return_tags: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[DocsDoc]:
        """Method `docs.getById()`

        :param docs: Document IDs. Example: , "66748_91488,66748_91455",
        :param return_tags:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getById", params)
        model = DocsGetByIdResponse
        return model(**response).response

    async def get_messages_upload_server(
        self,
        peer_id: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `docs.getMessagesUploadServer()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param type: Document type.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getMessagesUploadServer", params)
        model = DocsGetUploadServerResponse
        return model(**response).response

    async def get_types(
        self,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DocsGetTypesResponseModel:
        """Method `docs.getTypes()`

        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getTypes", params)
        model = DocsGetTypesResponse
        return model(**response).response

    async def get_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `docs.getUploadServer()`

        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getUploadServer", params)
        model = DocsGetUploadServerResponse
        return model(**response).response

    async def get_wall_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `docs.getWallUploadServer()`

        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getWallUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def restore(
        self,
        doc_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `docs.restore()`

        :param doc_id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.restore", params)
        model = BaseOkResponse
        return model(**response).response

    async def save(
        self,
        file: str,
        return_tags: typing.Optional[bool] = None,
        tags: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> DocsSaveResponseModel:
        """Method `docs.save()`

        :param file: This parameter is returned when the file is [vk.ru/dev/upload_files_2|uploaded to the server].
        :param return_tags:
        :param tags: Document tags.
        :param title: Document title.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.save", params)
        model = DocsSaveResponse
        return model(**response).response

    async def search(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        return_tags: typing.Optional[bool] = None,
        search_own: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> DocsSearchResponseModel:
        """Method `docs.search()`

        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        :param q: Search query string.
        :param return_tags:
        :param search_own:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.search", params)
        model = DocsSearchResponse
        return model(**response).response


__all__ = ("DocsCategory",)
