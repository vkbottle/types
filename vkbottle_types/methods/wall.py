import typing
from .base_category import BaseCategory
from vkbottle_types.responses import base, wall


class WallCategory(BaseCategory):
    async def check_copyright_link(
        self, link: str, **kwargs
    ) -> base.BoolResponseModel:
        """wall.checkCopyrightLink method
        :param link:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.checkCopyrightLink", params)
        model = base.BoolResponse
        return model(**response).response

    async def close_comments(
        self, owner_id: int, post_id: int, **kwargs
    ) -> base.BoolResponseModel:
        """wall.closeComments method
        :param owner_id:
        :param post_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.closeComments", params)
        model = base.BoolResponse
        return model(**response).response

    async def create_comment(
        self,
        post_id: int,
        owner_id: typing.Optional[int] = None,
        from_group: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        reply_to_comment: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        **kwargs
    ) -> wall.CreateCommentResponseModel:
        """Adds a comment to a post on a user wall or community wall.
        :param post_id: Post ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param from_group: Group ID.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param reply_to_comment: ID of comment to reply.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media ojbect: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. For example: "photo100172_166443618,photo66748_265827614"
        :param sticker_id: Sticker ID.
        :param guid: Unique identifier to avoid repeated comments.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.createComment", params)
        model = wall.CreateCommentResponse
        return model(**response).response

    async def delete(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Deletes a post from a user wall or community wall.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be deleted.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.delete", params)
        model = base.OkResponse
        return model(**response).response

    async def delete_comment(
        self, comment_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a comment on a post on a user wall or community wall.
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.deleteComment", params)
        model = base.OkResponse
        return model(**response).response

    async def edit(
        self,
        post_id: int,
        owner_id: typing.Optional[int] = None,
        friends_only: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        services: typing.Optional[str] = None,
        signed: typing.Optional[bool] = None,
        publish_date: typing.Optional[int] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        mark_as_ads: typing.Optional[bool] = None,
        close_comments: typing.Optional[bool] = None,
        donut_paid_duration: typing.Optional[int] = None,
        poster_bkg_id: typing.Optional[int] = None,
        poster_bkg_owner_id: typing.Optional[int] = None,
        poster_bkg_access_hash: typing.Optional[str] = None,
        copyright: typing.Optional[str] = None,
        **kwargs
    ) -> wall.EditResponseModel:
        """Edits a post on a user wall or community wall.
        :param post_id:
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param friends_only:
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error is thrown."
        :param services:
        :param signed:
        :param publish_date:
        :param lat:
        :param long:
        :param place_id:
        :param mark_as_ads:
        :param close_comments:
        :param donut_paid_duration:
        :param poster_bkg_id:
        :param poster_bkg_owner_id:
        :param poster_bkg_access_hash:
        :param copyright:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.edit", params)
        model = wall.EditResponse
        return model(**response).response

    async def edit_ads_stealth(
        self,
        post_id: int,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        signed: typing.Optional[bool] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        link_button: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Allows to edit hidden post.
        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param link_button: Link button ID
        :param link_title: Link title
        :param link_image: Link image url
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.editAdsStealth", params)
        model = base.OkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits a comment on a user wall or community wall.
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: , "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. For example: "photo100172_166443618,photo66748_265827614"
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.editComment", params)
        model = base.OkResponse
        return model(**response).response

    async def get(
        self,
        owner_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> wall.GetResponseModel:
        """Returns a list of posts on a user wall or community wall.
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param domain: User or community short address.
        :param offset: Offset needed to return a specific subset of posts.
        :param count: Number of posts to return (maximum 100).
        :param filter:
        :param extended: '1' — to return 'wall', 'profiles', and 'groups' fields, '0' — to return no additional fields (default)
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.get", params)
        model = self.get_model(
            {("extended",): wall.GetExtendedResponse},
            default=wall.GetResponse,
            params=params,
        )
        return model(**response).response

    async def get_by_id(
        self,
        posts: typing.List[str],
        extended: typing.Optional[bool] = None,
        copy_history_depth: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> wall.GetByIdLegacyResponseModel:
        """Returns a list of posts from user or community walls by their IDs.
        :param posts: User or community IDs and post IDs, separated by underscores. Use a negative value to designate a community ID. Example: "93388_21539,93388_20904,2943_4276,-1_1"
        :param extended: '1' — to return user and community objects needed to display posts, '0' — no additional fields are returned (default)
        :param copy_history_depth: Sets the number of parent elements to include in the array 'copy_history' that is returned if the post is a repost from another wall.
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getById", params)
        model = self.get_model(
            {("extended",): wall.GetByIdExtendedResponse},
            default=wall.GetByIdLegacyResponse,
            params=params,
        )
        return model(**response).response

    async def get_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> wall.GetCommentResponseModel:
        """Returns a comment on a post on a user wall or community wall.
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param extended:
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getComment", params)
        model = self.get_model(
            {("extended",): wall.GetCommentExtendedResponse},
            default=wall.GetCommentResponse,
            params=params,
        )
        return model(**response).response

    async def get_comments(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        preview_length: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
        **kwargs
    ) -> wall.GetCommentsResponseModel:
        """Returns a list of comments on a post on a user wall or community wall.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param need_likes: '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id:
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return (maximum 100).
        :param sort: Sort order: 'asc' — chronological, 'desc' — reverse chronological
        :param preview_length: Number of characters at which to truncate comments when previewed. By default, '90'. Specify '0' if you do not want to truncate comments.
        :param extended:
        :param fields:
        :param comment_id: Comment ID.
        :param thread_items_count: Count items in threads.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getComments", params)
        model = self.get_model(
            {("extended",): wall.GetCommentsExtendedResponse},
            default=wall.GetCommentsResponse,
            params=params,
        )
        return model(**response).response

    async def get_reposts(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> wall.GetRepostsResponseModel:
        """Returns information about reposts of a post on user wall or community wall.
        :param owner_id: User ID or community ID. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param offset: Offset needed to return a specific subset of reposts.
        :param count: Number of reposts to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getReposts", params)
        model = wall.GetRepostsResponse
        return model(**response).response

    async def open_comments(
        self, owner_id: int, post_id: int, **kwargs
    ) -> base.BoolResponseModel:
        """wall.openComments method
        :param owner_id:
        :param post_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.openComments", params)
        model = base.BoolResponse
        return model(**response).response

    async def pin(
        self, post_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Pins the post on wall.
        :param post_id: Post ID.
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.pin", params)
        model = base.OkResponse
        return model(**response).response

    async def post(
        self,
        owner_id: typing.Optional[int] = None,
        friends_only: typing.Optional[bool] = None,
        from_group: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        services: typing.Optional[str] = None,
        signed: typing.Optional[bool] = None,
        publish_date: typing.Optional[int] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        mark_as_ads: typing.Optional[bool] = None,
        close_comments: typing.Optional[bool] = None,
        donut_paid_duration: typing.Optional[int] = None,
        mute_notifications: typing.Optional[bool] = None,
        copyright: typing.Optional[str] = None,
        **kwargs
    ) -> wall.PostResponseModel:
        """Adds a new post on a user wall or community wall. Can also be used to publish suggested or scheduled posts.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param friends_only: '1' — post will be available to friends only, '0' — post will be available to all users (default)
        :param from_group: For a community: '1' — post will be published by the community, '0' — post will be published by the user (default)
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param services: List of services or websites the update will be exported to, if the user has so requested. Sample values: 'twitter', 'facebook'.
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param publish_date: Publication date (in Unix time). If used, posting will be delayed until the set time.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param guid:
        :param mark_as_ads:
        :param close_comments:
        :param donut_paid_duration:
        :param mute_notifications:
        :param copyright:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.post", params)
        model = wall.PostResponse
        return model(**response).response

    async def post_ads_stealth(
        self,
        owner_id: int,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        signed: typing.Optional[bool] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        link_button: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
        **kwargs
    ) -> wall.PostAdsStealthResponseModel:
        """Allows to create hidden post which will not be shown on the community's wall and can be used for creating an ad with type "Community post".
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param guid: Unique identifier to avoid duplication the same post.
        :param link_button: Link button ID
        :param link_title: Link title
        :param link_image: Link image url
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.postAdsStealth", params)
        model = wall.PostAdsStealthResponse
        return model(**response).response

    async def report_comment(
        self,
        owner_id: int,
        comment_id: int,
        reason: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Reports (submits a complaint about) a comment on a post on a user wall or community wall.
        :param owner_id: ID of the user or community that owns the wall.
        :param comment_id: Comment ID.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.reportComment", params)
        model = base.OkResponse
        return model(**response).response

    async def report_post(
        self,
        owner_id: int,
        post_id: int,
        reason: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Reports (submits a complaint about) a post on a user wall or community wall.
        :param owner_id: ID of the user or community that owns the wall.
        :param post_id: Post ID.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.reportPost", params)
        model = base.OkResponse
        return model(**response).response

    async def repost(
        self,
        object: str,
        message: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        mark_as_ads: typing.Optional[bool] = None,
        mute_notifications: typing.Optional[bool] = None,
        **kwargs
    ) -> wall.RepostResponseModel:
        """Reposts (copies) an object to a user wall or community wall.
        :param object: ID of the object to be reposted on the wall. Example: "wall66748_3675"
        :param message: Comment to be added along with the reposted object.
        :param group_id: Target community ID when reposting to a community.
        :param mark_as_ads:
        :param mute_notifications:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.repost", params)
        model = wall.RepostResponse
        return model(**response).response

    async def restore(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Restores a post deleted from a user wall or community wall.
        :param owner_id: User ID or community ID from whose wall the post was deleted. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be restored.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.restore", params)
        model = base.OkResponse
        return model(**response).response

    async def restore_comment(
        self, comment_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Restores a comment deleted from a user wall or community wall.
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.restoreComment", params)
        model = base.OkResponse
        return model(**response).response

    async def search(
        self,
        owner_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        owners_only: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> wall.SearchResponseModel:
        """Allows to search posts on user or community walls.
        :param owner_id: user or community id. "Remember that for a community 'owner_id' must be negative."
        :param domain: user or community screen name.
        :param query: search query string.
        :param owners_only: '1' - returns only page owner's posts.
        :param count: count of posts to return.
        :param offset: Offset needed to return a specific subset of posts.
        :param extended: show extended post info.
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.search", params)
        model = self.get_model(
            {("extended",): wall.SearchExtendedResponse},
            default=wall.SearchResponse,
            params=params,
        )
        return model(**response).response

    async def unpin(
        self, post_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Unpins the post on wall.
        :param post_id: Post ID.
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.unpin", params)
        model = base.OkResponse
        return model(**response).response
