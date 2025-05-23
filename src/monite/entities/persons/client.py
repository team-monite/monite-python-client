# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.allowed_countries import AllowedCountries
from ...types.optional_person_address_request import OptionalPersonAddressRequest
from ...types.optional_person_relationship import OptionalPersonRelationship
from ...types.person_address_request import PersonAddressRequest
from ...types.person_relationship_request import PersonRelationshipRequest
from ...types.person_response import PersonResponse
from ...types.persons_response import PersonsResponse
from .raw_client import AsyncRawPersonsClient, RawPersonsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PersonsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPersonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPersonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPersonsClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> PersonsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonsResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.entities.persons.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        email: str,
        first_name: str,
        last_name: str,
        relationship: PersonRelationshipRequest,
        address: typing.Optional[PersonAddressRequest] = OMIT,
        citizenship: typing.Optional[AllowedCountries] = OMIT,
        date_of_birth: typing.Optional[str] = OMIT,
        id_number: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        ssn_last4: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonResponse:
        """
        Parameters
        ----------
        email : str
            The person's email address

        first_name : str
            The person's first name

        last_name : str
            The person's last name

        relationship : PersonRelationshipRequest
            Describes the person's relationship to the entity

        address : typing.Optional[PersonAddressRequest]
            The person's address

        citizenship : typing.Optional[AllowedCountries]
            Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.

        date_of_birth : typing.Optional[str]
            The person's date of birth

        id_number : typing.Optional[str]
            The person's ID number, as appropriate for their country

        phone : typing.Optional[str]
            The person's phone number

        ssn_last4 : typing.Optional[str]
            The last four digits of the person's Social Security number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        from monite import PersonRelationshipRequest
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.entities.persons.create(email='email', first_name='first_name', last_name='last_name', relationship=PersonRelationshipRequest(), )
        """
        _response = self._raw_client.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            relationship=relationship,
            address=address,
            citizenship=citizenship,
            date_of_birth=date_of_birth,
            id_number=id_number,
            phone=phone,
            ssn_last4=ssn_last4,
            request_options=request_options,
        )
        return _response.data

    def get_by_id(self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PersonResponse:
        """
        Parameters
        ----------
        person_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.entities.persons.get_by_id(person_id='person_id', )
        """
        _response = self._raw_client.get_by_id(person_id, request_options=request_options)
        return _response.data

    def delete_by_id(self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        person_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.entities.persons.delete_by_id(person_id='person_id', )
        """
        _response = self._raw_client.delete_by_id(person_id, request_options=request_options)
        return _response.data

    def update_by_id(
        self,
        person_id: str,
        *,
        address: typing.Optional[OptionalPersonAddressRequest] = OMIT,
        citizenship: typing.Optional[AllowedCountries] = OMIT,
        date_of_birth: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id_number: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        relationship: typing.Optional[OptionalPersonRelationship] = OMIT,
        ssn_last4: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonResponse:
        """
        Parameters
        ----------
        person_id : str

        address : typing.Optional[OptionalPersonAddressRequest]
            The person's address

        citizenship : typing.Optional[AllowedCountries]
            Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.

        date_of_birth : typing.Optional[str]
            The person's date of birth

        email : typing.Optional[str]
            The person's email address

        first_name : typing.Optional[str]
            The person's first name

        id_number : typing.Optional[str]
            The person's ID number, as appropriate for their country

        last_name : typing.Optional[str]
            The person's last name

        phone : typing.Optional[str]
            The person's phone number

        relationship : typing.Optional[OptionalPersonRelationship]
            Describes the person's relationship to the entity

        ssn_last4 : typing.Optional[str]
            The last four digits of the person's Social Security number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonResponse
            Successful Response

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.entities.persons.update_by_id(person_id='person_id', )
        """
        _response = self._raw_client.update_by_id(
            person_id,
            address=address,
            citizenship=citizenship,
            date_of_birth=date_of_birth,
            email=email,
            first_name=first_name,
            id_number=id_number,
            last_name=last_name,
            phone=phone,
            relationship=relationship,
            ssn_last4=ssn_last4,
            request_options=request_options,
        )
        return _response.data

    def upload_onboarding_documents(
        self,
        person_id: str,
        *,
        additional_verification_document_back: typing.Optional[str] = OMIT,
        additional_verification_document_front: typing.Optional[str] = OMIT,
        verification_document_back: typing.Optional[str] = OMIT,
        verification_document_front: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Provide files for person onboarding verification

        Parameters
        ----------
        person_id : str

        additional_verification_document_back : typing.Optional[str]

        additional_verification_document_front : typing.Optional[str]

        verification_document_back : typing.Optional[str]

        verification_document_front : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from monite import Monite
        client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        client.entities.persons.upload_onboarding_documents(person_id='person_id', )
        """
        _response = self._raw_client.upload_onboarding_documents(
            person_id,
            additional_verification_document_back=additional_verification_document_back,
            additional_verification_document_front=additional_verification_document_front,
            verification_document_back=verification_document_back,
            verification_document_front=verification_document_front,
            request_options=request_options,
        )
        return _response.data


class AsyncPersonsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPersonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPersonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPersonsClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> PersonsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonsResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.entities.persons.get()
        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        email: str,
        first_name: str,
        last_name: str,
        relationship: PersonRelationshipRequest,
        address: typing.Optional[PersonAddressRequest] = OMIT,
        citizenship: typing.Optional[AllowedCountries] = OMIT,
        date_of_birth: typing.Optional[str] = OMIT,
        id_number: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        ssn_last4: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonResponse:
        """
        Parameters
        ----------
        email : str
            The person's email address

        first_name : str
            The person's first name

        last_name : str
            The person's last name

        relationship : PersonRelationshipRequest
            Describes the person's relationship to the entity

        address : typing.Optional[PersonAddressRequest]
            The person's address

        citizenship : typing.Optional[AllowedCountries]
            Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.

        date_of_birth : typing.Optional[str]
            The person's date of birth

        id_number : typing.Optional[str]
            The person's ID number, as appropriate for their country

        phone : typing.Optional[str]
            The person's phone number

        ssn_last4 : typing.Optional[str]
            The last four digits of the person's Social Security number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        from monite import PersonRelationshipRequest
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.entities.persons.create(email='email', first_name='first_name', last_name='last_name', relationship=PersonRelationshipRequest(), )
        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            relationship=relationship,
            address=address,
            citizenship=citizenship,
            date_of_birth=date_of_birth,
            id_number=id_number,
            phone=phone,
            ssn_last4=ssn_last4,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PersonResponse:
        """
        Parameters
        ----------
        person_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.entities.persons.get_by_id(person_id='person_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id(person_id, request_options=request_options)
        return _response.data

    async def delete_by_id(self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        person_id : str

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
            await client.entities.persons.delete_by_id(person_id='person_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.delete_by_id(person_id, request_options=request_options)
        return _response.data

    async def update_by_id(
        self,
        person_id: str,
        *,
        address: typing.Optional[OptionalPersonAddressRequest] = OMIT,
        citizenship: typing.Optional[AllowedCountries] = OMIT,
        date_of_birth: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id_number: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        relationship: typing.Optional[OptionalPersonRelationship] = OMIT,
        ssn_last4: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonResponse:
        """
        Parameters
        ----------
        person_id : str

        address : typing.Optional[OptionalPersonAddressRequest]
            The person's address

        citizenship : typing.Optional[AllowedCountries]
            Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.

        date_of_birth : typing.Optional[str]
            The person's date of birth

        email : typing.Optional[str]
            The person's email address

        first_name : typing.Optional[str]
            The person's first name

        id_number : typing.Optional[str]
            The person's ID number, as appropriate for their country

        last_name : typing.Optional[str]
            The person's last name

        phone : typing.Optional[str]
            The person's phone number

        relationship : typing.Optional[OptionalPersonRelationship]
            Describes the person's relationship to the entity

        ssn_last4 : typing.Optional[str]
            The last four digits of the person's Social Security number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonResponse
            Successful Response

        Examples
        --------
        from monite import AsyncMonite
        import asyncio
        client = AsyncMonite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
        async def main() -> None:
            await client.entities.persons.update_by_id(person_id='person_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.update_by_id(
            person_id,
            address=address,
            citizenship=citizenship,
            date_of_birth=date_of_birth,
            email=email,
            first_name=first_name,
            id_number=id_number,
            last_name=last_name,
            phone=phone,
            relationship=relationship,
            ssn_last4=ssn_last4,
            request_options=request_options,
        )
        return _response.data

    async def upload_onboarding_documents(
        self,
        person_id: str,
        *,
        additional_verification_document_back: typing.Optional[str] = OMIT,
        additional_verification_document_front: typing.Optional[str] = OMIT,
        verification_document_back: typing.Optional[str] = OMIT,
        verification_document_front: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Provide files for person onboarding verification

        Parameters
        ----------
        person_id : str

        additional_verification_document_back : typing.Optional[str]

        additional_verification_document_front : typing.Optional[str]

        verification_document_back : typing.Optional[str]

        verification_document_front : typing.Optional[str]

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
            await client.entities.persons.upload_onboarding_documents(person_id='person_id', )
        asyncio.run(main())
        """
        _response = await self._raw_client.upload_onboarding_documents(
            person_id,
            additional_verification_document_back=additional_verification_document_back,
            additional_verification_document_front=additional_verification_document_front,
            verification_document_back=verification_document_back,
            verification_document_front=verification_document_front,
            request_options=request_options,
        )
        return _response.data
