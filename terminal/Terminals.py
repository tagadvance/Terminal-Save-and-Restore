import glob
from subprocess import run, PIPE

from terminal.Files import Files


class Terminals:
    
    @staticmethod
    def tty():
        """
        Originally this was going to be used to exclude the current terminal; however, I decided to
        use a shell script to have this script disconnect and run in the background.
        """
        
        result = run(["tty"], stdout=PIPE)
        return result.stdout.decode('utf-8').strip()
    
    @staticmethod
    def logname():
        result = run(["logname"], stdout=PIPE)
        return result.stdout.decode('utf-8').strip()
    
    @classmethod
    def listPseudoterminalsOwnedBy(cls, user: str=None) -> list:
        files = glob.glob("/dev/pts/*")
        return [file for file in files if Files.owner(file) == user] if user else files
    
    @staticmethod
    def restore(*, columns: int, rows: int, x: int, y: int, cwd: str, virtual_env: str):
        args = [
            "gnome-terminal",
            "--geometry",
            "{}x{}+{}+{}".format(columns, rows, x, y),
            "--working-directory",
            cwd
        ]
        print(" ".join(args))
        run(args, stdout=PIPE)
        
        # TODO: restore virtual environment
        # TODO: restore sudo su