import bpy

for obj in bpy.context.scene.objects:
    for mod in obj.modifiers:
        if mod.type == "SUBSURF":
            mod.show_viewport = False
            mod.show_render = False
