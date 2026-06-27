import bpy
import random

step = 3
start = 0

base_building = bpy.data.objects["Cube"]
for x in range(5):
    new_building = base_building.copy()
    new_building.data = base_building.data.copy()
    
    new_building.location.x = start
    new_building.location.y = 0
    new_building.location.z = 0
    
    new_building.scale.z = random.uniform(1,5)
    
    bpy.context.collection.objects.link(new_building)
    
    start += step
 