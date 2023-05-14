#!/usr/bin/python3
import sibling_path
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print("---First Model----")
print(my_model)
my_model.save()
print("---First Model After Save----")
print(my_model)
my_model_json = my_model.to_dict()
print("---First Model After to_dict----")
print(my_model)
print("---First Model to_dict copy----")
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

my_model_2 = BaseModel(**{"name": "Adetola", "age": 23, "id": 23})
print(my_model_2)
my_model_2_dic = my_model_2.to_dict()
print(my_model_2_dic)
