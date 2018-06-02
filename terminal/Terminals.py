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
    def restore(cls, *, columns: int, rows: int, x: int, y: int, cwd: str, virtual_env: str, command: str):
        isRoot = System.isRoot()
        if isRoot:
            logging.warn("Must run as root to restore virtual environment and run command!, e.g. `sudo !!`")
        
        if isRoot:
            beforeTerminals = cls.listPseudoterminalsOwnedBy()
        
        geometry = "{}x{}+{}+{}".format(columns, rows, x, y)
        
        if isRoot:
            logname = System.logname()
            args = [
                "su",
                "-",
                logname,
                "-c",
                "gnome-terminal --geometry {} --working-directory '{}'".format(geometry, cwd)
            ]
        else:            
            args = [
                "gnome-terminal",
                "--geometry",
                geometry,
                "--working-directory",
                cwd
            ]
        run(args, stdout=PIPE)
        
        if isRoot:
            afterTerminals = cls.listPseudoterminalsOwnedBy()
            terminals = list(set(afterTerminals) - set(beforeTerminals))
            if len(terminals) == 1:
                tty = terminals.pop()
                terminal = Terminal(tty)
                if virtual_env:
                    cmd = "source {}/bin/activate".format(virtual_env)
                    terminal.execute(cmd)
                    terminal.execute("clear")
                if command:
                    terminal.execute(command)
            else:
                logging.warn("Unable to restore virtual environment or run command due to ambiguous results!")
        
        # TODO: restore sudo su