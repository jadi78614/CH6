import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]

# hd = float(request.form.get('head', 0.95))  
# t = float(request.form.get('torso', 0.85))
# l = float(request.form.get('legs', 1.10))
# c = float(request.form.get('calves', 0.90))
# s = float(request.form.get('shoulders', 0.80))
# a = float(request.form.get('arms', 0.85))
# fa = float(request.form.get('forearms', 0.85))
# hp = float(request.form.get('hips', 1.10))
# h = float(request.form.get('height', 0.95))

hd = float(argv[0]) / 0.95
t = float(argv[1]) / 0.85
l = float(argv[2]) / 1.10
c = float(argv[3]) / 0.90
s = float(argv[4]) / 0.80
a = float(argv[5]) / 0.85
fa = float(argv[6]) / 0.85
hp = float(argv[7]) / 1.10
h = float(argv[8]) / 0.95

ob = bpy.context.object
me = ob.data
is_editmode = me.is_editmode

bpy.ops.object.mode_set(mode='EDIT')

# HEAD
ob.vertex_groups.active = ob.vertex_groups["Head"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(hd, hd, hd),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.18,
    use_proportional_connected=False,
    use_proportional_projected=False
)

# TORSO
ob.vertex_groups.active = ob.vertex_groups["Torso"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(t, t, 1),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.18,
    use_proportional_connected=False,
    use_proportional_projected=False
)

# LEGS
ob.vertex_groups.active = ob.vertex_groups["Leg"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(l, l, l),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.163508,
    use_proportional_connected=False,
    use_proportional_projected=False
)

# CALVES
ob.vertex_groups.active = ob.vertex_groups["Calves"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(c, c, c),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.15,
    use_proportional_connected=False,
    use_proportional_projected=False
)

# SHOULDERS
ob.vertex_groups.active = ob.vertex_groups["Shoulder"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(s, s, s),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.20,
    use_proportional_connected=False,
    use_proportional_projected=False
)

# HIPS
ob.vertex_groups.active = ob.vertex_groups["Hips"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(hp, hp, hp),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.24,
    use_proportional_connected=False,
    use_proportional_projected=False
)

# ARMS
ob.vertex_groups.active = ob.vertex_groups["Arm"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(a, a, a),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.1,
    use_proportional_connected=False,
    use_proportional_projected=False
)

# FOREARMS
ob.vertex_groups.active = ob.vertex_groups["Forearm"]
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_select()

bpy.ops.transform.resize(
    value=(fa, fa, fa),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=True,
    proportional_edit_falloff='SMOOTH',
    proportional_size=0.1,
    use_proportional_connected=False,
    use_proportional_projected=False
)

bpy.ops.object.editmode_toggle()

# HEIGHT
bpy.ops.transform.resize(
    value=(h, h, h),
    orient_type='GLOBAL',
    orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    orient_matrix_type='GLOBAL',
    mirror=True,
    use_proportional_edit=False,
)

bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

# Ensure you're working with the correct object
bpy.context.view_layer.objects.active = ob  # Set the active object to the intended one

# Apply transformations before exporting
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

# Ensure to exit Edit Mode if you are in it
if bpy.context.active_object.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='OBJECT')

# Deselect all objects to ensure only the active one is exported
bpy.ops.object.select_all(action='DESELECT')
ob.select_set(True)  # Select the active object

# Export the selected object only
exportPath = "/Users/phun/Downloads/3D-Human-Body-Generator/pythonscripts/projectexports/generatedbody.glb"
bpy.ops.export_scene.gltf(filepath=exportPath, use_selection=True)




# import bpy
# import sys

# argv = sys.argv
# argv = argv[argv.index("--") + 1:]

# # Scaling factors from input
# hd = float(argv[0]) / 0.95
# t = float(argv[1]) / 0.85
# l = float(argv[2]) / 1.10
# c = float(argv[3]) / 0.90
# s = float(argv[4]) / 0.80
# a = float(argv[5]) / 0.85
# fa = float(argv[6]) / 0.85
# hp = float(argv[7]) / 1.10
# h = float(argv[8]) / 0.95

