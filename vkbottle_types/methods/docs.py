from vkbottle_types.responses import docs, base
from typing import Optional, Any, List
from .base_category import BaseCategory


class DocsCategory(BaseCategory):
    async def add(
        self, owner_id: int, doc_id: int, access_key: Optional[str] = None
    ) -> docs.AddResponseModel:
        """Copies a document to a user's or community's document list.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.
        """

        params = self.get_set_params(locals())
        return docs.AddResponse(**await self.api.request("docs.add", params))

    async def delete(self, owner_id: int, doc_id: int) -> base.OkResponseModel:
        """Deletes a user or community document.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("docs.delete", params))

    async def edit(
        self,
        owner_id: int,
        doc_id: int,
        title: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> base.OkResponseModel:
        """Edits a document.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param title: Document title.
        :param tags: Document tags.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("docs.edit", params))

    async def get(
        self,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        type: Optional[int] = None,
        owner_id: Optional[int] = None,
        return_tags: Optional[bool] = None,
    ) -> docs.GetResponseModel:
        """Returns detailed information about user or community documents.
        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param type:
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_tags:
        """

        params = self.get_set_params(locals())
        return docs.GetResponse(**await self.api.request("docs.get", params))

    async def get_by_id(
        self, docs: List[str], return_tags: Optional[bool] = None
    ) -> docs.GetByIdResponseModel:
        """Returns information about documents by their IDs.
        :param docs: Document IDs. Example: , "66748_91488,66748_91455",
        :param return_tags:
        """

        params = self.get_set_params(locals())
        return docs.GetByIdResponse(**await self.api.request("docs.getById", params))

    async def get_messages_upload_server(
        self, type: Optional[str] = None, peer_id: Optional[int] = None
    ) -> base.GetUploadServerResponseModel:
        """Returns the server address for document upload.
        :param type: Document type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """

        params = self.get_set_params(locals())
        return base.GetUploadServerResponse(
            **await self.api.request("docs.getMessagesUploadServer", params)
        )

    async def get_types(self, owner_id: int) -> docs.GetTypesResponseModel:
        """Returns documents types available for current user.
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        return docs.GetTypesResponse(**await self.api.request("docs.getTypes", params))

    async def get_upload_server(
        self, group_id: Optional[int] = None
    ) -> docs.GetUploadServerModel:
        """Returns the server address for document upload.
        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        params = self.get_set_params(locals())
        return docs.GetUploadServer(
            **await self.api.request("docs.getUploadServer", params)
        )

    async def get_wall_upload_server(
        self, group_id: Optional[int] = None
    ) -> base.GetUploadServerResponseModel:
        """Returns the server address for document upload onto a user's or community's wall.
        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        params = self.get_set_params(locals())
        return base.GetUploadServerResponse(
            **await self.api.request("docs.getWallUploadServer", params)
        )

    async def save(
        self,
        file: str,
        title: Optional[str] = None,
        tags: Optional[str] = None,
        return_tags: Optional[bool] = None,
    ) -> docs.SaveResponseModel:
        """Saves a document after [vk.com/dev/upload_files_2|uploading it to a server].
        :param file: This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: Document title.
        :param tags: Document tags.
        :param return_tags:
        """

        params = self.get_set_params(locals())
        return docs.SaveResponse(**await self.api.request("docs.save", params))

    async def search(
        self,
        q: str,
        search_own: Optional[bool] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        return_tags: Optional[bool] = None,
    ) -> docs.SearchResponseModel:
        """Returns a list of documents matching the search criteria.
        :param q: Search query string.
        :param search_own:
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        :param return_tags:
        """

        params = self.get_set_params(locals())
        return docs.SearchResponse(**await self.api.request("docs.search", params))
