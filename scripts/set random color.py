import bpy

def assign_material_to_selection(obj):
    def create_unique_random_color():
        import random  # Importing random inside the function
        while True:
            color = (random.random(), random.random(), random.random(), 1)
            if all([color != mat.diffuse_color for mat in bpy.data.materials]):
                return color

    if not obj or obj.type != 'MESH':
        print("No mesh object selected")
        return

    # Check if the object has any materials
    if not obj.data.materials:
        # Add a default material if none exist
        default_mat = bpy.data.materials.new(name="DefaultMat")
        obj.data.materials.append(default_mat)

    # Create a new material with a unique color
    mat_name = f"RandomMat_{len(bpy.data.materials)}"
    mat = bpy.data.materials.new(name=mat_name)
    mat.diffuse_color = create_unique_random_color()

    # Add the new material to the object
    obj.data.materials.append(mat)
    mat_index = obj.data.materials.find(mat.name)

    # Assign the new material to selected faces
    bpy.ops.object.mode_set(mode='OBJECT')  # Switch to object mode
    mesh = obj.data
    for poly in mesh.polygons:
        if poly.select:
            poly.material_index = mat_index
    bpy.ops.object.mode_set(mode='OBJECT')  # Switch back to object mode

# Example usage
obj = bpy.context.active_object
assign_material_to_selection(obj)
