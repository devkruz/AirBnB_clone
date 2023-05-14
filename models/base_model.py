#!/usr/bin/python3
"""Base model"""
import uuid
from datetime import datetime


class BaseModel():
    """Base model"""
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        from models import storage
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or\
                            key == "updated_at":
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """Return BaseModel string representation"""
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at to current time"""
        from models import storage
        self.created_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation
        of instance
        """
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        for key in dic.keys():
            if key in ("created_at", "updated_at"):
                dic[key] = dic[key].isoformat()

        return dic
