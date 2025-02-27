# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .entity_address_response_schema import EntityAddressResponseSchema
from .individual_response_schema import IndividualResponseSchema
from .file_schema3 import FileSchema3
from .entity_status_enum import EntityStatusEnum
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .organization_response_schema import OrganizationResponseSchema


class EntityResponse_Individual(UniversalBaseModel):
    """
    A schema for a response after creation of an entity of different types
    """

    type: typing.Literal["individual"] = "individual"
    id: str
    created_at: dt.datetime
    updated_at: dt.datetime
    address: EntityAddressResponseSchema
    email: typing.Optional[str] = None
    individual: IndividualResponseSchema
    logo: typing.Optional[FileSchema3] = None
    phone: typing.Optional[str] = None
    status: EntityStatusEnum
    tax_id: typing.Optional[str] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntityResponse_Organization(UniversalBaseModel):
    """
    A schema for a response after creation of an entity of different types
    """

    type: typing.Literal["organization"] = "organization"
    id: str
    created_at: dt.datetime
    updated_at: dt.datetime
    address: EntityAddressResponseSchema
    email: typing.Optional[str] = None
    logo: typing.Optional[FileSchema3] = None
    organization: OrganizationResponseSchema
    phone: typing.Optional[str] = None
    status: EntityStatusEnum
    tax_id: typing.Optional[str] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


EntityResponse = typing.Union[EntityResponse_Individual, EntityResponse_Organization]
