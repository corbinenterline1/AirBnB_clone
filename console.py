#!/usr/bin/python3
"""
this module imports cmd that creates the entry point
to the commmand line interpreter
"""
import cmd
from datetime import datetime
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import shlex
import sys


all_classes = {"BaseModel": BaseModel, "User": User, "State": State, "City":
               City, "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
    this method defines a new class HBNBCommand inheritance from cmd module
    """
    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """
        this method does nothing when an empty line is entered
        in response to prompt
        """
        pass

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")
        print()

    do_quit = do_EOF

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def do_create(self, args):
        """
        creates new instance of BaseModel
        saves to JSON file then prints the id
        """
        parse = args.split(" ")
        if not args:
            print("** class name missing **")
        elif parse[0] in all_classes:
            for key, val in all_classes.items():
                if key == parse[0]:
                    new_inst = all_classes[key]()
            storage.save()
            print("{}".format(new_inst.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        prints ths string representation of an instance
        based on the class name and id
        """
        from models import storage
        parse = args.split(" ")
        if not args:
            print("** class name missing **")
        elif parse[0] not in all_classes:
            print("** class doesn't exist **")
        elif len(parse) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(parse[0], parse[1]) not in storage.all():
            print("** no instance found **")
        else:
            for key, val in storage.all().items():
                if key == parse[0] + '.' + parse[1]:
                    print(val)

    def do_destroy(self, args):
        """
        deletes an instance based on the class name and id
        saves change into the JSON file
        """
        from models import storage
        parse = args.split(" ")
        if not args:
            print("** class name missing **")
        elif parse[0] not in all_classes:
            print("** class doesn't exist **")
        elif len(parse) >= 1:
            try:
                new_key = parse[0] + '.' + parse[1]
                storage.all().pop(new_key)
                storage.save()
            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, args):
        """
        prints all string representation of all instances
        based or not on the class name
        """
        from models import storage
        parse = args.split(" ")
        inst = []
        if not args:
            for key, val in storage.all().items():
                inst.append(str(val))
            print(inst)
            return
        elif parse[0] not in all_classes:
            print("** class doesn't exist **")
            return
        else:
            for key, val in storage.all().items():
                if storage.all()[key].__class__.__name__ == parse[0]:
                    inst.append(str(val))
                print(inst)

    def do_update(self, args):
        """
        updates an instance based on the class name and id
        by adding/updating attribute (save chance in JSON file)
        """
        from models import storage
        parse = args.split(" ")
        if not args:
            print("** class name missing **")
        elif parse[0] not in all_classes:
            print("** class doesn't exist **")
        elif len(parse) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(parse[0], parse[1]) not in storage.all():
            print("** no instance found **")
        elif len(parse) == 2:
            print("** attribute name missing **")
        elif len(parse) == 3:
            print("** value missing **")
        else:
            for key, val in storage.all().items():
                if key == "{}.{}".format(parse[0], parse[1]):
                    all_val = storage.all().get(key)
                    setattr(val, parse[2], parse[3].strip('"'))
                    val.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
