# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FileResponse(UniversalBaseModel):
    id: str
    created_at: dt.datetime
    updated_at: dt.datetime
    file_type: str
    md5: str
    mimetype: str
    name: str
    region: str
    s3bucket: typing_extensions.Annotated[str, FieldMetadata(alias="s3_bucket")]
    s3file_path: typing_extensions.Annotated[str, FieldMetadata(alias="s3_file_path")]
    size: int
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
