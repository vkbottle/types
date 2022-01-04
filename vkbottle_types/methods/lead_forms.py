import typing
from .base_category import BaseCategory
from vkbottle_types.responses.lead_forms import (
    CreateResponse,
    CreateResponseModel,
    DeleteResponse,
    DeleteResponseModel,
    GetLeadsResponse,
    GetLeadsResponseModel,
    GetResponse,
    LeadFormsForm,
    ListResponse,
    UploadUrlResponse,
)


class LeadFormsCategory(BaseCategory):
    async def create(
        self,
        group_id: int,
        name: str,
        title: str,
        description: str,
        questions: str,
        policy_link_url: str,
        photo: typing.Optional[str] = None,
        confirmation: typing.Optional[str] = None,
        site_link_url: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        once_per_user: typing.Optional[bool] = None,
        pixel_code: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> CreateResponseModel:
        """leadForms.create method

        :param group_id:
        :param name:
        :param title:
        :param description:
        :param questions:
        :param policy_link_url:
        :param photo:
        :param confirmation:
        :param site_link_url:
        :param active:
        :param once_per_user:
        :param pixel_code:
        :param notify_admins:
        :param notify_emails:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.create", params)
        model = CreateResponse
        return model(**response).response

    async def delete(
        self, group_id: int, form_id: int, **kwargs
    ) -> DeleteResponseModel:
        """leadForms.delete method

        :param group_id:
        :param form_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.delete", params)
        model = DeleteResponse
        return model(**response).response

    async def get(self, group_id: int, form_id: int, **kwargs) -> LeadFormsForm:
        """leadForms.get method

        :param group_id:
        :param form_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.get", params)
        model = GetResponse
        return model(**response).response

    async def get_leads(
        self,
        group_id: int,
        form_id: int,
        limit: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        **kwargs
    ) -> GetLeadsResponseModel:
        """leadForms.getLeads method

        :param group_id:
        :param form_id:
        :param limit:
        :param next_page_token:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.getLeads", params)
        model = GetLeadsResponse
        return model(**response).response

    async def get_upload_url(self, **kwargs) -> str:
        """leadForms.getUploadURL method"""

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.getUploadURL", params)
        model = UploadUrlResponse
        return model(**response).response

    async def list(self, group_id: int, **kwargs) -> typing.List[LeadFormsForm]:
        """leadForms.list method

        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.list", params)
        model = ListResponse
        return model(**response).response

    async def update(
        self,
        group_id: int,
        form_id: int,
        name: str,
        title: str,
        description: str,
        questions: str,
        policy_link_url: str,
        photo: typing.Optional[str] = None,
        confirmation: typing.Optional[str] = None,
        site_link_url: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        once_per_user: typing.Optional[bool] = None,
        pixel_code: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> CreateResponseModel:
        """leadForms.update method

        :param group_id:
        :param form_id:
        :param name:
        :param title:
        :param description:
        :param questions:
        :param policy_link_url:
        :param photo:
        :param confirmation:
        :param site_link_url:
        :param active:
        :param once_per_user:
        :param pixel_code:
        :param notify_admins:
        :param notify_emails:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.update", params)
        model = CreateResponse
        return model(**response).response
