#!/usr/bin/python3
""" this module creates class BaseModel """
from datetime import datetime
import uuid
""" will we need to import anything for cmd """


class BaseModel:
""" defines class BaseModel and all commmon
attributes/method for inherited classes
 """

def __init__(self, *args, **kwargs):
"""
initialize BaseModel with public attributes
id : created_at : updated_at
"""

if len(kwargs) != 0:
for key in **kwargs:
if kwargs[key] != None
setattr(self, key, kwargs[key]) """ this SHOULD work """

""" convert created_at, updated_at from str to date object """
""" locally tested formatting for .strptime - works in theory """
updated_at_obj = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f')

""" PUBLIC INSTANCE ATTRIBUTES """
""" do we need getters and setters for all ? """

def id(self):
""" uuid assigned here """
id = str(uuid.uuid4())

def created_at(self):
""" datetime used here at creation """
self.created_at = datetime.now()
""" specific datetime formatting provided """

def updated_at(self):
""" datetime used here at creation and update or change """
self.updated_at = .datetime.now()
""" specific datetime formatting provided """

def __str__(self):
""" retruns string to be printed with provided format """
""" [<class name>] (<self.id>) <self.__dict__> """
base_m_str = ""
return base_m_str


""" PUBLIC INSTANCE METHODS """

def save(self):
""" updates PUB instance updated_at with datetime """
return self.updated_at """ idk about this """

def to_dict(self):
""" returns dictionary with all keys/values of __dict__ instance """
return BaseModel.__dict__ """ idk about this """
dict[__class__] = BaseModel """ a __class key must be added to this dictionary """
created_at_str = created_at.isoformat()
updated_at_str = updated_at.isoformat()
