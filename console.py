#!/usr/bin/python3
"""Airbnb Console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Airbnb Console Commands"""
    prompt = "(hbnb) "
    intro = "Welcome to Airbnb Console Commands"
    avaliable_class = ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]

    def do_EOF(self, args):
        """Exit the programe"""
        return True

    def emptyline(self):
        """Do not execute previous command for empty input"""
        pass

    def do_quit(self, args):
        """Quit the programe"""
        return True

    def do_create(self, args):
        """
        Creates a new instance
        Usage: create <class name>
        """
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
        Usage: show <class name> <id>
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
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance
        Usage: destroy <class name> <id>
        """
        if args == "":
            print("** class name missing **")
            return
        input = args.split()
        class_name = input[0]
        if class_name not in self.avaliable_class:
            print("** class doesn't exist **")
            return
        try:
            id = input[1]
        except IndexError:
            print("** instance id missing **")
            return
        else:
            all_models = storage.all()
            key_id = "{}.{}".format(class_name, id)
            if key_id in all_models:
                del all_models[key_id]
                storage.save()
                storage.reload()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation
        of all instances or the specified one only
        Usage: all <class name> | all
        """
        all_instances = storage.all().values()
        if args == "":
            print([str(obj) for obj in all_instances])
            return
        input = args.split()
        class_name = input[0]
        if class_name not in self.avaliable_class:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in all_instances
                   if class_name == obj.__class__.__name__])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        all_instances = storage.all()
        if args == "":
            print("** class name missing **")
            return
        input = args.split()
        class_name = input[0]
        if class_name not in self.avaliable_class:
            print("** class doesn't exist **")
            return
        try:
            id = input[1]
        except IndexError:
            print("** instance id missing **")
        else:
            # search for the id
            for key in all_instances.keys():
                if all_instances[key].id == id:
                    try:
                        attr = input[2]
                    except IndexError:
                        print("** attribute name missing **")
                        return
                    else:
                        try:
                            val = input[3]
                        except IndexError:
                            print("** value missing **")
                            return
                        else:
                            setattr(all_instances[key], attr, val)
                            all_instances[key].save()
                            storage.reload()
                            return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
