#!/usr/bin/python3
import sibling_path
from models.user import User

us = User()
us.first_name = "new user"
us.save()
