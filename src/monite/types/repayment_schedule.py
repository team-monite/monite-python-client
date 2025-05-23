# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RepaymentSchedule(UniversalBaseModel):
    """
    Repayment schedule model
    """

    repayment_date: str = pydantic.Field()
    """
    Repayment date in ISO 8601 format
    """

    repayment_amount: int = pydantic.Field()
    """
    Repayment amount in minor units
    """

    repayment_fee_amount: int = pydantic.Field()
    """
    Repayment fee amount in minor units
    """

    repayment_principal_amount: int = pydantic.Field()
    """
    Repayment principal amount in minor units
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
