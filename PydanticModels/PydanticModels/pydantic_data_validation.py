from pydantic import BaseModel, field_validator, ValidationError
from enum import Enum
from typing import Optional


class UserType(str, Enum):
    FREE = 'free'
    PREMIUM = 'premium'

class User(BaseModel):
    user_type: UserType
    credit_card: str | None = None

    @field_validator('credit_card')
    def validate_credit_card(cls, v, values):
        if values.data['user_type'] == UserType.PREMIUM and v is None:
            raise ValueError("credit card required for premium users")
        return v

def main():
    try:
        User(user_type = 'premium', credit_card= '235-1234-9081-6758-3452')
    except ValidationError as e:
        print(f"Error Description is: {e}")

if __name__ == '__main__':
    main()























