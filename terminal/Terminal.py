from fcntl import ioctl
from termios import TIOCSTI

from terminal.Files import Files


class Terminal:
    
    def __init__(self, ttyPath: str):
        self._path = ttyPath
    
    def exit(self):
        self.execute("exit")
    
    def execute(self, command: str) -> str:
        """
        Send a command to a pseudoterminal. Requires root.
        """
        
        output = Files.tmpName()
        command += "> {}\n".format(output)
        
        mode = "w"
        with open(self._path, mode) as fileDescriptor:
            for c in command:
                ioctl(fileDescriptor, TIOCSTI, c)
        
        Files.waitUntilPathExists(output)
        with open(output) as handle:
            return handle.read()