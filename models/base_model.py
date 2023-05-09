#!/usr/bin/python3
"""Base model"""
import uuid
from datetime import datetime

class BaseModle():
    """Base model"""
    def __init__(self):
        """Initialize BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return BaseModel string representation"""
        return "[{}] ({}) <{}>"\
                .format(type(self).__name__, self.id, self.__dict__)


b1 = BaseModle()
b2 = BaseModle()

print(b1)
print(b2)
