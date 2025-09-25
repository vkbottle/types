import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import VideoLiveCategory, VideoPlaylistPrivacyCategory, VideoSaveResult, VideoVideoAlbumFull
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.video import *  # noqa: F401,F403  # type: ignore


class VideoCategory(BaseCategory):
    async def add(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.add()`

        :param owner_id: ID of the user or community that owns the video. Use a negative value to designate a community ID.
        :param video_id: Video ID.
        :param target_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.add", params)
        model = BaseOkResponse
        return model(**response).response

    async def add_album(
        self,
        group_id: typing.Optional[int] = None,
        privacy: typing.Optional[typing.List[VideoPlaylistPrivacyCategory]] = None,
        title: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> VideoAddAlbumResponseModel:
        """Method `video.addAlbum()`

        :param group_id: Community ID (if the album will be created in a community).
        :param privacy: new access permissions for the album. Possible values: , *'0' - all users,, *'1' - friends only,, *'2' - friends and friends of friends,, *'3' - "only me".
        :param title: Album title.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.addAlbum", params)
        model = VideoAddAlbumResponse
        return model(**response).response

    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.addToAlbum()`

        :param owner_id:
        :param video_id:
        :param album_id:
        :param album_ids:
        :param target_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.addToAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def create_comment(
        self,
        video_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        guid: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        track_code: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `video.createComment()`

        :param video_id: Video ID.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media attachment owner. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' - to post the comment from a community name (only if 'owner_id'<0)
        :param guid:
        :param message: New comment text.
        :param owner_id: ID of the user or community that owns the video.
        :param reply_to_comment:
        :param sticker_id:
        :param track_code:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.createComment", params)
        model = VideoCreateCommentResponse
        return model(**response).response

    async def delete(
        self,
        video_id: int,
        owner_id: typing.Optional[int] = None,
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.delete()`

        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param target_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.delete", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_album(
        self,
        album_id: int,
        group_id: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.deleteAlbum()`

        :param album_id: Album ID.
        :param group_id: Community ID (if the album is owned by a community).
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.deleteAlbum", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.deleteComment()`

        :param comment_id: ID of the comment to be deleted.
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.deleteComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_thread(
        self,
        owner_id: int,
        thread_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.deleteThread()`

        :param owner_id: ID of the user or community that owns the video.
        :param thread_id: ID of the main comment to be deleted as thread.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.deleteThread", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit(
        self,
        video_id: int,
        desc: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        no_comments: typing.Optional[bool] = None,
        ord_info: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        repeat: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> VideoEditResponseModel:
        """Method `video.edit()`

        :param video_id: Video ID.
        :param desc: New video description.
        :param name: New video title.
        :param no_comments: Disable comments for the group video.
        :param ord_info:
        :param owner_id: ID of the user or community that owns the video.
        :param privacy_comment: Privacy settings for comments in a [vk.ru/dev/privacy_setting|special format].
        :param privacy_view: Privacy settings in a [vk.ru/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
        :param repeat: '1' - to repeat the playback of the video, '0' - to play the video once,
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.edit", params)
        model = VideoEditResponse
        return model(**response).response

    async def edit_album(
        self,
        album_id: int,
        group_id: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        privacy: typing.Optional[typing.List[VideoPlaylistPrivacyCategory]] = None,
        title: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.editAlbum()`

        :param album_id: Album ID.
        :param group_id: Community ID (if the album edited is owned by a community).
        :param owner_id:
        :param privacy: new access permissions for the album. Possible values: , *'0' - all users,, *'1' - friends only,, *'2' - friends and friends of friends,, *'3' - "only me".
        :param title: New album title.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.editAlbum", params)
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
        """Method `video.editComment()`

        :param comment_id: Comment ID.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media attachment owner. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param message: New comment text.
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.editComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort_album: typing.Optional[int] = None,
        videos: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> VideoGetResponseModel:
        """Method `video.get()`

        :param album_id: ID of the album containing the video(s).
        :param count: Number of videos to return.
        :param extended: '1' - to return an extended response with additional fields
        :param fields:
        :param offset: Offset needed to return a specific subset of videos.
        :param owner_id: ID of the user or community that owns the video(s).
        :param sort_album: Sort order: '0' - newest video first, '1' - oldest video first
        :param videos: Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.get", params)
        model = VideoGetResponse
        return model(**response).response

    async def get_album_by_id(
        self,
        album_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "VideoVideoAlbumFull":
        """Method `video.getAlbumById()`

        :param album_id: Album ID.
        :param owner_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getAlbumById", params)
        model = VideoGetAlbumByIdResponse
        return model(**response).response

    @typing.overload
    async def get_albums(
        self,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        need_system: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoGetAlbumsExtendedResponseModel: ...

    @typing.overload
    async def get_albums(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        need_system: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoGetAlbumsResponseModel: ...

    async def get_albums(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        need_system: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[VideoGetAlbumsExtendedResponseModel, VideoGetAlbumsResponseModel]:
        """Method `video.getAlbums()`

        :param extended: '1' - to return additional information about album privacy settings for the current user
        :param count: Number of video albums to return.
        :param need_system:
        :param offset: Offset needed to return a specific subset of video albums.
        :param owner_id: ID of the user or community that owns the video album(s).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getAlbums", params)
        model = self.get_model(
            ((("extended",), VideoGetAlbumsExtendedResponse),),
            default=VideoGetAlbumsResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        extended: typing.Literal[True],
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoGetAlbumsByVideoExtendedResponseModel: ...

    @typing.overload
    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[int]: ...

    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        extended: typing.Optional[bool] = None,
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[VideoGetAlbumsByVideoExtendedResponseModel, typing.List[int]]:
        """Method `video.getAlbumsByVideo()`

        :param owner_id:
        :param video_id:
        :param extended:
        :param target_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getAlbumsByVideo", params)
        model = self.get_model(
            ((("extended",), VideoGetAlbumsByVideoExtendedResponse),),
            default=VideoGetAlbumsByVideoResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_comments(
        self,
        video_id: int,
        extended: typing.Literal[True],
        comment_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoGetCommentsExtendedResponseModel: ...

    @typing.overload
    async def get_comments(
        self,
        video_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        comment_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoGetCommentsResponseModel: ...

    async def get_comments(
        self,
        video_id: int,
        extended: typing.Optional[bool] = None,
        comment_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[VideoGetCommentsExtendedResponseModel, VideoGetCommentsResponseModel]:
        """Method `video.getComments()`

        :param video_id: Video ID.
        :param extended:
        :param comment_id:
        :param count: Number of comments to return.
        :param fields:
        :param need_likes: '1' - to return an additional 'likes' field
        :param offset: Offset needed to return a specific subset of comments.
        :param owner_id: ID of the user or community that owns the video.
        :param sort: Sort order: 'asc' - oldest comment first, 'desc' - newest comment first
        :param start_comment_id:
        :param thread_items_count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getComments", params)
        model = self.get_model(
            ((("extended",), VideoGetCommentsExtendedResponse),),
            default=VideoGetCommentsResponse,
            params=params,
        )
        return model(**response).response

    async def get_long_poll_server(
        self,
        video_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoGetLongPollServerResponseModel:
        """Method `video.getLongPollServer()`

        :param video_id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getLongPollServer", params)
        model = VideoGetLongPollServerResponse
        return model(**response).response

    async def get_oembed(
        self,
        url: str,
        maxheight: typing.Optional[int] = None,
        maxwidth: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoGetOembedResponseModel:
        """Method `video.getOembed()`

        :param url: Link to video
        :param maxheight: Maximum width of player
        :param maxwidth: Maximum width of player
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getOembed", params)
        model = VideoGetOembedResponse
        return model(**response).response

    async def get_thumb_upload_url(
        self,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> VideoGetThumbUploadUrlResponseModel:
        """Method `video.getThumbUploadUrl()`

        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getThumbUploadUrl", params)
        model = VideoGetThumbUploadUrlResponse
        return model(**response).response

    async def live_get_categories(
        self,
        **kwargs: typing.Any,
    ) -> typing.List[VideoLiveCategory]:
        """Method `video.liveGetCategories()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("video.liveGetCategories", params)
        model = VideoLiveGetCategoriesResponse
        return model(**response).response

    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.removeFromAlbum()`

        :param owner_id:
        :param video_id:
        :param album_id:
        :param album_ids:
        :param target_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.removeFromAlbum", params)
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
        """Method `video.reorderAlbums()`

        :param album_id: Album ID.
        :param after: ID of the album after which the album in question shall be placed.
        :param before: ID of the album before which the album in question shall be placed.
        :param owner_id: ID of the user or community that owns the albums..
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.reorderAlbums", params)
        model = BaseOkResponse
        return model(**response).response

    async def reorder_videos(
        self,
        owner_id: int,
        video_id: int,
        after_owner_id: typing.Optional[int] = None,
        after_video_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        before_owner_id: typing.Optional[int] = None,
        before_video_id: typing.Optional[int] = None,
        target_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.reorderVideos()`

        :param owner_id: ID of the user or community that owns the video.
        :param video_id: ID of the video.
        :param after_owner_id: ID of the user or community that owns the video after which the photo in question shall be placed.
        :param after_video_id: ID of the video after which the photo in question shall be placed.
        :param album_id: ID of the video album.
        :param before_owner_id: ID of the user or community that owns the video before which the video in question shall be placed.
        :param before_video_id: ID of the video before which the video in question shall be placed.
        :param target_id: ID of the user or community that owns the album with videos.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.reorderVideos", params)
        model = BaseOkResponse
        return model(**response).response

    async def report(
        self,
        owner_id: int,
        video_id: int,
        comment: typing.Optional[str] = None,
        reason: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.report()`

        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param comment: Comment describing the complaint.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        :param search_query: (If the video was found in search results.) Search query string.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.report", params)
        model = BaseOkResponse
        return model(**response).response

    async def report_comment(
        self,
        comment_id: int,
        owner_id: int,
        reason: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.reportComment()`

        :param comment_id: ID of the comment being reported.
        :param owner_id: ID of the user or community that owns the video.
        :param reason: Reason for the complaint: , 0 - spam , 1 - child pornography , 2 - extremism , 3 - violence , 4 - drug propaganda , 5 - adult material , 6 - insult, abuse
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.reportComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore(
        self,
        video_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.restore()`

        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.restore", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `video.restoreComment()`

        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.restoreComment", params)
        model = BaseBoolResponse
        return model(**response).response

    async def restore_thread(
        self,
        owner_id: int,
        thread_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.restoreThread()`

        :param owner_id: ID of the user or community that owns the video.
        :param thread_id: ID of the main comment to be deleted as thread.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.restoreThread", params)
        model = BaseOkResponse
        return model(**response).response

    async def save(
        self,
        album_id: typing.Optional[int] = None,
        auto_publish: typing.Optional[bool] = None,
        compression: typing.Optional[bool] = None,
        description: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        is_private: typing.Optional[bool] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        no_comments: typing.Optional[bool] = None,
        ord_info: typing.Optional[str] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        repeat: typing.Optional[bool] = None,
        wallpost: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> "VideoSaveResult":
        """Method `video.save()`

        :param album_id: ID of the album to which the saved video will be added.
        :param auto_publish:
        :param compression:
        :param description: Description of the video.
        :param group_id: ID of the community in which the video will be saved. By default, the current user's page.
        :param is_private: '1' - to designate the video as private (send it via a private message), the video will not appear on the user's video list and will not be available by ID for other users, '0' - not to designate the video as private
        :param link: URL for embedding the video from an external website.
        :param name: Name of the video.
        :param no_comments:
        :param ord_info:
        :param privacy_comment:
        :param privacy_view:
        :param repeat: '1' - to repeat the playback of the video, '0' - to play the video once,
        :param wallpost: '1' - to post the saved video on a user's wall, '0' - not to post the saved video on a user's wall
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.save", params)
        model = VideoSaveResponse
        return model(**response).response

    async def save_uploaded_thumb(
        self,
        owner_id: int,
        thumb_json: str,
        random_tag: typing.Optional[str] = None,
        set_thumb: typing.Optional[bool] = None,
        thumb_size: typing.Optional[str] = None,
        video_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoSaveUploadedThumbResponseModel:
        """Method `video.saveUploadedThumb()`

        :param owner_id:
        :param thumb_json:
        :param random_tag:
        :param set_thumb: If flag passed uploaded thumb will automatically set to passed video. Work only with video_id.
        :param thumb_size:
        :param video_id: Video ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.saveUploadedThumb", params)
        model = VideoSaveUploadedThumbResponse
        return model(**response).response

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[True],
        adult: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        filters: typing.Optional[typing.List[typing.Literal["long", "short", "vimeo", "vk", "youtube"]]] = None,
        hd: typing.Optional[int] = None,
        live: typing.Optional[bool] = None,
        longer: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        search_own: typing.Optional[bool] = None,
        shorter: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        adult: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        filters: typing.Optional[typing.List[typing.Literal["long", "short", "vimeo", "vk", "youtube"]]] = None,
        hd: typing.Optional[int] = None,
        live: typing.Optional[bool] = None,
        longer: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        search_own: typing.Optional[bool] = None,
        shorter: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoSearchResponseModel: ...

    async def search(
        self,
        extended: typing.Optional[bool] = None,
        adult: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        filters: typing.Optional[typing.List[typing.Literal["long", "short", "vimeo", "vk", "youtube"]]] = None,
        hd: typing.Optional[int] = None,
        live: typing.Optional[bool] = None,
        longer: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        search_own: typing.Optional[bool] = None,
        shorter: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[VideoSearchExtendedResponseModel, VideoSearchResponseModel]:
        """Method `video.search()`

        :param extended:
        :param adult: '1' - to disable the Safe Search filter, '0' - to enable the Safe Search filter
        :param count: Number of videos to return.
        :param fields:
        :param filters: Filters to apply: 'youtube' - return YouTube videos only, 'vimeo' - return Vimeo videos only, 'vk' - return VK videos only, 'short' - return short videos only, 'long' - return long videos only
        :param hd: If not null, only searches for high-definition videos.
        :param live:
        :param longer:
        :param offset: Offset needed to return a specific subset of videos.
        :param owner_id:
        :param q: Search query string (e.g., 'The Beatles').
        :param search_own:
        :param shorter:
        :param sort: Sort order: '1' - by duration, '2' - by relevance, '0' - by date added
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.search", params)
        model = self.get_model(
            ((("extended",), VideoSearchExtendedResponse),),
            default=VideoSearchResponse,
            params=params,
        )
        return model(**response).response

    async def start_streaming(
        self,
        category_id: typing.Optional[int] = None,
        description: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        no_comments: typing.Optional[bool] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        publish: typing.Optional[bool] = None,
        video_id: typing.Optional[int] = None,
        wallpost: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> VideoStartStreamingResponseModel:
        """Method `video.startStreaming()`

        :param category_id:
        :param description:
        :param group_id:
        :param name:
        :param no_comments:
        :param privacy_comment:
        :param privacy_view:
        :param publish:
        :param video_id:
        :param wallpost:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.startStreaming", params)
        model = VideoStartStreamingResponse
        return model(**response).response

    async def stop_streaming(
        self,
        group_id: typing.Optional[int] = None,
        video_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> VideoStopStreamingResponseModel:
        """Method `video.stopStreaming()`

        :param group_id:
        :param video_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.stopStreaming", params)
        model = VideoStopStreamingResponse
        return model(**response).response

    async def unpin_comment(
        self,
        comment_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `video.unpinComment()`

        :param comment_id:
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.unpinComment", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("VideoCategory",)
