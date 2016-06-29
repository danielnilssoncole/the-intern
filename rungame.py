#Run the game

from mapengine import *
from scenes import *

map = Map('interview')

engine = Engine(map)

engine.play()