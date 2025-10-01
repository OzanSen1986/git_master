from datetime import datetime, timedelta
from pydantic import BaseModel, ValidationError, field_validator

class Coupon(BaseModel):
    code: str
    expiry_date: datetime

    @field_validator('expiry_date')
    def validate_expiry(cls, v):
        if v < datetime.now():
            raise ValueError("Coupon expired")
        if v > datetime.now() + timedelta(days=365):
            raise ValueError("max validity is 1 year")
        return v

def main() -> None:
    try:
        coupon = Coupon(code= 'ABCDEFGH', expiry_date = "2026-01-07T14:00")
    except ValidationError as e:
        print(e)


if __name__ == '__main__':
    main()


