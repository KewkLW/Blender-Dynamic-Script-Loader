import bpy

def create_collections_from_empties():
    # Iterate through all objects in the scene
    for obj in list(bpy.context.scene.objects):  # Convert to list to prevent iteration issues
        # Check if the object is an empty
        if obj.type == 'EMPTY':
            # Create a new collection with the same name as the empty
            new_collection = bpy.data.collections.new(name=obj.name)
            bpy.context.scene.collection.children.link(new_collection)

            # Link the empty to the new collection
            new_collection.objects.link(obj)
            
            # Get a list of all objects parented to the empty
            children = [child for child in obj.children]
            
            # Move the objects to the new collection and unparent them while keeping their transformations
            for child in children:
                # Store the current world matrix of the child
                current_matrix = child.matrix_world.copy()
                
                # Unparent the object
                child.parent = None
                
                # Restore the world matrix to keep the transformation
                child.matrix_world = current_matrix
                
                # Link object to the new collection
                new_collection.objects.link(child)
                
            # Delete the empty
            bpy.data.objects.remove(obj, do_unlink=True)

# Call the function to create collections from empties
create_collections_from_empties()

def mark_assets():
    # Mark all mesh objects as assets
    for obj in bpy.data.objects:
        if obj.type == 'MESH':  # Ensure the object is a mesh
            if not obj.asset_data:  # Check if the object is already marked as an asset
                obj.asset_mark()  # Mark the object as an asset
                print(f'Marked {obj.name} as an asset.')  # Print a message for each marked object
            else:
                print(f'{obj.name} is already marked as an asset.')  # Print a message if the object is already marked as an asset
                
    # Mark all collections as assets
    for collection in bpy.data.collections:
        if not collection.asset_data:  # Check if the collection is already marked as an asset
            collection.asset_mark()  # Mark the collection as an asset
            print(f'Marked collection {collection.name} as an asset.')  # Print a message for each marked collection
        else:
            print(f'Collection {collection.name} is already marked as an asset.')  # Print a message if the collection is already marked as an asset

    # Mark all materials as assets
    for material in bpy.data.materials:
        if not material.asset_data:  # Check if the material is already marked as an asset
            material.asset_mark()  # Mark the material as an asset
            print(f'Marked material {material.name} as an asset.')  # Print a message for each marked material
        else:
            print(f'Material {material.name} is already marked as an asset.')  # Print a message if the material is already marked as an asset

# Call the function to mark all meshes, collections, and materials as assets
mark_assets()
