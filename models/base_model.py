#!/usr/bin/python3
"""Base model"""
import uuid
from datetime import datetime
from __init__ import storage

class BaseModel():
    """Base model"""
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
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
        return "[{}] ({}) <{}>"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at to current time"""
        self.created_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation
        of instance
        """
        dic = self.__dict__
        dic["__class__"] = type(self).__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()

        return dic

all_objs = storage.all()
print("-- Reloaded objects --")
print(all_objs)
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_2 = BaseModel()
my_3 = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
# print(my_model)