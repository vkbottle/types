import typing
from typing import Optional, List

from vkbottle_types.responses import base, market
from .base_category import BaseCategory

if typing.TYPE_CHECKING:
    from vkbottle_types.objects import users as objects_users


class MarketCategory(BaseCategory):
    async def add(
        self,
        owner_id: int,
        name: str,
        description: str,
        category_id: int,
        main_photo_id: int,
        price: Optional[float] = None,
        old_price: Optional[float] = None,
        deleted: Optional[bool] = None,
        photo_ids: Optional[List[int]] = None,
        url: Optional[str] = None,
        dimension_width: Optional[int] = None,
        dimension_height: Optional[int] = None,
        dimension_length: Optional[int] = None,
        weight: Optional[int] = None,
        **kwargs
    ) -> market.AddResponseModel:
        """Ads a new item to the market.
        :param owner_id: ID of an item owner community.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param main_photo_id: Cover photo ID.
        :param price: Item price.
        :param old_price:
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.
        :param dimension_width:
        :param dimension_height:
        :param dimension_length:
        :param weight:
        """

        params = self.get_set_params(locals())
        return market.AddResponse(**await self.api.request("market.add", params))

    async def add_album(
        self,
        owner_id: int,
        title: str,
        photo_id: Optional[int] = None,
        main_album: Optional[bool] = None,
        **kwargs
    ) -> market.AddAlbumResponseModel:
        """Creates new collection of items
        :param owner_id: ID of an item owner community.
        :param title: Collection title.
        :param photo_id: Cover photo ID.
        :param main_album: Set as main ('1' – set, '0' – no).
        """

        params = self.get_set_params(locals())
        return market.AddAlbumResponse(
            **await self.api.request("market.addAlbum", params)
        )

    async def add_to_album(
        self, owner_id: int, item_id: int, album_ids: List[int], **kwargs
    ) -> base.OkResponseModel:
        """Adds an item to one or multiple collections.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to add item to.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.addToAlbum", params))

    async def create_comment(
        self,
        owner_id: int,
        item_id: int,
        message: Optional[str] = None,
        attachments: Optional[List[str]] = None,
        from_group: Optional[bool] = None,
        reply_to_comment: Optional[int] = None,
        sticker_id: Optional[int] = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> market.CreateCommentResponseModel:
        """Creates a new comment for an item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param message: Comment text (required if 'attachments' parameter is not specified)
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param reply_to_comment: ID of a comment to reply with current comment to.
        :param sticker_id: Sticker ID.
        :param guid: Random value to avoid resending one comment.
        """

        params = self.get_set_params(locals())
        return market.CreateCommentResponse(
            **await self.api.request("market.createComment", params)
        )

    async def delete(
        self, owner_id: int, item_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Deletes an item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.delete", params))

    async def delete_album(
        self, owner_id: int, album_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a collection of items.
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.deleteAlbum", params))

    async def delete_comment(
        self, owner_id: int, comment_id: int, **kwargs
    ) -> market.DeleteCommentResponseModel:
        """Deletes an item's comment
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: comment id
        """

        params = self.get_set_params(locals())
        return market.DeleteCommentResponse(
            **await self.api.request("market.deleteComment", params)
        )

    async def edit(
        self,
        owner_id: int,
        item_id: int,
        name: str,
        description: str,
        category_id: int,
        price: float,
        main_photo_id: int,
        deleted: Optional[bool] = None,
        photo_ids: Optional[List[int]] = None,
        url: Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits an item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param main_photo_id: Cover photo ID.
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.edit", params))

    async def edit_album(
        self,
        owner_id: int,
        album_id: int,
        title: str,
        photo_id: Optional[int] = None,
        main_album: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits a collection of items
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        :param title: Collection title.
        :param photo_id: Cover photo id
        :param main_album: Set as main ('1' – set, '0' – no).
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.editAlbum", params))

    async def edit_comment(
        self,
        owner_id: int,
        comment_id: int,
        message: Optional[str] = None,
        attachments: Optional[List[str]] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Chages item comment's text
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param message: New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.editComment", params))

    async def get(
        self,
        owner_id: int,
        album_id: Optional[int] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> market.GetExtendedResponseModel:
        """Returns items list for a community.
        :param owner_id: ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_id:
        :param count: Number of items to return.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' – method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        """

        params = self.get_set_params(locals())
        return market.GetExtendedResponse(
            **await self.api.request("market.get", params)
        )

    async def get_album_by_id(
        self, owner_id: int, album_ids: List[int], **kwargs
    ) -> market.GetAlbumByIdResponseModel:
        """Returns items album's data
        :param owner_id: identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_ids: collections identifiers to obtain data from
        """

        params = self.get_set_params(locals())
        return market.GetAlbumByIdResponse(
            **await self.api.request("market.getAlbumById", params)
        )

    async def get_albums(
        self,
        owner_id: int,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> market.GetAlbumsResponseModel:
        """Returns community's collections list.
        :param owner_id: ID of an items owner community.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        """

        params = self.get_set_params(locals())
        return market.GetAlbumsResponse(
            **await self.api.request("market.getAlbums", params)
        )

    async def get_by_id(
        self, item_ids: List[str], extended: Optional[bool] = None, **kwargs
    ) -> market.GetByIdExtendedResponseModel:
        """Returns information about market items by their ids.
        :param item_ids: Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        """

        params = self.get_set_params(locals())
        return market.GetByIdExtendedResponse(
            **await self.api.request("market.getById", params)
        )

    async def get_categories(
        self, count: Optional[int] = None, offset: Optional[int] = None, **kwargs
    ) -> market.GetCategoriesResponseModel:
        """Returns a list of market categories.
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        """

        params = self.get_set_params(locals())
        return market.GetCategoriesResponse(
            **await self.api.request("market.getCategories", params)
        )

    async def get_comments(
        self,
        owner_id: int,
        item_id: int,
        need_likes: Optional[bool] = None,
        start_comment_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[str] = None,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        **kwargs
    ) -> market.GetCommentsResponseModel:
        """Returns comments list for an item.
        :param owner_id: ID of an item owner community
        :param item_id: Item ID.
        :param need_likes: '1' — to return likes info.
        :param start_comment_id: ID of a comment to start a list from (details below).
        :param offset:
        :param count: Number of results to return.
        :param sort: Sort order ('asc' — from old to new, 'desc' — from new to old)
        :param extended: '1' — comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
        :param fields: List of additional profile fields to return. See the [vk.com/dev/fields|details]
        """

        params = self.get_set_params(locals())
        return market.GetCommentsResponse(
            **await self.api.request("market.getComments", params)
        )

    async def remove_from_album(
        self, owner_id: int, item_id: int, album_ids: List[int], **kwargs
    ) -> base.OkResponseModel:
        """Removes an item from one or multiple collections.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to remove item from.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("market.removeFromAlbum", params)
        )

    async def reorder_albums(
        self,
        owner_id: int,
        album_id: int,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Reorders the collections list.
        :param owner_id: ID of an item owner community.
        :param album_id: Collection ID.
        :param before: ID of a collection to place current collection before it.
        :param after: ID of a collection to place current collection after it.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.reorderAlbums", params))

    async def reorder_items(
        self,
        owner_id: int,
        item_id: int,
        album_id: Optional[int] = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Changes item place in a collection.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_id: ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param before: ID of an item to place current item before it.
        :param after: ID of an item to place current item after it.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.reorderItems", params))

    async def report(
        self, owner_id: int, item_id: int, reason: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Sends a complaint to the item.
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.report", params))

    async def report_comment(
        self, owner_id: int, comment_id: int, reason: int, **kwargs
    ) -> base.OkResponseModel:
        """Sends a complaint to the item's comment.
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.reportComment", params))

    async def restore(
        self, owner_id: int, item_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Restores recently deleted item
        :param owner_id: ID of an item owner community.
        :param item_id: Deleted item ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("market.restore", params))

    async def restore_comment(
        self, owner_id: int, comment_id: int, **kwargs
    ) -> market.RestoreCommentResponseModel:
        """Restores a recently deleted comment
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: deleted comment id
        """

        params = self.get_set_params(locals())
        return market.RestoreCommentResponse(
            **await self.api.request("market.restoreComment", params)
        )

    async def search(
        self,
        owner_id: int,
        album_id: Optional[int] = None,
        q: Optional[str] = None,
        price_from: Optional[int] = None,
        price_to: Optional[int] = None,
        sort: Optional[int] = None,
        rev: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        status: Optional[int] = None,
        **kwargs
    ) -> market.SearchExtendedResponseModel:
        """Searches market items in a community's catalog
        :param owner_id: ID of an items owner community.
        :param album_id:
        :param q: Search query, for example "pink slippers".
        :param price_from: Minimum item price value.
        :param price_to: Maximum item price value.
        :param sort:
        :param rev: '0' — do not use reverse order, '1' — use reverse order
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param status:
        """

        params = self.get_set_params(locals())
        return market.SearchExtendedResponse(
            **await self.api.request("market.search", params)
        )
