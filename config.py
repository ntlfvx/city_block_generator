import math

BUILDINGS_PER_SIDE = 5
CELL_SIZE = 6            # distance between buildings (grid system)
ROAD_WIDTH = 8           # empty space between left/right rows

MIN_BUILDING_HEIGHT = 2
MAX_BUILDING_HEIGHT = 8

ALLOWED_ROTATIONS = [0, math.radians(90), math.radians(180)]

BASE_TEMPLATES = ["Cube", "Cylinder", "Cone"] 