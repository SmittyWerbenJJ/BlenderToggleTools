for obj in bpy.context.scene.objects:    
    if obj.type=="MESH":
        for mod in obj.modifiers:    
            if mod.type=="CORRECTIVE_SMOOTH":
                mod.show_viewport=True
                mod.show_render=True
