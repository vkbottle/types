import typing
from .base_category import BaseCategory
from vkbottle_types.responses import base, fave


class FaveCategory(BaseCategory):
    async def add_article(
        self, url: str, **kwargs
    ) -> base.OkResponseModel:
        """fave.addArticle method
        :param url:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addArticle", params)
        model = base.OkResponse
        return model(**response).response

    async def add_link(
        self, link: str, **kwargs
    ) -> base.OkResponseModel:
        """Adds a link to user faves.
        :param link: Link URL.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addLink", params)
        model = base.OkResponse
        return model(**response).response

    async def add_page(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """fave.addPage method
        :param user_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addPage", params)
        model = base.OkResponse
        return model(**response).response

    async def add_post(
        self, owner_id: int, id: int, access_key: typing.Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """fave.addPost method
        :param owner_id:
        :param id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addPost", params)
        model = base.OkResponse
        return model(**response).response

    async def add_product(
        self, owner_id: int, id: int, access_key: typing.Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """fave.addProduct method
        :param owner_id:
        :param id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addProduct", params)
        model = base.OkResponse
        return model(**response).response

    async def add_tag(
        self,
        name: typing.Optional[str] = None,
        position: typing.Optional[str] = None,
        **kwargs
    ) -> fave.AddTagResponseModel:
        """fave.addTag method
        :param name:
        :param position:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addTag", params)
        model = fave.AddTagResponse
        return model(**response).response

    async def add_video(
        self, owner_id: int, id: int, access_key: typing.Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """fave.addVideo method
        :param owner_id:
        :param id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.addVideo", params)
        model = base.OkResponse
        return model(**response).response

    async def edit_tag(
        self, id: int, name: str, **kwargs
    ) -> base.OkResponseModel:
        """fave.editTag method
        :param id:
        :param name:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.editTag", params)
        model = base.OkResponse
        return model(**response).response

    async def get(
        self,
        extended: typing.Optional[bool] = None,
        item_type: typing.Optional[str] = None,
        tag_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        is_from_snackbar: typing.Optional[bool] = None,
        **kwargs
    ) -> fave.GetResponseModel:
        """fave.get method
        :param extended: '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type:
        :param tag_id: Tag ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields:
        :param is_from_snackbar:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.get", params)
        model = self.get_model(
            {("extended",): fave.GetExtendedResponse},
            default=fave.GetResponse,
            params=params,
        )
        return model(**response).response

    async def get_pages(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        tag_id: typing.Optional[int] = None,
        **kwargs
    ) -> fave.GetPagesResponseModel:
        """fave.getPages method
        :param offset:
        :param count:
        :param type:
        :param fields:
        :param tag_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.getPages", params)
        model = fave.GetPagesResponse
        return model(**response).response

    async def get_tags(
        self, **kwargs
    ) -> fave.GetTagsResponseModel:
        """fave.getTags method"""

        params = self.get_set_params(locals())
        response = await self.api.request("fave.getTags", params)
        model = fave.GetTagsResponse
        return model(**response).response

    async def mark_seen(
        self, **kwargs
    ) -> base.BoolResponseModel:
        """fave.markSeen method"""

        params = self.get_set_params(locals())
        response = await self.api.request("fave.markSeen", params)
        model = base.BoolResponse
        return model(**response).response

    async def remove_article(
        self, owner_id: int, article_id: int, **kwargs
    ) -> base.BoolResponseModel:
        """fave.removeArticle method
        :param owner_id:
        :param article_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeArticle", params)
        model = base.BoolResponse
        return model(**response).response

    async def remove_link(
        self,
        link_id: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Removes link from the user's faves.
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeLink", params)
        model = base.OkResponse
        return model(**response).response

    async def remove_page(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """fave.removePage method
        :param user_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removePage", params)
        model = base.OkResponse
        return model(**response).response

    async def remove_post(
        self, owner_id: int, id: int, **kwargs
    ) -> base.OkResponseModel:
        """fave.removePost method
        :param owner_id:
        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removePost", params)
        model = base.OkResponse
        return model(**response).response

    async def remove_product(
        self, owner_id: int, id: int, **kwargs
    ) -> base.OkResponseModel:
        """fave.removeProduct method
        :param owner_id:
        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeProduct", params)
        model = base.OkResponse
        return model(**response).response

    async def remove_tag(
        self, id: int, **kwargs
    ) -> base.OkResponseModel:
        """fave.removeTag method
        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeTag", params)
        model = base.OkResponse
        return model(**response).response

    async def remove_video(
        self, owner_id: int, id: int, **kwargs
    ) -> base.OkResponseModel:
        """fave.removeVideo method
        :param owner_id:
        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.removeVideo", params)
        model = base.OkResponse
        return model(**response).response

    async def reorder_tags(
        self, ids: typing.List[int], **kwargs
    ) -> base.OkResponseModel:
        """fave.reorderTags method
        :param ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.reorderTags", params)
        model = base.OkResponse
        return model(**response).response

    async def set_page_tags(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """fave.setPageTags method
        :param user_id:
        :param group_id:
        :param tag_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.setPageTags", params)
        model = base.OkResponse
        return model(**response).response

    async def set_tags(
        self,
        item_type: typing.Optional[str] = None,
        item_owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
        link_id: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """fave.setTags method
        :param item_type:
        :param item_owner_id:
        :param item_id:
        :param tag_ids:
        :param link_id:
        :param link_url:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.setTags", params)
        model = base.OkResponse
        return model(**response).response

    async def track_page_interaction(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """fave.trackPageInteraction method
        :param user_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("fave.trackPageInteraction", params)
        model = base.OkResponse
        return model(**response).response
