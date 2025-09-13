import os
import eel
from engine.features import *
from engine.command import *

eel.init("front")
playAssistantSound()

eel.start('index.html', mode='chrome', host='localhost', block=True)