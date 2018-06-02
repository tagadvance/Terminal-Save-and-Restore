from subprocess import run, PIPE


class Shell:
    
    def logname(self):
        #result = run(["logname"], stdout=PIPE)
        #return result.stdout.decode('utf-8').strip()
        return self.execute("echo ${SUDO_USER:-${USER}}")
    
    def metaData(self):
        xwininfo = self._xwininfo()
        return {
            'x': xwininfo['Absolute upper-left X'],
            'y': xwininfo['Absolute upper-left Y'],
            'columns': self.execute("tput cols"),
            'rows': self.execute("tput lines"),
            'cwd': self.execute("pwd"),
            'virtual_env': self.execute("echo $VIRTUAL_ENV"),
            # TODO: title
        }
        
    def _xwininfo(self):
        prefix = "  "
        delimiter = ":"
        
        data = {}
        
        command = "xwininfo -id $(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')"
        xwininfo = self.execute(command)
        
        for line in xwininfo.splitlines():
            if line.startswith(prefix) and delimiter in line:
                tokens = line.split(delimiter)
                key, value = map(str.strip, tokens)
                data[key] = value
                
        return data

    def execute(self, command: str) -> str:
        result = run(command, shell=True, check=True, stdout=PIPE)
        return result.stdout.decode('utf-8').strip()