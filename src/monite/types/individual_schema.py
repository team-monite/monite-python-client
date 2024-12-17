# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class IndividualSchema(UniversalBaseModel):
    """
    A schema contains metadata for an individual
    """

    date_of_birth: typing.Optional[str] = None
    first_name: str = pydantic.Field()
    """
    A first name of an individual
    """

    id_number: typing.Optional[str] = None
    last_name: str = pydantic.Field()
    """
    A last name of an individual
    """

    ssn_last4: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ssn_last_4")] = pydantic.Field(
        default=None
    )
    """
    The last four digits of the individual's Social Security number
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    A title of an individual
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
