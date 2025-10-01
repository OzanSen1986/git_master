from pydantic import BaseModel, ValidationError, field_validator, model_validator

class Order(BaseModel):
    items: list[str]
    discount_code: str | None = None
    total: float

    @model_validator(mode = 'after')
    def validate_order(self):
        if self.discount_code == 'BIGSALE' and len(self.items) < 3:
            raise ValueError("BIGSALE requires 3+ items")
        if self.total > 1000 and self.discount_code is None:
            raise ValueError("Orders over $1000 require a discount code")
        return self

def main() -> None:
    try:
        order = Order(items = ['Apple', 'Apricot', 'Eggplant'], discount_code = 'BIGSALE', total = 1500)
    except ValidationError as e:
        print(e)

if __name__ == '__main__':
    main()




