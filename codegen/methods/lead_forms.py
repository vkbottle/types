import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import LeadFormsForm
from vkbottle_types.responses.lead_forms import *  # noqa: F401,F403  # type: ignore


class LeadFormsCategory(BaseCategory):
    async def create(
        self,
        description: str,
        group_id: int,
        name: str,
        policy_link_url: str,
        questions: str,
        title: str,
        active: typing.Optional[bool] = None,
        confirmation: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        once_per_user: typing.Optional[bool] = None,
        photo: typing.Optional[str] = None,
        pixel_code: typing.Optional[str] = None,
        site_link_url: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> LeadFormsCreateResponseModel:
        """Method `leadForms.create()`

        :param description:
        :param group_id:
        :param name:
        :param policy_link_url:
        :param questions:
        :param title:
        :param active:
        :param confirmation:
        :param notify_admins:
        :param notify_emails:
        :param once_per_user:
        :param photo:
        :param pixel_code:
        :param site_link_url:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.create", params)
        model = LeadFormsCreateResponse
        return model(**response).response

    async def delete(
        self,
        form_id: int,
        group_id: int,
        **kwargs: typing.Any,
    ) -> LeadFormsDeleteResponseModel:
        """Method `leadForms.delete()`

        :param form_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.delete", params)
        model = LeadFormsDeleteResponse
        return model(**response).response

    async def get(
        self,
        form_id: int,
        group_id: int,
        **kwargs: typing.Any,
    ) -> "LeadFormsForm":
        """Method `leadForms.get()`

        :param form_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.get", params)
        model = LeadFormsGetResponse
        return model(**response).response

    async def get_leads(
        self,
        form_id: int,
        group_id: int,
        limit: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> LeadFormsGetLeadsResponseModel:
        """Method `leadForms.getLeads()`

        :param form_id:
        :param group_id:
        :param limit:
        :param next_page_token:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.getLeads", params)
        model = LeadFormsGetLeadsResponse
        return model(**response).response

    async def get_upload_url(
        self,
        **kwargs: typing.Any,
    ) -> str:
        """Method `leadForms.getUploadURL()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.getUploadURL", params)
        model = LeadFormsUploadUrlResponse
        return model(**response).response

    async def list(
        self,
        group_id: int,
        **kwargs: typing.Any,
    ) -> typing.List[LeadFormsForm]:
        """Method `leadForms.list()`

        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.list", params)
        model = LeadFormsListResponse
        return model(**response).response

    async def update(
        self,
        description: str,
        form_id: int,
        group_id: int,
        name: str,
        policy_link_url: str,
        questions: str,
        title: str,
        active: typing.Optional[bool] = None,
        confirmation: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        once_per_user: typing.Optional[bool] = None,
        photo: typing.Optional[str] = None,
        pixel_code: typing.Optional[str] = None,
        site_link_url: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> LeadFormsCreateResponseModel:
        """Method `leadForms.update()`

        :param description:
        :param form_id:
        :param group_id:
        :param name:
        :param policy_link_url:
        :param questions:
        :param title:
        :param active:
        :param confirmation:
        :param notify_admins:
        :param notify_emails:
        :param once_per_user:
        :param photo:
        :param pixel_code:
        :param site_link_url:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.update", params)
        model = LeadFormsCreateResponse
        return model(**response).response


__all__ = ("LeadFormsCategory",)
