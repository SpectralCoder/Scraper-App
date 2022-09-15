from datetime import date, datetime
from pydantic import BaseModel

class Info(BaseModel):
    id = int
    name = str
    address = str
    phone = str
    more = str
    # hours = str
    pincode = str
    time_created = str

    class Config:
        orm_mode = True