#!/usr/bin/python3
"""Airbnb Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Airbnb Console Commands"""
    prompt = "(hbnb) "
    intro = "Welcome to Airbnb Console Commands"

    def do_EOF(self, args):
        """Exit the programe"""
        return True

    def emptyline(self):
        """Do not execute previous command for empty input"""
        pass

    def do_quit(self, args):
        """Quit the programe"""
        exit(1)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
