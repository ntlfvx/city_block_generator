import bpy
import random


def create_building(template, location, height, rotation):
    obj = template.copy()
    obj.data = template.data.copy()

    # location
    obj.location = location

    # unique name (VERY important for debugging/tools)
    obj.name = f"GEN_building_{random.randint(1000, 999999)}"

    # scale only Z (height variation)
    obj.scale = (1, 1, height)

    # rotation
    obj.rotation_euler = (0, 0, rotation)

    # safer linking (uses active collection)
    bpy.context.collection.objects.link(obj)

    return obj