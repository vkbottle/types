import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUploadServer, MarketUploadPhotoData, UsersFields
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseGetUploadServerResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.market import *  # noqa: F401,F403  # type: ignore


class MarketCategory(BaseCategory):
    async def add(
        self,
        category_id: int,
        description: str,
        name: str,
        owner_id: int,
        deleted: typing.Optional[bool] = None,
        dimension_height: typing.Optional[int] = None,
        dimension_length: typing.Optional[int] = None,
        dimension_width: typing.Optional[int] = None,
        is_main_variant: typing.Optional[bool] = None,
        main_photo_id: typing.Optional[int] = None,
        old_price: typing.Optional[float] = None,
        photo_ids: typing.Optional[typing.List[int]] = None,
        price: typing.Optional[float] = None,
        sku: typing.Optional[str] = None,
        stock_amount: typing.Optional[int] = None,
        url: typing.Optional[str] = None,
        variant_ids: typing.Optional[typing.List[int]] = None,
        video_ids: typing.Optional[typing.List[int]] = None,
        weight: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketAddResponseModel:
        """Method `market.add()`

        :param category_id: Item category ID.
        :param description: Item description.
        :param name: Item name.
        :param owner_id: ID of an item owner community.
        :param deleted: Item status ('1' - deleted, '0' - not deleted).
        :param dimension_height:
        :param dimension_length:
        :param dimension_width:
        :param is_main_variant: Is main in their group.
        :param main_photo_id: Cover photo ID.
        :param old_price:
        :param photo_ids: IDs of additional photos.
        :param price: Item price.
        :param sku:
        :param stock_amount:
        :param url: Url for button in market item.
        :param variant_ids: IDs of properties variants.
        :param video_ids: IDs of additional videos.
        :param weight:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.add", params)
        model = MarketAddResponse
        return model(**response).response

    async def add_album(
        self,
        owner_id: int,
        title: str,
        is_hidden: typing.Optional[bool] = None,
        main_album: typing.Optional[bool] = None,
        photo_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketAddAlbumResponseModel:
        """Method `market.addAlbum()`

        :param owner_id: ID of an item owner community.
        :param title: Collection title.
        :param is_hidden: Set as hidden
        :param main_album: Set as main ('1' - set, '0' - no).
        :param photo_id: Cover photo ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.addAlbum", params)
        model = MarketAddAlbumResponse
        return model(**response).response

    async def add_property(
        self,
        group_id: int,
        title: str,
        **kwargs: typing.Any,
    ) -> MarketAddPropertyResponseModel:
        """Method `market.addProperty()`

        :param group_id: Group id.
        :param title: Property name.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.addProperty", params)
        model = MarketAddPropertyResponse
        return model(**response).response

    async def add_property_variant(
        self,
        group_id: int,
        property_id: int,
        title: str,
        **kwargs: typing.Any,
    ) -> MarketAddPropertyVariantResponseModel:
        """Method `market.addPropertyVariant()`

        :param group_id: Group id.
        :param property_id: Property id.
        :param title: Variant name.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.addPropertyVariant", params)
        model = MarketAddPropertyVariantResponse
        return model(**response).response

    async def add_to_album(
        self,
        album_ids: typing.List[int],
        item_ids: typing.List[int],
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.addToAlbum()`

        :param album_ids: Collections IDs to add item to.
        :param item_ids:
        :param owner_id: ID of an item owner community.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.addToAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def create_comment(
        self,
        item_id: int,
        owner_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        guid: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `market.createComment()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param guid: Random value to avoid resending one comment.
        :param message: Comment text (required if 'attachments' parameter is not specified)
        :param reply_to_comment: ID of a comment to reply with current comment to.
        :param sticker_id: Sticker ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.createComment", params)
        model = MarketCreateCommentResponse
        return model(**response).response

    async def delete(
        self,
        item_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.delete()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.delete", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_album(
        self,
        album_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.deleteAlbum()`

        :param album_id: Collection ID.
        :param owner_id: ID of an collection owner community.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.deleteAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `market.deleteComment()`

        :param comment_id: comment id
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.ru/apiclub|VK API] community "
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.deleteComment", params)
        model = BaseBoolResponse
        return model(**response).response

    async def delete_property(
        self,
        group_id: int,
        property_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.deleteProperty()`

        :param group_id: Group id.
        :param property_id: Property id.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.deleteProperty", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_property_variant(
        self,
        group_id: int,
        variant_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.deletePropertyVariant()`

        :param group_id: Group id.
        :param variant_id: Variant id.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.deletePropertyVariant", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit(
        self,
        item_id: int,
        owner_id: int,
        category_id: typing.Optional[int] = None,
        deleted: typing.Optional[bool] = None,
        description: typing.Optional[str] = None,
        dimension_height: typing.Optional[int] = None,
        dimension_length: typing.Optional[int] = None,
        dimension_width: typing.Optional[int] = None,
        is_main_variant: typing.Optional[bool] = None,
        main_photo_id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        old_price: typing.Optional[float] = None,
        photo_ids: typing.Optional[typing.List[int]] = None,
        price: typing.Optional[float] = None,
        sku: typing.Optional[str] = None,
        stock_amount: typing.Optional[int] = None,
        url: typing.Optional[str] = None,
        variant_ids: typing.Optional[typing.List[int]] = None,
        video_ids: typing.Optional[typing.List[int]] = None,
        weight: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.edit()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param category_id: Item category ID.
        :param deleted: Item status ('1' - deleted, '0' - not deleted).
        :param description: Item description.
        :param dimension_height:
        :param dimension_length:
        :param dimension_width:
        :param is_main_variant: Is main in their group.
        :param main_photo_id: Cover photo ID.
        :param name: Item name.
        :param old_price:
        :param photo_ids: IDs of additional photos.
        :param price: Item price.
        :param sku:
        :param stock_amount:
        :param url: Url for button in market item.
        :param variant_ids: IDs of properties variants.
        :param video_ids: IDs of additional videos.
        :param weight:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.edit", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_album(
        self,
        album_id: int,
        owner_id: int,
        title: str,
        is_hidden: typing.Optional[bool] = None,
        main_album: typing.Optional[bool] = None,
        photo_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.editAlbum()`

        :param album_id: Collection ID.
        :param owner_id: ID of an collection owner community.
        :param title: Collection title.
        :param is_hidden: Set as hidden
        :param main_album: Set as main ('1' - set, '0' - no).
        :param photo_id: Cover photo id
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.editAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        owner_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        message: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.editComment()`

        :param comment_id: Comment ID.
        :param owner_id: ID of an item owner community.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param message: New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.editComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_order(
        self,
        order_id: int,
        user_id: int,
        comment_for_user: typing.Optional[str] = None,
        delivery_price: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        length: typing.Optional[int] = None,
        merchant_comment: typing.Optional[str] = None,
        payment_status: typing.Optional[str] = None,
        receipt_link: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        track_number: typing.Optional[str] = None,
        weight: typing.Optional[int] = None,
        width: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.editOrder()`

        :param order_id:
        :param user_id:
        :param comment_for_user:
        :param delivery_price:
        :param height:
        :param length:
        :param merchant_comment:
        :param payment_status:
        :param receipt_link:
        :param status:
        :param track_number:
        :param weight:
        :param width:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.editOrder", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_property(
        self,
        group_id: int,
        property_id: int,
        title: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.editProperty()`

        :param group_id: Group id.
        :param property_id: Property id.
        :param title: Property name
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.editProperty", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_property_variant(
        self,
        group_id: int,
        title: str,
        variant_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.editPropertyVariant()`

        :param group_id: Group id.
        :param title: Variant name.
        :param variant_id: Variant id.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.editPropertyVariant", params)
        model = BaseOkResponse
        return model(**response).response

    async def filter_categories(
        self,
        category_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> MarketGetCategoriesNewResponseModel:
        """Method `market.filterCategories()`

        :param category_id: Category_id filter categories
        :param count: Number of results to return.
        :param query: Query filter categories
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.filterCategories", params)
        model = MarketGetCategoriesNewResponse
        return model(**response).response

    @typing.overload
    async def get(
        self,
        owner_id: int,
        extended: typing.Literal[True],
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        need_variants: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        with_disabled: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> MarketGetExtendedResponseModel: ...

    @typing.overload
    async def get(
        self,
        owner_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        need_variants: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        with_disabled: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> MarketGetResponseModel: ...

    async def get(
        self,
        owner_id: int,
        extended: typing.Optional[bool] = None,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        need_variants: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        with_disabled: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MarketGetResponseModel, MarketGetExtendedResponseModel]:
        """Method `market.get()`

        :param owner_id: ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.ru/apiclub|VK API] community "
        :param extended: '1' - method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        :param album_id:
        :param count: Number of items to return.
        :param date_from: Items update date from (format: yyyy-mm-dd)
        :param date_to: Items update date to (format: yyyy-mm-dd)
        :param fields:
        :param need_variants: Add variants to response if exist
        :param offset: Offset needed to return a specific subset of results.
        :param with_disabled: Add disabled items to response
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.get", params)
        model = self.get_model(
            ((("extended",), MarketGetExtendedResponse),),
            default=MarketGetResponse,
            params=params,
        )
        return model(**response).response

    async def get_album_by_id(
        self,
        album_ids: typing.List[int],
        owner_id: int,
        **kwargs: typing.Any,
    ) -> MarketGetAlbumByIdResponseModel:
        """Method `market.getAlbumById()`

        :param album_ids: collections identifiers to obtain data from
        :param owner_id: identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.ru/apiclub|VK API] community "
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getAlbumById", params)
        model = MarketGetAlbumByIdResponse
        return model(**response).response

    async def get_albums(
        self,
        owner_id: int,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetAlbumsResponseModel:
        """Method `market.getAlbums()`

        :param owner_id: ID of an items owner community.
        :param count: Number of items to return.
        :param offset: Offset needed to return a specific subset of results.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getAlbums", params)
        model = MarketGetAlbumsResponse
        return model(**response).response

    @typing.overload
    async def get_by_id(
        self,
        item_ids: typing.List[str],
        extended: typing.Literal[True],
        **kwargs: typing.Any,
    ) -> MarketGetByIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_id(
        self,
        item_ids: typing.List[str],
        extended: typing.Optional[typing.Literal[False]] = None,
        **kwargs: typing.Any,
    ) -> MarketGetByIdResponseModel: ...

    async def get_by_id(
        self,
        item_ids: typing.List[str],
        extended: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MarketGetByIdExtendedResponseModel, MarketGetByIdResponseModel]:
        """Method `market.getById()`

        :param item_ids: Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: '1' - to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getById", params)
        model = self.get_model(
            ((("extended",), MarketGetByIdExtendedResponse),),
            default=MarketGetByIdResponse,
            params=params,
        )
        return model(**response).response

    async def get_categories(
        self,
        album_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetCategoriesNewResponseModel:
        """Method `market.getCategories()`

        :param album_id:
        :param group_id: Group Id.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getCategories", params)
        model = MarketGetCategoriesNewResponse
        return model(**response).response

    async def get_comments(
        self,
        item_id: int,
        owner_id: int,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetCommentsResponseModel:
        """Method `market.getComments()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community
        :param count: Number of results to return.
        :param extended: '1' - comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
        :param fields: List of additional profile fields to return. See the [vk.ru/dev/fields|details]
        :param need_likes: '1' - to return likes info.
        :param offset:
        :param sort: Sort order ('asc' - from old to new, 'desc' - from new to old)
        :param start_comment_id: ID of a comment to start a list from (details below).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getComments", params)
        model = MarketGetCommentsResponse
        return model(**response).response

    async def get_faves_for_attach(
        self,
        count: typing.Optional[int] = None,
        current_group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        public_only: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> MarketGetFavesForAttachResponseModel:
        """Method `market.getFavesForAttach()`

        :param count: Number of users to return.
        :param current_group_id: Group which represents content
        :param offset: Offset needed to return a specific subset of users.
        :param public_only:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getFavesForAttach", params)
        model = MarketGetFavesForAttachResponse
        return model(**response).response

    async def get_group_orders(
        self,
        count: typing.Optional[int] = None,
        group_id: typing.Optional[typing.Union["int", "str"]] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetGroupOrdersResponseModel:
        """Method `market.getGroupOrders()`

        :param count:
        :param group_id: ID or groups domain
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getGroupOrders", params)
        model = MarketGetGroupOrdersResponse
        return model(**response).response

    async def get_order_by_id(
        self,
        order_id: int,
        extended: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetOrderByIdResponseModel:
        """Method `market.getOrderById()`

        :param order_id:
        :param extended:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getOrderById", params)
        model = MarketGetOrderByIdResponse
        return model(**response).response

    async def get_order_items(
        self,
        order_id: int,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetOrderItemsResponseModel:
        """Method `market.getOrderItems()`

        :param order_id:
        :param count:
        :param offset:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getOrderItems", params)
        model = MarketGetOrderItemsResponse
        return model(**response).response

    @typing.overload
    async def get_orders(
        self,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetOrdersExtendedResponseModel: ...

    @typing.overload
    async def get_orders(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGetOrdersResponseModel: ...

    async def get_orders(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MarketGetOrdersResponseModel, MarketGetOrdersExtendedResponseModel]:
        """Method `market.getOrders()`

        :param extended:
        :param count:
        :param date_from: Orders status updated date from (format: yyyy-mm-dd)
        :param date_to: Orders status updated date to (format: yyyy-mm-dd)
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getOrders", params)
        model = self.get_model(
            ((("extended",), MarketGetOrdersExtendedResponse),),
            default=MarketGetOrdersResponse,
            params=params,
        )
        return model(**response).response

    async def get_product_photo_upload_server(
        self,
        group_id: int,
        bulk: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `market.getProductPhotoUploadServer()`

        :param group_id: Community ID.
        :param bulk:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getProductPhotoUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def get_properties(
        self,
        group_id: int,
        **kwargs: typing.Any,
    ) -> MarketGetPropertiesResponseModel:
        """Method `market.getProperties()`

        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.getProperties", params)
        model = MarketGetPropertiesResponse
        return model(**response).response

    async def group_items(
        self,
        group_id: int,
        item_ids: typing.List[int],
        item_group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketGroupItemsResponseModel:
        """Method `market.groupItems()`

        :param group_id: Group id.
        :param item_ids: Item ids.
        :param item_group_id: Items group id.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.groupItems", params)
        model = MarketGroupItemsResponse
        return model(**response).response

    async def remove_from_album(
        self,
        album_ids: typing.List[int],
        item_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.removeFromAlbum()`

        :param album_ids: Collections IDs to remove item from.
        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.removeFromAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def reorder_albums(
        self,
        album_id: int,
        owner_id: int,
        after: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.reorderAlbums()`

        :param album_id: Collection ID.
        :param owner_id: ID of an item owner community.
        :param after: ID of a collection to place current collection after it.
        :param before: ID of a collection to place current collection before it.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.reorderAlbums", params)
        model = BaseOkResponse
        return model(**response).response

    async def reorder_items(
        self,
        item_id: int,
        owner_id: int,
        after: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.reorderItems()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param after: ID of an item to place current item after it.
        :param album_id: ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param before: ID of an item to place current item before it.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.reorderItems", params)
        model = BaseOkResponse
        return model(**response).response

    async def report(
        self,
        item_id: int,
        owner_id: int,
        reason: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.report()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param reason: Complaint reason. Possible values: *'0' - spam,, *'1' - child porn,, *'2' - extremism,, *'3' - violence,, *'4' - drugs propaganda,, *'5' - adult materials,, *'6' - insult.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.report", params)
        model = BaseOkResponse
        return model(**response).response

    async def report_comment(
        self,
        comment_id: int,
        owner_id: int,
        reason: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.reportComment()`

        :param comment_id: Comment ID.
        :param owner_id: ID of an item owner community.
        :param reason: Complaint reason. Possible values: *'0' - spam,, *'1' - child porn,, *'2' - extremism,, *'3' - violence,, *'4' - drugs propaganda,, *'5' - adult materials,, *'6' - insult.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.reportComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore(
        self,
        item_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.restore()`

        :param item_id: Deleted item ID.
        :param owner_id: ID of an item owner community.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.restore", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `market.restoreComment()`

        :param comment_id: deleted comment id
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.ru/apiclub|VK API] community "
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.restoreComment", params)
        model = BaseBoolResponse
        return model(**response).response

    async def save_product_photo(
        self,
        upload_response: str,
        **kwargs: typing.Any,
    ) -> MarketPhotoIdResponseModel:
        """Method `market.saveProductPhoto()`

        :param upload_response: Upload response
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.saveProductPhoto", params)
        model = MarketPhotoIdResponse
        return model(**response).response

    async def save_product_photo_bulk(
        self,
        upload_response: str,
        **kwargs: typing.Any,
    ) -> typing.List[MarketUploadPhotoData]:
        """Method `market.saveProductPhotoBulk()`

        :param upload_response: Upload response
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.saveProductPhotoBulk", params)
        model = MarketPhotoIdBulkResponse
        return model(**response).response

    @typing.overload
    async def search(
        self,
        owner_id: int,
        extended: typing.Literal[True],
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        need_variants: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        rev: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        status: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> MarketSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        owner_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        need_variants: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        rev: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        status: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> MarketSearchResponseModel: ...

    async def search(
        self,
        owner_id: int,
        extended: typing.Optional[bool] = None,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        need_variants: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        rev: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        status: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MarketSearchResponseModel, MarketSearchExtendedResponseModel]:
        """Method `market.search()`

        :param owner_id: ID of an items owner community.
        :param extended: '1' - to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param album_id:
        :param count: Number of items to return.
        :param need_variants: Add variants to response if exist
        :param offset: Offset needed to return a specific subset of results.
        :param price_from: Minimum item price value.
        :param price_to: Maximum item price value.
        :param q: Search query, for example "pink slippers".
        :param rev: '0' - do not use reverse order, '1' - use reverse order
        :param sort:
        :param status:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.search", params)
        model = self.get_model(
            ((("extended",), MarketSearchExtendedResponse),),
            default=MarketSearchResponse,
            params=params,
        )
        return model(**response).response

    async def search_items(
        self,
        q: str,
        category_id: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        country: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        sort_by: typing.Optional[int] = None,
        sort_direction: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketSearchResponseModel:
        """Method `market.searchItems()`

        :param q:
        :param category_id:
        :param city:
        :param count:
        :param country:
        :param offset:
        :param price_from:
        :param price_to:
        :param sort_by:
        :param sort_direction:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.searchItems", params)
        model = MarketSearchResponse
        return model(**response).response

    async def search_items_basic(
        self,
        q: str,
        category_id: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        country: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        only_my_groups: typing.Optional[bool] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        sort_by: typing.Optional[int] = None,
        sort_direction: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MarketSearchBasicResponseModel:
        """Method `market.searchItemsBasic()`

        :param q:
        :param category_id:
        :param city:
        :param count:
        :param country:
        :param offset:
        :param only_my_groups:
        :param price_from:
        :param price_to:
        :param sort_by:
        :param sort_direction:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.searchItemsBasic", params)
        model = MarketSearchBasicResponse
        return model(**response).response

    async def ungroup_items(
        self,
        group_id: int,
        item_group_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `market.ungroupItems()`

        :param group_id: Group id.
        :param item_group_id: Items group id.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("market.ungroupItems", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("MarketCategory",)
