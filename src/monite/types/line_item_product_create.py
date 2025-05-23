# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .price import Price
from .product_service_type_enum import ProductServiceTypeEnum
from .unit_request import UnitRequest


class LineItemProductCreate(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the product.
    """

    ledger_account_id: typing.Optional[str] = None
    measure_unit: typing.Optional[UnitRequest] = None
    name: str = pydantic.Field()
    """
    Name of the product.
    """

    price: Price
    smallest_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The smallest amount allowed for this product.
    """

    type: typing.Optional[ProductServiceTypeEnum] = pydantic.Field(default=None)
    """
    Specifies whether this offering is a product or service. This may affect the applicable tax rates.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
