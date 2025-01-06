# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MailboxResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Mailbox UUID
    """

    mailbox_domain_id: typing.Optional[str] = None
    mailbox_full_address: str
    mailbox_name: str
    related_object_type: str
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
