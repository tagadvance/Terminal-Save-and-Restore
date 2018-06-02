import os
from subprocess import run, PIPE


class System:
    
    @staticmethod
    def isRoot():
        return os.geteuid() == 0
    
    @staticmethod
    def logname():
        #result = run(["logname"], stdout=PIPE)
        result = run("echo ${SUDO_USER:-${USER}}", shell=True, check=True, stdout=PIPE)
        return result.stdout.decode('utf-8').strip()
