import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUserGroupFields
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.wall import *  # noqa: F401,F403  # type: ignore


class WallCategory(BaseCategory):
    async def check_copyright_link(
        self,
        link: str,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `wall.checkCopyrightLink()`

        :param link:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.checkCopyrightLink", params)
        model = BaseBoolResponse
        return model(**response).response

    async def close_comments(
        self,
        owner_id: int,
        post_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `wall.closeComments()`

        :param owner_id:
        :param post_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.closeComments", params)
        model = BaseBoolResponse
        return model(**response).response

    async def create_comment(
        self,
        post_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallCreateCommentResponseModel:
        """Method `wall.createComment()`

        :param post_id: Post ID.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media ojbect: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media owner. '<media_id>' - Media ID. For example: "photo100172_166443618,photo66748_265827614"
        :param from_group: Group ID.
        :param guid: Unique identifier to avoid repeated comments.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param reply_to_comment: ID of comment to reply.
        :param sticker_id: Sticker ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.createComment", params)
        model = WallCreateCommentResponse
        return model(**response).response

    async def delete(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.delete()`

        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be deleted.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.delete", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.deleteComment()`

        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.deleteComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit(
        self,
        post_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        close_comments: typing.Optional[bool] = None,
        copyright: typing.Optional[str] = None,
        donut_paid_duration: typing.Optional[int] = None,
        friends_only: typing.Optional[bool] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
        mark_as_ads: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        poster_bkg_access_hash: typing.Optional[str] = None,
        poster_bkg_id: typing.Optional[int] = None,
        poster_bkg_owner_id: typing.Optional[int] = None,
        publish_date: typing.Optional[int] = None,
        services: typing.Optional[str] = None,
        signed: typing.Optional[bool] = None,
        topic_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallEditResponseModel:
        """Method `wall.edit()`

        :param post_id:
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media application owner. '<media_id>' - Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error is thrown."
        :param close_comments:
        :param copyright:
        :param donut_paid_duration:
        :param friends_only:
        :param lat:
        :param long:
        :param mark_as_ads:
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param place_id:
        :param poster_bkg_access_hash:
        :param poster_bkg_id:
        :param poster_bkg_owner_id:
        :param publish_date:
        :param services:
        :param signed:
        :param topic_id: Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.edit", params)
        model = WallEditResponse
        return model(**response).response

    async def edit_ads_stealth(
        self,
        post_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        lat: typing.Optional[float] = None,
        link_button: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
        long: typing.Optional[float] = None,
        message: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        signed: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.editAdsStealth()`

        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'page' - wiki-page, 'note' - note, 'poll' - poll, 'album' - photo album, '<owner_id>' - ID of the media application owner. '<media_id>' - Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param link_button: Link button ID
        :param link_image: Link image url
        :param link_title: Link title
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param place_id: ID of the location where the user was tagged.
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' - post will be signed with the name of the posting user, '0' - post will not be signed (default)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.editAdsStealth", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        message: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.editComment()`

        :param comment_id: Comment ID.
        :param attachments: List of objects attached to the comment, in the following format: , "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media attachment owner. '<media_id>' - Media attachment ID. For example: "photo100172_166443618,photo66748_265827614"
        :param message: New comment text.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.editComment", params)
        model = BaseOkResponse
        return model(**response).response

    @typing.overload
    async def get(
        self,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        domain: typing.Optional[typing.Union["int", "str"]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filter: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallGetExtendedResponseModel: ...

    @typing.overload
    async def get(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        domain: typing.Optional[typing.Union["int", "str"]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filter: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallGetResponseModel: ...

    async def get(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        domain: typing.Optional[typing.Union["int", "str"]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filter: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[WallGetExtendedResponseModel, WallGetResponseModel]:
        """Method `wall.get()`

        :param extended: '1' - to return 'wall', 'profiles', and 'groups' fields, '0' - to return no additional fields (default)
        :param count: Number of posts to return (maximum 100).
        :param domain: User or community short address.
        :param fields:
        :param filter:
        :param offset: Offset needed to return a specific subset of posts.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.get", params)
        model = self.get_model(
            ((("extended",), WallGetExtendedResponse),),
            default=WallGetResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_by_id(
        self,
        posts: typing.List[str],
        extended: typing.Literal[True],
        copy_history_depth: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> WallGetByIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_id(
        self,
        posts: typing.List[str],
        extended: typing.Optional[typing.Literal[False]] = None,
        copy_history_depth: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> WallGetByIdResponseModel: ...

    async def get_by_id(
        self,
        posts: typing.List[str],
        extended: typing.Optional[bool] = None,
        copy_history_depth: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[WallGetByIdExtendedResponseModel, WallGetByIdResponseModel]:
        """Method `wall.getById()`

        :param posts: User or community IDs and post IDs, separated by underscores. Use a negative value to designate a community ID. Example: "93388_21539,93388_20904,2943_4276,-1_1"
        :param extended: '1' - to return user and community objects needed to display posts, '0' - no additional fields are returned (default)
        :param copy_history_depth: Sets the number of parent elements to include in the array 'copy_history' that is returned if the post is a repost from another wall.
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getById", params)
        model = self.get_model(
            ((("extended",), WallGetByIdExtendedResponse),),
            default=WallGetByIdResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_comment(
        self,
        comment_id: int,
        extended: typing.Literal[True],
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallGetCommentExtendedResponseModel: ...

    @typing.overload
    async def get_comment(
        self,
        comment_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallGetCommentResponseModel: ...

    async def get_comment(
        self,
        comment_id: int,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[WallGetCommentExtendedResponseModel, WallGetCommentResponseModel]:
        """Method `wall.getComment()`

        :param comment_id: Comment ID.
        :param extended:
        :param fields:
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getComment", params)
        model = self.get_model(
            ((("extended",), WallGetCommentExtendedResponse),),
            default=WallGetCommentResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_comments(
        self,
        extended: typing.Literal[True],
        comment_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallGetCommentsExtendedResponseModel: ...

    @typing.overload
    async def get_comments(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        comment_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallGetCommentsResponseModel: ...

    async def get_comments(
        self,
        extended: typing.Optional[bool] = None,
        comment_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[WallGetCommentsResponseModel, WallGetCommentsExtendedResponseModel]:
        """Method `wall.getComments()`

        :param extended:
        :param comment_id: Comment ID.
        :param count: Number of comments to return (maximum 100).
        :param fields:
        :param need_likes: '1' - to return the 'likes' field, '0' - not to return the 'likes' field (default)
        :param offset: Offset needed to return a specific subset of comments.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param preview_length: Number of characters at which to truncate comments when previewed. By default, '90'. Specify '0' if you do not want to truncate comments.
        :param sort: Sort order: 'asc' - chronological, 'desc' - reverse chronological
        :param start_comment_id:
        :param thread_items_count: Count items in threads.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getComments", params)
        model = self.get_model(
            ((("extended",), WallGetCommentsExtendedResponse),),
            default=WallGetCommentsResponse,
            params=params,
        )
        return model(**response).response

    async def get_reposts(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WallGetRepostsResponseModel:
        """Method `wall.getReposts()`

        :param count: Number of reposts to return.
        :param offset: Offset needed to return a specific subset of reposts.
        :param owner_id: User ID or community ID. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.getReposts", params)
        model = WallGetRepostsResponse
        return model(**response).response

    async def open_comments(
        self,
        owner_id: int,
        post_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `wall.openComments()`

        :param owner_id:
        :param post_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.openComments", params)
        model = BaseBoolResponse
        return model(**response).response

    async def parse_attached_link(
        self,
        links: str,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> WallParseAttachedLinkResponseModel:
        """Method `wall.parseAttachedLink()`

        :param links:
        :param extended:
        :param fields:
        :param name_case:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.parseAttachedLink", params)
        model = WallParseAttachedLinkResponse
        return model(**response).response

    async def pin(
        self,
        post_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.pin()`

        :param post_id: Post ID.
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.pin", params)
        model = BaseOkResponse
        return model(**response).response

    async def post(
        self,
        attachments: typing.Optional[typing.List[str]] = None,
        close_comments: typing.Optional[bool] = None,
        copyright: typing.Optional[str] = None,
        donut_paid_duration: typing.Optional[int] = None,
        friends_only: typing.Optional[bool] = None,
        from_group: typing.Optional[bool] = None,
        guid: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        link_photo_id: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        long: typing.Optional[float] = None,
        mark_as_ads: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        mute_notifications: typing.Optional[bool] = None,
        owner_id: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        publish_date: typing.Optional[int] = None,
        services: typing.Optional[str] = None,
        signed: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> WallPostResponseModel:
        """Method `wall.post()`

        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'page' - wiki-page, 'note' - note, 'poll' - poll, 'album' - photo album, '<owner_id>' - ID of the media application owner. '<media_id>' - Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param close_comments:
        :param copyright:
        :param donut_paid_duration:
        :param friends_only: '1' - post will be available to friends only, '0' - post will be available to all users (default)
        :param from_group: For a community: '1' - post will be published by the community, '0' - post will be published by the user (default)
        :param guid:
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param link_photo_id:
        :param link_title:
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param mark_as_ads:
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param mute_notifications:
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param place_id: ID of the location where the user was tagged.
        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param publish_date: Publication date (in Unix time). If used, posting will be delayed until the set time.
        :param services: List of services or websites the update will be exported to, if the user has so requested. Sample values: 'twitter', 'facebook'.
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' - post will be signed with the name of the posting user, '0' - post will not be signed (default)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.post", params)
        model = WallPostResponse
        return model(**response).response

    async def post_ads_stealth(
        self,
        owner_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        guid: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        link_button: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
        long: typing.Optional[float] = None,
        message: typing.Optional[str] = None,
        place_id: typing.Optional[int] = None,
        signed: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> WallPostAdsStealthResponseModel:
        """Method `wall.postAdsStealth()`

        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'page' - wiki-page, 'note' - note, 'poll' - poll, 'album' - photo album, '<owner_id>' - ID of the media application owner. '<media_id>' - Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param guid: Unique identifier to avoid duplication the same post.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param link_button: Link button ID
        :param link_image: Link image url
        :param link_title: Link title
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param place_id: ID of the location where the user was tagged.
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' - post will be signed with the name of the posting user, '0' - post will not be signed (default)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.postAdsStealth", params)
        model = WallPostAdsStealthResponse
        return model(**response).response

    async def report_comment(
        self,
        comment_id: int,
        owner_id: int,
        reason: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.reportComment()`

        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the wall.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.reportComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def report_post(
        self,
        owner_id: int,
        post_id: int,
        reason: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.reportPost()`

        :param owner_id: ID of the user or community that owns the wall.
        :param post_id: Post ID.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.reportPost", params)
        model = BaseOkResponse
        return model(**response).response

    async def repost(
        self,
        object: str,
        group_id: typing.Optional[int] = None,
        mark_as_ads: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        mute_notifications: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> WallRepostResponseModel:
        """Method `wall.repost()`

        :param object: ID of the object to be reposted on the wall. Example: "wall66748_3675"
        :param group_id: Target community ID when reposting to a community.
        :param mark_as_ads:
        :param message: Comment to be added along with the reposted object.
        :param mute_notifications:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.repost", params)
        model = WallRepostResponse
        return model(**response).response

    async def restore(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.restore()`

        :param owner_id: User ID or community ID from whose wall the post was deleted. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be restored.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.restore", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.restoreComment()`

        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.restoreComment", params)
        model = BaseOkResponse
        return model(**response).response

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        domain: typing.Optional[typing.Union["int", "str"]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        owners_only: typing.Optional[bool] = None,
        query: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> WallSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        domain: typing.Optional[typing.Union["int", "str"]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        owners_only: typing.Optional[bool] = None,
        query: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> WallSearchResponseModel: ...

    async def search(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        domain: typing.Optional[typing.Union["int", "str"]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        owners_only: typing.Optional[bool] = None,
        query: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[WallSearchResponseModel, WallSearchExtendedResponseModel]:
        """Method `wall.search()`

        :param extended: show extended post info.
        :param count: count of posts to return.
        :param domain: user or community screen name.
        :param fields:
        :param offset: Offset needed to return a specific subset of posts.
        :param owners_only: '1' - returns only page owner's posts.
        :param query: search query string.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.search", params)
        model = self.get_model(
            ((("extended",), WallSearchExtendedResponse),),
            default=WallSearchResponse,
            params=params,
        )
        return model(**response).response

    async def unpin(
        self,
        post_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `wall.unpin()`

        :param post_id: Post ID.
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("wall.unpin", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("WallCategory",)
