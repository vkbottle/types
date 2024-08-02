import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import AsrTask, BaseUploadServer
from vkbottle_types.responses.asr import *  # noqa: F401,F403
from vkbottle_types.responses.base import (
    BaseGetUploadServerResponse,
)


class AsrCategory(BaseCategory):
    async def check_status(
        self,
        task_id: str,
        **kwargs: typing.Any,
    ) -> "AsrTask":
        """Method `asr.checkStatus()`

        :param task_id: ID of ASR task in UUID format.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("asr.checkStatus", params)
        model = AsrCheckStatusResponse
        return model(**response).response

    async def get_upload_url(
        self,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `asr.getUploadUrl()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("asr.getUploadUrl", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def process(
        self,
        audio: str,
        _model: str,
        **kwargs: typing.Any,
    ) -> AsrProcessResponseModel:
        """Method `asr.process()`

        :param audio: This parameter is a JSON response returned from [vk.com/dev/upload_files_2|file uploading server].
        :param model: Which model to use for recognition. `neutral` -- general purpose (interviews, TV shows, etc.), `spontaneous` -- for NSFW audios (slang, profanity, etc.)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("asr.process", params)
        model = AsrProcessResponse
        return model(**response).response


__all__ = ("AsrCategory",)
