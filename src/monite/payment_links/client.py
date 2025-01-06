# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.monite_all_payment_methods_types import MoniteAllPaymentMethodsTypes
from ..types.payment_account_object import PaymentAccountObject
from ..types.currency_enum import CurrencyEnum
import datetime as dt
from ..types.invoice import Invoice
from ..types.payment_object import PaymentObject
from ..core.request_options import RequestOptions
from ..types.public_payment_link_response import PublicPaymentLinkResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..errors.internal_server_error import InternalServerError
from ..types.error_schema_response import ErrorSchemaResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PaymentLinksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        payment_methods: typing.Sequence[MoniteAllPaymentMethodsTypes],
        recipient: PaymentAccountObject,
        amount: typing.Optional[int] = OMIT,
        currency: typing.Optional[CurrencyEnum] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        invoice: typing.Optional[Invoice] = OMIT,
        object: typing.Optional[PaymentObject] = OMIT,
        payment_reference: typing.Optional[str] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublicPaymentLinkResponse:
        """
        Parameters
        ----------
        payment_methods : typing.Sequence[MoniteAllPaymentMethodsTypes]

        recipient : PaymentAccountObject

        amount : typing.Optional[int]
            The payment amount in [minor units](https://docs.monite.com/docs/currencies#minor-units). Required if `object` is not specified.

        currency : typing.Optional[CurrencyEnum]
            The payment currency. Required if `object` is not specified.

        expires_at : typing.Optional[dt.datetime]

        invoice : typing.Optional[Invoice]
            An object containing information about the invoice being paid. Used only if `object` is not specified.

        object : typing.Optional[PaymentObject]
            If the invoice being paid is a payable or receivable stored in Monite, provide the `object` object containing the invoice type and ID. Otherwise, use the `amount`, `currency`, `payment_reference`, and (optionally) `invoice` fields to specify the invoice-related data.

        payment_reference : typing.Optional[str]
            A payment reference number that the recipient can use to identify the payer or purpose of the transaction. Required if `object` is not specified.

        return_url : typing.Optional[str]
            The URL where to redirect the payer after the payment. If `return_url` is specified, then after the payment is completed the payment page will display the "Return to platform" link that navigates to this URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicPaymentLinkResponse
            Successful Response

        Examples
        --------
        from monite import Monite, PaymentAccountObject

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.payment_links.create(
            payment_methods=["sepa_credit"],
            recipient=PaymentAccountObject(
                id="id",
                type="entity",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "payment_links",
            method="POST",
            json={
                "amount": amount,
                "currency": currency,
                "expires_at": expires_at,
                "invoice": convert_and_respect_annotation_metadata(
                    object_=invoice, annotation=Invoice, direction="write"
                ),
                "object": convert_and_respect_annotation_metadata(
                    object_=object, annotation=PaymentObject, direction="write"
                ),
                "payment_methods": payment_methods,
                "payment_reference": payment_reference,
                "recipient": convert_and_respect_annotation_metadata(
                    object_=recipient, annotation=PaymentAccountObject, direction="write"
                ),
                "return_url": return_url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PublicPaymentLinkResponse,
                    parse_obj_as(
                        type_=PublicPaymentLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_by_id(
        self, payment_link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublicPaymentLinkResponse:
        """
        Parameters
        ----------
        payment_link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicPaymentLinkResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.payment_links.get_by_id(
            payment_link_id="payment_link_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"payment_links/{jsonable_encoder(payment_link_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PublicPaymentLinkResponse,
                    parse_obj_as(
                        type_=PublicPaymentLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def expire_by_id(
        self, payment_link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublicPaymentLinkResponse:
        """
        Parameters
        ----------
        payment_link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicPaymentLinkResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.payment_links.expire_by_id(
            payment_link_id="payment_link_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"payment_links/{jsonable_encoder(payment_link_id)}/expire",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PublicPaymentLinkResponse,
                    parse_obj_as(
                        type_=PublicPaymentLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPaymentLinksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        payment_methods: typing.Sequence[MoniteAllPaymentMethodsTypes],
        recipient: PaymentAccountObject,
        amount: typing.Optional[int] = OMIT,
        currency: typing.Optional[CurrencyEnum] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        invoice: typing.Optional[Invoice] = OMIT,
        object: typing.Optional[PaymentObject] = OMIT,
        payment_reference: typing.Optional[str] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublicPaymentLinkResponse:
        """
        Parameters
        ----------
        payment_methods : typing.Sequence[MoniteAllPaymentMethodsTypes]

        recipient : PaymentAccountObject

        amount : typing.Optional[int]
            The payment amount in [minor units](https://docs.monite.com/docs/currencies#minor-units). Required if `object` is not specified.

        currency : typing.Optional[CurrencyEnum]
            The payment currency. Required if `object` is not specified.

        expires_at : typing.Optional[dt.datetime]

        invoice : typing.Optional[Invoice]
            An object containing information about the invoice being paid. Used only if `object` is not specified.

        object : typing.Optional[PaymentObject]
            If the invoice being paid is a payable or receivable stored in Monite, provide the `object` object containing the invoice type and ID. Otherwise, use the `amount`, `currency`, `payment_reference`, and (optionally) `invoice` fields to specify the invoice-related data.

        payment_reference : typing.Optional[str]
            A payment reference number that the recipient can use to identify the payer or purpose of the transaction. Required if `object` is not specified.

        return_url : typing.Optional[str]
            The URL where to redirect the payer after the payment. If `return_url` is specified, then after the payment is completed the payment page will display the "Return to platform" link that navigates to this URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicPaymentLinkResponse
            Successful Response

        Examples
        --------
        import asyncio

        from monite import AsyncMonite, PaymentAccountObject

        client = AsyncMonite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payment_links.create(
                payment_methods=["sepa_credit"],
                recipient=PaymentAccountObject(
                    id="id",
                    type="entity",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "payment_links",
            method="POST",
            json={
                "amount": amount,
                "currency": currency,
                "expires_at": expires_at,
                "invoice": convert_and_respect_annotation_metadata(
                    object_=invoice, annotation=Invoice, direction="write"
                ),
                "object": convert_and_respect_annotation_metadata(
                    object_=object, annotation=PaymentObject, direction="write"
                ),
                "payment_methods": payment_methods,
                "payment_reference": payment_reference,
                "recipient": convert_and_respect_annotation_metadata(
                    object_=recipient, annotation=PaymentAccountObject, direction="write"
                ),
                "return_url": return_url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PublicPaymentLinkResponse,
                    parse_obj_as(
                        type_=PublicPaymentLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_by_id(
        self, payment_link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublicPaymentLinkResponse:
        """
        Parameters
        ----------
        payment_link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicPaymentLinkResponse
            Successful Response

        Examples
        --------
        import asyncio

        from monite import AsyncMonite

        client = AsyncMonite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payment_links.get_by_id(
                payment_link_id="payment_link_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"payment_links/{jsonable_encoder(payment_link_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PublicPaymentLinkResponse,
                    parse_obj_as(
                        type_=PublicPaymentLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def expire_by_id(
        self, payment_link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublicPaymentLinkResponse:
        """
        Parameters
        ----------
        payment_link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicPaymentLinkResponse
            Successful Response

        Examples
        --------
        import asyncio

        from monite import AsyncMonite

        client = AsyncMonite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payment_links.expire_by_id(
                payment_link_id="payment_link_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"payment_links/{jsonable_encoder(payment_link_id)}/expire",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PublicPaymentLinkResponse,
                    parse_obj_as(
                        type_=PublicPaymentLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
