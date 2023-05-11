#!/usr/bin/python3
"""Include parent path in python path"""
import os
import sys


current_path = os.path.dirname(os.path.abspath(__name__))
parent_path = os.path.abspath(os.path.join(current_path, "models"))

sys.path.append(current_path)
print(parent_path)
