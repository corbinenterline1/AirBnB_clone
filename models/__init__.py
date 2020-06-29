#!/usr/bin/python3
"""
this module updates __init__ to create a unique instance of FileStorage
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
