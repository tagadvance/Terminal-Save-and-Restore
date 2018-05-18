#!/usr/bin/env python3

import argparse
import json

from terminal.Terminal import Terminal
from terminal.Terminals import Terminals

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save and restore terminals sessions.')
    parser.add_argument("--export-file", help='File path to write terminal information to.')
    parser.add_argument("--close", action='store_true', help='Close terminals after export.')
    parser.add_argument("--import-file", help='File path to read terminal information from.')
    controller = parser.parse_args()
    
    if controller.export_file:
        with open(controller.export_file, 'w') as handle:
            who = Terminals.logname()
            terminals = Terminals.listPseudoterminalsOwnedBy(who)
            def getMetaAndClose(pts):
                terminal = Terminal(pts)
                metaData = terminal.metaData()
                if controller.close:
                    terminal.exit()
                return metaData
            data = list(map(getMetaAndClose, terminals))
            json.dump(data, handle, indent=4)
    
    if controller.import_file:
        with open(controller.import_file) as handle:
            terminals = json.load(handle)
            for terminal in terminals:
                Terminals.restore(**terminal)