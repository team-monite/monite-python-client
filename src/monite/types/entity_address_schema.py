# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .allowed_countries import AllowedCountries


class EntityAddressSchema(UniversalBaseModel):
    """
    A schema represents address info of the entity
    """

    city: str = pydantic.Field()
    """
    A city (a full name) where the entity is registered
    """

    country: AllowedCountries = pydantic.Field()
    """
    A country name (as ISO code) where the entity is registered 
    """

    line1: str = pydantic.Field()
    """
    A street where the entity is registered
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    An alternative street used by the entity
    """

    postal_code: str = pydantic.Field()
    """
    A postal code of the address where the entity is registered
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State, county, province, prefecture, region, or similar component of the entity's address. For US entities, `state` is required and must be a two-letter [USPS state abbreviation](https://pe.usps.com/text/pub28/28apb.htm), for example, NY or CA.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
