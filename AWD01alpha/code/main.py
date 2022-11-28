import ActionsWithDirectory
import sys

err = lambda: print('No such argument exists.')

def Action():
    print("ACTION         1 - MakeDir, 2 - RemoveDir, 3 - RenameDir.\n               action [number action].")
    action = input('>')
    if action == 'action 1':
        ActionsWithDirectory.DirActions.MadeDir()
    elif action == 'action 2':
        ActionsWithDirectory.DirActions.RemoveDir()
    elif action == 'action 3':
        ActionsWithDirectory.DirActions.RenameDir()
    else:
        err()
    
    sys.exit()