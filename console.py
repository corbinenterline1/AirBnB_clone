#!/usr/bin/python3
"""
this module imports cmd that creates the entry point
to the commmand line interpreter
"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """
    this method defines a new class HBNBCommand inheritance from cmd module
    """
    prompt = '(hbnb) '

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
        print("Quit command to eit the program")
        print()


    def do_create(self, args):
        """
        creates new instance of BaseModel
        saves to JSON file then prints the id
        """
        if not args:
            print("** class name missing **")
        if args != 'BaseModel':
            print("** class doesn't exist **")
        else:
            """ create new instance, save to JSON, print id """

    def do_show(self, args):
        """
        prints ths string representation of an instance
        based on the class name and id
        """
        print(BaseModel.id.__str__()) """ not sure this is quite right """

if __name__=='__main__':
    HBNBCommand().cmdloop()
