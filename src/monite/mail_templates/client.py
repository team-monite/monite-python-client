# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.custom_template_data_schema import CustomTemplateDataSchema
from ..types.custom_templates_cursor_fields import CustomTemplatesCursorFields
from ..types.custom_templates_pagination_response import CustomTemplatesPaginationResponse
from ..types.document_object_type_request_enum import DocumentObjectTypeRequestEnum
from ..types.language_code_enum import LanguageCodeEnum
from ..types.order_enum import OrderEnum
from ..types.preview_template_response import PreviewTemplateResponse
from ..types.system_templates import SystemTemplates
from .raw_client import AsyncRawMailTemplatesClient, RawMailTemplatesClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MailTemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMailTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMailTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMailTemplatesClient
        """
        return self._raw_client

    def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[CustomTemplatesCursorFields] = None,
        type: typing.Optional[DocumentObjectTypeRequestEnum] = None,
        type_in: typing.Optional[
            typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]
        ] = None,
        type_not_in: typing.Optional[
            typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]
        ] = None,
        is_default: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        name_iexact: typing.Optional[str] = None,
        name_contains: typing.Optional[str] = None,
        name_icontains: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomTemplatesPaginationResponse:
        """
        Get all custom templates

        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[CustomTemplatesCursorFields]
            Allowed sort fields

        type : typing.Optional[DocumentObjectTypeRequestEnum]

        type_in : typing.Optional[typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]]

        type_not_in : typing.Optional[typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]]

        is_default : typing.Optional[bool]

        name : typing.Optional[str]

        name_iexact : typing.Optional[str]

        name_contains : typing.Optional[str]

        name_icontains : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplatesPaginationResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.get()
        """
        _response = self._raw_client.get(
            order=order,
            limit=limit,
            pagination_token=pagination_token,
            sort=sort,
            type=type,
            type_in=type_in,
            type_not_in=type_not_in,
            is_default=is_default,
            name=name,
            name_iexact=name_iexact,
            name_contains=name_contains,
            name_icontains=name_icontains,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        body_template: str,
        name: str,
        subject_template: str,
        type: DocumentObjectTypeRequestEnum,
        is_default: typing.Optional[bool] = OMIT,
        language: typing.Optional[LanguageCodeEnum] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomTemplateDataSchema:
        """
        Create custom template

        Parameters
        ----------
        body_template : str
            Jinja2 compatible string with email body

        name : str
            Custom template name

        subject_template : str
            Jinja2 compatible string with email subject

        type : DocumentObjectTypeRequestEnum
            Document type of content

        is_default : typing.Optional[bool]
            Is default template

        language : typing.Optional[LanguageCodeEnum]
            Lowercase ISO code of language

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.create(body_template='body_template', name='name', subject_template='subject_template', type="receivables_quote", )
        """
        _response = self._raw_client.create(
            body_template=body_template,
            name=name,
            subject_template=subject_template,
            type=type,
            is_default=is_default,
            language=language,
            request_options=request_options,
        )
        return _response.data

    def preview(
        self,
        *,
        body: str,
        document_type: DocumentObjectTypeRequestEnum,
        language_code: LanguageCodeEnum,
        subject: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreviewTemplateResponse:
        """
        Preview rendered template

        Parameters
        ----------
        body : str
            Body text of the template

        document_type : DocumentObjectTypeRequestEnum
            Document type of content

        language_code : LanguageCodeEnum
            Lowercase ISO code of language

        subject : str
            Subject text of the template

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewTemplateResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.preview(body='body', document_type="receivables_quote", language_code="ab", subject='subject', )
        """
        _response = self._raw_client.preview(
            body=body,
            document_type=document_type,
            language_code=language_code,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    def get_system(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemTemplates:
        """
        Get all system templates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemTemplates
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.get_system()
        """
        _response = self._raw_client.get_system(request_options=request_options)
        return _response.data

    def get_by_id(
        self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomTemplateDataSchema:
        """
        Get custom template by ID

        Parameters
        ----------
        template_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.get_by_id(template_id='template_id', )
        """
        _response = self._raw_client.get_by_id(template_id, request_options=request_options)
        return _response.data

    def delete_by_id(self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete custom template bt ID

        Parameters
        ----------
        template_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.delete_by_id(template_id='template_id', )
        """
        _response = self._raw_client.delete_by_id(template_id, request_options=request_options)
        return _response.data

    def update_by_id(
        self,
        template_id: str,
        *,
        body_template: typing.Optional[str] = OMIT,
        language: typing.Optional[LanguageCodeEnum] = OMIT,
        name: typing.Optional[str] = OMIT,
        subject_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomTemplateDataSchema:
        """
        Update custom template by ID

        Parameters
        ----------
        template_id : str

        body_template : typing.Optional[str]
            Jinja2 compatible string with email body

        language : typing.Optional[LanguageCodeEnum]
            Lowercase ISO code of language

        name : typing.Optional[str]
            Custom template name

        subject_template : typing.Optional[str]
            Jinja2 compatible string with email subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.update_by_id(template_id='template_id', )
        """
        _response = self._raw_client.update_by_id(
            template_id,
            body_template=body_template,
            language=language,
            name=name,
            subject_template=subject_template,
            request_options=request_options,
        )
        return _response.data

    def make_default_by_id(
        self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomTemplateDataSchema:
        """
        Make template default

        Parameters
        ----------
        template_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.mail_templates.make_default_by_id(template_id='template_id', )
        """
        _response = self._raw_client.make_default_by_id(template_id, request_options=request_options)
        return _response.data


class AsyncMailTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMailTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMailTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMailTemplatesClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[CustomTemplatesCursorFields] = None,
        type: typing.Optional[DocumentObjectTypeRequestEnum] = None,
        type_in: typing.Optional[
            typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]
        ] = None,
        type_not_in: typing.Optional[
            typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]
        ] = None,
        is_default: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        name_iexact: typing.Optional[str] = None,
        name_contains: typing.Optional[str] = None,
        name_icontains: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomTemplatesPaginationResponse:
        """
        Get all custom templates

        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[CustomTemplatesCursorFields]
            Allowed sort fields

        type : typing.Optional[DocumentObjectTypeRequestEnum]

        type_in : typing.Optional[typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]]

        type_not_in : typing.Optional[typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]]

        is_default : typing.Optional[bool]

        name : typing.Optional[str]

        name_iexact : typing.Optional[str]

        name_contains : typing.Optional[str]

        name_icontains : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplatesPaginationResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.get()
        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            order=order,
            limit=limit,
            pagination_token=pagination_token,
            sort=sort,
            type=type,
            type_in=type_in,
            type_not_in=type_not_in,
            is_default=is_default,
            name=name,
            name_iexact=name_iexact,
            name_contains=name_contains,
            name_icontains=name_icontains,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        body_template: str,
        name: str,
        subject_template: str,
        type: DocumentObjectTypeRequestEnum,
        is_default: typing.Optional[bool] = OMIT,
        language: typing.Optional[LanguageCodeEnum] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomTemplateDataSchema:
        """
        Create custom template

        Parameters
        ----------
        body_template : str
            Jinja2 compatible string with email body

        name : str
            Custom template name

        subject_template : str
            Jinja2 compatible string with email subject

        type : DocumentObjectTypeRequestEnum
            Document type of content

        is_default : typing.Optional[bool]
            Is default template

        language : typing.Optional[LanguageCodeEnum]
            Lowercase ISO code of language

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.create(body_template='body_template', name='name', subject_template='subject_template', type="receivables_quote", )
        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            body_template=body_template,
            name=name,
            subject_template=subject_template,
            type=type,
            is_default=is_default,
            language=language,
            request_options=request_options,
        )
        return _response.data

    async def preview(
        self,
        *,
        body: str,
        document_type: DocumentObjectTypeRequestEnum,
        language_code: LanguageCodeEnum,
        subject: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreviewTemplateResponse:
        """
        Preview rendered template

        Parameters
        ----------
        body : str
            Body text of the template

        document_type : DocumentObjectTypeRequestEnum
            Document type of content

        language_code : LanguageCodeEnum
            Lowercase ISO code of language

        subject : str
            Subject text of the template

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewTemplateResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.preview(body='body', document_type="receivables_quote", language_code="ab", subject='subject', )
        asyncio.run(main())
        """
        _response = await self._raw_client.preview(
            body=body,
            document_type=document_type,
            language_code=language_code,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    async def get_system(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemTemplates:
        """
        Get all system templates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemTemplates
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.get_system()
        asyncio.run(main())
        """
        _response = await self._raw_client.get_system(request_options=request_options)
        return _response.data

    async def get_by_id(
        self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomTemplateDataSchema:
        """
        Get custom template by ID

        Parameters
        ----------
        template_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.get_by_id(template_id='template_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id(template_id, request_options=request_options)
        return _response.data

    async def delete_by_id(self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete custom template bt ID

        Parameters
        ----------
        template_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.delete_by_id(template_id='template_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.delete_by_id(template_id, request_options=request_options)
        return _response.data

    async def update_by_id(
        self,
        template_id: str,
        *,
        body_template: typing.Optional[str] = OMIT,
        language: typing.Optional[LanguageCodeEnum] = OMIT,
        name: typing.Optional[str] = OMIT,
        subject_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomTemplateDataSchema:
        """
        Update custom template by ID

        Parameters
        ----------
        template_id : str

        body_template : typing.Optional[str]
            Jinja2 compatible string with email body

        language : typing.Optional[LanguageCodeEnum]
            Lowercase ISO code of language

        name : typing.Optional[str]
            Custom template name

        subject_template : typing.Optional[str]
            Jinja2 compatible string with email subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.update_by_id(template_id='template_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.update_by_id(
            template_id,
            body_template=body_template,
            language=language,
            name=name,
            subject_template=subject_template,
            request_options=request_options,
        )
        return _response.data

    async def make_default_by_id(
        self, template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CustomTemplateDataSchema:
        """
        Make template default

        Parameters
        ----------
        template_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomTemplateDataSchema
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.mail_templates.make_default_by_id(template_id='template_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.make_default_by_id(template_id, request_options=request_options)
        return _response.data
