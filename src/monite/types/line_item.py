# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .discount import Discount
import pydantic
from .line_item_product_create import LineItemProductCreate
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LineItem(UniversalBaseModel):
    discount: typing.Optional[Discount] = pydantic.Field(default=None)
    """
    The discount for a product.
    """

    product: typing.Optional[LineItemProductCreate] = pydantic.Field(default=None)
    """
    Object of product. Can be used instead of product_id, created in product's catalog
    """

    product_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the product.
    """

    quantity: float = pydantic.Field()
    """
    The quantity of each of the goods, materials, or services listed in the receivable.
    """

    tax_rate_value: typing.Optional[int] = pydantic.Field(default=None)
    """
    Percent minor units. Example: 12.5% is 1250. This field is only required on invoices issued by entities in the US, Pakistan, and other unsupported countries.
    """

    vat_rate_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the vat rate object. This field is required for all entities in supported countries except the US and Pakistan.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
