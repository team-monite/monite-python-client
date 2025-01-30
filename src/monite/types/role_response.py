# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .biz_objects_schema_output import BizObjectsSchemaOutput
from .status_enum import StatusEnum
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class RoleResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    UUID role ID
    """

    name: str = pydantic.Field()
    """
    Role name
    """

    permissions: BizObjectsSchemaOutput = pydantic.Field()
    """
    Access permissions
    """

    status: StatusEnum = pydantic.Field()
    """
    record status, 'active' by default
    """

    created_at: dt.datetime = pydantic.Field()
    """
    UTC datetime
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    UTC datetime
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
