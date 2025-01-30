# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.order_enum import OrderEnum
from ..types.payment_record_cursor_fields import PaymentRecordCursorFields
from ..core.request_options import RequestOptions
from ..types.payment_record_response_list import PaymentRecordResponseList
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.currency_enum import CurrencyEnum
from ..types.payment_record_object_request import PaymentRecordObjectRequest
import datetime as dt
from ..types.payment_record_response import PaymentRecordResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PaymentRecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[PaymentRecordCursorFields] = None,
        is_external: typing.Optional[bool] = None,
        object_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentRecordResponseList:
        """
        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[PaymentRecordCursorFields]
            Allowed sort fields

        is_external : typing.Optional[bool]

        object_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRecordResponseList
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.payment_records.get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "payment_records",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "pagination_token": pagination_token,
                "sort": sort,
                "is_external": is_external,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaymentRecordResponseList,
                    parse_obj_as(
                        type_=PaymentRecordResponseList,  # type: ignore
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
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        amount: int,
        currency: CurrencyEnum,
        object: PaymentRecordObjectRequest,
        paid_at: dt.datetime,
        payment_intent_id: str,
        entity_user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentRecordResponse:
        """
        Parameters
        ----------
        amount : int

        currency : CurrencyEnum

        object : PaymentRecordObjectRequest

        paid_at : dt.datetime

        payment_intent_id : str

        entity_user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRecordResponse
            Successful Response

        Examples
        --------
        import datetime

        from monite import Monite, PaymentRecordObjectRequest

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.payment_records.create(
            amount=1,
            currency="AED",
            object=PaymentRecordObjectRequest(
                id="id",
                type="receivable",
            ),
            paid_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            payment_intent_id="payment_intent_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "payment_records",
            method="POST",
            json={
                "amount": amount,
                "currency": currency,
                "entity_user_id": entity_user_id,
                "object": convert_and_respect_annotation_metadata(
                    object_=object, annotation=PaymentRecordObjectRequest, direction="write"
                ),
                "paid_at": paid_at,
                "payment_intent_id": payment_intent_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaymentRecordResponse,
                    parse_obj_as(
                        type_=PaymentRecordResponse,  # type: ignore
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
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_by_id(
        self, payment_record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaymentRecordResponse:
        """
        Parameters
        ----------
        payment_record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRecordResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.payment_records.get_by_id(
            payment_record_id="payment_record_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"payment_records/{jsonable_encoder(payment_record_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaymentRecordResponse,
                    parse_obj_as(
                        type_=PaymentRecordResponse,  # type: ignore
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
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPaymentRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[PaymentRecordCursorFields] = None,
        is_external: typing.Optional[bool] = None,
        object_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentRecordResponseList:
        """
        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[PaymentRecordCursorFields]
            Allowed sort fields

        is_external : typing.Optional[bool]

        object_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRecordResponseList
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
            await client.payment_records.get()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "payment_records",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "pagination_token": pagination_token,
                "sort": sort,
                "is_external": is_external,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaymentRecordResponseList,
                    parse_obj_as(
                        type_=PaymentRecordResponseList,  # type: ignore
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
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        amount: int,
        currency: CurrencyEnum,
        object: PaymentRecordObjectRequest,
        paid_at: dt.datetime,
        payment_intent_id: str,
        entity_user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentRecordResponse:
        """
        Parameters
        ----------
        amount : int

        currency : CurrencyEnum

        object : PaymentRecordObjectRequest

        paid_at : dt.datetime

        payment_intent_id : str

        entity_user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRecordResponse
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from monite import AsyncMonite, PaymentRecordObjectRequest

        client = AsyncMonite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payment_records.create(
                amount=1,
                currency="AED",
                object=PaymentRecordObjectRequest(
                    id="id",
                    type="receivable",
                ),
                paid_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                payment_intent_id="payment_intent_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "payment_records",
            method="POST",
            json={
                "amount": amount,
                "currency": currency,
                "entity_user_id": entity_user_id,
                "object": convert_and_respect_annotation_metadata(
                    object_=object, annotation=PaymentRecordObjectRequest, direction="write"
                ),
                "paid_at": paid_at,
                "payment_intent_id": payment_intent_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaymentRecordResponse,
                    parse_obj_as(
                        type_=PaymentRecordResponse,  # type: ignore
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
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_by_id(
        self, payment_record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaymentRecordResponse:
        """
        Parameters
        ----------
        payment_record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRecordResponse
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
            await client.payment_records.get_by_id(
                payment_record_id="payment_record_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"payment_records/{jsonable_encoder(payment_record_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaymentRecordResponse,
                    parse_obj_as(
                        type_=PaymentRecordResponse,  # type: ignore
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
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
