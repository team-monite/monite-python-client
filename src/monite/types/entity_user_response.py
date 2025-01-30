# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import datetime as dt
import typing
from .status_enum import StatusEnum
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EntityUserResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    UUID entity user ID
    """

    created_at: dt.datetime = pydantic.Field()
    """
    UTC datetime
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    UTC datetime
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    An entity user business email
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First name
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last name
    """

    login: str = pydantic.Field()
    """
    Login
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    An entity user phone number in the international format
    """

    role_id: str = pydantic.Field()
    """
    UUID role ID
    """

    status: StatusEnum = pydantic.Field()
    """
    record status, 'active' by default
    """

    userpic_file_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
