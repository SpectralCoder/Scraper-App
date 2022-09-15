from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, DateTime
from database import Base
class info(Base):
    __tablename__ = "information"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(44))
    address = Column(Text())
    phone = Column(String(44), unique=True)
    more = Column(String(100))
    hours = Column(String(44))
    pincode = Column(Integer)
    time_created = Column(DateTime, nullable=False)

    def __iter__(self):
        return [ self.id, 
                 self.name, 
                 self.address, 
                 self.phone, 
                 self.more, 
                 self.hours, 
                 self.pincode, 
                 self.time_created ] 
