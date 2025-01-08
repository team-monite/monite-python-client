# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import datetime as dt
import typing
from .counterpart_tag_category import CounterpartTagCategory
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CounterpartTagSchema(UniversalBaseModel):
    """
    Represents a user-defined tag that can be assigned to resources to filter them.
    """

    id: str = pydantic.Field()
    """
    A unique ID of this tag.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Date and time when the tag was created. Timestamps follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Date and time when the tag was last updated. Timestamps follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.
    """

    category: typing.Optional[CounterpartTagCategory] = pydantic.Field(default=None)
    """
    The tag category.
    """

    created_by_entity_user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the user who created the tag
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tag description.
    """

    name: str = pydantic.Field()
    """
    The tag name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
