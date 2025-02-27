# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.domain_list_response import DomainListResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.forbidden_error import ForbiddenError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.domain_response import DomainResponse
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..types.verify_response import VerifyResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MailboxDomainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> DomainListResponse:
        """
        Get all domains owned by partner_id

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DomainListResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.mailbox_domains.get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "mailbox_domains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DomainListResponse,
                    parse_obj_as(
                        type_=DomainListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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

    def create(self, *, domain: str, request_options: typing.Optional[RequestOptions] = None) -> DomainResponse:
        """
        Create domain for the partner_id

        Parameters
        ----------
        domain : str
            The domain name, such as `mail.mycompany.com`. Can contain only alphanumeric characters (A..Z a..z 0..9), dots (.), and hyphens (-). Each segment of the domain name must start and end with either a letter or a digit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DomainResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.mailbox_domains.create(
            domain="domain",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "mailbox_domains",
            method="POST",
            json={
                "domain": domain,
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
                    DomainResponse,
                    parse_obj_as(
                        type_=DomainResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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

    def delete_by_id(self, domain_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete domain for the partner_id

        Parameters
        ----------
        domain_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.mailbox_domains.delete_by_id(
            domain_id="domain_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mailbox_domains/{jsonable_encoder(domain_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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

    def verify_by_id(
        self, domain_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyResponse:
        """
        Verify domain for the partner_id

        Parameters
        ----------
        domain_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyResponse
            Successful Response

        Examples
        --------
        from monite import Monite

        client = Monite(
            monite_version="YOUR_MONITE_VERSION",
            monite_entity_id="YOUR_MONITE_ENTITY_ID",
            token="YOUR_TOKEN",
        )
        client.mailbox_domains.verify_by_id(
            domain_id="domain_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mailbox_domains/{jsonable_encoder(domain_id)}/verify",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VerifyResponse,
                    parse_obj_as(
                        type_=VerifyResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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


class AsyncMailboxDomainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> DomainListResponse:
        """
        Get all domains owned by partner_id

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DomainListResponse
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
            await client.mailbox_domains.get()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mailbox_domains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DomainListResponse,
                    parse_obj_as(
                        type_=DomainListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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

    async def create(self, *, domain: str, request_options: typing.Optional[RequestOptions] = None) -> DomainResponse:
        """
        Create domain for the partner_id

        Parameters
        ----------
        domain : str
            The domain name, such as `mail.mycompany.com`. Can contain only alphanumeric characters (A..Z a..z 0..9), dots (.), and hyphens (-). Each segment of the domain name must start and end with either a letter or a digit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DomainResponse
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
            await client.mailbox_domains.create(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mailbox_domains",
            method="POST",
            json={
                "domain": domain,
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
                    DomainResponse,
                    parse_obj_as(
                        type_=DomainResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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

    async def delete_by_id(self, domain_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete domain for the partner_id

        Parameters
        ----------
        domain_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

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
            await client.mailbox_domains.delete_by_id(
                domain_id="domain_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mailbox_domains/{jsonable_encoder(domain_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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

    async def verify_by_id(
        self, domain_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyResponse:
        """
        Verify domain for the partner_id

        Parameters
        ----------
        domain_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyResponse
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
            await client.mailbox_domains.verify_by_id(
                domain_id="domain_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mailbox_domains/{jsonable_encoder(domain_id)}/verify",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VerifyResponse,
                    parse_obj_as(
                        type_=VerifyResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
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
