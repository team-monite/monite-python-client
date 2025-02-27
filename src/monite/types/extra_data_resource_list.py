# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .extra_data_resource import ExtraDataResource
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ExtraDataResourceList(UniversalBaseModel):
    data: typing.List[ExtraDataResource]
    next_pagination_token: typing.Optional[str] = None
    prev_pagination_token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
