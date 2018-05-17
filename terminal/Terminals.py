import glob
from os import stat
from pwd import getpwuid

class Terminals:
    
    _TTY_GLOB = '/dev/tty*'
    
    @classmethod
    def listTerminals(cls, user=None):
        def fileOwner(filename):
            return getpwuid(stat(filename).st_uid).pw_name
        
        files = glob.glob(cls._TTY_GLOB)
        return [file for file in files if fileOwner(file) == user] if user else files

if __name__ == '__main__':
    terminals = Terminals.listTerminals('tag')
    print(terminals)