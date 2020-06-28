#!/usr/bin/python3
"""
this module updates __init__ to create a unique instance of FileStorage
"""
from models.engine import file_storage


""" unsure about syntax below on both """
storage = file_storage.FileStorage()
storage = storage.reload()
