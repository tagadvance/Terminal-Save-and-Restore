from fcntl import ioctl
from termios import TIOCSTI

class Terminal:
    
    def __init__(self, ttyPath):
        self._path = ttyPath
    
    def execute(self, command):
        mode = 'w'
        with open(self._path, mode) as fileDescriptor:
            for c in command:
                ioctl(fileDescriptor, TIOCSTI, c)