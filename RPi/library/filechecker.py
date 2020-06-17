import os

def containsfile(filename):
    """Checks if there is a file in the directory
    str filename - the path to file
    """
    return os.path.isfile(filename)

def containsdir(dirname):
    """Checks if there is a directory in the directory
    str dirname - the path to the directory
    """
    return os.path.isdir(dirname)

def contains(name):
    """Checks if there is a file or directory
    str name - the path to the file or directory
    """
    return os.path.exists(name)

def makedir(dirname):
    """Creates a directory """
    os.makedirs(dirname)
