# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...types.order_enum import OrderEnum
from ...types.ledger_account_cursor_fields import LedgerAccountCursorFields
from ...core.request_options import RequestOptions
from ...types.ledger_account_list_response import LedgerAccountListResponse
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from ...errors.internal_server_error import InternalServerError
from ...types.error_schema_response import ErrorSchemaResponse
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.ledger_account_response import LedgerAccountResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.client_wrapper import AsyncClientWrapper


class LedgerAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[LedgerAccountCursorFields] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LedgerAccountListResponse:
        """
        Get all ledger accounts

        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[LedgerAccountCursorFields]
            Allowed sort fields

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LedgerAccountListResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.accounting.ledger_accounts.get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ledger_accounts",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "pagination_token": pagination_token,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LedgerAccountListResponse,
                    parse_obj_as(
                        type_=LedgerAccountListResponse,  # type: ignore
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
        self, ledger_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LedgerAccountResponse:
        """
        Get ledger account by id

        Parameters
        ----------
        ledger_account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LedgerAccountResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.accounting.ledger_accounts.get_by_id(
            ledger_account_id="ledger_account_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ledger_accounts/{jsonable_encoder(ledger_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LedgerAccountResponse,
                    parse_obj_as(
                        type_=LedgerAccountResponse,  # type: ignore
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


class AsyncLedgerAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[LedgerAccountCursorFields] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LedgerAccountListResponse:
        """
        Get all ledger accounts

        Parameters
        ----------
        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[LedgerAccountCursorFields]
            Allowed sort fields

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LedgerAccountListResponse
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
            await client.accounting.ledger_accounts.get()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ledger_accounts",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "pagination_token": pagination_token,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LedgerAccountListResponse,
                    parse_obj_as(
                        type_=LedgerAccountListResponse,  # type: ignore
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
        self, ledger_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LedgerAccountResponse:
        """
        Get ledger account by id

        Parameters
        ----------
        ledger_account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LedgerAccountResponse
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
            await client.accounting.ledger_accounts.get_by_id(
                ledger_account_id="ledger_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ledger_accounts/{jsonable_encoder(ledger_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LedgerAccountResponse,
                    parse_obj_as(
                        type_=LedgerAccountResponse,  # type: ignore
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
