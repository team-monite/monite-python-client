# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.message_response import MessageResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..errors.internal_server_error import InternalServerError
from ..types.error_schema_response import ErrorSchemaResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.grant_type import GrantType
from ..types.access_token_response import AccessTokenResponse
from ..errors.unauthorized_error import UnauthorizedError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AccessTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def revoke(
        self, *, client_id: str, client_secret: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        Revoke an existing token immediately.

        Parameters
        ----------
        client_id : str

        client_secret : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.access_tokens.revoke(
            client_id="client_id",
            client_secret="client_secret",
            token="token",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/revoke",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "token": token,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,  # type: ignore
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

    def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: GrantType,
        entity_user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessTokenResponse:
        """
        Create a new access token based on client ID and client secret.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : GrantType

        entity_user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessTokenResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.access_tokens.create(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="client_credentials",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/token",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "entity_user_id": entity_user_id,
                "grant_type": grant_type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AccessTokenResponse,
                    parse_obj_as(
                        type_=AccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
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


class AsyncAccessTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def revoke(
        self, *, client_id: str, client_secret: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageResponse:
        """
        Revoke an existing token immediately.

        Parameters
        ----------
        client_id : str

        client_secret : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
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
            await client.access_tokens.revoke(
                client_id="client_id",
                client_secret="client_secret",
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/revoke",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "token": token,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,  # type: ignore
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

    async def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: GrantType,
        entity_user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessTokenResponse:
        """
        Create a new access token based on client ID and client secret.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : GrantType

        entity_user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessTokenResponse
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
            await client.access_tokens.create(
                client_id="client_id",
                client_secret="client_secret",
                grant_type="client_credentials",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/token",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "entity_user_id": entity_user_id,
                "grant_type": grant_type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AccessTokenResponse,
                    parse_obj_as(
                        type_=AccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        ErrorSchemaResponse,
                        parse_obj_as(
                            type_=ErrorSchemaResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
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
