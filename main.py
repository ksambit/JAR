import os
import eel
from engine.features import *
from engine.command import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def list_files(dir='.'):
    try:
        return os.listdir(dir)
    except OSError:
        return []

eel.init("front")

playAssistantSound()

eel.start('index.html', mode='chrome', host='localhost', block=True)