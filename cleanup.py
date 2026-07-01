import bpy

def clear_generated():
    for obj in list(bpy.data.objects):
        if obj.name.startswith("GEN_"):
            bpy.data.objects.remove(obj, do_unlink=True)