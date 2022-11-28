import os
import time
from load import *
from colorama import init
init()
from colorama import Fore, Back, Style

ErrExcept = lambda: print('     A file name cannot contain any of the following characters: \/:*?"<>|')
ActionFailed = lambda: print(f'{Fore.RED}     Action failed')
Done = lambda: print(f'{Fore.GREEN}     done')

class DirActions():
    # Made
    def MadeDir():
        forbiddenchars = ['<','>',':','"','/','|','?','*']
        path = input('Absolute path of directory >')
        title = input('Name of directory >')
        time.sleep(1)
        while title in forbiddenchars:
            ErrExcept()
            title = input('Name of directory >')
        try:
            LoadActions.MadeLoad()
            os.mkdir(f'{path}\{title}')
        except Exception:
            ActionFailed()
        else:
            Done()

    # Removed
    def RemoveDir():
        path = input('Absolute path of directory >')
        title = input('Name of directory >')
        time.sleep(1)
        try:
            LoadActions.RemoveLoad()
            os.rmdir(f'{path}\{title}')
        except Exception:
            ActionFailed()
        else:
           Done()

    # Rename
    def RenameDir():
        forbiddenchars = ['<','>',':','"','/','|','?','*']
        path = input('Absolute path of directory >')
        title = input('Name of directory >')
        NewTitle = input('New name of directiry >')
        while NewTitle in forbiddenchars:
            ErrExcept()
            NewTitle = input('New name of directory >')
        time.sleep(1)
        try:
            LoadActions.RenameLoad()
            os.rename(f'{path}\{title}', f'{path}\{NewTitle}')
        except Exception:
            ActionFailed()
        else:
            Done()