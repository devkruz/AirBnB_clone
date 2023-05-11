#!/usr/bin/python3
"""Airbnb Console"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Airbnb Console Commands"""
    prompt = "(hbnb) "
    intro = "Welcome to Airbnb Console Commands"
    avaliable_class = ["BaseModel"]

    def do_EOF(self, args):
        """Exit the programe"""
        return True

    def emptyline(self):
        """Do not execute previous command for empty input"""
        pass

    def do_quit(self, args):
        """Quit the programe"""
        exit(1)

    def do_create(self, args):
        """Creates a new instance"""
        if args == "":
            print("** class name missing **")
            return
        elif args not in self.avaliable_class:
            print("** class doesn't exist **")
            return
        new_obj = eval(args)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, args):
        """
        Prints the string representation
        of an instance
        """
        if args == "":
            print("** class name missing **")
            return
        input = args.split()
        if input[0] not in self.avaliable_class:
            print("** class doesn't exist **")
            return
        try:
            id = input[1]
        except IndexError:
            print("** instance id missing **")
            return
        else:
            all_models = storage.all()
            for obj in all_models.values():
                if id == obj.id:
                    print(obj)
                    return
            print("* no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
