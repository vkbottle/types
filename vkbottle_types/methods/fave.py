from vkbottle_types.responses import fave, base
from typing import Optional, Any, List
import typing
from .base_category import BaseCategory

if typing.TYPE_CHECKING:
    from vkbottle_types.objects import base as objects_base


class FaveCategory(BaseCategory):
    async def add_article(self, url: str) -> base.OkResponseModel:
        """fave.addArticle method
        :param url:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.addArticle", params))

    async def add_link(self, link: str) -> base.OkResponseModel:
        """Adds a link to user faves.
        :param link: Link URL.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.addLink", params))

    async def add_page(
        self, user_id: Optional[int] = None, group_id: Optional[int] = None
    ) -> base.OkResponseModel:
        """fave.addPage method
        :param user_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.addPage", params))

    async def add_post(
        self, owner_id: int, id: int, access_key: Optional[str] = None
    ) -> base.OkResponseModel:
        """fave.addPost method
        :param owner_id:
        :param id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.addPost", params))

    async def add_product(
        self, owner_id: int, id: int, access_key: Optional[str] = None
    ) -> base.OkResponseModel:
        """fave.addProduct method
        :param owner_id:
        :param id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.addProduct", params))

    async def add_tag(
        self, name: Optional[str] = None, position: Optional[str] = None
    ) -> fave.AddTagResponseModel:
        """fave.addTag method
        :param name:
        :param position:
        """

        params = self.get_set_params(locals())
        return fave.AddTagResponse(**await self.api.request("fave.addTag", params))

    async def add_video(
        self, owner_id: int, id: int, access_key: Optional[str] = None
    ) -> base.OkResponseModel:
        """fave.addVideo method
        :param owner_id:
        :param id:
        :param access_key:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.addVideo", params))

    async def edit_tag(self, id: int, name: str) -> base.OkResponseModel:
        """fave.editTag method
        :param id:
        :param name:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.editTag", params))

    async def get(
        self,
        extended: Optional[bool] = None,
        item_type: Optional[str] = None,
        tag_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[str] = None,
        is_from_snackbar: Optional[bool] = None,
    ) -> fave.GetExtendedResponseModel:
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
        return fave.GetExtendedResponse(**await self.api.request("fave.get", params))

    async def get_pages(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        type: Optional[str] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
        tag_id: Optional[int] = None,
    ) -> fave.GetPagesResponseModel:
        """fave.getPages method
        :param offset:
        :param count:
        :param type:
        :param fields:
        :param tag_id:
        """

        params = self.get_set_params(locals())
        return fave.GetPagesResponse(**await self.api.request("fave.getPages", params))

    async def get_tags(
        self,
    ) -> fave.GetTagsResponseModel:
        """fave.getTags method"""

        params = self.get_set_params(locals())
        return fave.GetTagsResponse(**await self.api.request("fave.getTags", params))

    async def mark_seen(
        self,
    ) -> base.BoolResponseModel:
        """fave.markSeen method"""

        params = self.get_set_params(locals())
        return base.BoolResponse(**await self.api.request("fave.markSeen", params))

    async def remove_article(
        self, owner_id: int, article_id: int
    ) -> base.BoolResponseModel:
        """fave.removeArticle method
        :param owner_id:
        :param article_id:
        """

        params = self.get_set_params(locals())
        return base.BoolResponse(**await self.api.request("fave.removeArticle", params))

    async def remove_link(
        self, link_id: Optional[str] = None, link: Optional[str] = None
    ) -> base.OkResponseModel:
        """Removes link from the user's faves.
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.removeLink", params))

    async def remove_page(
        self, user_id: Optional[int] = None, group_id: Optional[int] = None
    ) -> base.OkResponseModel:
        """fave.removePage method
        :param user_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.removePage", params))

    async def remove_post(self, owner_id: int, id: int) -> base.OkResponseModel:
        """fave.removePost method
        :param owner_id:
        :param id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.removePost", params))

    async def remove_product(self, owner_id: int, id: int) -> base.OkResponseModel:
        """fave.removeProduct method
        :param owner_id:
        :param id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.removeProduct", params))

    async def remove_tag(self, id: int) -> base.OkResponseModel:
        """fave.removeTag method
        :param id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.removeTag", params))

    async def reorder_tags(self, ids: List[int]) -> base.OkResponseModel:
        """fave.reorderTags method
        :param ids:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.reorderTags", params))

    async def set_page_tags(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        tag_ids: Optional[List[int]] = None,
    ) -> base.OkResponseModel:
        """fave.setPageTags method
        :param user_id:
        :param group_id:
        :param tag_ids:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("fave.setPageTags", params))

    async def set_tags(
        self,
        item_type: Optional[str] = None,
        item_owner_id: Optional[int] = None,
        item_id: Optional[int] = None,
        tag_ids: Optional[List[int]] = None,
        link_id: Optional[str] = None,
        link_url: Optional[str] = None,
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
        return base.OkResponse(**await self.api.request("fave.setTags", params))

    async def track_page_interaction(
        self, user_id: Optional[int] = None, group_id: Optional[int] = None
    ) -> base.OkResponseModel:
        """fave.trackPageInteraction method
        :param user_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("fave.trackPageInteraction", params)
        )
