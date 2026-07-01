import math
import random

import bpy

# --------------------------
# CONFIGURATION
# --------------------------

BUILDINGS_PER_SIDE = 5
CELL_SIZE = 6            # distance between buildings (grid system)
ROAD_WIDTH = 8           # empty space between left/right rows

MIN_BUILDING_HEIGHT = 2
MAX_BUILDING_HEIGHT = 8

ALLOWED_ROTATIONS = [0, math.radians(90), math.radians(180)]

BASE_TEMPLATES = ["Cube", "Cylinder", "Cone"]  # list of base building templates
BASE_NAME = "Cube"

available_templates = []  # list of available base building templates

for template_name in BASE_TEMPLATES:
    if template_name in bpy.data.objects:
        available_templates.append(bpy.data.objects[template_name])
    else:
        print(f"Error: Base template '{template_name}' not found in the scene.")


def clear_generated():
    for obj in bpy.data.objects:
        if obj.name.startswith("GEN_"):
            bpy.data.objects.remove(obj, do_unlink=True)

def create_building(template, location, height, rotation):
    obj = template.copy()
    obj.data = template.data.copy()

    obj.location = location

    obj.name = "GEN_building"

    obj.scale = (1,1, height)

    obj.rotation_euler = (0, 0, rotation)

    bpy.context.collection.objects.link(obj)

    return obj

def build_random_sides(side_offset):
        
        template = random.choice(available_templates)
        height = random.uniform(MIN_BUILDING_HEIGHT, MAX_BUILDING_HEIGHT)
        rotation = random.choice(ALLOWED_ROTATIONS)

        return template, height, rotation, side_offset



def generate_city():
    clear_generated()

    # grid center shift for road
    offset_y = ROAD_WIDTH / 2

    sides = [-offset_y, offset_y]

    if not available_templates:
        print("Error: No available base templates found. Cannot generate city.")
        return
    
    for i in range(BUILDINGS_PER_SIDE):
        start_x = -((BUILDINGS_PER_SIDE - 1) * CELL_SIZE) / 2
        x = start_x + i * CELL_SIZE

        for side in sides:

            template, height, rotation, side_offset = build_random_sides(side)

            create_building(template, (x, side_offset, 0), height, rotation)
            print(f"Selected base template: {template.name}")

generate_city()

print("City generated successfully.")