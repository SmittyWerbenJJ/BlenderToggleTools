import bpy
from . import addon_updater_ops
from . import addon_updater_ui
from . import addon_updater
from . import toggle_tools

modules = [addon_updater_ui, toggle_tools]


def register():
    addon_updater_ops.register(bl_info)
    for module in modules:
        module.register()


def unregister():
    addon_updater_ops.unregister()
    for module in modules:
        module.unregister()
