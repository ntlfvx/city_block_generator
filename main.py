import bpy
import os
import sys

project_dir = os.path.dirname(bpy.data.filepath)

if project_dir not in sys.path:
    sys.path.append(project_dir)

print("Project dir:", project_dir)


import asset_loader
import cg_generator

templates = asset_loader.load_templates()

cg_generator.generate_city(templates)

print("City generated successfully.")