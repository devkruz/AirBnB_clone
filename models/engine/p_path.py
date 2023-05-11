from os.path import dirname, abspath, join
import sys

def runpath():

    current_path = dirname(abspath(__file__))
    parent_path = abspath(join(current_path, '..'))

    sys.path.append(parent_path)
