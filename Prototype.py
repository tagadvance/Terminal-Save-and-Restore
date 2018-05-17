from fcntl import ioctl
from termios import TIOCSTI

with open('/dev/tty2', 'w') as fd:
    for c in "ls\n":
        ioctl(fd, TIOCSTI, c)