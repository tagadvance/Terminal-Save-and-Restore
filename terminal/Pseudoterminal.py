from fcntl import ioctl
from termios import TIOCSTI
from typing import Optional

from terminal.Files import Files
from terminal.System import System


class Pseudoterminal:
    
    def __init__(self, ttyPath: str):
        self._path = ttyPath
    
    def exit(self):
        self.execute("exit")
    
    def execute(self, command: str, captureOutput: bool=False) -> Optional[str]:
        """
        Send a command to a pseudoterminal. Requires root privileges.
        """
        
        if not System.isRoot():
            raise RuntimeError("This method requires root privileges!")
        
        if captureOutput:
            output = Files.tmpName()
            command += "> {}".format(output)
        
        command += "\n"
        
        mode = "w"
        with open(self._path, mode) as fileDescriptor:
            for c in command:
                ioctl(fileDescriptor, TIOCSTI, c)
        
        if captureOutput:
            Files.waitUntilPathExists(output)
            with open(output) as handle:
                return handle.read()