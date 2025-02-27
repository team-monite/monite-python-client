# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .payable_action_schema import PayableActionSchema
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PayableSchemaOutput(UniversalBaseModel):
    actions: typing.Optional[typing.List[PayableActionSchema]] = pydantic.Field(default=None)
    """
    List of actions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
