#!/usr/bin/python3
"""
this module creates a class FileStorage that serializes instances to JSON
and deserializes JSON file to instance
"""
import json
import models
from console import all_classes
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """
    Serializes instances to a JSON file & deserializes JSON file to
    instance.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        this PUBLIC method returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        this PUBLIC method sets <obj class name>.id as key in __objects
        """
        self.__objects["{}.{}".format(str(type(obj).__name__), obj.id)] = obj

    def save(self):
        """
        this PUBLIC method serializes __objects to the JSON file __file_path
        """
        tmpdic = {}
        for key, val in self.__objects.items():
            if type(val) is not dict:
                tmpdic[key] = val.to_dict()
            else:
                tmpdic[key] = val
        with open(self.__file_path, 'w') as f:
            json.dump(tmpdic, f)

    def reload(self):
        """
        this PUBLIC method deserilaizes the JSON file to __objects
        only IF JSON file __file_path exists ELSE
        do nothing - IF __file_path does not exist NO EXCEPTION
        """
        try:
            with open(self.__file_path, 'r') as f:
                g = f.read()
                data = json.loads(g)
                for key in list(data.keys()):
                    self.__objects[key] = all_classes[data[key]['__class__']](
                        **data[key])
        except FileNotFoundError:
            pass
