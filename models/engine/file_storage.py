#!/usr/bin/python3
"""File storage model"""

from json import dump, load
import os
from models.base_model import BaseModel


class FileStorage():
    """File storage"""
    __file_path = "airbnb.json"
    __objects = {}

    def all(self):
        """Return all objects saved"""
        return self.__class__.__objects

    def new(self, obj):
        """Sets new object"""
        this_class = self.__class__
        this_class.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        file_path = self.__class__.__file_path
        py_obj = self.__class__.__objects
        py_dic = {}
        for key, value in py_obj.items():
            py_dic[key] = value.to_dict()

        with open(file_path, mode="w") as file:
            dump(py_dic, file)

    def reload(self):
        """
        deserializes the JSON file to
        __objects
        only if the JSON file
        (__file_path) exists
        """
        file_path = self.__class__.__file_path
        if os.path.exists(file_path):
            with open(file_path) as file:
                py_obj = load(file)
                for obj in py_obj.values():
                    self.new(eval(obj["__class__"])(**obj))