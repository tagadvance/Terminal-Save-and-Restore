import json
import os
from os import path

from terminal.System import System
from terminal.Terminals import Terminals


class Session:
    
    CONFIG_DIRECTORY = '/home/{}/.config/terminal-sessions'
    
    def __init__(self, name: str):
        self._name = name
        
        path = Session._configDirectory()
        self._file = '{}/{}.json'.format(path, self._name)
    
    def list(self) -> list:
        return self._read().keys()
    
    def addToSession(self, name: str, metaData: dict):
        session = self._read(False)
        session[name] = metaData
        self._write(session)

    def removeFromSession(self, name: str):
        session = self._read()
        del session[name]
        self._write(session)
    
    def restore(self, name: str):
        sessions = self._read()
        if name == "*":
            for meta in sessions.values():
                Terminals.restore(**meta)
        else:
            Terminals.restore(**sessions[name])
    
    def _read(self, raiseErrorIfNotExist: bool=True) -> dict:
        if not path.exists(self._file):
            if raiseErrorIfNotExist:
                message = "Session '{}' does not exist!".format(self._name)
                raise RuntimeError(message)
            return {}
        
        with open(self._file) as handle:
            return json.load(handle)
    
    def _write(self, session: dict):
        Session._createConfigDirectory()
        with open(self._file, 'w') as handle:
            json.dump(session, handle, indent=4)
    
    @classmethod
    def _configDirectory(cls) -> str:
        logname = System.logname()
        return cls.CONFIG_DIRECTORY.format(logname)
    
    @classmethod
    def _createConfigDirectory(cls):
        path = cls._configDirectory()
        mode = 0o700
        os.makedirs(path, mode, True)
