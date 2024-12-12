# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .based_on_transition_type import BasedOnTransitionType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ReceivableCreateBasedOnPayload(UniversalBaseModel):
    based_on: str = pydantic.Field()
    """
    The unique ID of a previous document related to the receivable if applicable.
    """

    tag_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of IDs of user-defined tags (labels) assigned to this receivable.
    """

    type: BasedOnTransitionType = pydantic.Field()
    """
    The type of a created receivable. Currently supported transitions:quote -> invoice; invoice -> credit_note
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
