#!/usr/bin/python3
"""
class State Module.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        INIT
        """

        super().__init__(**kwargs)
