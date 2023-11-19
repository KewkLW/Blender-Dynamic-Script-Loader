import bpy

# Function to mark all meshes and collections as assets
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

# Call the function to mark all meshes and collections as assets
mark_assets()
