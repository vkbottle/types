import typing
from .base_category import BaseCategory
from vkbottle_types.responses import polls, base


class PollsCategory(BaseCategory):
    async def add_vote(
        self,
        poll_id: int,
        answer_ids: typing.List[int],
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        **kwargs
    ) -> polls.AddVoteResponseModel:
        """Adds the current user's vote to the selected answer in the poll.
        :param poll_id: Poll ID.
        :param answer_ids:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.addVote", params)
        model = polls.AddVoteResponse
        return model(**response).response

    async def create(
        self,
        question: typing.Optional[str] = None,
        is_anonymous: typing.Optional[bool] = None,
        is_multiple: typing.Optional[bool] = None,
        end_date: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        app_id: typing.Optional[int] = None,
        add_answers: typing.Optional[str] = None,
        photo_id: typing.Optional[int] = None,
        background_id: typing.Optional[str] = None,
        disable_unvote: typing.Optional[bool] = None,
        **kwargs
    ) -> polls.CreateResponseModel:
        """Creates polls that can be attached to the users' or communities' posts.
        :param question: question text
        :param is_anonymous: '1' - anonymous poll, participants list is hidden,, '0' - public poll, participants list is available,, Default value is '0'.
        :param is_multiple:
        :param end_date:
        :param owner_id: If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
        :param app_id:
        :param add_answers: available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
        :param photo_id:
        :param background_id:
        :param disable_unvote:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.create", params)
        model = polls.CreateResponse
        return model(**response).response

    async def delete_vote(
        self,
        poll_id: int,
        answer_id: int,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        **kwargs
    ) -> polls.DeleteVoteResponseModel:
        """Deletes the current user's vote from the selected answer in the poll.
        :param poll_id: Poll ID.
        :param answer_id: Answer ID.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.deleteVote", params)
        model = polls.DeleteVoteResponse
        return model(**response).response

    async def edit(
        self,
        poll_id: int,
        owner_id: typing.Optional[int] = None,
        question: typing.Optional[str] = None,
        add_answers: typing.Optional[str] = None,
        edit_answers: typing.Optional[str] = None,
        delete_answers: typing.Optional[str] = None,
        end_date: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        background_id: typing.Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits created polls
        :param poll_id: edited poll's id
        :param owner_id: poll owner id
        :param question: new question text
        :param add_answers: answers list, for example: , "["yes","no","maybe"]"
        :param edit_answers: object containing answers that need to be edited,, key - answer id, value - new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
        :param delete_answers: list of answer ids to be deleted. For example: "[382967099, 382967103]"
        :param end_date:
        :param photo_id:
        :param background_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.edit", params)
        model = base.OkResponse
        return model(**response).response

    async def get_backgrounds(
        self, **kwargs
    ) -> polls.GetBackgroundsResponseModel:
        """polls.getBackgrounds method"""

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getBackgrounds", params)
        model = polls.GetBackgroundsResponse
        return model(**response).response

    async def get_by_id(
        self,
        poll_id: int,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        extended: typing.Optional[bool] = None,
        friends_count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs
    ) -> polls.GetByIdResponseModel:
        """Returns detailed information about a poll by its ID.
        :param poll_id: Poll ID.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: '1' - poll is in a board, '0' - poll is on a wall. '0' by default.
        :param extended:
        :param friends_count:
        :param fields:
        :param name_case:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getById", params)
        model = polls.GetByIdResponse
        return model(**response).response

    async def get_photo_upload_server(
        self, owner_id: typing.Optional[int] = None, **kwargs
    ) -> base.GetUploadServerResponseModel:
        """polls.getPhotoUploadServer method
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getPhotoUploadServer", params)
        model = base.GetUploadServerResponse
        return model(**response).response

    async def get_voters(
        self,
        poll_id: int,
        answer_ids: typing.List[int],
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        friends_only: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs
    ) -> polls.GetVotersResponseModel:
        """Returns a list of IDs of users who selected specific answers in the poll.
        :param poll_id: Poll ID.
        :param answer_ids: Answer IDs.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board:
        :param friends_only: '1' — to return only current user's friends, '0' — to return all users (default),
        :param offset: Offset needed to return a specific subset of voters. '0' — (default)
        :param count: Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' — (default)
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getVoters", params)
        model = polls.GetVotersResponse
        return model(**response).response

    async def save_photo(
        self, photo: str, hash: str, **kwargs
    ) -> polls.SavePhotoResponseModel:
        """polls.savePhoto method
        :param photo:
        :param hash:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.savePhoto", params)
        model = polls.SavePhotoResponse
        return model(**response).response
