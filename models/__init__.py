#!/usr/bin/python3
"""Models initialization"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
print(f'Invoking __init__.py for {__name__}')
