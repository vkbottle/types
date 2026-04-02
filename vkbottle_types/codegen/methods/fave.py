import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import *
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.fave import *  # noqa: F401,F403  # type: ignore


class FaveCategory(BaseCategory):
    async def add_article(
        self,
        url: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.addArticle()`

        :param url:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addArticle", params)
        model = BaseOkResponse
        return model(**response).response

    async def add_link(
        self,
        link: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.addLink()`

        :param link: Link URL.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addLink", params)
        model = BaseOkResponse
        return model(**response).response

    async def add_page(
        self,
        group_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.addPage()`

        :param group_id:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addPage", params)
        model = BaseOkResponse
        return model(**response).response

    async def add_post(
        self,
        id: int,
        owner_id: int,
        access_key: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.addPost()`

        :param id:
        :param owner_id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addPost", params)
        model = BaseOkResponse
        return model(**response).response

    async def add_product(
        self,
        id: int,
        owner_id: int,
        access_key: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.addProduct()`

        :param id:
        :param owner_id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addProduct", params)
        model = BaseOkResponse
        return model(**response).response

    async def add_tag(
        self,
        name: str | None = None,
        position: str | None = None,
        **kwargs: typing.Any,
    ) -> "FaveTag":
        """Method `fave.addTag()`

        :param name:
        :param position:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addTag", params)
        model = FaveAddTagResponse
        return model(**response).response

    async def add_video(
        self,
        id: int,
        owner_id: int,
        access_key: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.addVideo()`

        :param id:
        :param owner_id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addVideo", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_tag(
        self,
        id: int,
        name: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.editTag()`

        :param id:
        :param name:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.editTag", params)
        model = BaseOkResponse
        return model(**response).response

    @typing.overload
    async def get(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: str | None = None,
        is_from_snackbar: bool | None = None,
        item_type: str | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
        **kwargs: typing.Any,
    ) -> FaveGetExtendedResponseModel: ...

    @typing.overload
    async def get(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: str | None = None,
        is_from_snackbar: bool | None = None,
        item_type: str | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
        **kwargs: typing.Any,
    ) -> FaveGetResponseModel: ...

    async def get(
        self,
        extended: bool | None = None,
        count: int | None = None,
        fields: str | None = None,
        is_from_snackbar: bool | None = None,
        item_type: str | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
        **kwargs: typing.Any,
    ) -> FaveGetExtendedResponseModel | FaveGetResponseModel:
        """Method `fave.get()`

        :param extended: '1' - to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param count: Number of users to return.
        :param fields:
        :param is_from_snackbar:
        :param item_type:
        :param offset: Offset needed to return a specific subset of users.
        :param tag_id: Tag ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.get", params)
        model = self.get_model(
            ((("extended",), FaveGetExtendedResponse),),
            default=FaveGetResponse,
            params=params,
        )
        return model(**response).response

    async def get_pages(
        self,
        count: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
        type: str | None = None,
        **kwargs: typing.Any,
    ) -> FaveGetPagesResponseModel:
        """Method `fave.getPages()`

        :param count:
        :param fields:
        :param offset:
        :param tag_id:
        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.getPages", params)
        model = FaveGetPagesResponse
        return model(**response).response

    async def get_tags(
        self,
        **kwargs: typing.Any,
    ) -> FaveGetTagsResponseModel:
        """Method `fave.getTags()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("fave.getTags", params)
        model = FaveGetTagsResponse
        return model(**response).response

    async def mark_seen(
        self,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `fave.markSeen()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("fave.markSeen", params)
        model = BaseBoolResponse
        return model(**response).response

    async def remove_article(
        self,
        article_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `fave.removeArticle()`

        :param article_id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeArticle", params)
        model = BaseBoolResponse
        return model(**response).response

    async def remove_link(
        self,
        link: str | None = None,
        link_id: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.removeLink()`

        :param link: Link URL
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeLink", params)
        model = BaseOkResponse
        return model(**response).response

    async def remove_page(
        self,
        group_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.removePage()`

        :param group_id:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removePage", params)
        model = BaseOkResponse
        return model(**response).response

    async def remove_post(
        self,
        id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.removePost()`

        :param id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removePost", params)
        model = BaseOkResponse
        return model(**response).response

    async def remove_product(
        self,
        id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.removeProduct()`

        :param id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeProduct", params)
        model = BaseOkResponse
        return model(**response).response

    async def remove_tag(
        self,
        id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.removeTag()`

        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeTag", params)
        model = BaseOkResponse
        return model(**response).response

    async def remove_video(
        self,
        id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.removeVideo()`

        :param id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeVideo", params)
        model = BaseOkResponse
        return model(**response).response

    async def reorder_tags(
        self,
        ids: list[int],
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.reorderTags()`

        :param ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.reorderTags", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_page_tags(
        self,
        group_id: int | None = None,
        tag_ids: list[int] | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.setPageTags()`

        :param group_id:
        :param tag_ids:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.setPageTags", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_tags(
        self,
        item_id: int | None = None,
        item_owner_id: int | None = None,
        item_type: str | None = None,
        link_id: str | None = None,
        link_url: str | None = None,
        tag_ids: list[int] | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.setTags()`

        :param item_id:
        :param item_owner_id:
        :param item_type:
        :param link_id:
        :param link_url:
        :param tag_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.setTags", params)
        model = BaseOkResponse
        return model(**response).response

    async def track_page_interaction(
        self,
        group_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `fave.trackPageInteraction()`

        :param group_id:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.trackPageInteraction", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("FaveCategory",)
