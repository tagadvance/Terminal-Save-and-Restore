import glob
import logging
from shlex import quote
from subprocess import run, PIPE

from terminal.Files import Files
from terminal.Pseudoterminal import Pseudoterminal
from terminal.Shell import Shell
from terminal.System import System


class Terminals:
    
    @classmethod
    def listPseudoterminalsOwnedBy(cls, user: str=None) -> list:
        files = glob.glob("/dev/pts/*")
        return [file for file in files if Files.owner(file) == user] if user else files
    
    @classmethod
    def restore(cls, *, columns: int, rows: int, x: int, y: int, cwd: str, virtual_env: str, command: str=None):
        method = cls._restoreRoot if System.isRoot() else cls._restore
        method(columns, rows, x, y, cwd, virtual_env, command)
        
    @classmethod
    def _restore(cls, columns: int, rows: int, x: int, y: int, cwd: str, virtual_env: str, command: str):
        logging.warn("Must run as root to restore virtual environment and run command!, e.g. `sudo !!`")
        
        args = [
            "gnome-terminal",
            "--geometry",
            "{}x{}+{}+{}".format(columns, rows, x, y),
            "--working-directory",
            cwd
        ]
        run(args, stdout=PIPE)
        
    @classmethod
    def _restoreRoot(cls, columns: int, rows: int, x: int, y: int, cwd: str, virtual_env: str, command: str):
        beforeTerminals = cls.listPseudoterminalsOwnedBy()
        
        logname = Shell().logname()
        geometry = "{}x{}+{}+{}".format(columns, rows, x, y)
        args = [
            "su",
            "-",
            logname,
            "-c",
            "gnome-terminal --geometry {} --working-directory {}".format(geometry, quote(cwd))
        ]
        run(args, stdout=PIPE)
        
        afterTerminals = cls.listPseudoterminalsOwnedBy()
        terminals = list(set(afterTerminals) - set(beforeTerminals))
        if len(terminals) == 1:
            tty = terminals.pop()
            terminal = Pseudoterminal(tty)
            if virtual_env:
                cmd = "source {}/bin/activate".format(virtual_env)
                terminal.execute(cmd)
                terminal.execute("clear")
            if command:
                terminal.execute(command)
        else:
            logging.warn("Unable to restore virtual environment or run command due to ambiguous results!")