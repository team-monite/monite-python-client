# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.conflict_error import ConflictError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.business_profile_input import BusinessProfileInput
from ...types.entity_onboarding_data_response import EntityOnboardingDataResponse
from ...types.ownership_declaration_input import OwnershipDeclarationInput
from ...types.terms_of_service_acceptance_input import TermsOfServiceAcceptanceInput

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawOnboardingDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, entity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntityOnboardingDataResponse]:
        """
        Parameters
        ----------
        entity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityOnboardingDataResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entities/{jsonable_encoder(entity_id)}/onboarding_data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityOnboardingDataResponse,
                    parse_obj_as(
                        type_=EntityOnboardingDataResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        entity_id: str,
        *,
        business_profile: typing.Optional[BusinessProfileInput] = OMIT,
        ownership_declaration: typing.Optional[OwnershipDeclarationInput] = OMIT,
        tos_acceptance: typing.Optional[TermsOfServiceAcceptanceInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityOnboardingDataResponse]:
        """
        Parameters
        ----------
        entity_id : str

        business_profile : typing.Optional[BusinessProfileInput]
            Business information about the entity.

        ownership_declaration : typing.Optional[OwnershipDeclarationInput]
            Used to attest that the beneficial owner information provided is both current and correct.

        tos_acceptance : typing.Optional[TermsOfServiceAcceptanceInput]
            Details on the entity's acceptance of the service agreement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityOnboardingDataResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entities/{jsonable_encoder(entity_id)}/onboarding_data",
            method="PATCH",
            json={
                "business_profile": convert_and_respect_annotation_metadata(
                    object_=business_profile, annotation=BusinessProfileInput, direction="write"
                ),
                "ownership_declaration": convert_and_respect_annotation_metadata(
                    object_=ownership_declaration, annotation=OwnershipDeclarationInput, direction="write"
                ),
                "tos_acceptance": convert_and_respect_annotation_metadata(
                    object_=tos_acceptance, annotation=TermsOfServiceAcceptanceInput, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityOnboardingDataResponse,
                    parse_obj_as(
                        type_=EntityOnboardingDataResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawOnboardingDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, entity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntityOnboardingDataResponse]:
        """
        Parameters
        ----------
        entity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityOnboardingDataResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entities/{jsonable_encoder(entity_id)}/onboarding_data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityOnboardingDataResponse,
                    parse_obj_as(
                        type_=EntityOnboardingDataResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        entity_id: str,
        *,
        business_profile: typing.Optional[BusinessProfileInput] = OMIT,
        ownership_declaration: typing.Optional[OwnershipDeclarationInput] = OMIT,
        tos_acceptance: typing.Optional[TermsOfServiceAcceptanceInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityOnboardingDataResponse]:
        """
        Parameters
        ----------
        entity_id : str

        business_profile : typing.Optional[BusinessProfileInput]
            Business information about the entity.

        ownership_declaration : typing.Optional[OwnershipDeclarationInput]
            Used to attest that the beneficial owner information provided is both current and correct.

        tos_acceptance : typing.Optional[TermsOfServiceAcceptanceInput]
            Details on the entity's acceptance of the service agreement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityOnboardingDataResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entities/{jsonable_encoder(entity_id)}/onboarding_data",
            method="PATCH",
            json={
                "business_profile": convert_and_respect_annotation_metadata(
                    object_=business_profile, annotation=BusinessProfileInput, direction="write"
                ),
                "ownership_declaration": convert_and_respect_annotation_metadata(
                    object_=ownership_declaration, annotation=OwnershipDeclarationInput, direction="write"
                ),
                "tos_acceptance": convert_and_respect_annotation_metadata(
                    object_=tos_acceptance, annotation=TermsOfServiceAcceptanceInput, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityOnboardingDataResponse,
                    parse_obj_as(
                        type_=EntityOnboardingDataResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
