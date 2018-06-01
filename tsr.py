#!/usr/bin/env python3

import argparse

from terminal.Session import Session
from terminal.Shell import Shell

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save and restore terminals sessions.")
    parser.add_argument("--session", default="default", help="session name (default: 'default')")
    parser.add_argument("--add", help="add terminal name")
    parser.add_argument("--remove", help="remove terminal name")
    parser.add_argument("--list", action="store_true", help="list session names")
    parser.add_argument("--restore", nargs="?", const="*", help="restore session name (default: '*')")
    controller = parser.parse_args()
    
    session = Session(controller.session)
    
    if controller.add:
        metaData = Shell().metaData()
        session.addToSession(controller.add, metaData)
    
    if controller.remove:
        session.removeFromSession(controller.remove)
    
    if controller.list:
        for name in session.list():
            print(name)
    
    if controller.restore:
        print(controller.restore)
        session.restore(controller.restore)