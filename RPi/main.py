#!/usr/bin/python3

import sys
sys.path.append('library/')
sys.path.append('module/')
sys.path.append('engine/')
sys.path.append('storage-api/')
sys.path.append('config/')
sys.path.append('module/serial/')
sys.path.append('module/sensor/')
from engine import Engine

def main():
    print("Program starting...")

    arg = sys.argv[1]
    eng = Engine(arg)

    print("Program stopped running.")

if __name__ == "__main__":
    main()
