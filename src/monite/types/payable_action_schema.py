# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .payable_action_enum import PayableActionEnum
import pydantic
from .permission_enum import PermissionEnum
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PayableActionSchema(UniversalBaseModel):
    action_name: typing.Optional[PayableActionEnum] = pydantic.Field(default=None)
    """
    Action name
    """

    permission: typing.Optional[PermissionEnum] = pydantic.Field(default=None)
    """
    Permission type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
