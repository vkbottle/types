import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.docs import *
from vkbottle_types.responses.base import OkResponse


class DocsCategory(BaseCategory):
    async def add(
        self,
        owner_id: int,
        doc_id: int,
        access_key: typing.Optional[str] = None,
        **kwargs,
    ) -> DocsAddResponseModel:
        """docs.add method


        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsAddResponse

        return model(**response).response

    async def delete(
        self,
        owner_id: int,
        doc_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """docs.delete method


        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit(
        self,
        doc_id: int,
        title: str,
        owner_id: typing.Optional[int] = None,
        tags: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """docs.edit method


        :param doc_id: Document ID.
        :param title: Document title.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param tags: Document tags.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def get(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[int] = 0,
        owner_id: typing.Optional[int] = None,
        return_tags: typing.Optional[bool] = 0,
        **kwargs,
    ) -> DocsGetResponseModel:
        """docs.get method


        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param type:
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_tags:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsGetResponse

        return model(**response).response

    async def get_by_id(
        self,
        docs: typing.List[str],
        return_tags: typing.Optional[bool] = 0,
        **kwargs,
    ) -> DocsGetByIdResponseModel:
        """docs.getById method


        :param docs: Document IDs. Example: , "66748_91488,66748_91455",
        :param return_tags:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsGetByIdResponse

        return model(**response).response

    async def get_messages_upload_server(
        self,
        type: typing.Optional[str] = "doc",
        peer_id: typing.Optional[int] = None,
        **kwargs,
    ) -> DocsGetUploadServerResponseModel:
        """docs.getMessagesUploadServer method


        :param type: Document type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsGetUploadServerResponse

        return model(**response).response

    async def get_types(
        self,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ) -> DocsGetTypesResponseModel:
        """docs.getTypes method


        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsGetTypesResponse

        return model(**response).response

    async def get_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> DocsGetUploadServerResponseModel:
        """docs.getUploadServer method


        :param group_id: Community ID (if the document will be uploaded to the community).
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsGetUploadServerResponse

        return model(**response).response

    async def get_wall_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseGetUploadServerResponseModel:
        """docs.getWallUploadServer method


        :param group_id: Community ID (if the document will be uploaded to the community).
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseGetUploadServerResponse

        return model(**response).response

    async def save(
        self,
        file: str,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        return_tags: typing.Optional[bool] = 0,
        **kwargs,
    ) -> DocsSaveResponseModel:
        """docs.save method


        :param file: This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: Document title.
        :param tags: Document tags.
        :param return_tags:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsSaveResponse

        return model(**response).response

    async def search(
        self,
        q: typing.Optional[str] = None,
        search_own: typing.Optional[bool] = None,
        count: typing.Optional[int] = 20,
        offset: typing.Optional[int] = None,
        return_tags: typing.Optional[bool] = None,
        **kwargs,
    ) -> DocsSearchResponseModel:
        """docs.search method


        :param q: Search query string.
        :param search_own:
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        :param return_tags:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = DocsSearchResponse

        return model(**response).response


__all__ = ("DocsCategory",)
