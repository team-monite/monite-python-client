# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class UpdateIssuedInvoiceEntity_Organization(UniversalBaseModel):
    type: typing.Literal["organization"] = "organization"
    email: typing.Optional[str] = None
    logo: typing.Optional[str] = None
    name: str
    phone: typing.Optional[str] = None
    tax_id: typing.Optional[str] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateIssuedInvoiceEntity_Individual(UniversalBaseModel):
    type: typing.Literal["individual"] = "individual"
    email: typing.Optional[str] = None
    first_name: str
    last_name: str
    logo: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    tax_id: typing.Optional[str] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UpdateIssuedInvoiceEntity = typing.Union[UpdateIssuedInvoiceEntity_Organization, UpdateIssuedInvoiceEntity_Individual]
