#!/usr/bin/python3
"""
this module creates a class FileStorage that serializes instances to JSON
and deserializes JSON file to instance
"""

class FileStorage:

def __init__(self, file_path, objects):
    """
    initializes FileStorage class attributes
    """
    self.__file_path = file_path
    self.__objects = objects
    """ BaseModel object with id 121212 the key will be BaseModel.121212 """

def all(self):
    """
    this PUBLIC method returns the dictionary __objects
    """
    return dict(__objects)

def new(self):
    """
    this PUBLIC method sets <obj class name>.id as key in __objects
    """

def save(self):
    """
    this PUBLIC method serializes __objects to the JSON file __file_path
    """
    json.dumps(__objects)

def reload(self):
    """
    this PUBLIC method deserilaizes the JSON file to __objects
    only IF JSON file __file_path exists ELSE
    do nothing - IF __file_path does not exist NO EXCEPTION
    """
    if (__file_path):
        json.loads(__objects)
    else:
        pass
