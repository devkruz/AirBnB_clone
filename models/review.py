#!/usr/bin/python3
"""Reviw Model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """reviw model"""
    place_id = ""
    user_id = ""
    text = ""
