# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .root_schema_input import RootSchemaInput
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BizObjectsSchemaInput(UniversalBaseModel):
    objects: typing.Optional[typing.List[RootSchemaInput]] = pydantic.Field(default=None)
    """
    List of objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
