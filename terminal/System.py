import os

from terminal.Shell import Shell


class System:
    
    @staticmethod
    def isRoot():
        return os.geteuid() == 0
    
    @staticmethod
    def logname():
        #result = run(["logname"], stdout=PIPE)
        #return result.stdout.decode('utf-8').strip()
        return Shell().execute("echo ${SUDO_USER:-${USER}}")
