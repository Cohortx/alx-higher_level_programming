#!/usr/bin/python3
"""
this module contains A class square thats inherits from `Rectangle`
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ inisializing the attribute oof the class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Reurning information for Square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getter got size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method for Square class """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ returning the dictinary representatin of Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
