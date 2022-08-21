# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
import bpy.utils.previews

addon_keymaps = {}
_icons = None


class SNA_OT_Enable_All_Cloth__Cf9Cd(bpy.types.Operator):
    bl_idname = "sna.enable_all_cloth__cf9cd"
    bl_label = "Enable All Cloth "
    bl_description = "Enable All Cloth Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            for mod in obj.modifiers:
                if mod.type == "CLOTH":
                    mod.show_viewport = True
                    mod.show_render = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Disable_All_Cloth__3Fc69(bpy.types.Operator):
    bl_idname = "sna.disable_all_cloth__3fc69"
    bl_label = "Disable All Cloth "
    bl_description = "Disable All Cloth Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            for mod in obj.modifiers:
                if mod.type == "CLOTH":
                    mod.show_viewport = False
                    mod.show_render = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Enable_All_Corrective_Smooth__F7F60(bpy.types.Operator):
    bl_idname = "sna.enable_all_corrective_smooth__f7f60"
    bl_label = "Enable All Corrective Smooth "
    bl_description = "Enable All Corrective Smooth "
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            if obj.type == "MESH":
                for mod in obj.modifiers:
                    if mod.type == "CORRECTIVE_SMOOTH":
                        mod.show_viewport = True
                        mod.show_render = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Disable_All_Corrective_Smooth__1Fbc1(bpy.types.Operator):
    bl_idname = "sna.disable_all_corrective_smooth__1fbc1"
    bl_label = "Disable All Corrective Smooth "
    bl_description = "Disable All Corrective Smooth "
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            if obj.type == "MESH":
                for mod in obj.modifiers:
                    if mod.type == "CORRECTIVE_SMOOTH":
                        mod.show_viewport = False
                        mod.show_render = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Disable_All_Shrinkwrap_41082(bpy.types.Operator):
    bl_idname = "sna.disable_all_shrinkwrap_41082"
    bl_label = "Disable All Shrinkwrap"
    bl_description = "Disable All Shrinkwrap Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            for mod in obj.modifiers:
                if mod.type == "SHRINKWRAP":
                    mod.show_viewport = False
                    mod.show_render = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Enable_All_Shrinkwrap_C005A(bpy.types.Operator):
    bl_idname = "sna.enable_all_shrinkwrap_c005a"
    bl_label = "Enable All Shrinkwrap"
    bl_description = "Enable All Shrinkwrap Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            for mod in obj.modifiers:
                if mod.type == "SHRINKWRAP":
                    mod.show_viewport = True
                    mod.show_render = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Disable_All_Subsurf_3Ee13(bpy.types.Operator):
    bl_idname = "sna.disable_all_subsurf_3ee13"
    bl_label = "Disable All Subsurf"
    bl_description = "Disable All Subsurf Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            for mod in obj.modifiers:
                if mod.type == "SUBSURF":
                    mod.show_viewport = False
                    mod.show_render = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Enable_All_Subsurf_B931F(bpy.types.Operator):
    bl_idname = "sna.enable_all_subsurf_b931f"
    bl_label = "Enable All Subsurf"
    bl_description = "Enable All Subsurf Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            for mod in obj.modifiers:
                if mod.type == "SUBSURF":
                    mod.show_viewport = True
                    mod.show_render = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_MT_D9AB6(bpy.types.Menu):
    bl_idname = "SNA_MT_D9AB6"
    bl_label = "Toogles"

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw(self, context):
        layout = self.layout.column_flow(columns=1)
        layout.operator_context = "INVOKE_DEFAULT"
        layout.menu("SNA_MT_C4177", text="Smooth Corrective", icon_value=465)
        layout.menu("SNA_MT_45C0F", text="Cloth", icon_value=468)
        layout.menu("SNA_MT_1ED80", text="Wrap - Shrinkwrap", icon_value=461)
        layout.menu("SNA_MT_87208", text="Subsurf", icon_value=448)


class SNA_MT_C4177(bpy.types.Menu):
    bl_idname = "SNA_MT_C4177"
    bl_label = "Smooth Corrective"

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw(self, context):
        layout = self.layout.column_flow(columns=1)
        layout.operator_context = "INVOKE_DEFAULT"
        op = layout.operator(
            "sna.enable_all_corrective_smooth__f7f60",
            text="Enable " + "Smooth Corrective " + " | All Objects",
            icon_value=0,
            emboss=True,
            depress=False,
        )
        op = layout.operator(
            "sna.disable_all_corrective_smooth__1fbc1",
            text="Disable " + "Smooth Corrective " + " | All Objects",
            icon_value=0,
            emboss=True,
            depress=False,
        )


