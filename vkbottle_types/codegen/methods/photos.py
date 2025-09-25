import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUploadServer, PhotosPhoto, PhotosPhotoAlbumFull, PhotosPhotoTag, PhotosPhotoUpload, UsersFields
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseGetUploadServerResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.photos import *  # noqa: F401,F403  # type: ignore


class PhotosCategory(BaseCategory):
    async def confirm_tag(
        self,
        photo_id: str,
        tag_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.confirmTag()`

        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.confirmTag", params)
        model = BaseOkResponse
        return model(**response).response

    async def copy(
        self,
        owner_id: int,
        photo_id: int,
        access_key: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `photos.copy()`

        :param owner_id: photo's owner ID
        :param photo_id: photo ID
        :param access_key: for private photos
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.copy", params)
        model = PhotosCopyResponse
        return model(**response).response

    async def create_album(
        self,
        title: str,
        comments_disabled: typing.Optional[bool] = None,
        description: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        upload_by_admins_only: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> "PhotosPhotoAlbumFull":
        """Method `photos.createAlbum()`

        :param title: Album title.
        :param comments_disabled:
        :param description: Album description.
        :param group_id: ID of the community in which the album will be created.
        :param privacy_comment:
        :param privacy_view:
        :param upload_by_admins_only:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.createAlbum", params)
        model = PhotosCreateAlbumResponse
        return model(**response).response

    async def create_comment(
        self,
        photo_id: int,
        access_key: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        guid: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `photos.createComment()`

        :param photo_id: Photo ID.
        :param access_key:
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - Media attachment owner ID. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' - to post a comment from the community
        :param guid:
        :param message: Comment text.
        :param owner_id: ID of the user or community that owns the photo.
        :param reply_to_comment:
        :param sticker_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.createComment", params)
        model = PhotosCreateCommentResponse
        return model(**response).response

    async def delete(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        photos: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.delete()`

        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param photos:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.delete", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_album(
        self,
        album_id: int,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.deleteAlbum()`

        :param album_id: Album ID.
        :param group_id: ID of the community that owns the album.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.deleteAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `photos.deleteComment()`

        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.deleteComment", params)
        model = BaseBoolResponse
        return model(**response).response

    async def edit(
        self,
        photo_id: int,
        caption: typing.Optional[str] = None,
        delete_place: typing.Optional[bool] = None,
        foursquare_id: typing.Optional[str] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        owner_id: typing.Optional[int] = None,
        place_str: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.edit()`

        :param photo_id: Photo ID.
        :param caption: New caption for the photo. If this parameter is not set, it is considered to be equal to an empty string.
        :param delete_place:
        :param foursquare_id:
        :param latitude:
        :param longitude:
        :param owner_id: ID of the user or community that owns the photo.
        :param place_str:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.edit", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_album(
        self,
        album_id: int,
        comments_disabled: typing.Optional[bool] = None,
        description: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        title: typing.Optional[str] = None,
        upload_by_admins_only: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.editAlbum()`

        :param album_id: ID of the photo album to be edited.
        :param comments_disabled:
        :param description: New album description.
        :param owner_id: ID of the user or community that owns the album.
        :param privacy_comment:
        :param privacy_view:
        :param title: New album title.
        :param upload_by_admins_only:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.editAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        message: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.editComment()`

        :param comment_id: Comment ID.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - Media attachment owner ID. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param message: New text of the comment.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.editComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        album_id: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        feed: typing.Optional[int] = None,
        feed_type: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        photo_ids: typing.Optional[typing.List[str]] = None,
        photo_sizes: typing.Optional[bool] = None,
        rev: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetResponseModel:
        """Method `photos.get()`

        :param album_id: Photo album ID. To return information about photos from service albums, use the following string values: 'profile, wall, saved'.
        :param count:
        :param extended: '1' - to return additional 'likes', 'comments', and 'tags' fields, '0' - (default)
        :param feed: unixtime, that can be obtained with [vk.ru/dev/newsfeed.get|newsfeed.get] method in date field to get all photos uploaded by the user on a specific day, or photos the user has been tagged on. Also, 'uid' parameter of the user the event happened with shall be specified.
        :param feed_type: Type of feed obtained in 'feed' field of the method.
        :param offset:
        :param owner_id: ID of the user or community that owns the photos. Use a negative value to designate a community ID.
        :param photo_ids: Photo IDs.
        :param photo_sizes: '1' - to return photo sizes in a [vk.ru/dev/photo_sizes|special format]
        :param rev: Sort order: '1' - reverse chronological, '0' - chronological
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.get", params)
        model = PhotosGetResponse
        return model(**response).response

    async def get_albums(
        self,
        album_ids: typing.Optional[typing.List[int]] = None,
        count: typing.Optional[int] = None,
        need_covers: typing.Optional[bool] = None,
        need_system: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        photo_sizes: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetAlbumsResponseModel:
        """Method `photos.getAlbums()`

        :param album_ids: Album IDs.
        :param count: Number of albums to return.
        :param need_covers: '1' - to return an additional 'thumb_src' field, '0' - (default)
        :param need_system: '1' - to return system albums with negative IDs
        :param offset: Offset needed to return a specific subset of albums.
        :param owner_id: ID of the user or community that owns the albums.
        :param photo_sizes: '1' - to return photo sizes in a
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getAlbums", params)
        model = PhotosGetAlbumsResponse
        return model(**response).response

    async def get_albums_count(
        self,
        group_id: typing.Optional[int] = None,
        need_system: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `photos.getAlbumsCount()`

        :param group_id: Community ID.
        :param need_system:
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getAlbumsCount", params)
        model = PhotosGetAlbumsCountResponse
        return model(**response).response

    async def get_all(
        self,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        need_hidden: typing.Optional[bool] = None,
        no_service_albums: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        photo_sizes: typing.Optional[bool] = None,
        skip_hidden: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetAllResponseModel:
        """Method `photos.getAll()`

        :param count: Number of photos to return.
        :param extended: '1' - to return detailed information about photos
        :param need_hidden: '1' - to show information about photos being hidden from the block above the wall.
        :param no_service_albums: '1' - to return photos only from standard albums, '0' - to return all photos including those in service albums, e.g., 'My wall photos' (default)
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param owner_id: ID of a user or community that owns the photos. Use a negative value to designate a community ID.
        :param photo_sizes: '1' - to return image sizes in [vk.ru/dev/photo_sizes|special format].
        :param skip_hidden: '1' - not to return photos being hidden from the block above the wall. Works only with owner_id>0, no_service_albums is ignored.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getAll", params)
        model = PhotosGetAllResponse
        return model(**response).response

    async def get_all_comments(
        self,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetAllCommentsResponseModel:
        """Method `photos.getAllComments()`

        :param album_id: Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
        :param count: Number of comments to return. By default, '20'. Maximum value, '100'.
        :param need_likes: '1' - to return an additional 'likes' field, '0' - (default)
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param owner_id: ID of the user or community that owns the album(s).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getAllComments", params)
        model = PhotosGetAllCommentsResponse
        return model(**response).response

    async def get_by_id(
        self,
        photos: typing.List[str],
        extended: typing.Optional[bool] = None,
        photo_sizes: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[PhotosPhoto]:
        """Method `photos.getById()`

        :param photos: IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
        :param extended: '1' - to return additional fields, '0' - (default)
        :param photo_sizes: '1' - to return photo sizes in a
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getById", params)
        model = PhotosGetByIdResponse
        return model(**response).response

    async def get_chat_upload_server(
        self,
        chat_id: int,
        crop_width: typing.Optional[int] = None,
        crop_x: typing.Optional[int] = None,
        crop_y: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `photos.getChatUploadServer()`

        :param chat_id: ID of the chat for which you want to upload a cover photo.
        :param crop_width: Width (in pixels) of the photo after cropping.
        :param crop_x:
        :param crop_y:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getChatUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    @typing.overload
    async def get_comments(
        self,
        photo_id: int,
        extended: typing.Literal[True],
        access_key: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetCommentsExtendedResponseModel: ...

    @typing.overload
    async def get_comments(
        self,
        photo_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        access_key: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetCommentsResponseModel: ...

    async def get_comments(
        self,
        photo_id: int,
        extended: typing.Optional[bool] = None,
        access_key: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[PhotosGetCommentsResponseModel, PhotosGetCommentsExtendedResponseModel]:
        """Method `photos.getComments()`

        :param photo_id: Photo ID.
        :param extended:
        :param access_key:
        :param count: Number of comments to return.
        :param fields:
        :param need_likes: '1' - to return an additional 'likes' field, '0' - (default)
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param owner_id: ID of the user or community that owns the photo.
        :param sort: Sort order: 'asc' - old first, 'desc' - new first
        :param start_comment_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getComments", params)
        model = self.get_model(
            ((("extended",), PhotosGetCommentsExtendedResponse),),
            default=PhotosGetCommentsResponse,
            params=params,
        )
        return model(**response).response

    async def get_market_album_upload_server(
        self,
        group_id: int,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `photos.getMarketAlbumUploadServer()`

        :param group_id: Community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getMarketAlbumUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def get_messages_upload_server(
        self,
        peer_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "PhotosPhotoUpload":
        """Method `photos.getMessagesUploadServer()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getMessagesUploadServer", params)
        model = PhotosGetMessagesUploadServerResponse
        return model(**response).response

    async def get_new_tags(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetNewTagsResponseModel:
        """Method `photos.getNewTags()`

        :param count: Number of photos to return.
        :param offset: Offset needed to return a specific subset of photos.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getNewTags", params)
        model = PhotosGetNewTagsResponse
        return model(**response).response

    async def get_owner_cover_photo_upload_server(
        self,
        crop_x: typing.Optional[int] = None,
        crop_x2: typing.Optional[int] = None,
        crop_y: typing.Optional[int] = None,
        crop_y2: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        is_video_cover: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `photos.getOwnerCoverPhotoUploadServer()`

        :param crop_x: X coordinate of the left-upper corner
        :param crop_x2: X coordinate of the right-bottom corner
        :param crop_y: Y coordinate of the left-upper corner
        :param crop_y2: Y coordinate of the right-bottom corner
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param is_video_cover:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getOwnerCoverPhotoUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def get_owner_photo_upload_server(
        self,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `photos.getOwnerPhotoUploadServer()`

        :param owner_id: identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' - user, 'owner_id=-1' - community, "
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getOwnerPhotoUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def get_tags(
        self,
        photo_id: int,
        access_key: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[PhotosPhotoTag]:
        """Method `photos.getTags()`

        :param photo_id: Photo ID.
        :param access_key:
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getTags", params)
        model = PhotosGetTagsResponse
        return model(**response).response

    async def get_upload_server(
        self,
        album_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "PhotosPhotoUpload":
        """Method `photos.getUploadServer()`

        :param album_id:
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getUploadServer", params)
        model = PhotosGetUploadServerResponse
        return model(**response).response

    async def get_user_photos(
        self,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> PhotosGetUserPhotosResponseModel:
        """Method `photos.getUserPhotos()`

        :param count: Number of photos to return. Maximum value is 1000.
        :param extended: '1' - to return an additional 'likes' field, '0' - (default)
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param sort: Sort order: '1' - by date the tag was added in ascending order, '0' - by date the tag was added in descending order
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getUserPhotos", params)
        model = PhotosGetUserPhotosResponse
        return model(**response).response

    async def get_wall_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "PhotosPhotoUpload":
        """Method `photos.getWallUploadServer()`

        :param group_id: ID of community to whose wall the photo will be uploaded.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getWallUploadServer", params)
        model = PhotosGetWallUploadServerResponse
        return model(**response).response

    async def make_cover(
        self,
        photo_id: int,
        album_id: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.makeCover()`

        :param photo_id: Photo ID.
        :param album_id: Album ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.makeCover", params)
        model = BaseOkResponse
        return model(**response).response

    async def move(
        self,
        photo_ids: typing.List[int],
        target_album_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.move()`

        :param photo_ids:
        :param target_album_id: ID of the album to which the photo will be moved.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.move", params)
        model = BaseOkResponse
        return model(**response).response

    async def put_tag(
        self,
        photo_id: int,
        user_id: int,
        owner_id: typing.Optional[int] = None,
        x: typing.Optional[float] = None,
        x2: typing.Optional[float] = None,
        y: typing.Optional[float] = None,
        y2: typing.Optional[float] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `photos.putTag()`

        :param photo_id: Photo ID.
        :param user_id: ID of the user to be tagged.
        :param owner_id: ID of the user or community that owns the photo.
        :param x: Upper left-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param x2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y: Upper left-corner coordinate of the tagged area (as a percentage of the photo's height).
        :param y2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's height).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.putTag", params)
        model = PhotosPutTagResponse
        return model(**response).response

    async def remove_tag(
        self,
        photo_id: int,
        tag_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.removeTag()`

        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.removeTag", params)
        model = BaseOkResponse
        return model(**response).response

    async def reorder_albums(
        self,
        album_id: int,
        after: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.reorderAlbums()`

        :param album_id: Album ID.
        :param after: ID of the album after which the album in question shall be placed.
        :param before: ID of the album before which the album in question shall be placed.
        :param owner_id: ID of the user or community that owns the album.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.reorderAlbums", params)
        model = BaseOkResponse
        return model(**response).response

    async def reorder_photos(
        self,
        photo_id: int,
        after: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.reorderPhotos()`

        :param photo_id: Photo ID.
        :param after: ID of the photo after which the photo in question shall be placed.
        :param before: ID of the photo before which the photo in question shall be placed.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.reorderPhotos", params)
        model = BaseOkResponse
        return model(**response).response

    async def report(
        self,
        owner_id: int,
        photo_id: int,
        reason: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.report()`

        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse, '8' - suicide calls
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.report", params)
        model = BaseOkResponse
        return model(**response).response

    async def report_comment(
        self,
        comment_id: int,
        owner_id: int,
        reason: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.reportComment()`

        :param comment_id: ID of the comment being reported.
        :param owner_id: ID of the user or community that owns the photo.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.reportComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore(
        self,
        photo_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `photos.restore()`

        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.restore", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `photos.restoreComment()`

        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.restoreComment", params)
        model = BaseBoolResponse
        return model(**response).response

    async def save(
        self,
        album_id: typing.Optional[int] = None,
        caption: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        hash: typing.Optional[str] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        photos_list: typing.Optional[str] = None,
        server: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[PhotosPhoto]:
        """Method `photos.save()`

        :param album_id: ID of the album to save photos to.
        :param caption: Text describing the photo. 2048 digits max.
        :param group_id: ID of the community to save photos to.
        :param hash: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param photos_list: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.save", params)
        model = PhotosSaveResponse
        return model(**response).response

    async def save_market_album_photo(
        self,
        group_id: int,
        hash: str,
        photo: str,
        server: int,
        **kwargs: typing.Any,
    ) -> typing.List[PhotosPhoto]:
        """Method `photos.saveMarketAlbumPhoto()`

        :param group_id: Community ID.
        :param hash: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        :param photo: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.saveMarketAlbumPhoto", params)
        model = PhotosSaveMarketAlbumPhotoResponse
        return model(**response).response

    async def save_messages_photo(
        self,
        photo: str,
        hash: typing.Optional[str] = None,
        server: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[PhotosPhoto]:
        """Method `photos.saveMessagesPhoto()`

        :param photo: Parameter returned when the photo is [vk.ru/dev/upload_files|uploaded to the server].
        :param hash:
        :param server:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.saveMessagesPhoto", params)
        model = PhotosSaveMessagesPhotoResponse
        return model(**response).response

    async def save_owner_cover_photo(
        self,
        crop_height: typing.Optional[int] = None,
        crop_width: typing.Optional[int] = None,
        crop_x: typing.Optional[int] = None,
        crop_y: typing.Optional[int] = None,
        hash: typing.Optional[str] = None,
        is_video_cover: typing.Optional[bool] = None,
        photo: typing.Optional[str] = None,
        response_json: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> PhotosSaveOwnerCoverPhotoResponseModel:
        """Method `photos.saveOwnerCoverPhoto()`

        :param crop_height:
        :param crop_width:
        :param crop_x:
        :param crop_y:
        :param hash: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        :param is_video_cover:
        :param photo: Parameter returned when photos are [vk.ru/dev/upload_files|uploaded to server].
        :param response_json:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.saveOwnerCoverPhoto", params)
        model = PhotosSaveOwnerCoverPhotoResponse
        return model(**response).response

    async def save_owner_photo(
        self,
        hash: typing.Optional[str] = None,
        photo: typing.Optional[str] = None,
        server: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> PhotosSaveOwnerPhotoResponseModel:
        """Method `photos.saveOwnerPhoto()`

        :param hash: parameter returned after [vk.ru/dev/upload_files|photo upload].
        :param photo: parameter returned after [vk.ru/dev/upload_files|photo upload].
        :param server: parameter returned after [vk.ru/dev/upload_files|photo upload].
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.saveOwnerPhoto", params)
        model = PhotosSaveOwnerPhotoResponse
        return model(**response).response

    async def save_wall_photo(
        self,
        photo: str,
        caption: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        hash: typing.Optional[str] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        server: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[PhotosPhoto]:
        """Method `photos.saveWallPhoto()`

        :param photo: Parameter returned when the the photo is [vk.ru/dev/upload_files|uploaded to the server].
        :param caption: Text describing the photo. 2048 digits max.
        :param group_id: ID of community on whose wall the photo will be saved.
        :param hash:
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param server:
        :param user_id: ID of the user on whose wall the photo will be saved.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.saveWallPhoto", params)
        model = PhotosSaveWallPhotoResponse
        return model(**response).response

    async def search(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[float] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        start_time: typing.Optional[float] = None,
        **kwargs: typing.Any,
    ) -> PhotosSearchResponseModel:
        """Method `photos.search()`

        :param count: Number of photos to return.
        :param end_time:
        :param lat: Geographical latitude, in degrees (from '-90' to '90').
        :param long: Geographical longitude, in degrees (from '-180' to '180').
        :param offset: Offset needed to return a specific subset of photos.
        :param q: Search query string.
        :param radius: Radius of search in meters (works very approximately). Available values: '10', '100', '800', '6000', '50000'.
        :param sort: Sort order:
        :param start_time:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.search", params)
        model = PhotosSearchResponse
        return model(**response).response


__all__ = ("PhotosCategory",)
