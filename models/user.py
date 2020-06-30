#!/usr/bin/python3
"""class User Module."""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """INIT"""

        super().__init__(**kwargs)