# # Reference to the object
# ob = bpy.context.object
# me = ob.data

# # Log available vertex groups
# print("Available vertex groups:")
# for group in ob.vertex_groups:
#     print(group.name)

# # Function to get a vertex group if it exists, or print a warning
# def get_vertex_group(name):
#     if name in ob.vertex_groups:
#         return ob.vertex_groups[name]
#     else:
#         print(f"Warning: Vertex group '{name}' not found.")
#         return None

# # Ensure we are in Edit Mode to select and transform vertices
# bpy.ops.object.mode_set(mode='EDIT')

# # HEAD
# head_group = get_vertex_group("Head")  # Update this name if necessary
# if head_group:
#     ob.vertex_groups.active = head_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(hd, hd, hd),
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.18,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # TORSO
# torso_group = get_vertex_group("Torso")  # Update this name if necessary
# if torso_group:
#     ob.vertex_groups.active = torso_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(t, t, 1),
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.18,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # SHOULDERS
# shoulders_group = get_vertex_group("Shoulder")  # Update this name if necessary
# if shoulders_group:
#     ob.vertex_groups.active = shoulders_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(s, s, s),
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.20,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # HIPS
# hips_group = get_vertex_group("Hips")  # Update this name if necessary
# if hips_group:
#     ob.vertex_groups.active = hips_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(hp, hp, hp),
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.24,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # LEGS - Bring them closer by reducing the width significantly
# legs_group = get_vertex_group("Leg")  # Update this name if necessary
# if legs_group:
#     ob.vertex_groups.active = legs_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(l * 0.2, l, l * 0.2),  # Reduce width to bring legs closer
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.1,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # CALVES - Bring them closer as well
# calves_group = get_vertex_group("Calves")  # Update this name if necessary
# if calves_group:
#     ob.vertex_groups.active = calves_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(c * 0.5, c * 0.5, c),  # Adjust to make them narrower and closer
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.08,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # ARMS
# arms_group = get_vertex_group("Arm")  # Update this name if necessary
# if arms_group:
#     ob.vertex_groups.active = arms_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(a, a, a),
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.1,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # FOREARMS
# forearms_group = get_vertex_group("Forearm")  # Update this name if necessary
# if forearms_group:
#     ob.vertex_groups.active = forearms_group
#     bpy.ops.mesh.select_all(action='DESELECT')
#     bpy.ops.object.vertex_group_select()
#     bpy.ops.transform.resize(
#         value=(fa, fa, fa),
#         orient_type='GLOBAL',
#         mirror=True,
#         use_proportional_edit=True,
#         proportional_edit_falloff='SMOOTH',
#         proportional_size=0.1,
#         use_proportional_connected=False,
#         use_proportional_projected=False
#     )

# # Exit Edit Mode
# bpy.ops.object.editmode_toggle()

# # HEIGHT - Adjust overall height
# bpy.ops.transform.resize(
#     value=(h, h, h),
#     orient_type='GLOBAL',
#     mirror=True,
#     use_proportional_edit=False,
# )

# bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

# # Ensure the object is active
# bpy.context.view_layer.objects.active = ob  # Set the active object to the intended one

# # Apply transformations before exporting
# bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

# # Ensure to exit Edit Mode if you are in it
# if bpy.context.active_object.mode == 'EDIT':
#     bpy.ops.object.mode_set(mode='OBJECT')

# # Deselect all objects to ensure only the active one is exported
# bpy.ops.object.select_all(action='DESELECT')
# ob.select_set(True)  # Select the active object

# # Export the selected object only
# exportPath = "/Users/phun/Downloads/3D-Human-Body-Generator/pythonscripts/projectexports/generatedbody_withcloserlegs.glb"
# bpy.ops.export_scene.gltf(filepath=exportPath, use_selection=True)
