# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from ...types.accounting_payable_list import AccountingPayableList
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from ...errors.internal_server_error import InternalServerError
from ...types.error_schema_response import ErrorSchemaResponse
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.accounting_payable import AccountingPayable
from ...core.jsonable_encoder import jsonable_encoder
from ...core.client_wrapper import AsyncClientWrapper


class PayablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingPayableList:
        """
        Returns a list of accounts payable invoices (bills) that exist in the entity's accounting system. This requires that an accounting connection has been previously established. Refer to the [Accounting integration guide](https://docs.monite.com/accounting/integration/index) for details.

        This endpoint only provides read-only access to the accounting system's data but does not pull those payables into Monite. You can use it to review the data in the accounting system and find out which of those payables already exist or do not exist in Monite.

        Data is actual as of the date and time of the last accounting synchronization, which is specified by the `last_pull` value in the response from `GET /accounting_connections/{connection_id}`. To make sure you are accessing the most up-to-date accounting data, you can use `POST /accounting_connections/{connection_id}/sync` to trigger on-demand synchronization before getting the list of payables.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of results per page.

        offset : typing.Optional[int]
            Number of results to skip before selecting items to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingPayableList
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.accounting.payables.get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/payables",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AccountingPayableList,
                    parse_obj_as(
                        type_=AccountingPayableList,  # type: ignore
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
        self, payable_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingPayable:
        """
        Returns information about an individual payable invoice (bill) that exists in the entity's accounting system. This payable may or may not also exist in Monite.

        Parameters
        ----------
        payable_id : str
            An internal ID of the payable invoice (bill) in the accounting system. You can get these IDs from `GET /accounting/payables`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingPayable
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.accounting.payables.get_by_id(
            payable_id="payable_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/payables/{jsonable_encoder(payable_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AccountingPayable,
                    parse_obj_as(
                        type_=AccountingPayable,  # type: ignore
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


class AsyncPayablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingPayableList:
        """
        Returns a list of accounts payable invoices (bills) that exist in the entity's accounting system. This requires that an accounting connection has been previously established. Refer to the [Accounting integration guide](https://docs.monite.com/accounting/integration/index) for details.

        This endpoint only provides read-only access to the accounting system's data but does not pull those payables into Monite. You can use it to review the data in the accounting system and find out which of those payables already exist or do not exist in Monite.

        Data is actual as of the date and time of the last accounting synchronization, which is specified by the `last_pull` value in the response from `GET /accounting_connections/{connection_id}`. To make sure you are accessing the most up-to-date accounting data, you can use `POST /accounting_connections/{connection_id}/sync` to trigger on-demand synchronization before getting the list of payables.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of results per page.

        offset : typing.Optional[int]
            Number of results to skip before selecting items to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingPayableList
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
            await client.accounting.payables.get()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/payables",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AccountingPayableList,
                    parse_obj_as(
                        type_=AccountingPayableList,  # type: ignore
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
        self, payable_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingPayable:
        """
        Returns information about an individual payable invoice (bill) that exists in the entity's accounting system. This payable may or may not also exist in Monite.

        Parameters
        ----------
        payable_id : str
            An internal ID of the payable invoice (bill) in the accounting system. You can get these IDs from `GET /accounting/payables`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingPayable
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
            await client.accounting.payables.get_by_id(
                payable_id="payable_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/payables/{jsonable_encoder(payable_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AccountingPayable,
                    parse_obj_as(
                        type_=AccountingPayable,  # type: ignore
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
