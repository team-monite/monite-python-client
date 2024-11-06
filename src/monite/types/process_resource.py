# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .process_status_enum import ProcessStatusEnum
import pydantic
import typing
from .process_resource_script_snapshot import ProcessResourceScriptSnapshot
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ProcessResource(UniversalBaseModel):
    id: str
    status: ProcessStatusEnum = pydantic.Field()
    """
    Tthe current status of the approval policy process.
    """

    input: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    The input for the script.
    """

    error: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    The error for the process.
    """

    script_snapshot: typing.Optional[ProcessResourceScriptSnapshot] = pydantic.Field(default=None)
    """
    The script snapshot taken when script started.
    """

    metadata: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    The metadata for the process.
    """

    created_at: dt.datetime
    updated_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    updated_by: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
