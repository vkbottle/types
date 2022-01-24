import typing

from typing_extensions import Literal
from vkbottle_types.responses.base import (
    BaseGetUploadServerResponse,
    BaseUploadServer,
    OkResponse,
)
from vkbottle_types.responses.docs import (
    AddResponse,
    DocsDoc,
    GetByIdResponse,
    GetResponse,
    GetResponseModel,
    GetTypesResponse,
    GetTypesResponseModel,
    GetUploadServerResponse,
    SaveResponse,
    SaveResponseModel,
    SearchResponse,
    SearchResponseModel,
)

from .base_category import BaseCategory


class DocsCategory(BaseCategory):
    async def add(
        self,
        owner_id: int,
        doc_id: int,
        access_key: typing.Optional[str] = None,
        **kwargs
    ) -> int:
        """Copies a document to a user's or community's document list.

        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.add", params)
        model = AddResponse
        return model(**response).response

    async def delete(self, owner_id: int, doc_id: int, **kwargs) -> int:
        """Deletes a user or community document.

        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.delete", params)
        model = OkResponse
        return model(**response).response

    async def edit(
        self,
        owner_id: int,
        doc_id: int,
        title: str,
        tags: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> int:
        """Edits a document.

        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param title: Document title.
        :param tags: Document tags.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.edit", params)
        model = OkResponse
        return model(**response).response

    async def get(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8] = None,
        owner_id: typing.Optional[int] = None,
        return_tags: typing.Optional[bool] = None,
        **kwargs
    ) -> GetResponseModel:
        """Returns detailed information about user or community documents.

        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param type:
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_tags:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.get", params)
        model = GetResponse
        return model(**response).response

    async def get_by_id(
        self,
        docs: typing.List[str],
        return_tags: typing.Optional[bool] = None,
        **kwargs
    ) -> typing.List[DocsDoc]:
        """Returns information about documents by their IDs.

        :param docs: Document IDs. Example: , "66748_91488,66748_91455",
        :param return_tags:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getById", params)
        model = GetByIdResponse
        return model(**response).response

    async def get_messages_upload_server(
        self,
        type: Literal["audio_message", "doc", "graffiti"] = None,
        peer_id: typing.Optional[int] = None,
        **kwargs
    ) -> BaseUploadServer:
        """Returns the server address for document upload.

        :param type: Document type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getMessagesUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def get_types(self, owner_id: int, **kwargs) -> GetTypesResponseModel:
        """Returns documents types available for current user.

        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getTypes", params)
        model = GetTypesResponse
        return model(**response).response

    async def get_upload_server(
        self, group_id: typing.Optional[int] = None, **kwargs
    ) -> BaseUploadServer:
        """Returns the server address for document upload.

        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getUploadServer", params)
        model = GetUploadServerResponse
        return model(**response).response

    async def get_wall_upload_server(
        self, group_id: typing.Optional[int] = None, **kwargs
    ) -> BaseUploadServer:
        """Returns the server address for document upload onto a user's or community's wall.

        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.getWallUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def save(
        self,
        file: str,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        return_tags: typing.Optional[bool] = None,
        **kwargs
    ) -> SaveResponseModel:
        """Saves a document after [vk.com/dev/upload_files_2|uploading it to a server].

        :param file: This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: Document title.
        :param tags: Document tags.
        :param return_tags:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.save", params)
        model = SaveResponse
        return model(**response).response

    async def search(
        self,
        q: str,
        search_own: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        return_tags: typing.Optional[bool] = None,
        **kwargs
    ) -> SearchResponseModel:
        """Returns a list of documents matching the search criteria.

        :param q: Search query string.
        :param search_own:
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        :param return_tags:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("docs.search", params)
        model = SearchResponse
        return model(**response).response
