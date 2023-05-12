import sibling_path as sibling_path
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
print(len(all_objs))
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Base_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
