import json
from enum import Enum
from decimal import Decimal
from pydantic import BaseModel, Field,ValidationError, field_validator, model_validator, ConfigDict, EmailStr, HttpUrl, PositiveInt,condecimal,create_model
from datetime import datetime, date, timedelta
from typing import Optional, Any, Annotated, Union
from pydantic.functional_validators import AfterValidator
from pydantic.json_schema import model_json_schema
import uuid
import re

# 1. BASIC MODEL
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    tags: list[str]= []

# 2. FIELD VALIDATION
class Product(BaseModel):
    id: PositiveInt
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(gt=0, le=9.99)
    description: Optional[str]= Field(None, max_length=500)
    in_stock: bool = True
    categories: list[str] = Field(default_factory=list)


    @field_validator('name')
    @classmethod
    def validate_price(cls, v):
        if not v.strip():
            raise ValueError('Name can not be empty or white space!!!')
        return v.title()
    
item = Product(id=34505249, name= 'ALICE', price=9.99, description=None, is_stock=False,categories=['A', 'B', 'C'])
# print(item)

# 3.ADVANCED VALIDATION
class AdvancedUser(BaseModel):
    email: EmailStr
    website: list[HttpUrl] = None
    age: int = Field(ge=13, le=120)
    password: str = Field(..., min_length=8, pattern= re.compile(r'^(?=.*[A-Za-z])(?=.*\d)'))

    @field_validator('email', mode='before')
    @classmethod
    def normalize_email(cls, v):
        if isinstance(v, str):
            return v.upper().strip()
        return v

def main():
    try:
        check_email = AdvancedUser(email='example35k@gmail.com', website=['https://www.google.com'], age=19, password='ALEKO345?_*$')
        print(check_email.email)
    except ValidationError as e:
        print(e)

if __name__ == "__main__":
    main()

# 4. Model Validation
class Order(BaseModel):
    items: dict[str, int]
    prices: dict[str, int]
    total: Decimal
    discount: Decimal = Field(ge=0, le=1)

    @model_validator(mode='after')
    def validate_total_vs_items(self):
        calculated_total = sum(price * qty for item, price in self.prices.items() for item, qty in self.items.items())
        if abs(float(self.total) - calculated_total) > 0.01:
            raise ValueError('Total does not much sum!')
        return self

def main():
    try:
        check_total = Order(items={'A':2, 'B':5}, prices={'A':4, 'B':6}, total=38.0, discount=0.01)
    except ValidationError as e:
        print(e)

if __name__ == "__main__":
    main()


   
















