#!/usr/bin/python3
"""
Module implementing the BaseModel class.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class defining common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        Format: "[<class name>] (<self.id>) <self.__dict__>"
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.

        Returns:
            dict: Dictionary containing instance attributes.
        """
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = self.__class__.__name__
        for a, b in self.__dict__.items():
            if a in ("created_at", "updated_at"):
                b = self.__dict__[a].isoformat()
                n_dict[a] = b
        return n_dict
