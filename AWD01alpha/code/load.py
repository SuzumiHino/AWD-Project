from rich.progress import Progress
import time

def ProgressBar(desc):
    with Progress() as progress:
        task = progress.add_task(f'[green]{desc}', total=100)
        while not progress.finished:
            progress.update(task, advance=15)
            time.sleep(.1)

class LoadActions():
    def MadeLoad():
        ProgressBar('          Making:\n')
    def RemoveLoad():
        ProgressBar('          Removal:\n')
    def RenameLoad():
        ProgressBar('          Renaming:\n')
