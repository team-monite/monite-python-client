# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .allowed_countries import AllowedCountries
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PersonAddressRequest(UniversalBaseModel):
    city: str = pydantic.Field()
    """
    City, district, suburb, town, or village
    """

    country: AllowedCountries = pydantic.Field()
    """
    Two-letter country code (ISO 3166-1 alpha-2)
    """

    line1: str = pydantic.Field()
    """
    Address line 1 (e.g., street, PO Box, or company name)
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address line 2 (e.g., apartment, suite, unit, or building)
    """

    postal_code: str = pydantic.Field()
    """
    ZIP or postal code
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State, county, province, or region
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
