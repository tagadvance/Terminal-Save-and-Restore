import os

from terminal.Shell import Shell


class System:
    
    @staticmethod
    def isRoot():
        return os.geteuid() == 0