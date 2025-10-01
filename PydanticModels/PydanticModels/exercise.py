from pydantic import BaseModel, ValidationError, Field, ConfigDict
from typing import Optional, Annotated
from datetime import datetime


class User(BaseModel):
    model_config = {'extra': 'allow'}
    
    id: int
    name: str
    signup_ts: datetime = datetime.today()


# 2 options below to validate Model
m = User.model_validate({'id':13,'name':'Jack', 'age':34})
m1 = User.model_validate(User(id=13, name='Jack', age= 34))

print(m)
print(m1)







