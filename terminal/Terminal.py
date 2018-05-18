from fcntl import ioctl
from termios import TIOCSTI

from terminal.Files import Files


class Terminal:
    
    def __init__(self, ttyPath: str):
        self._path = ttyPath
    
    def metaData(self):
        xwininfo = self._xwininfo()
        return {
            'x': xwininfo['Absolute upper-left X'],
            'y': xwininfo['Absolute upper-left Y'],
            'columns': self.execute("tput cols").strip(),
            'rows': self.execute("tput lines").strip(),
            'cwd': self.execute("pwd").strip(),
            'virtual_env': self.execute("echo $VIRTUAL_ENV").strip(),
            # TODO: title
        }
        
    def _xwininfo(self):
        prefix = "  "
        delimiter = ':'
        
        data = {}
        
        command = "xwininfo -id $(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')"
        xwininfo = self.execute(command)
        for line in xwininfo.splitlines():
            if line.startswith(prefix) and delimiter in line:
                tokens = line.split(delimiter)
                key, value = map(str.strip, tokens)
                data[key] = value
                
        return data
    
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