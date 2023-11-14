#!/usr/bin/python3
"""
Contains the FileStorage class model.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

# Dictionary mapping class names to their corresponding classes
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the 'obj' with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(self.__file_path, mode="w") as file:
            dict_storage = {}
            for key, instance in self.__objects.items():
                dict_storage[key] = instance.to_dict()
            json.dump(dict_storage, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects when it exists.
        """
        try:
            with open(self.__file_path, 'r') as file:
                json_data = json.load(file)
            for key in json_data:
                instance_data = json_data[key]
                class_name = instance_data["__class__"]
                self.__objects[key] = classes[class_name](**instance_data)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading instances: {e}")
