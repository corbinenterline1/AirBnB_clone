#!/usr/bin/python3
"""
class Review Module.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        INIT
        """

        super().__init__(**kwargs)
