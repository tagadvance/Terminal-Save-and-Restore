from subprocess import run, PIPE


class System:
    
    @staticmethod
    def logname():
        result = run(["logname"], stdout=PIPE)
        return result.stdout.decode('utf-8').strip()
