import bpy

# =========================
# CONFIG (design layer)
# =========================
BUILDINGS_PER_SIDE = 5
CELL_SIZE = 6            # distance between buildings (grid system)
ROAD_WIDTH = 8           # empty space between left/right rows

BASE_NAME = "Cube"


def clear_generated():
    for obj in bpy.data.objects:
        if obj.name.startswith("GEN_"):
            bpy.data.objects.remove(obj, do_unlink=True)

def create_building(template, location):
    obj = template.copy()
    obj.data = template.data.copy()

    obj.location = location
    obj.name = "GEN_building"

    bpy.context.collection.objects.link(obj)

    return obj


def generate_city():
    clear_generated()

    base = bpy.data.objects[BASE_NAME]

    # grid center shift for road
    offset_y = ROAD_WIDTH / 2

    for i in range(BUILDINGS_PER_SIDE):

        x = i * CELL_SIZE

        # LEFT SIDE
        create_building(base, (x, -offset_y, 0))

        # RIGHT SIDE
        create_building(base, (x, offset_y, 0))

generate_city()

print("City generated successfully.")