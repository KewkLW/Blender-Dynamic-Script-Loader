import bpy

def unbind_keymap_item(keymaps, keymap_name, idname, alt, shift, ctrl, type, value):
    """ Unbind a specific keymap item """
    km = keymaps[keymap_name]
    for kmi in km.keymap_items:
        if (kmi.idname == idname and kmi.alt == alt and kmi.shift == shift and 
                kmi.ctrl == ctrl and kmi.type == type and kmi.value == value):
            km.keymap_items.remove(kmi)
            print(f"Unbound {idname} from {keymap_name}")
            break

def bind_keymap_item(keymaps, keymap_name, idname, alt, shift, ctrl, type, value):
    """ Bind a keymap item with specified properties """
    km = keymaps[keymap_name]
    new_kmi = km.keymap_items.new(idname, type, value, shift=shift, ctrl=ctrl, alt=alt)
    print(f"Bound {idname} to {keymap_name} with {type} {value}")

# Get the keymap
wm = bpy.context.window_manager
keyconfigs = wm.keyconfigs
keymaps = keyconfigs.active.keymaps

# Unbind Alt + Middle Mouse from view2d.pan
unbind_keymap_item(keymaps, 'View2D', 'view2d.pan', alt=True, shift=False, ctrl=False, type='MIDDLEMOUSE', value='PRESS')

# Bind Alt + Middle Mouse to view3d.move
bind_keymap_item(keymaps, '3D View', 'view3d.move', alt=True, shift=False, ctrl=False, type='MIDDLEMOUSE', value='PRESS')
