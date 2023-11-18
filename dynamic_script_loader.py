bl_info = {
    "name": "Dynamic Script Buttons",
    "description": "Creates a panel with buttons to run scripts from a user-specified folder and a refresh button",
    "author": "Hai, I'm Kewk",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Tools",
    "category": "Development",
}

import bpy
import os

def get_scripts_folder():
    user_preferences = bpy.context.preferences
    addon_prefs = user_preferences.addons[__name__].preferences
    return addon_prefs.scripts_folder

# Global variable to store scripts
loaded_scripts = []

def load_scripts():
    global loaded_scripts
    scripts_folder = get_scripts_folder()
    loaded_scripts.clear()
    if os.path.isdir(scripts_folder):
        for file in os.listdir(scripts_folder):
            if file.endswith(".py"):
                loaded_scripts.append(file)

class ExecuteScriptOperator(bpy.types.Operator):
    """Execute Script"""
    bl_idname = "wm.execute_script"
    bl_label = "Execute Script"
    script_name: bpy.props.StringProperty()

    def execute(self, context):
        filepath = os.path.join(get_scripts_folder(), self.script_name)
        exec(compile(open(filepath).read(), filepath, 'exec'))
        return {'FINISHED'}

class RefreshScriptsOperator(bpy.types.Operator):
    """Refresh Scripts List"""
    bl_idname = "wm.refresh_scripts"
    bl_label = "Refresh Scripts"

    def execute(self, context):
        load_scripts()
        # Redraw the UI to reflect changes
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()
        return {'FINISHED'}

class ScriptsPanel(bpy.types.Panel):
    """Creates a Panel in the 3D View Tool Shelf to run scripts"""
    bl_label = "Dynamic Scripts"
    bl_idname = "VIEW3D_PT_dynamic_scripts"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        # Refresh button
        layout.operator("wm.refresh_scripts", text="Refresh Scripts", icon='FILE_REFRESH')
        # Script buttons
        for script in loaded_scripts:
            op = layout.operator("wm.execute_script", text=script)
            op.script_name = script

class DynamicScriptButtonsAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    scripts_folder: bpy.props.StringProperty(
        name="Scripts Folder",
        subtype='DIR_PATH',
        default="//"
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "scripts_folder")

def register():
    bpy.utils.register_class(ExecuteScriptOperator)
    bpy.utils.register_class(RefreshScriptsOperator)
    bpy.utils.register_class(ScriptsPanel)
    bpy.utils.register_class(DynamicScriptButtonsAddonPreferences)
    load_scripts()

def unregister():
    bpy.utils.unregister_class(ExecuteScriptOperator)
    bpy.utils.unregister_class(RefreshScriptsOperator)
    bpy.utils.unregister_class(ScriptsPanel)
    bpy.utils.unregister_class(DynamicScriptButtonsAddonPreferences)

if __name__ == "__main__":
    register()
