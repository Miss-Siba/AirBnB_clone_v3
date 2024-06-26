#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models import base_model, amenity, city, place, review, state, user
from datetime import datetime

strptime = datetime.strptime
to_json = base_model.BaseModel.to_json


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    classes = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    # string - path to the JSON file
    __file_path = './dev/file.json'
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls:
            new_dict = {}
            for class_id, obj in FileStorage.__objects.items():
                if type(obj).__name__ == cls:
                    new_dict[class_id] = obj
            return new_dict
        return FileStorage.__objects

    def get(self, cls, id):
        """Retrieve one object by class and ID"""
        all_class = self.all(cls)
        for obj in all_class.values():
            if id == str(obj.id):
                return obj
        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        return len(self.all(cls))

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Retrieve one object by class and ID"""
        all_objects = self.all(cls)
        for obj_id, obj in all_objects.items():
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """Count the number of objects in storage
        count of instances
        :param cls: class
        :return: number of instances
        """

        return len(self.all(cls))
    def get(self, cls, id):
        """
        gets required object
        :param cls: class
        :param id: id of instance
        :return: object or None
        """
        all_class = self.all(cls)

        for obj in all_class.values():
            if id == str(obj.id):
                return obj

        return None
