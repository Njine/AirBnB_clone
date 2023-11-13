#!/usr/bin/python3
"""Implementation of the Review class model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements the Review model"""
    place_id = ""
    user_id = ""
    text = ""
