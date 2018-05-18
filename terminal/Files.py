from datetime import datetime, timedelta
from os import stat, path
from pwd import getpwuid
import tempfile
from time import sleep


class Files:
    
    @staticmethod
    def owner(filePath: str) -> str:
            return getpwuid(stat(filePath).st_uid).pw_name
    
    @staticmethod
    def tmpName() -> str:
        '''
        Return the path to a temporary file.
        '''
        
        tempdir = tempfile._get_default_tempdir()
        name = next(tempfile._get_candidate_names())
        return '{}/{}'.format(tempdir, name)
    
    @staticmethod
    def waitUntilPathExists(filePath: str, limit:timedelta=timedelta(minutes=1)):
        start = datetime.now()
        
        seconds = .1
        while not path.exists(filePath):
            now = datetime.now()
            if now - start > limit:
                raise TimeoutError()
            
            sleep(seconds)