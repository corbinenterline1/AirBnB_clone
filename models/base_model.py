#!/usr/bin/python3
"""
this module creates BaseModel class with public attributes and methods
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    defines class BaseModel and all attributes/methods
    inherited by other classes
    """

    def __init__(self, *args, **kwargs):
        """
        this method is constructor for BaseModel
        """
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        PUBLIC attribute with [<class name>] (<self.id>) <self.__dict__> format
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        this PUBLIC method updates PUB instance attr updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        this PUBLIC method returns a dict containing all key/values
        of __dict__ instance
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["id"] = self.id
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
