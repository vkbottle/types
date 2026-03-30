import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUploadServer, PollsBackground, PollsFieldsVoters, PollsPoll, PollsPollExtended, PollsVoters, UsersFields
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseGetUploadServerResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.polls import *  # noqa: F401,F403  # type: ignore


class PollsCategory(BaseCategory):
    async def add_vote(
        self,
        answer_ids: list[int],
        poll_id: int,
        is_board: bool | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `polls.addVote()`

        :param answer_ids:
        :param poll_id: Poll ID.
        :param is_board:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.addVote", params)
        model = BaseBoolResponse
        return model(**response).response

    async def create(
        self,
        add_answers: str | None = None,
        app_id: int | None = None,
        background_id: str | None = None,
        disable_unvote: bool | None = None,
        end_date: int | None = None,
        is_anonymous: bool | None = None,
        is_multiple: bool | None = None,
        owner_id: int | None = None,
        photo_id: int | None = None,
        question: str | None = None,
        **kwargs: typing.Any,
    ) -> "PollsPoll":
        """Method `polls.create()`

        :param add_answers: available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
        :param app_id:
        :param background_id:
        :param disable_unvote:
        :param end_date:
        :param is_anonymous: '1' - anonymous poll, participants list is hidden,, '0' - public poll, participants list is available,, Default value is '0'.
        :param is_multiple:
        :param owner_id: If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
        :param photo_id:
        :param question: question text
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.create", params)
        model = PollsCreateResponse
        return model(**response).response

    async def delete_vote(
        self,
        poll_id: int,
        is_board: bool | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `polls.deleteVote()`

        :param poll_id: Poll ID.
        :param is_board:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.deleteVote", params)
        model = BaseBoolResponse
        return model(**response).response

    async def edit(
        self,
        poll_id: int,
        add_answers: str | None = None,
        background_id: str | None = None,
        delete_answers: str | None = None,
        edit_answers: str | None = None,
        end_date: int | None = None,
        owner_id: int | None = None,
        photo_id: int | None = None,
        question: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `polls.edit()`

        :param poll_id: edited poll's id
        :param add_answers: answers list, for example: , "["yes","no","maybe"]"
        :param background_id:
        :param delete_answers: list of answer ids to be deleted. For example: "[382967099, 382967103]"
        :param edit_answers: object containing answers that need to be edited,, key - answer id, value - new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
        :param end_date:
        :param owner_id: poll owner id
        :param photo_id:
        :param question: new question text
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.edit", params)
        model = BaseOkResponse
        return model(**response).response

    async def get_backgrounds(
        self,
        **kwargs: typing.Any,
    ) -> list[PollsBackground]:
        """Method `polls.getBackgrounds()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getBackgrounds", params)
        model = PollsGetBackgroundsResponse
        return model(**response).response

    async def get_by_id(
        self,
        poll_id: int,
        extended: bool | None = None,
        fields: list[str] | None = None,
        friends_count: int | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> "PollsPollExtended":
        """Method `polls.getById()`

        :param poll_id: Poll ID.
        :param extended:
        :param fields:
        :param friends_count:
        :param is_board: '1' - poll is in a board, '0' - poll is on a wall. '0' by default.
        :param name_case:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getById", params)
        model = PollsGetByIdResponse
        return model(**response).response

    async def get_photo_upload_server(
        self,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `polls.getPhotoUploadServer()`

        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getPhotoUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    @typing.overload
    async def get_voters(
        self,
        answer_ids: list[int],
        poll_id: int,
        fields: list[UsersFields],
        count: int | None = None,
        friends_only: bool | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> list[PollsFieldsVoters]: ...

    @typing.overload
    async def get_voters(
        self,
        answer_ids: list[int],
        poll_id: int,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        friends_only: bool | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> list[PollsVoters]: ...

    async def get_voters(
        self,
        answer_ids: list[int],
        poll_id: int,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        friends_only: bool | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> list[PollsVoters] | list[PollsFieldsVoters]:
        """Method `polls.getVoters()`

        :param answer_ids: Answer IDs.
        :param poll_id: Poll ID.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param count: Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' - (default)
        :param friends_only: '1' - to return only current user's friends, '0' - to return all users (default),
        :param is_board:
        :param name_case: Case for declension of user name and surname: , 'nom' - nominative (default) , 'gen' - genitive , 'dat' - dative , 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param offset: Offset needed to return a specific subset of voters. '0' - (default)
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.getVoters", params)
        model = self.get_model(
            ((("fields",), PollsGetVotersFieldsResponse),),
            default=PollsGetVotersResponse,
            params=params,
        )
        return model(**response).response

    async def save_photo(
        self,
        hash: str | None = None,
        photo: str | None = None,
        **kwargs: typing.Any,
    ) -> "PollsBackground":
        """Method `polls.savePhoto()`

        :param hash:
        :param photo:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("polls.savePhoto", params)
        model = PollsSavePhotoResponse
        return model(**response).response


__all__ = ("PollsCategory",)
