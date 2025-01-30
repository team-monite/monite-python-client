# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .document_type_enum import DocumentTypeEnum
import typing
from .variable import Variable
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class VariablesObject(UniversalBaseModel):
    object_subtype: DocumentTypeEnum
    object_type: str
    variables: typing.List[Variable]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
