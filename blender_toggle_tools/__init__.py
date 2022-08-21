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

bl_info = {
    "name" : "Blender Toggle Tools",
    "author" : "SmittyWerben", 
    "description" : "Toggle Various Options For many Objects",
    "blender" : (3, 0, 0),
    "version" : (0, 1, 3),
    "location" : "3D-Viewe > Top Bar",
    "warning" : "",
    "doc_url": "https://github.com/SmittyWerbenJJ/BlenderToggleTools/wiki", 
    "tracker_url": "https://github.com/SmittyWerbenJJ/BlenderToggleTools/issues", 
    "category" : "3D View" 
}

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

