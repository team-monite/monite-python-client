# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .receivable_templates_variables_object import ReceivableTemplatesVariablesObject
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ReceivableTemplatesVariablesObjectList(UniversalBaseModel):
    data: typing.List[ReceivableTemplatesVariablesObject]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
