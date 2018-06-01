import glob
import logging
from subprocess import run, PIPE

from terminal.Files import Files
from terminal.System import System
from terminal.Terminal import Terminal


class Terminals:
    
    @staticmethod
    def tty():
        """
        Originally this was going to be used to exclude the current terminal; however, I decided to
        use a shell script to have this script disconnect and run in the background.
        """
        
        result = run(["tty"], stdout=PIPE)
        return result.stdout.decode('utf-8').strip()
    
    @classmethod
    def listPseudoterminalsOwnedBy(cls, user: str=None) -> list:
        files = glob.glob("/dev/pts/*")
        return [file for file in files if Files.owner(file) == user] if user else files
    
    @classmethod
    def restore(cls, *, columns: int, rows: int, x: int, y: int, cwd: str, virtual_env: str):
        isRoot = System.isRoot()
        if virtual_env and not isRoot:
            logging.warn("Must run as root to restore virtual environments!, e.g. `sudo !!`")
        
        if virtual_env and isRoot:
            beforeTerminals = cls.listPseudoterminalsOwnedBy()
        
        args = [
            "gnome-terminal",
            "--geometry",
            "{}x{}+{}+{}".format(columns, rows, x, y),
            "--working-directory",
            cwd
        ]
        run(args, stdout=PIPE)
        
        if virtual_env and isRoot:
            afterTerminals = cls.listPseudoterminalsOwnedBy()
            terminals = list(set(afterTerminals) - set(beforeTerminals))
            if len(terminals) == 1:
                tty = terminals.pop()
                terminal = Terminal(tty)
                command = "source {}/bin/activate".format(virtual_env)
                terminal.execute(command)
                terminal.execute("clear")
            else:
                logging.warn("Unable to restore virtual environment due to ambiguous results!")
        
        # TODO: restore sudo su