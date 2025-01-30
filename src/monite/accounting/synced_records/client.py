# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
from ...types.object_match_types import ObjectMatchTypes
import typing
from ...types.order_enum import OrderEnum
from ...types.sync_record_cursor_fields import SyncRecordCursorFields
import datetime as dt
from ...core.request_options import RequestOptions
from ...types.sync_record_resource_list import SyncRecordResourceList
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from ...errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.sync_record_resource import SyncRecordResource
from ...core.jsonable_encoder import jsonable_encoder
from ...core.client_wrapper import AsyncClientWrapper


class SyncedRecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        object_type: ObjectMatchTypes,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[SyncRecordCursorFields] = None,
        object_id: typing.Optional[str] = None,
        object_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_gte: typing.Optional[dt.datetime] = None,
        created_at_lte: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_gte: typing.Optional[dt.datetime] = None,
        updated_at_lte: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncRecordResourceList:
        """
        Get synchronized records

        Parameters
        ----------
        object_type : ObjectMatchTypes

        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[SyncRecordCursorFields]
            Allowed sort fields

        object_id : typing.Optional[str]

        object_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        created_at_gt : typing.Optional[dt.datetime]

        created_at_lt : typing.Optional[dt.datetime]

        created_at_gte : typing.Optional[dt.datetime]

        created_at_lte : typing.Optional[dt.datetime]

        updated_at_gt : typing.Optional[dt.datetime]

        updated_at_lt : typing.Optional[dt.datetime]

        updated_at_gte : typing.Optional[dt.datetime]

        updated_at_lte : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncRecordResourceList
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.accounting.synced_records.get(
            object_type="product",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting_synced_records",
            method="GET",
            params={
                "object_type": object_type,
                "order": order,
                "limit": limit,
                "pagination_token": pagination_token,
                "sort": sort,
                "object_id": object_id,
                "object_id__in": object_id_in,
                "created_at__gt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "created_at__lt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "created_at__gte": serialize_datetime(created_at_gte) if created_at_gte is not None else None,
                "created_at__lte": serialize_datetime(created_at_lte) if created_at_lte is not None else None,
                "updated_at__gt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updated_at__lt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updated_at__gte": serialize_datetime(updated_at_gte) if updated_at_gte is not None else None,
                "updated_at__lte": serialize_datetime(updated_at_lte) if updated_at_lte is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SyncRecordResourceList,
                    parse_obj_as(
                        type_=SyncRecordResourceList,  # type: ignore
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
        self, synced_record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncRecordResource:
        """
        Get synchronized record by id

        Parameters
        ----------
        synced_record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncRecordResource
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.accounting.synced_records.get_by_id(
            synced_record_id="synced_record_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting_synced_records/{jsonable_encoder(synced_record_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SyncRecordResource,
                    parse_obj_as(
                        type_=SyncRecordResource,  # type: ignore
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

    def push_by_id(
        self, synced_record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncRecordResource:
        """
        Push object to the accounting system manually

        Parameters
        ----------
        synced_record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncRecordResource
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.accounting.synced_records.push_by_id(
            synced_record_id="synced_record_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting_synced_records/{jsonable_encoder(synced_record_id)}/push",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SyncRecordResource,
                    parse_obj_as(
                        type_=SyncRecordResource,  # type: ignore
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


class AsyncSyncedRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        object_type: ObjectMatchTypes,
        order: typing.Optional[OrderEnum] = None,
        limit: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        sort: typing.Optional[SyncRecordCursorFields] = None,
        object_id: typing.Optional[str] = None,
        object_id_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_gte: typing.Optional[dt.datetime] = None,
        created_at_lte: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_gte: typing.Optional[dt.datetime] = None,
        updated_at_lte: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncRecordResourceList:
        """
        Get synchronized records

        Parameters
        ----------
        object_type : ObjectMatchTypes

        order : typing.Optional[OrderEnum]
            Order by

        limit : typing.Optional[int]
            Max is 100

        pagination_token : typing.Optional[str]
            A token, obtained from previous page. Prior over other filters

        sort : typing.Optional[SyncRecordCursorFields]
            Allowed sort fields

        object_id : typing.Optional[str]

        object_id_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        created_at_gt : typing.Optional[dt.datetime]

        created_at_lt : typing.Optional[dt.datetime]

        created_at_gte : typing.Optional[dt.datetime]

        created_at_lte : typing.Optional[dt.datetime]

        updated_at_gt : typing.Optional[dt.datetime]

        updated_at_lt : typing.Optional[dt.datetime]

        updated_at_gte : typing.Optional[dt.datetime]

        updated_at_lte : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncRecordResourceList
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
            await client.accounting.synced_records.get(
                object_type="product",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting_synced_records",
            method="GET",
            params={
                "object_type": object_type,
                "order": order,
                "limit": limit,
                "pagination_token": pagination_token,
                "sort": sort,
                "object_id": object_id,
                "object_id__in": object_id_in,
                "created_at__gt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "created_at__lt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "created_at__gte": serialize_datetime(created_at_gte) if created_at_gte is not None else None,
                "created_at__lte": serialize_datetime(created_at_lte) if created_at_lte is not None else None,
                "updated_at__gt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updated_at__lt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updated_at__gte": serialize_datetime(updated_at_gte) if updated_at_gte is not None else None,
                "updated_at__lte": serialize_datetime(updated_at_lte) if updated_at_lte is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SyncRecordResourceList,
                    parse_obj_as(
                        type_=SyncRecordResourceList,  # type: ignore
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
        self, synced_record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncRecordResource:
        """
        Get synchronized record by id

        Parameters
        ----------
        synced_record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncRecordResource
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
            await client.accounting.synced_records.get_by_id(
                synced_record_id="synced_record_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting_synced_records/{jsonable_encoder(synced_record_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SyncRecordResource,
                    parse_obj_as(
                        type_=SyncRecordResource,  # type: ignore
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

    async def push_by_id(
        self, synced_record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncRecordResource:
        """
        Push object to the accounting system manually

        Parameters
        ----------
        synced_record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncRecordResource
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
            await client.accounting.synced_records.push_by_id(
                synced_record_id="synced_record_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting_synced_records/{jsonable_encoder(synced_record_id)}/push",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SyncRecordResource,
                    parse_obj_as(
                        type_=SyncRecordResource,  # type: ignore
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
