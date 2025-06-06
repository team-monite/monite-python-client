# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.currency_enum import CurrencyEnum
from ..types.order_enum import OrderEnum
from ..types.purchase_order_cursor_fields import PurchaseOrderCursorFields
from ..types.purchase_order_email_preview_response import PurchaseOrderEmailPreviewResponse
from ..types.purchase_order_email_sent_response import PurchaseOrderEmailSentResponse
from ..types.purchase_order_item import PurchaseOrderItem
from ..types.purchase_order_pagination_response import PurchaseOrderPaginationResponse
from ..types.purchase_order_response_schema import PurchaseOrderResponseSchema
from ..types.purchase_order_status_enum import PurchaseOrderStatusEnum
from ..types.variables_object_list import VariablesObjectList
from .raw_client import AsyncRawPurchaseOrdersClient, RawPurchaseOrdersClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PurchaseOrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPurchaseOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPurchaseOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPurchaseOrdersClient
        """
        return self._raw_client

    def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[PurchaseOrderCursorFields] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_gte: typing.Optional[dt.datetime] = None,
        created_at_lte: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_gte: typing.Optional[dt.datetime] = None,
        updated_at_lte: typing.Optional[dt.datetime] = None,
        issued_at_gt: typing.Optional[dt.datetime] = None,
        issued_at_lt: typing.Optional[dt.datetime] = None,
        issued_at_gte: typing.Optional[dt.datetime] = None,
        issued_at_lte: typing.Optional[dt.datetime] = None,
        status: typing.Optional[PurchaseOrderStatusEnum] = None,
        document_id: typing.Optional[str] = None,
        document_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        created_by: typing.Optional[str] = None,
        counterpart_id: typing.Optional[str] = None,
        counterpart_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        counterpart_name: typing.Optional[str] = None,
        currency: typing.Optional[CurrencyEnum] = None,
        currency_in: typing.Optional[typing.Union[CurrencyEnum, typing.Sequence[CurrencyEnum]]] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderPaginationResponse:
        """
        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Sort order (ascending by default). Typically used together with the `sort` parameter.

        limit : typing.Optional[int]
            The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.

        pagination_token : typing.Optional[str]
            A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

            If not specified, the first page of results will be returned.

        sort : typing.Optional[PurchaseOrderCursorFields]
            The field to sort the results by. Typically used together with the `order` parameter.

        created_at_gt : typing.Optional[dt.datetime]

        created_at_lt : typing.Optional[dt.datetime]

        created_at_gte : typing.Optional[dt.datetime]

        created_at_lte : typing.Optional[dt.datetime]

        updated_at_gt : typing.Optional[dt.datetime]

        updated_at_lt : typing.Optional[dt.datetime]

        updated_at_gte : typing.Optional[dt.datetime]

        updated_at_lte : typing.Optional[dt.datetime]

        issued_at_gt : typing.Optional[dt.datetime]

        issued_at_lt : typing.Optional[dt.datetime]

        issued_at_gte : typing.Optional[dt.datetime]

        issued_at_lte : typing.Optional[dt.datetime]

        status : typing.Optional[PurchaseOrderStatusEnum]

        document_id : typing.Optional[str]

        document_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        created_by : typing.Optional[str]

        counterpart_id : typing.Optional[str]

        counterpart_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        counterpart_name : typing.Optional[str]

        currency : typing.Optional[CurrencyEnum]

        currency_in : typing.Optional[typing.Union[CurrencyEnum, typing.Sequence[CurrencyEnum]]]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderPaginationResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.get()
        """
        _response = self._raw_client.get(
            order=order,
            limit=limit,
            pagination_token=pagination_token,
            sort=sort,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
            updated_at_gt=updated_at_gt,
            updated_at_lt=updated_at_lt,
            updated_at_gte=updated_at_gte,
            updated_at_lte=updated_at_lte,
            issued_at_gt=issued_at_gt,
            issued_at_lt=issued_at_lt,
            issued_at_gte=issued_at_gte,
            issued_at_lte=issued_at_lte,
            status=status,
            document_id=document_id,
            document_id_in=document_id_in,
            created_by=created_by,
            counterpart_id=counterpart_id,
            counterpart_id_in=counterpart_id_in,
            counterpart_name=counterpart_name,
            currency=currency,
            currency_in=currency_in,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        counterpart_id: str,
        currency: CurrencyEnum,
        items: typing.Sequence[PurchaseOrderItem],
        message: str,
        valid_for_days: int,
        counterpart_address_id: typing.Optional[str] = OMIT,
        entity_vat_id_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderResponseSchema:
        """
        Parameters
        ----------
        counterpart_id : str
            Counterpart unique ID.

        currency : CurrencyEnum
            The currency in which the price of the product is set. (all items need to have the same currency)

        items : typing.Sequence[PurchaseOrderItem]
            List of item to purchase

        message : str
            Msg which will be send to counterpart for who the purchase order is issued.

        valid_for_days : int
            Number of days for which purchase order is valid

        counterpart_address_id : typing.Optional[str]
            The ID of counterpart address object stored in counterparts service. If not provided, counterpart's default address is used.

        entity_vat_id_id : typing.Optional[str]
            Entity VAT ID identifier that applied to purchase order

        project_id : typing.Optional[str]
            Project ID of a purchase order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponseSchema
            Successful Response

        Examples
        --------
        from monite import Monite
        from monite import PurchaseOrderItem
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.create(counterpart_id='counterpart_id', currency="AED", items=[PurchaseOrderItem(currency="AED", name='name', price=1, quantity=1, unit='unit', vat_rate=1, )], message='message', valid_for_days=1, )
        """
        _response = self._raw_client.create(
            counterpart_id=counterpart_id,
            currency=currency,
            items=items,
            message=message,
            valid_for_days=valid_for_days,
            counterpart_address_id=counterpart_address_id,
            entity_vat_id_id=entity_vat_id_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    def get_variables(self, *, request_options: typing.Optional[RequestOptions] = None) -> VariablesObjectList:
        """
        Get a list of placeholders allowed to insert into an email template for customization

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VariablesObjectList
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.get_variables()
        """
        _response = self._raw_client.get_variables(request_options=request_options)
        return _response.data

    def get_by_id(
        self, purchase_order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PurchaseOrderResponseSchema:
        """
        Parameters
        ----------
        purchase_order_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponseSchema
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.get_by_id(purchase_order_id='purchase_order_id', )
        """
        _response = self._raw_client.get_by_id(purchase_order_id, request_options=request_options)
        return _response.data

    def delete_by_id(self, purchase_order_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        purchase_order_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.delete_by_id(purchase_order_id='purchase_order_id', )
        """
        _response = self._raw_client.delete_by_id(purchase_order_id, request_options=request_options)
        return _response.data

    def update_by_id(
        self,
        purchase_order_id: str,
        *,
        counterpart_address_id: typing.Optional[str] = OMIT,
        counterpart_id: typing.Optional[str] = OMIT,
        entity_vat_id_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[PurchaseOrderItem]] = OMIT,
        message: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        valid_for_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderResponseSchema:
        """
        Parameters
        ----------
        purchase_order_id : str

        counterpart_address_id : typing.Optional[str]
            The ID of counterpart address object stored in counterparts service. If not provided, counterpart's default address is used.

        counterpart_id : typing.Optional[str]
            Counterpart unique ID.

        entity_vat_id_id : typing.Optional[str]
            Entity VAT ID identifier that applied to purchase order

        items : typing.Optional[typing.Sequence[PurchaseOrderItem]]
            List of item to purchase

        message : typing.Optional[str]
            Msg which will be send to counterpart for who the purchase order is issued.

        project_id : typing.Optional[str]
            Project ID of a purchase order

        valid_for_days : typing.Optional[int]
            Number of days for which purchase order is valid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponseSchema
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.update_by_id(purchase_order_id='purchase_order_id', )
        """
        _response = self._raw_client.update_by_id(
            purchase_order_id,
            counterpart_address_id=counterpart_address_id,
            counterpart_id=counterpart_id,
            entity_vat_id_id=entity_vat_id_id,
            items=items,
            message=message,
            project_id=project_id,
            valid_for_days=valid_for_days,
            request_options=request_options,
        )
        return _response.data

    def preview_by_id(
        self,
        purchase_order_id: str,
        *,
        body_text: str,
        subject_text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderEmailPreviewResponse:
        """
        Parameters
        ----------
        purchase_order_id : str

        body_text : str

        subject_text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderEmailPreviewResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.preview_by_id(purchase_order_id='purchase_order_id', body_text='body_text', subject_text='subject_text', )
        """
        _response = self._raw_client.preview_by_id(
            purchase_order_id, body_text=body_text, subject_text=subject_text, request_options=request_options
        )
        return _response.data

    def send_by_id(
        self,
        purchase_order_id: str,
        *,
        body_text: str,
        subject_text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderEmailSentResponse:
        """
        Parameters
        ----------
        purchase_order_id : str

        body_text : str

        subject_text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderEmailSentResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.purchase_orders.send_by_id(purchase_order_id='purchase_order_id', body_text='body_text', subject_text='subject_text', )
        """
        _response = self._raw_client.send_by_id(
            purchase_order_id, body_text=body_text, subject_text=subject_text, request_options=request_options
        )
        return _response.data


class AsyncPurchaseOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPurchaseOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPurchaseOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPurchaseOrdersClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[PurchaseOrderCursorFields] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_gte: typing.Optional[dt.datetime] = None,
        created_at_lte: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_gte: typing.Optional[dt.datetime] = None,
        updated_at_lte: typing.Optional[dt.datetime] = None,
        issued_at_gt: typing.Optional[dt.datetime] = None,
        issued_at_lt: typing.Optional[dt.datetime] = None,
        issued_at_gte: typing.Optional[dt.datetime] = None,
        issued_at_lte: typing.Optional[dt.datetime] = None,
        status: typing.Optional[PurchaseOrderStatusEnum] = None,
        document_id: typing.Optional[str] = None,
        document_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        created_by: typing.Optional[str] = None,
        counterpart_id: typing.Optional[str] = None,
        counterpart_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        counterpart_name: typing.Optional[str] = None,
        currency: typing.Optional[CurrencyEnum] = None,
        currency_in: typing.Optional[typing.Union[CurrencyEnum, typing.Sequence[CurrencyEnum]]] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderPaginationResponse:
        """
        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Sort order (ascending by default). Typically used together with the `sort` parameter.

        limit : typing.Optional[int]
            The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.

        pagination_token : typing.Optional[str]
            A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

            If not specified, the first page of results will be returned.

        sort : typing.Optional[PurchaseOrderCursorFields]
            The field to sort the results by. Typically used together with the `order` parameter.

        created_at_gt : typing.Optional[dt.datetime]

        created_at_lt : typing.Optional[dt.datetime]

        created_at_gte : typing.Optional[dt.datetime]

        created_at_lte : typing.Optional[dt.datetime]

        updated_at_gt : typing.Optional[dt.datetime]

        updated_at_lt : typing.Optional[dt.datetime]

        updated_at_gte : typing.Optional[dt.datetime]

        updated_at_lte : typing.Optional[dt.datetime]

        issued_at_gt : typing.Optional[dt.datetime]

        issued_at_lt : typing.Optional[dt.datetime]

        issued_at_gte : typing.Optional[dt.datetime]

        issued_at_lte : typing.Optional[dt.datetime]

        status : typing.Optional[PurchaseOrderStatusEnum]

        document_id : typing.Optional[str]

        document_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        created_by : typing.Optional[str]

        counterpart_id : typing.Optional[str]

        counterpart_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        counterpart_name : typing.Optional[str]

        currency : typing.Optional[CurrencyEnum]

        currency_in : typing.Optional[typing.Union[CurrencyEnum, typing.Sequence[CurrencyEnum]]]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderPaginationResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.purchase_orders.get()
        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            order=order,
            limit=limit,
            pagination_token=pagination_token,
            sort=sort,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
            updated_at_gt=updated_at_gt,
            updated_at_lt=updated_at_lt,
            updated_at_gte=updated_at_gte,
            updated_at_lte=updated_at_lte,
            issued_at_gt=issued_at_gt,
            issued_at_lt=issued_at_lt,
            issued_at_gte=issued_at_gte,
            issued_at_lte=issued_at_lte,
            status=status,
            document_id=document_id,
            document_id_in=document_id_in,
            created_by=created_by,
            counterpart_id=counterpart_id,
            counterpart_id_in=counterpart_id_in,
            counterpart_name=counterpart_name,
            currency=currency,
            currency_in=currency_in,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        counterpart_id: str,
        currency: CurrencyEnum,
        items: typing.Sequence[PurchaseOrderItem],
        message: str,
        valid_for_days: int,
        counterpart_address_id: typing.Optional[str] = OMIT,
        entity_vat_id_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderResponseSchema:
        """
        Parameters
        ----------
        counterpart_id : str
            Counterpart unique ID.

        currency : CurrencyEnum
            The currency in which the price of the product is set. (all items need to have the same currency)

        items : typing.Sequence[PurchaseOrderItem]
            List of item to purchase

        message : str
            Msg which will be send to counterpart for who the purchase order is issued.

        valid_for_days : int
            Number of days for which purchase order is valid

        counterpart_address_id : typing.Optional[str]
            The ID of counterpart address object stored in counterparts service. If not provided, counterpart's default address is used.

        entity_vat_id_id : typing.Optional[str]
            Entity VAT ID identifier that applied to purchase order

        project_id : typing.Optional[str]
            Project ID of a purchase order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponseSchema
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        from monite import PurchaseOrderItem
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.purchase_orders.create(counterpart_id='counterpart_id', currency="AED", items=[PurchaseOrderItem(currency="AED", name='name', price=1, quantity=1, unit='unit', vat_rate=1, )], message='message', valid_for_days=1, )
        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            counterpart_id=counterpart_id,
            currency=currency,
            items=items,
            message=message,
            valid_for_days=valid_for_days,
            counterpart_address_id=counterpart_address_id,
            entity_vat_id_id=entity_vat_id_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    async def get_variables(self, *, request_options: typing.Optional[RequestOptions] = None) -> VariablesObjectList:
        """
        Get a list of placeholders allowed to insert into an email template for customization

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VariablesObjectList
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.purchase_orders.get_variables()
        asyncio.run(main())
        """
        _response = await self._raw_client.get_variables(request_options=request_options)
        return _response.data

    async def get_by_id(
        self, purchase_order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PurchaseOrderResponseSchema:
        """
        Parameters
        ----------
        purchase_order_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponseSchema
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.purchase_orders.get_by_id(purchase_order_id='purchase_order_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id(purchase_order_id, request_options=request_options)
        return _response.data

    async def delete_by_id(
        self, purchase_order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        purchase_order_id : str

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
            await client.purchase_orders.delete_by_id(purchase_order_id='purchase_order_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.delete_by_id(purchase_order_id, request_options=request_options)
        return _response.data

    async def update_by_id(
        self,
        purchase_order_id: str,
        *,
        counterpart_address_id: typing.Optional[str] = OMIT,
        counterpart_id: typing.Optional[str] = OMIT,
        entity_vat_id_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[PurchaseOrderItem]] = OMIT,
        message: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        valid_for_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderResponseSchema:
        """
        Parameters
        ----------
        purchase_order_id : str

        counterpart_address_id : typing.Optional[str]
            The ID of counterpart address object stored in counterparts service. If not provided, counterpart's default address is used.

        counterpart_id : typing.Optional[str]
            Counterpart unique ID.

        entity_vat_id_id : typing.Optional[str]
            Entity VAT ID identifier that applied to purchase order

        items : typing.Optional[typing.Sequence[PurchaseOrderItem]]
            List of item to purchase

        message : typing.Optional[str]
            Msg which will be send to counterpart for who the purchase order is issued.

        project_id : typing.Optional[str]
            Project ID of a purchase order

        valid_for_days : typing.Optional[int]
            Number of days for which purchase order is valid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponseSchema
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.purchase_orders.update_by_id(purchase_order_id='purchase_order_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.update_by_id(
            purchase_order_id,
            counterpart_address_id=counterpart_address_id,
            counterpart_id=counterpart_id,
            entity_vat_id_id=entity_vat_id_id,
            items=items,
            message=message,
            project_id=project_id,
            valid_for_days=valid_for_days,
            request_options=request_options,
        )
        return _response.data

    async def preview_by_id(
        self,
        purchase_order_id: str,
        *,
        body_text: str,
        subject_text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderEmailPreviewResponse:
        """
        Parameters
        ----------
        purchase_order_id : str

        body_text : str

        subject_text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderEmailPreviewResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.purchase_orders.preview_by_id(purchase_order_id='purchase_order_id', body_text='body_text', subject_text='subject_text', )
        asyncio.run(main())
        """
        _response = await self._raw_client.preview_by_id(
            purchase_order_id, body_text=body_text, subject_text=subject_text, request_options=request_options
        )
        return _response.data

    async def send_by_id(
        self,
        purchase_order_id: str,
        *,
        body_text: str,
        subject_text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderEmailSentResponse:
        """
        Parameters
        ----------
        purchase_order_id : str

        body_text : str

        subject_text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderEmailSentResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.purchase_orders.send_by_id(purchase_order_id='purchase_order_id', body_text='body_text', subject_text='subject_text', )
        asyncio.run(main())
        """
        _response = await self._raw_client.send_by_id(
            purchase_order_id, body_text=body_text, subject_text=subject_text, request_options=request_options
        )
        return _response.data
