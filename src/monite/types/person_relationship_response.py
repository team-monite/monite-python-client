# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PersonRelationshipResponse(UniversalBaseModel):
    director: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the person is a director of the account's legal entity
    """

    executive: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the person has significant responsibility to control, manage, or direct the organization
    """

    owner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the person is an owner of the account's legal entity
    """

    percent_ownership: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percent owned by the person of the account's legal entity
    """

    representative: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the person is authorized as the primary representative of the account
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's title (e.g., CEO, Support Engineer)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
