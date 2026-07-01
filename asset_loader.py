import bpy
import config

def load_templates():

    available_templates = []

    for template_name in config.BASE_TEMPLATES:
        if template_name in bpy.data.objects:
            available_templates.append(bpy.data.objects[template_name])
        else:
            print(f"Error: Base template '{template_name}' not found in the scene.")

    return available_templates