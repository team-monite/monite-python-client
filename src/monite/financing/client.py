# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.financing_invoice_cursor_fields import FinancingInvoiceCursorFields
from ..types.financing_invoice_list_response import FinancingInvoiceListResponse
from ..types.financing_invoice_type import FinancingInvoiceType
from ..types.financing_offers_response import FinancingOffersResponse
from ..types.financing_push_invoices_request_invoice import FinancingPushInvoicesRequestInvoice
from ..types.financing_push_invoices_response import FinancingPushInvoicesResponse
from ..types.financing_token_response import FinancingTokenResponse
from ..types.order_enum import OrderEnum
from ..types.wc_invoice_status import WcInvoiceStatus
from .raw_client import AsyncRawFinancingClient, RawFinancingClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FinancingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFinancingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFinancingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFinancingClient
        """
        return self._raw_client

    def get_financing_invoices(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[FinancingInvoiceCursorFields] = None,
        invoice_id: typing.Optional[str] = None,
        invoice_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[WcInvoiceStatus] = None,
        status_in: typing.Optional[typing.Union[WcInvoiceStatus, typing.Sequence[WcInvoiceStatus]]] = None,
        type: typing.Optional[FinancingInvoiceType] = None,
        type_in: typing.Optional[typing.Union[FinancingInvoiceType, typing.Sequence[FinancingInvoiceType]]] = None,
        document_id: typing.Optional[str] = None,
        document_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        issue_date_gt: typing.Optional[dt.datetime] = None,
        issue_date_lt: typing.Optional[dt.datetime] = None,
        issue_date_gte: typing.Optional[dt.datetime] = None,
        issue_date_lte: typing.Optional[dt.datetime] = None,
        due_date_gt: typing.Optional[dt.datetime] = None,
        due_date_lt: typing.Optional[dt.datetime] = None,
        due_date_gte: typing.Optional[dt.datetime] = None,
        due_date_lte: typing.Optional[dt.datetime] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_gte: typing.Optional[dt.datetime] = None,
        created_at_lte: typing.Optional[dt.datetime] = None,
        total_amount: typing.Optional[int] = None,
        total_amount_gt: typing.Optional[int] = None,
        total_amount_lt: typing.Optional[int] = None,
        total_amount_gte: typing.Optional[int] = None,
        total_amount_lte: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancingInvoiceListResponse:
        """
        Returns a list of invoices requested for financing

        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[FinancingInvoiceCursorFields]
            Allowed sort fields

        invoice_id : typing.Optional[str]
            ID of a payable or receivable invoice.

        invoice_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of invoice IDs.

        status : typing.Optional[WcInvoiceStatus]
            Status of the invoice.

        status_in : typing.Optional[typing.Union[WcInvoiceStatus, typing.Sequence[WcInvoiceStatus]]]
            List of invoice statuses.

        type : typing.Optional[FinancingInvoiceType]
            Type of the invoice. payable or receivable.

        type_in : typing.Optional[typing.Union[FinancingInvoiceType, typing.Sequence[FinancingInvoiceType]]]
            List of invoice types.

        document_id : typing.Optional[str]
            Document ID of the invoice.

        document_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of document IDs.

        issue_date_gt : typing.Optional[dt.datetime]
            Issue date greater than.

        issue_date_lt : typing.Optional[dt.datetime]
            Issue date less than.

        issue_date_gte : typing.Optional[dt.datetime]
            Issue date greater than or equal.

        issue_date_lte : typing.Optional[dt.datetime]
            Issue date less than or equal.

        due_date_gt : typing.Optional[dt.datetime]
            Due date greater than.

        due_date_lt : typing.Optional[dt.datetime]
            Due date less than.

        due_date_gte : typing.Optional[dt.datetime]
            Due date greater than or equal.

        due_date_lte : typing.Optional[dt.datetime]
            Due date less than or equal.

        created_at_gt : typing.Optional[dt.datetime]
            Created date greater than.

        created_at_lt : typing.Optional[dt.datetime]
            Created date less than.

        created_at_gte : typing.Optional[dt.datetime]
            Created date greater than or equal.

        created_at_lte : typing.Optional[dt.datetime]
            Created date less than or equal.

        total_amount : typing.Optional[int]
            Total amount of the invoice in minor units.

        total_amount_gt : typing.Optional[int]
            Total amount greater than.

        total_amount_lt : typing.Optional[int]
            Total amount less than.

        total_amount_gte : typing.Optional[int]
            Total amount greater than or equal.

        total_amount_lte : typing.Optional[int]
            Total amount less than or equal.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingInvoiceListResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.financing.get_financing_invoices()
        """
        _response = self._raw_client.get_financing_invoices(
            order=order,
            limit=limit,
            pagination_token=pagination_token,
            sort=sort,
            invoice_id=invoice_id,
            invoice_id_in=invoice_id_in,
            status=status,
            status_in=status_in,
            type=type,
            type_in=type_in,
            document_id=document_id,
            document_id_in=document_id_in,
            issue_date_gt=issue_date_gt,
            issue_date_lt=issue_date_lt,
            issue_date_gte=issue_date_gte,
            issue_date_lte=issue_date_lte,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            due_date_gte=due_date_gte,
            due_date_lte=due_date_lte,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
            total_amount=total_amount,
            total_amount_gt=total_amount_gt,
            total_amount_lt=total_amount_lt,
            total_amount_gte=total_amount_gte,
            total_amount_lte=total_amount_lte,
            request_options=request_options,
        )
        return _response.data

    def post_financing_invoices(
        self,
        *,
        invoices: typing.Sequence[FinancingPushInvoicesRequestInvoice],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancingPushInvoicesResponse:
        """
        Returns a session token and a connect token to open Kanmon SDK for confirming invoice details.

        Parameters
        ----------
        invoices : typing.Sequence[FinancingPushInvoicesRequestInvoice]
            A list of invoices to request financing for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingPushInvoicesResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        from monite import FinancingPushInvoicesRequestInvoice
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.financing.post_financing_invoices(invoices=[FinancingPushInvoicesRequestInvoice(id='id', type="payable", )], )
        """
        _response = self._raw_client.post_financing_invoices(invoices=invoices, request_options=request_options)
        return _response.data

    def get_financing_offers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FinancingOffersResponse:
        """
        Returns a list of financing offers and the business's onboarding status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingOffersResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.financing.get_financing_offers()
        """
        _response = self._raw_client.get_financing_offers(request_options=request_options)
        return _response.data

    def post_financing_tokens(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FinancingTokenResponse:
        """
        Returns a token for Kanmon SDK. Creates a business and user on Kanmon if not already exist.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingTokenResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.financing.post_financing_tokens()
        """
        _response = self._raw_client.post_financing_tokens(request_options=request_options)
        return _response.data


class AsyncFinancingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFinancingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFinancingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFinancingClient
        """
        return self._raw_client

    async def get_financing_invoices(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[FinancingInvoiceCursorFields] = None,
        invoice_id: typing.Optional[str] = None,
        invoice_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[WcInvoiceStatus] = None,
        status_in: typing.Optional[typing.Union[WcInvoiceStatus, typing.Sequence[WcInvoiceStatus]]] = None,
        type: typing.Optional[FinancingInvoiceType] = None,
        type_in: typing.Optional[typing.Union[FinancingInvoiceType, typing.Sequence[FinancingInvoiceType]]] = None,
        document_id: typing.Optional[str] = None,
        document_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        issue_date_gt: typing.Optional[dt.datetime] = None,
        issue_date_lt: typing.Optional[dt.datetime] = None,
        issue_date_gte: typing.Optional[dt.datetime] = None,
        issue_date_lte: typing.Optional[dt.datetime] = None,
        due_date_gt: typing.Optional[dt.datetime] = None,
        due_date_lt: typing.Optional[dt.datetime] = None,
        due_date_gte: typing.Optional[dt.datetime] = None,
        due_date_lte: typing.Optional[dt.datetime] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_gte: typing.Optional[dt.datetime] = None,
        created_at_lte: typing.Optional[dt.datetime] = None,
        total_amount: typing.Optional[int] = None,
        total_amount_gt: typing.Optional[int] = None,
        total_amount_lt: typing.Optional[int] = None,
        total_amount_gte: typing.Optional[int] = None,
        total_amount_lte: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancingInvoiceListResponse:
        """
        Returns a list of invoices requested for financing

        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[FinancingInvoiceCursorFields]
            Allowed sort fields

        invoice_id : typing.Optional[str]
            ID of a payable or receivable invoice.

        invoice_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of invoice IDs.

        status : typing.Optional[WcInvoiceStatus]
            Status of the invoice.

        status_in : typing.Optional[typing.Union[WcInvoiceStatus, typing.Sequence[WcInvoiceStatus]]]
            List of invoice statuses.

        type : typing.Optional[FinancingInvoiceType]
            Type of the invoice. payable or receivable.

        type_in : typing.Optional[typing.Union[FinancingInvoiceType, typing.Sequence[FinancingInvoiceType]]]
            List of invoice types.

        document_id : typing.Optional[str]
            Document ID of the invoice.

        document_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of document IDs.

        issue_date_gt : typing.Optional[dt.datetime]
            Issue date greater than.

        issue_date_lt : typing.Optional[dt.datetime]
            Issue date less than.

        issue_date_gte : typing.Optional[dt.datetime]
            Issue date greater than or equal.

        issue_date_lte : typing.Optional[dt.datetime]
            Issue date less than or equal.

        due_date_gt : typing.Optional[dt.datetime]
            Due date greater than.

        due_date_lt : typing.Optional[dt.datetime]
            Due date less than.

        due_date_gte : typing.Optional[dt.datetime]
            Due date greater than or equal.

        due_date_lte : typing.Optional[dt.datetime]
            Due date less than or equal.

        created_at_gt : typing.Optional[dt.datetime]
            Created date greater than.

        created_at_lt : typing.Optional[dt.datetime]
            Created date less than.

        created_at_gte : typing.Optional[dt.datetime]
            Created date greater than or equal.

        created_at_lte : typing.Optional[dt.datetime]
            Created date less than or equal.

        total_amount : typing.Optional[int]
            Total amount of the invoice in minor units.

        total_amount_gt : typing.Optional[int]
            Total amount greater than.

        total_amount_lt : typing.Optional[int]
            Total amount less than.

        total_amount_gte : typing.Optional[int]
            Total amount greater than or equal.

        total_amount_lte : typing.Optional[int]
            Total amount less than or equal.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingInvoiceListResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.financing.get_financing_invoices()
        asyncio.run(main())
        """
        _response = await self._raw_client.get_financing_invoices(
            order=order,
            limit=limit,
            pagination_token=pagination_token,
            sort=sort,
            invoice_id=invoice_id,
            invoice_id_in=invoice_id_in,
            status=status,
            status_in=status_in,
            type=type,
            type_in=type_in,
            document_id=document_id,
            document_id_in=document_id_in,
            issue_date_gt=issue_date_gt,
            issue_date_lt=issue_date_lt,
            issue_date_gte=issue_date_gte,
            issue_date_lte=issue_date_lte,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            due_date_gte=due_date_gte,
            due_date_lte=due_date_lte,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
            total_amount=total_amount,
            total_amount_gt=total_amount_gt,
            total_amount_lt=total_amount_lt,
            total_amount_gte=total_amount_gte,
            total_amount_lte=total_amount_lte,
            request_options=request_options,
        )
        return _response.data

    async def post_financing_invoices(
        self,
        *,
        invoices: typing.Sequence[FinancingPushInvoicesRequestInvoice],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancingPushInvoicesResponse:
        """
        Returns a session token and a connect token to open Kanmon SDK for confirming invoice details.

        Parameters
        ----------
        invoices : typing.Sequence[FinancingPushInvoicesRequestInvoice]
            A list of invoices to request financing for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingPushInvoicesResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        from monite import FinancingPushInvoicesRequestInvoice
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.financing.post_financing_invoices(invoices=[FinancingPushInvoicesRequestInvoice(id='id', type="payable", )], )
        asyncio.run(main())
        """
        _response = await self._raw_client.post_financing_invoices(invoices=invoices, request_options=request_options)
        return _response.data

    async def get_financing_offers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FinancingOffersResponse:
        """
        Returns a list of financing offers and the business's onboarding status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingOffersResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.financing.get_financing_offers()
        asyncio.run(main())
        """
        _response = await self._raw_client.get_financing_offers(request_options=request_options)
        return _response.data

    async def post_financing_tokens(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FinancingTokenResponse:
        """
        Returns a token for Kanmon SDK. Creates a business and user on Kanmon if not already exist.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancingTokenResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.financing.post_financing_tokens()
        asyncio.run(main())
        """
        _response = await self._raw_client.post_financing_tokens(request_options=request_options)
        return _response.data
