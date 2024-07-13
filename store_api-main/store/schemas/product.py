from typing import Optional
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity (must be positive)")
    price: float = Field(..., description="Product price (in USD)")
    status: bool = Field(..., description="Product status (active/inactive)")


class ProductOut(ProductBase):
    id: str = Field(..., description="Product ID")


class ProductUpdate(BaseModel):
    quantity: Optional[int] = Field(None, description="Updated product quantity (positive)")
    price: Optional[float] = Field(None, description="Updated product price (in USD)")
    status: Optional[bool] = Field(None, description="Updated product status")


class ProductUpdateOut(ProductOut):
    pass
