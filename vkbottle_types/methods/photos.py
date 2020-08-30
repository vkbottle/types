import typing
from typing import Optional, List

from vkbottle_types.responses import photos, base
from .base_category import BaseCategory

if typing.TYPE_CHECKING:
    from vkbottle_types.objects import users as objects_users


class PhotosCategory(BaseCategory):
    async def confirm_tag(
        self, photo_id: str, tag_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Confirms a tag on a photo.
        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.confirmTag", params)
        ).response

    async def copy(
        self, owner_id: int, photo_id: int, access_key: Optional[str] = None, **kwargs
    ) -> photos.CopyResponseModel:
        """Allows to copy a photo to the "Saved photos" album
        :param owner_id: photo's owner ID
        :param photo_id: photo ID
        :param access_key: for private photos
        """

        params = self.get_set_params(locals())
        return photos.CopyResponse(
            **await self.api.request("photos.copy", params)
        ).response

    async def create_album(
        self,
        title: str,
        group_id: Optional[int] = None,
        description: Optional[str] = None,
        privacy_view: Optional[List[str]] = None,
        privacy_comment: Optional[List[str]] = None,
        upload_by_admins_only: Optional[bool] = None,
        comments_disabled: Optional[bool] = None,
        **kwargs
    ) -> photos.CreateAlbumResponseModel:
        """Creates an empty photo album.
        :param title: Album title.
        :param group_id: ID of the community in which the album will be created.
        :param description: Album description.
        :param privacy_view:
        :param privacy_comment:
        :param upload_by_admins_only:
        :param comments_disabled:
        """

        params = self.get_set_params(locals())
        return photos.CreateAlbumResponse(
            **await self.api.request("photos.createAlbum", params)
        ).response

    async def create_comment(
        self,
        photo_id: int,
        owner_id: Optional[int] = None,
        message: Optional[str] = None,
        attachments: Optional[List[str]] = None,
        from_group: Optional[bool] = None,
        reply_to_comment: Optional[int] = None,
        sticker_id: Optional[int] = None,
        access_key: Optional[str] = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> photos.CreateCommentResponseModel:
        """Adds a new comment on the photo.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param message: Comment text.
        :param attachments: (Required if 'message' is not set., **kwargs) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' — to post a comment from the community
        :param reply_to_comment:
        :param sticker_id:
        :param access_key:
        :param guid:
        """

        params = self.get_set_params(locals())
        return photos.CreateCommentResponse(
            **await self.api.request("photos.createComment", params)
        ).response

    async def delete(
        self, photo_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a photo.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.delete", params)
        ).response

    async def delete_album(
        self, album_id: int, group_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a photo album belonging to the current user.
        :param album_id: Album ID.
        :param group_id: ID of the community that owns the album.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.deleteAlbum", params)
        ).response

    async def delete_comment(
        self, comment_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> photos.DeleteCommentResponseModel:
        """Deletes a comment on the photo.
        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        return photos.DeleteCommentResponse(
            **await self.api.request("photos.deleteComment", params)
        ).response

    async def edit(
        self,
        photo_id: int,
        owner_id: Optional[int] = None,
        caption: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        place_str: Optional[str] = None,
        foursquare_id: Optional[str] = None,
        delete_place: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits the caption of a photo.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param caption: New caption for the photo. If this parameter is not set, it is considered to be equal to an empty string.
        :param latitude:
        :param longitude:
        :param place_str:
        :param foursquare_id:
        :param delete_place:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("photos.edit", params)).response

    async def edit_album(
        self,
        album_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        owner_id: Optional[int] = None,
        privacy_view: Optional[List[str]] = None,
        privacy_comment: Optional[List[str]] = None,
        upload_by_admins_only: Optional[bool] = None,
        comments_disabled: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits information about a photo album.
        :param album_id: ID of the photo album to be edited.
        :param title: New album title.
        :param description: New album description.
        :param owner_id: ID of the user or community that owns the album.
        :param privacy_view:
        :param privacy_comment:
        :param upload_by_admins_only:
        :param comments_disabled:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.editAlbum", params)
        ).response

    async def edit_comment(
        self,
        comment_id: int,
        owner_id: Optional[int] = None,
        message: Optional[str] = None,
        attachments: Optional[List[str]] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits a comment on a photo.
        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param message: New text of the comment.
        :param attachments: (Required if 'message' is not set., **kwargs) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.editComment", params)
        ).response

    async def get(
        self,
        owner_id: Optional[int] = None,
        album_id: Optional[str] = None,
        photo_ids: Optional[List[str]] = None,
        rev: Optional[bool] = None,
        extended: Optional[bool] = None,
        feed_type: Optional[str] = None,
        feed: Optional[int] = None,
        photo_sizes: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> photos.GetExtendedResponseModel:
        """Returns a list of a user's or community's photos.
        :param owner_id: ID of the user or community that owns the photos. Use a negative value to designate a community ID.
        :param album_id: Photo album ID. To return information about photos from service albums, use the following string values: 'profile, wall, saved'.
        :param photo_ids: Photo IDs.
        :param rev: Sort order: '1' — reverse chronological, '0' — chronological
        :param extended: '1' — to return additional 'likes', 'comments', and 'tags' fields, '0' — (default)
        :param feed_type: Type of feed obtained in 'feed' field of the method.
        :param feed: unixtime, that can be obtained with [vk.com/dev/newsfeed.get|newsfeed.get] method in date field to get all photos uploaded by the user on a specific day, or photos the user has been tagged on. Also, 'uid' parameter of the user the event happened with shall be specified.
        :param photo_sizes: '1' — to return photo sizes in a [vk.com/dev/photo_sizes|special format]
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        return photos.GetExtendedResponse(
            **await self.api.request("photos.get", params)
        ).response

    async def get_albums(
        self,
        owner_id: Optional[int] = None,
        album_ids: Optional[List[int]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        need_system: Optional[bool] = None,
        need_covers: Optional[bool] = None,
        photo_sizes: Optional[bool] = None,
        **kwargs
    ) -> photos.GetAlbumsResponseModel:
        """Returns a list of a user's or community's photo albums.
        :param owner_id: ID of the user or community that owns the albums.
        :param album_ids: Album IDs.
        :param offset: Offset needed to return a specific subset of albums.
        :param count: Number of albums to return.
        :param need_system: '1' — to return system albums with negative IDs
        :param need_covers: '1' — to return an additional 'thumb_src' field, '0' — (default)
        :param photo_sizes: '1' — to return photo sizes in a
        """

        params = self.get_set_params(locals())
        return photos.GetAlbumsResponse(
            **await self.api.request("photos.getAlbums", params)
        ).response

    async def get_albums_count(
        self, user_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs
    ) -> photos.GetAlbumsCountResponseModel:
        """Returns the number of photo albums belonging to a user or community.
        :param user_id: User ID.
        :param group_id: Community ID.
        """

        params = self.get_set_params(locals())
        return photos.GetAlbumsCountResponse(
            **await self.api.request("photos.getAlbumsCount", params)
        ).response

    async def get_all(
        self,
        owner_id: Optional[int] = None,
        extended: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        photo_sizes: Optional[bool] = None,
        no_service_albums: Optional[bool] = None,
        need_hidden: Optional[bool] = None,
        skip_hidden: Optional[bool] = None,
        **kwargs
    ) -> photos.GetAllExtendedResponseModel:
        """Returns a list of photos belonging to a user or community, in reverse chronological order.
        :param owner_id: ID of a user or community that owns the photos. Use a negative value to designate a community ID.
        :param extended: '1' — to return detailed information about photos
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param count: Number of photos to return.
        :param photo_sizes: '1' – to return image sizes in [vk.com/dev/photo_sizes|special format].
        :param no_service_albums: '1' – to return photos only from standard albums, '0' – to return all photos including those in service albums, e.g., 'My wall photos' (default)
        :param need_hidden: '1' – to show information about photos being hidden from the block above the wall.
        :param skip_hidden: '1' – not to return photos being hidden from the block above the wall. Works only with owner_id>0, no_service_albums is ignored.
        """

        params = self.get_set_params(locals())
        return photos.GetAllExtendedResponse(
            **await self.api.request("photos.getAll", params)
        ).response

    async def get_all_comments(
        self,
        owner_id: Optional[int] = None,
        album_id: Optional[int] = None,
        need_likes: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> photos.GetAllCommentsResponseModel:
        """Returns a list of comments on a specific photo album or all albums of the user sorted in reverse chronological order.
        :param owner_id: ID of the user or community that owns the album(s).
        :param album_id: Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
        :param need_likes: '1' — to return an additional 'likes' field, '0' — (default)
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param count: Number of comments to return. By default, '20'. Maximum value, '100'.
        """

        params = self.get_set_params(locals())
        return photos.GetAllCommentsResponse(
            **await self.api.request("photos.getAllComments", params)
        ).response

    async def get_by_id(
        self,
        photos_: List[str],
        extended: Optional[bool] = None,
        photo_sizes: Optional[bool] = None,
        **kwargs
    ) -> photos.GetByIdExtendedResponseModel:
        """Returns information about photos by their IDs.
        :param photos_: IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
        :param extended: '1' — to return additional fields, '0' — (default)
        :param photo_sizes: '1' — to return photo sizes in a
        """

        params = self.get_set_params(locals())
        return photos.GetByIdExtendedResponse(
            **await self.api.request("photos.getById", params)
        ).response

    async def get_chat_upload_server(
        self,
        chat_id: int,
        crop_x: Optional[int] = None,
        crop_y: Optional[int] = None,
        crop_width: Optional[int] = None,
        **kwargs
    ) -> base.GetUploadServerResponseModel:
        """Returns an upload link for chat cover pictures.
        :param chat_id: ID of the chat for which you want to upload a cover photo.
        :param crop_x:
        :param crop_y:
        :param crop_width: Width (in pixels, **kwargs) of the photo after cropping.
        """

        params = self.get_set_params(locals())
        return base.GetUploadServerResponse(
            **await self.api.request("photos.getChatUploadServer", params)
        ).response

    async def get_comments(
        self,
        photo_id: int,
        owner_id: Optional[int] = None,
        need_likes: Optional[bool] = None,
        start_comment_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[str] = None,
        access_key: Optional[str] = None,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        **kwargs
    ) -> photos.GetCommentsExtendedResponseModel:
        """Returns a list of comments on a photo.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param need_likes: '1' — to return an additional 'likes' field, '0' — (default)
        :param start_comment_id:
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param count: Number of comments to return.
        :param sort: Sort order: 'asc' — old first, 'desc' — new first
        :param access_key:
        :param extended:
        :param fields:
        """

        params = self.get_set_params(locals())
        return photos.GetCommentsExtendedResponse(
            **await self.api.request("photos.getComments", params)
        ).response

    async def get_market_album_upload_server(
        self, group_id: int, **kwargs
    ) -> base.GetUploadServerResponseModel:
        """Returns the server address for market album photo upload.
        :param group_id: Community ID.
        """

        params = self.get_set_params(locals())
        return base.GetUploadServerResponse(
            **await self.api.request("photos.getMarketAlbumUploadServer", params)
        ).response

    async def get_market_upload_server(
        self,
        group_id: int,
        main_photo: Optional[bool] = None,
        crop_x: Optional[int] = None,
        crop_y: Optional[int] = None,
        crop_width: Optional[int] = None,
        **kwargs
    ) -> photos.GetMarketUploadServerResponseModel:
        """Returns the server address for market photo upload.
        :param group_id: Community ID.
        :param main_photo: '1' if you want to upload the main item photo.
        :param crop_x: X coordinate of the crop left upper corner.
        :param crop_y: Y coordinate of the crop left upper corner.
        :param crop_width: Width of the cropped photo in px.
        """

        params = self.get_set_params(locals())
        return photos.GetMarketUploadServerResponse(
            **await self.api.request("photos.getMarketUploadServer", params)
        ).response

    async def get_messages_upload_server(
        self, peer_id: Optional[int] = None, **kwargs
    ) -> photos.GetMessagesUploadServerResponseModel:
        """Returns the server address for photo upload in a private message for a user.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """

        params = self.get_set_params(locals())
        return photos.GetMessagesUploadServerResponse(
            **await self.api.request("photos.getMessagesUploadServer", params)
        ).response

    async def get_new_tags(
        self, offset: Optional[int] = None, count: Optional[int] = None, **kwargs
    ) -> photos.GetNewTagsResponseModel:
        """Returns a list of photos with tags that have not been viewed.
        :param offset: Offset needed to return a specific subset of photos.
        :param count: Number of photos to return.
        """

        params = self.get_set_params(locals())
        return photos.GetNewTagsResponse(
            **await self.api.request("photos.getNewTags", params)
        ).response

    async def get_owner_cover_photo_upload_server(
        self,
        group_id: int,
        crop_x: Optional[int] = None,
        crop_y: Optional[int] = None,
        crop_x2: Optional[int] = None,
        crop_y2: Optional[int] = None,
        **kwargs
    ) -> base.GetUploadServerResponseModel:
        """Returns the server address for owner cover upload.
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param crop_x: X coordinate of the left-upper corner
        :param crop_y: Y coordinate of the left-upper corner
        :param crop_x2: X coordinate of the right-bottom corner
        :param crop_y2: Y coordinate of the right-bottom corner
        """

        params = self.get_set_params(locals())
        return base.GetUploadServerResponse(
            **await self.api.request("photos.getOwnerCoverPhotoUploadServer", params)
        ).response

    async def get_owner_photo_upload_server(
        self, owner_id: Optional[int] = None, **kwargs
    ) -> base.GetUploadServerResponseModel:
        """Returns an upload server address for a profile or community photo.
        :param owner_id: identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' – user, 'owner_id=-1' – community, "
        """

        params = self.get_set_params(locals())
        return base.GetUploadServerResponse(
            **await self.api.request("photos.getOwnerPhotoUploadServer", params)
        ).response

    async def get_tags(
        self,
        photo_id: int,
        owner_id: Optional[int] = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> photos.GetTagsResponseModel:
        """Returns a list of tags on a photo.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param access_key:
        """

        params = self.get_set_params(locals())
        return photos.GetTagsResponse(
            **await self.api.request("photos.getTags", params)
        ).response

    async def get_upload_server(
        self, group_id: Optional[int] = None, album_id: Optional[int] = None, **kwargs
    ) -> photos.GetUploadServerResponseModel:
        """Returns the server address for photo upload.
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param album_id:
        """

        params = self.get_set_params(locals())
        return photos.GetUploadServerResponse(
            **await self.api.request("photos.getUploadServer", params)
        ).response

    async def get_user_photos(
        self,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        sort: Optional[str] = None,
        **kwargs
    ) -> photos.GetUserPhotosExtendedResponseModel:
        """Returns a list of photos in which a user is tagged.
        :param user_id: User ID.
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param count: Number of photos to return. Maximum value is 1000.
        :param extended: '1' — to return an additional 'likes' field, '0' — (default)
        :param sort: Sort order: '1' — by date the tag was added in ascending order, '0' — by date the tag was added in descending order
        """

        params = self.get_set_params(locals())
        return photos.GetUserPhotosExtendedResponse(
            **await self.api.request("photos.getUserPhotos", params)
        ).response

    async def get_wall_upload_server(
        self, group_id: Optional[int] = None, **kwargs
    ) -> photos.GetWallUploadServerResponseModel:
        """Returns the server address for photo upload onto a user's wall.
        :param group_id: ID of community to whose wall the photo will be uploaded.
        """

        params = self.get_set_params(locals())
        return photos.GetWallUploadServerResponse(
            **await self.api.request("photos.getWallUploadServer", params)
        ).response

    async def make_cover(
        self,
        photo_id: int,
        owner_id: Optional[int] = None,
        album_id: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Makes a photo into an album cover.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param album_id: Album ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.makeCover", params)
        ).response

    async def move(
        self,
        target_album_id: int,
        photo_id: int,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Moves a photo from one album to another.
        :param target_album_id: ID of the album to which the photo will be moved.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("photos.move", params)).response

    async def put_tag(
        self,
        photo_id: int,
        user_id: int,
        owner_id: Optional[int] = None,
        x: Optional[float] = None,
        y: Optional[float] = None,
        x2: Optional[float] = None,
        y2: Optional[float] = None,
        **kwargs
    ) -> photos.PutTagResponseModel:
        """Adds a tag on the photo.
        :param photo_id: Photo ID.
        :param user_id: ID of the user to be tagged.
        :param owner_id: ID of the user or community that owns the photo.
        :param x: Upper left-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y: Upper left-corner coordinate of the tagged area (as a percentage of the photo's height).
        :param x2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's height).
        """

        params = self.get_set_params(locals())
        return photos.PutTagResponse(
            **await self.api.request("photos.putTag", params)
        ).response

    async def remove_tag(
        self, photo_id: int, tag_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Removes a tag from a photo.
        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.removeTag", params)
        ).response

    async def reorder_albums(
        self,
        album_id: int,
        owner_id: Optional[int] = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Reorders the album in the list of user albums.
        :param album_id: Album ID.
        :param owner_id: ID of the user or community that owns the album.
        :param before: ID of the album before which the album in question shall be placed.
        :param after: ID of the album after which the album in question shall be placed.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.reorderAlbums", params)
        ).response

    async def reorder_photos(
        self,
        photo_id: int,
        owner_id: Optional[int] = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Reorders the photo in the list of photos of the user album.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param before: ID of the photo before which the photo in question shall be placed.
        :param after: ID of the photo after which the photo in question shall be placed.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.reorderPhotos", params)
        ).response

    async def report(
        self, owner_id: int, photo_id: int, reason: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Reports (submits a complaint about, **kwargs) a photo.
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.report", params)
        ).response

    async def report_comment(
        self, owner_id: int, comment_id: int, reason: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Reports (submits a complaint about, **kwargs) a comment on a photo.
        :param owner_id: ID of the user or community that owns the photo.
        :param comment_id: ID of the comment being reported.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.reportComment", params)
        ).response

    async def restore(
        self, photo_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Restores a deleted photo.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("photos.restore", params)
        ).response

    async def restore_comment(
        self, comment_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> photos.RestoreCommentResponseModel:
        """Restores a deleted comment on a photo.
        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the photo.
        """

        params = self.get_set_params(locals())
        return photos.RestoreCommentResponse(
            **await self.api.request("photos.restoreComment", params)
        ).response

    async def save(
        self,
        album_id: Optional[int] = None,
        group_id: Optional[int] = None,
        server: Optional[int] = None,
        photos_list: Optional[str] = None,
        hash: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        caption: Optional[str] = None,
        **kwargs
    ) -> photos.SaveResponseModel:
        """Saves photos after successful uploading.
        :param album_id: ID of the album to save photos to.
        :param group_id: ID of the community to save photos to.
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photos_list: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param caption: Text describing the photo. 2048 digits max.
        """

        params = self.get_set_params(locals())
        return photos.SaveResponse(
            **await self.api.request("photos.save", params)
        ).response

    async def save_market_album_photo(
        self, group_id: int, photo: str, server: int, hash: str, **kwargs
    ) -> photos.SaveMarketAlbumPhotoResponseModel:
        """Saves market album photos after successful uploading.
        :param group_id: Community ID.
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        params = self.get_set_params(locals())
        return photos.SaveMarketAlbumPhotoResponse(
            **await self.api.request("photos.saveMarketAlbumPhoto", params)
        ).response

    async def save_market_photo(
        self,
        photo: str,
        server: int,
        hash: str,
        group_id: Optional[int] = None,
        crop_data: Optional[str] = None,
        crop_hash: Optional[str] = None,
        **kwargs
    ) -> photos.SaveMarketPhotoResponseModel:
        """Saves market photos after successful uploading.
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param group_id: Community ID.
        :param crop_data: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param crop_hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        params = self.get_set_params(locals())
        return photos.SaveMarketPhotoResponse(
            **await self.api.request("photos.saveMarketPhoto", params)
        ).response

    async def save_messages_photo(
        self,
        photo: str,
        server: Optional[int] = None,
        hash: Optional[str] = None,
        **kwargs
    ) -> photos.SaveMessagesPhotoResponseModel:
        """Saves a photo after being successfully uploaded. URL obtained with [vk.com/dev/photos.getMessagesUploadServer|photos.getMessagesUploadServer] method.
        :param photo: Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server:
        :param hash:
        """

        params = self.get_set_params(locals())
        return photos.SaveMessagesPhotoResponse(
            **await self.api.request("photos.saveMessagesPhoto", params)
        ).response

    async def save_owner_cover_photo(
        self, hash: str, photo: str, **kwargs
    ) -> photos.SaveOwnerCoverPhotoResponseModel:
        """Saves cover photo after successful uploading.
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        params = self.get_set_params(locals())
        return photos.SaveOwnerCoverPhotoResponse(
            **await self.api.request("photos.saveOwnerCoverPhoto", params)
        ).response

    async def save_owner_photo(
        self,
        server: Optional[str] = None,
        hash: Optional[str] = None,
        photo: Optional[str] = None,
        **kwargs
    ) -> photos.SaveOwnerPhotoResponseModel:
        """Saves a profile or community photo. Upload URL can be got with the [vk.com/dev/photos.getOwnerPhotoUploadServer|photos.getOwnerPhotoUploadServer] method.
        :param server: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param hash: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param photo: parameter returned after [vk.com/dev/upload_files|photo upload].
        """

        params = self.get_set_params(locals())
        return photos.SaveOwnerPhotoResponse(
            **await self.api.request("photos.saveOwnerPhoto", params)
        ).response

    async def save_wall_photo(
        self,
        photo: str,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        server: Optional[int] = None,
        hash: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        caption: Optional[str] = None,
        **kwargs
    ) -> photos.SaveWallPhotoResponseModel:
        """Saves a photo to a user's or community's wall after being uploaded.
        :param photo: Parameter returned when the the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param user_id: ID of the user on whose wall the photo will be saved.
        :param group_id: ID of community on whose wall the photo will be saved.
        :param server:
        :param hash:
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param caption: Text describing the photo. 2048 digits max.
        """

        params = self.get_set_params(locals())
        return photos.SaveWallPhotoResponse(
            **await self.api.request("photos.saveWallPhoto", params)
        ).response

    async def search(
        self,
        q: Optional[str] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        radius: Optional[int] = None,
        **kwargs
    ) -> photos.SearchResponseModel:
        """Returns a list of photos.
        :param q: Search query string.
        :param lat: Geographical latitude, in degrees (from '-90' to '90').
        :param long: Geographical longitude, in degrees (from '-180' to '180').
        :param start_time:
        :param end_time:
        :param sort: Sort order:
        :param offset: Offset needed to return a specific subset of photos.
        :param count: Number of photos to return.
        :param radius: Radius of search in meters (works very approximately). Available values: '10', '100', '800', '6000', '50000'.
        """

        params = self.get_set_params(locals())
        return photos.SearchResponse(
            **await self.api.request("photos.search", params)
        ).response
