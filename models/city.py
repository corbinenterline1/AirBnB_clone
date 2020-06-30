#!/usr/bin/python3
"""
class City Module.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        INIT
        """

        super().__init__(**kwargs)
