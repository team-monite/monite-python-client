# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .business_info_schema import BusinessInfoSchema
from .connection_status import ConnectionStatus
from .error_schema import ErrorSchema


class AccountingConnectionResponse(UniversalBaseModel):
    id: str
    created_at: dt.datetime
    updated_at: dt.datetime
    business_info: typing.Optional[BusinessInfoSchema] = None
    connection_url: str
    errors: typing.Optional[typing.List[ErrorSchema]] = None
    last_pull: typing.Optional[dt.datetime] = None
    platform: typing.Optional[str] = None
    status: typing.Optional[ConnectionStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
