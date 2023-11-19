import bpy

# This function will set 'loadui' to False by default
def set_loadui_default_false():
    bpy.context.preferences.filepaths.use_load_ui = False

# Running the function to apply the setting
set_loadui_default_false()
