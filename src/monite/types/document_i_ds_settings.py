# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .document_id_separators import DocumentIdSeparators
from .document_type_prefix import DocumentTypePrefix
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DocumentIDsSettings(UniversalBaseModel):
    include_date: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Optionally add 4-digit of the current year
    """

    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional prefix. Does not substitute document_type prefix
    """

    separator: typing.Optional[DocumentIdSeparators] = pydantic.Field(default=None)
    """
    Which character should separate each part of the document_id
    """

    document_type_prefix: typing.Optional[DocumentTypePrefix] = pydantic.Field(default=None)
    """
    Prefixes for each document_type
    """

    min_digits: typing.Optional[int] = pydantic.Field(default=None)
    """
    Minimal size of number in document ID Number will be left padded with zeros if less
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
