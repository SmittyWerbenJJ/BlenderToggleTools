import bpy

for obj in bpy.context.scene.objects:
    for mod in obj.modifiers:
        if mod.type == "SUBSURF":
            mod.show_viewport = True
            mod.show_render = True
