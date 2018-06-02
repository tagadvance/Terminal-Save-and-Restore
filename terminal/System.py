import os


class System:
    
    @staticmethod
    def isRoot():
        return os.geteuid() == 0
