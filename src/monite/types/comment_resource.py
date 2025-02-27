# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .status_enum import StatusEnum
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CommentResource(UniversalBaseModel):
    id: str
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    created_by_entity_user_id: str
    entity_id: str
    object_id: str
    object_type: str
    reply_to_entity_user_id: typing.Optional[str] = None
    status: StatusEnum
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
