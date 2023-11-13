#!/usr/bin/python3
"""
Contains the FileStorage class model
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
class_mapping = {
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
    deserializes a JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all_instances(self):
        """
        Returns the dictionary __objects containing all instances
        """
        return self.__objects

    def add_instance(self, obj):
        """
        Adds the 'obj' to __objects with the key '<obj class name>.id'
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save_instances(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as file:
            serialized_data = {}
            for key, instance in self.__objects.items():
                serialized_data[key] = instance.to_dict()
            json.dump(serialized_data, file)

    def load_instances(self):
        """
        Deserializes the JSON file to __objects, only if the file exists
        """
        try:
            with open(self.__file_path, 'r') as file:
                json_data = json.load(file)
            for key in json_data:
                instance_data = json_data[key]
                class_name = instance_data["__class__"]
                self.__objects[key] = class_mapping[class_name](
                        **instance_data
                        )

        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading instances: {e}")
