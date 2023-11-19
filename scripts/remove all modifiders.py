import bpy

# Loop through all selected objects
for obj in bpy.context.selected_objects:
    # Check if the object is a mesh
    if obj.type == 'MESH':
        # Iterate over all modifiers of the object and remove them
        for modifier in obj.modifiers:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_remove(modifier=modifier.name)