class SNA_MT_1ED80(bpy.types.Menu):
    bl_idname = "SNA_MT_1ED80"
    bl_label = "Shrinkwrap"

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw(self, context):
        layout = self.layout.column_flow(columns=1)
        layout.operator_context = "INVOKE_DEFAULT"
        op = layout.operator(
            "sna.enable_all_shrinkwrap_c005a",
            text="Enable " + "Shrinkwrap" + " | All Objects",
            icon_value=0,
            emboss=True,
            depress=False,
        )
        op = layout.operator(
            "sna.disable_all_shrinkwrap_41082",
            text="Disable " + "Shrinkwrap" + " | All Objects",
            icon_value=0,
            emboss=True,
            depress=False,
        )


class SNA_MT_45C0F(bpy.types.Menu):
    bl_idname = "SNA_MT_45C0F"
    bl_label = "Cloth"

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw(self, context):
        layout = self.layout.column_flow(columns=1)
        layout.operator_context = "INVOKE_DEFAULT"
        op = layout.operator(
            "sna.enable_all_cloth__cf9cd",
            text="Enable " + "Cloth" + " | All Objects",
            icon_value=0,
            emboss=False,
            depress=False,
        )
        op = layout.operator(
            "sna.disable_all_cloth__3fc69",
            text="Disable " + "Cloth" + " | All Objects",
            icon_value=0,
            emboss=True,
            depress=False,
        )


class SNA_MT_87208(bpy.types.Menu):
    bl_idname = "SNA_MT_87208"
    bl_label = "Subsurf"

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw(self, context):
        layout = self.layout.column_flow(columns=1)
        layout.operator_context = "INVOKE_DEFAULT"
        op = layout.operator(
            "sna.enable_all_subsurf_b931f",
            text="Enable " + "Subsurf" + " | All Objects",
            icon_value=0,
            emboss=True,
            depress=False,
        )
        op = layout.operator(
            "sna.disable_all_subsurf_3ee13",
            text="Disable " + "Subsurf" + " | All Objects",
            icon_value=0,
            emboss=True,
            depress=False,
        )


def sna_add_to_view3d_mt_editor_menus_D36DE(self, context):
    if not (False):
        layout = self.layout
        layout.menu("SNA_MT_D9AB6", text="Toggle Addons", icon_value=0)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_OT_Enable_All_Cloth__Cf9Cd)
    bpy.utils.register_class(SNA_OT_Disable_All_Cloth__3Fc69)
    bpy.utils.register_class(SNA_OT_Enable_All_Corrective_Smooth__F7F60)
    bpy.utils.register_class(SNA_OT_Disable_All_Corrective_Smooth__1Fbc1)
    bpy.utils.register_class(SNA_OT_Disable_All_Shrinkwrap_41082)
    bpy.utils.register_class(SNA_OT_Enable_All_Shrinkwrap_C005A)
    bpy.utils.register_class(SNA_OT_Disable_All_Subsurf_3Ee13)
    bpy.utils.register_class(SNA_OT_Enable_All_Subsurf_B931F)
    bpy.utils.register_class(SNA_MT_D9AB6)
    bpy.utils.register_class(SNA_MT_C4177)
    bpy.utils.register_class(SNA_MT_1ED80)
    bpy.utils.register_class(SNA_MT_45C0F)
    bpy.utils.register_class(SNA_MT_87208)
    bpy.types.VIEW3D_MT_editor_menus.append(sna_add_to_view3d_mt_editor_menus_D36DE)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_OT_Enable_All_Cloth__Cf9Cd)
    bpy.utils.unregister_class(SNA_OT_Disable_All_Cloth__3Fc69)
    bpy.utils.unregister_class(SNA_OT_Enable_All_Corrective_Smooth__F7F60)
    bpy.utils.unregister_class(SNA_OT_Disable_All_Corrective_Smooth__1Fbc1)
    bpy.utils.unregister_class(SNA_OT_Disable_All_Shrinkwrap_41082)
    bpy.utils.unregister_class(SNA_OT_Enable_All_Shrinkwrap_C005A)
    bpy.utils.unregister_class(SNA_OT_Disable_All_Subsurf_3Ee13)
    bpy.utils.unregister_class(SNA_OT_Enable_All_Subsurf_B931F)
    bpy.utils.unregister_class(SNA_MT_D9AB6)
    bpy.utils.unregister_class(SNA_MT_C4177)
    bpy.utils.unregister_class(SNA_MT_1ED80)
    bpy.utils.unregister_class(SNA_MT_45C0F)
    bpy.utils.unregister_class(SNA_MT_87208)
    bpy.types.VIEW3D_MT_editor_menus.remove(sna_add_to_view3d_mt_editor_menus_D36DE)
