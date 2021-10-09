import typing
from .base_category import BaseCategory
from vkbottle_types.responses import base, video


class VideoCategory(BaseCategory):
    async def add(
        self,
        video_id: int,
        owner_id: int,
        target_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Adds a video to a user or community page.
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video. Use a negative value to designate a community ID.
        :param target_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.add", params)
        model = base.OkResponse
        return model(**response).response

    async def add_album(
        self,
        group_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        privacy: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> video.AddAlbumResponseModel:
        """Creates an empty album for videos.
        :param group_id: Community ID (if the album will be created in a community).
        :param title: Album title.
        :param privacy: new access permissions for the album. Possible values: , *'0' - all users,, *'1' - friends only,, *'2' - friends and friends of friends,, *'3' - "only me".
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.addAlbum", params)
        model = video.AddAlbumResponse
        return model(**response).response

    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        **kwargs
    ) -> int:
        """video.addToAlbum method
        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.addToAlbum", params)
        model = base.OkResponse
        return model(**response).response

    async def create_comment(
        self,
        video_id: int,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        **kwargs
    ) -> int:
        """Adds a new comment on a video.
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' — to post the comment from a community name (only if 'owner_id'<0)
        :param reply_to_comment:
        :param sticker_id:
        :param guid:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.createComment", params)
        model = video.CreateCommentResponse
        return model(**response).response

    async def delete(
        self,
        video_id: int,
        owner_id: typing.Optional[int] = None,
        target_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Deletes a video from a user or community page.
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param target_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.delete", params)
        model = base.OkResponse
        return model(**response).response

    async def delete_album(
        self, album_id: int, group_id: typing.Optional[int] = None, **kwargs
    ) -> int:
        """Deletes a video album.
        :param album_id: Album ID.
        :param group_id: Community ID (if the album is owned by a community).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.deleteAlbum", params)
        model = base.OkResponse
        return model(**response).response

    async def delete_comment(
        self, comment_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> int:
        """Deletes a comment on a video.
        :param comment_id: ID of the comment to be deleted.
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.deleteComment", params)
        model = base.OkResponse
        return model(**response).response

    async def edit(
        self,
        video_id: int,
        owner_id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        desc: typing.Optional[str] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        no_comments: typing.Optional[bool] = None,
        repeat: typing.Optional[bool] = None,
        **kwargs
    ) -> int:
        """Edits information about a video on a user or community page.
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param name: New video title.
        :param desc: New video description.
        :param privacy_view: Privacy settings in a [vk.com/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
        :param privacy_comment: Privacy settings for comments in a [vk.com/dev/privacy_setting|special format].
        :param no_comments: Disable comments for the group video.
        :param repeat: '1' — to repeat the playback of the video, '0' — to play the video once,
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.edit", params)
        model = base.OkResponse
        return model(**response).response

    async def edit_album(
        self,
        album_id: int,
        title: str,
        group_id: typing.Optional[int] = None,
        privacy: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> int:
        """Edits the title of a video album.
        :param album_id: Album ID.
        :param title: New album title.
        :param group_id: Community ID (if the album edited is owned by a community).
        :param privacy: new access permissions for the album. Possible values: , *'0' - all users,, *'1' - friends only,, *'2' - friends and friends of friends,, *'3' - "only me".
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.editAlbum", params)
        model = base.OkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> int:
        """Edits the text of a comment on a video.
        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the video.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.editComment", params)
        model = base.OkResponse
        return model(**response).response

    async def get(
        self,
        owner_id: typing.Optional[int] = None,
        videos: typing.Optional[typing.List[str]] = None,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> video.GetResponseModel:
        """Returns detailed information about videos.
        :param owner_id: ID of the user or community that owns the video(s).
        :param videos: Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
        :param album_id: ID of the album containing the video(s).
        :param count: Number of videos to return.
        :param offset: Offset needed to return a specific subset of videos.
        :param extended: '1' — to return an extended response with additional fields
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.get", params)
        model = video.GetResponse
        return model(**response).response

    async def get_album_by_id(
        self, album_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> video.VideoVideoAlbumFull:
        """Returns video album info
        :param album_id: Album ID.
        :param owner_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getAlbumById", params)
        model = video.GetAlbumByIdResponse
        return model(**response).response

    async def get_albums(
        self,
        owner_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        need_system: typing.Optional[bool] = None,
        **kwargs
    ) -> video.GetAlbumsResponseModel:
        """Returns a list of video albums owned by a user or community.
        :param owner_id: ID of the user or community that owns the video album(s).
        :param offset: Offset needed to return a specific subset of video albums.
        :param count: Number of video albums to return.
        :param extended: '1' — to return additional information about album privacy settings for the current user
        :param need_system:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getAlbums", params)
        model = self.get_model(
            {("extended",): video.GetAlbumsExtendedResponse},
            default=video.GetAlbumsResponse,
            params=params,
        )
        return model(**response).response

    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        **kwargs
    ) -> typing.List[int]:
        """video.getAlbumsByVideo method
        :param owner_id:
        :param video_id:
        :param target_id:
        :param extended:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getAlbumsByVideo", params)
        model = self.get_model(
            {("extended",): video.GetAlbumsByVideoExtendedResponse},
            default=video.GetAlbumsByVideoResponse,
            params=params,
        )
        return model(**response).response

    async def get_comments(
        self,
        video_id: int,
        owner_id: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> video.GetCommentsResponseModel:
        """Returns a list of comments on a video.
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param need_likes: '1' — to return an additional 'likes' field
        :param start_comment_id:
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return.
        :param sort: Sort order: 'asc' — oldest comment first, 'desc' — newest comment first
        :param extended:
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.getComments", params)
        model = self.get_model(
            {("extended",): video.GetCommentsExtendedResponse},
            default=video.GetCommentsResponse,
            params=params,
        )
        return model(**response).response

    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        **kwargs
    ) -> int:
        """video.removeFromAlbum method
        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.removeFromAlbum", params)
        model = base.OkResponse
        return model(**response).response

    async def reorder_albums(
        self,
        album_id: int,
        owner_id: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Reorders the album in the list of user video albums.
        :param album_id: Album ID.
        :param owner_id: ID of the user or community that owns the albums..
        :param before: ID of the album before which the album in question shall be placed.
        :param after: ID of the album after which the album in question shall be placed.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.reorderAlbums", params)
        model = base.OkResponse
        return model(**response).response

    async def reorder_videos(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        before_owner_id: typing.Optional[int] = None,
        before_video_id: typing.Optional[int] = None,
        after_owner_id: typing.Optional[int] = None,
        after_video_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Reorders the video in the video album.
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: ID of the video.
        :param target_id: ID of the user or community that owns the album with videos.
        :param album_id: ID of the video album.
        :param before_owner_id: ID of the user or community that owns the video before which the video in question shall be placed.
        :param before_video_id: ID of the video before which the video in question shall be placed.
        :param after_owner_id: ID of the user or community that owns the video after which the photo in question shall be placed.
        :param after_video_id: ID of the video after which the photo in question shall be placed.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.reorderVideos", params)
        model = base.OkResponse
        return model(**response).response

    async def report(
        self,
        owner_id: int,
        video_id: int,
        reason: typing.Optional[int] = None,
        comment: typing.Optional[str] = None,
        search_query: typing.Optional[str] = None,
        **kwargs
    ) -> int:
        """Reports (submits a complaint about) a video.
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        :param comment: Comment describing the complaint.
        :param search_query: (If the video was found in search results.) Search query string.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.report", params)
        model = base.OkResponse
        return model(**response).response

    async def report_comment(
        self,
        owner_id: int,
        comment_id: int,
        reason: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Reports (submits a complaint about) a comment on a video.
        :param owner_id: ID of the user or community that owns the video.
        :param comment_id: ID of the comment being reported.
        :param reason: Reason for the complaint: , 0 - spam , 1 - child pornography , 2 - extremism , 3 - violence , 4 - drug propaganda , 5 - adult material , 6 - insult, abuse
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.reportComment", params)
        model = base.OkResponse
        return model(**response).response

    async def restore(
        self, video_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> int:
        """Restores a previously deleted video.
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.restore", params)
        model = base.OkResponse
        return model(**response).response

    async def restore_comment(
        self, comment_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> video.BaseBoolInt:
        """Restores a previously deleted comment on a video.
        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the video.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.restoreComment", params)
        model = video.RestoreCommentResponse
        return model(**response).response

    async def save(
        self,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        is_private: typing.Optional[bool] = None,
        wallpost: typing.Optional[bool] = None,
        link: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        no_comments: typing.Optional[bool] = None,
        repeat: typing.Optional[bool] = None,
        compression: typing.Optional[bool] = None,
        **kwargs
    ) -> video.VideoSaveResult:
        """Returns a server address (required for upload) and video data.
        :param name: Name of the video.
        :param description: Description of the video.
        :param is_private: '1' — to designate the video as private (send it via a private message), the video will not appear on the user's video list and will not be available by ID for other users, '0' — not to designate the video as private
        :param wallpost: '1' — to post the saved video on a user's wall, '0' — not to post the saved video on a user's wall
        :param link: URL for embedding the video from an external website.
        :param group_id: ID of the community in which the video will be saved. By default, the current user's page.
        :param album_id: ID of the album to which the saved video will be added.
        :param privacy_view:
        :param privacy_comment:
        :param no_comments:
        :param repeat: '1' — to repeat the playback of the video, '0' — to play the video once,
        :param compression:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.save", params)
        model = video.SaveResponse
        return model(**response).response

    async def search(
        self,
        q: str,
        sort: typing.Optional[int] = None,
        hd: typing.Optional[int] = None,
        adult: typing.Optional[bool] = None,
        live: typing.Optional[bool] = None,
        filters: typing.Optional[typing.List[str]] = None,
        search_own: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        longer: typing.Optional[int] = None,
        shorter: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        **kwargs
    ) -> video.SearchResponseModel:
        """Returns a list of videos under the set search criterion.
        :param q: Search query string (e.g., 'The Beatles').
        :param sort: Sort order: '1' — by duration, '2' — by relevance, '0' — by date added
        :param hd: If not null, only searches for high-definition videos.
        :param adult: '1' — to disable the Safe Search filter, '0' — to enable the Safe Search filter
        :param live:
        :param filters: Filters to apply: 'youtube' — return YouTube videos only, 'vimeo' — return Vimeo videos only, 'short' — return short videos only, 'long' — return long videos only
        :param search_own:
        :param offset: Offset needed to return a specific subset of videos.
        :param longer:
        :param shorter:
        :param count: Number of videos to return.
        :param extended:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("video.search", params)
        model = self.get_model(
            {("extended",): video.SearchExtendedResponse},
            default=video.SearchResponse,
            params=params,
        )
        return model(**response).response
