# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     # Process face indices; assumes only the first part of the '1/1/1' format is needed
#                     face = []
#                     for f in parts[1:]:
#                         # Extract the vertex index from 'vertex/texture/normal'
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces


# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(map(str, f)) + '\n')

# def scale_pants(vertices, scale_factors):
#     # Example scale factors for waist, length, thighs
#     waist_scale, length_scale, thigh_scale = scale_factors
#     # Scale waist (assumed to be vertices with y-coordinate in a specific range)
#     for i, vertex in enumerate(vertices):
#         if vertex[1] > 2:  # Adjust this condition based on your model specifics
#             vertices[i][0] *= waist_scale  # scale x for waist width

#         # Scale length (z scaling)
#         vertices[i][2] *= length_scale

#         # Scale thighs (assuming x and y coordinates)
#         if vertex[1] < 2 and vertex[1] > 0.5:  # Adjust these conditions
#             vertices[i][0] *= thigh_scale
#             vertices[i][1] *= thigh_scale

#     return vertices

# # Load the OBJ file
# vertices, faces = load_obj('./test_data/meshes/pants/lower_5.obj')

# # Scale factors: [waist scale, length scale, thigh scale]
# scaled_vertices = scale_pants(vertices, [1.1, 1.05, 1.2])  # Increase width, length, and thigh sizes

# # Save the modified model
# save_obj('modified_lower_5.obj', scaled_vertices, faces)
# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     # Process the faces, taking only the vertex index from compound indices
#                     face = []
#                     for f in parts[1:]:
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx) for idx in f) + '\n')

# def widen_pants(vertices, width_factor):
#     # Modify the x-coordinate to widen the pants
#     for vertex in vertices:
#         vertex[0] *= width_factor
#     return vertices

# # Path to the original OBJ file
# input_file = './test_data/meshes/pants/lower_5.obj'
# # Path to save the modified OBJ file
# output_file = 'widened_lower_5.obj'

# # Load the original OBJ
# vertices, faces = load_obj(input_file)

# # Widen the pants by a factor (e.g., 1.2 for 20% wider)
# widened_vertices = widen_pants(vertices, 1.2)

# # Save the modified model to a new OBJ file
# save_obj(output_file, widened_vertices, faces)

#--------------------------------------------------------------------------------------------------------------


# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx) for idx in f) + '\n')

# def modify_pants(vertices, waist_factor, length_factor, thigh_factor):
#     # Adjust these ranges to fit your model's specific scale and proportions
#     waist_height_min, waist_height_max = 1.0, 1.5  # Min and max y-coordinates for the waist
#     thigh_height_min, thigh_height_max = 0.2, 0.9  # Min and max y-coordinates for the thighs
    
#     for vertex in vertices:
#         # Scale the waist width
#         if waist_height_min <= vertex[1] <= waist_height_max:
#             vertex[0] *= waist_factor
        
#         # Scale the entire pant length
#         vertex[2] *= length_factor

#         # Scale the thigh width
#         if thigh_height_min <= vertex[1] <= thigh_height_max:
#             vertex[0] *= thigh_factor

#     return vertices

# # Path to the original OBJ file
# input_file = './test_data/meshes/pants/lower_5.obj'
# # Path to save the modified OBJ file
# output_file = 'modified_lower_5.obj'

# # Load the original OBJ
# vertices, faces = load_obj(input_file)

# # Waist factor, Length factor, Thigh factor
# modified_vertices = modify_pants(vertices, waist_factor=3.4, length_factor=5.3, thigh_factor=2.2)

# # Save the modified model to a new OBJ file
# save_obj(output_file, modified_vertices, faces)

#--------------------------------------------------------------------------------------------------------------

# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx) for idx in f) + '\n')

# def modify_pants(vertices, waist_factor, length_factor, thigh_factor):
#     # You need to adjust these values based on your model's specific scale and proportions
#     waist_height_min, waist_height_max = 0.8, 1.2  # Adjusted y-coordinates for the waist
#     thigh_height_min, thigh_height_max = 0.2, 0.6  # Adjusted y-coordinates for the thighs
    
#     for vertex in vertices:
#         # Scale the waist width
#         if waist_height_min <= vertex[1] <= waist_height_max:
#             vertex[0] *= waist_factor
        
#         # Scale the entire pant length
#         vertex[2] *= length_factor

#         # Scale the thigh width
#         if thigh_height_min <= vertex[1] <= thigh_height_max:
#             vertex[0] *= thigh_factor

#     return vertices

# # Path to the original OBJ file
# input_file = './test_data/meshes/pants/lower_5.obj'
# # Path to save the modified OBJ file
# output_file = 'modified_lower_5.obj'

# # Load the original OBJ
# vertices, faces = load_obj(input_file)

# # Revised waist factor, length factor, thigh factor
# modified_vertices = modify_pants(vertices, waist_factor=1.1, length_factor=1.05, thigh_factor=1.1)

# # Save the modified model to a new OBJ file
# save_obj(output_file, modified_vertices, faces)
#--------------------------------------------------------------------------------------------------------------


# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx) for idx in f) + '\n')

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Adjusting y-coordinates range based on your model specifics
#     waist_height_min, waist_height_max = 0.8, 1.2
#     thigh_height_min, thigh_height_max = 0.2, 0.6
    
#     for vertex in vertices:
#         if waist_height_min <= vertex[1] <= waist_height_max:
#             vertex[0] *= waist_factor
#         vertex[2] *= length_factor
#         if thigh_height_min <= vertex[1] <= thigh_height_max:
#             vertex[0] *= thigh_factor

#     return vertices

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/lower_5.obj'
# output_file = 'modified_lower_5.obj'

# # Load the original OBJ
# vertices, faces = load_obj(input_file)

# # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 50
# current_length = 40
# desired_length = 60
# current_thighs = 24
# desired_thighs = 35

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Save the modified model
# save_obj(output_file, modified_vertices, faces)

#--------------------------------------------------------------------------------------------------------------



# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx) for idx in f) + '\n')

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Adjusting y-coordinates range based on your model specifics
#     waist_height_min, waist_height_max = 0.8, 1.2
#     thigh_height_min, thigh_height_max = 0.2, 0.6

#     # Determine the current height range (Z-axis) of the pants for length adjustment
#     z_min = np.min(vertices[:, 2])
#     z_max = np.max(vertices[:, 2])
    
#     for vertex in vertices:
#         # Scale the waist width
#         if waist_height_min <= vertex[1] <= waist_height_max:
#             vertex[0] *= waist_factor
        
#         # Scale the entire pant length by stretching along the Z-axis
#         if vertex[2] >= z_min:
#             vertex[2] *= length_factor

#         # Scale the thigh width
#         if thigh_height_min <= vertex[1] <= thigh_height_max:
#             vertex[0] *= thigh_factor

#     return vertices

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/lower_5.obj'
# output_file = 'modified_lower_5.obj'

# # Load the original OBJ
# vertices, faces = load_obj(input_file)

# # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 40
# current_length = 50
# desired_length = 60
# current_thighs = 24
# desired_thighs = 35

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Save the modified model
# save_obj(output_file, modified_vertices, faces)





#--------------------------------------------------------------------------------------------------------------


# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx) for idx in f) + '\n')

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Define ranges for the waist and thigh areas based on model specifics
#     waist_height_min, waist_height_max = 0.8, 1.2
#     thigh_height_min, thigh_height_max = 0.2, 0.6

#     # Determine the current min and max height (Z-axis) of the pants for length adjustment
#     z_min = np.min(vertices[:, 2])
#     z_max = np.max(vertices[:, 2])
#     height = z_max - z_min

#     # Calculate the vertical scaling factor (length adjustment)
#     vertical_scale_factor = (desired_length - current_length) / current_length + 1.0
    
#     for vertex in vertices:
#         # Scale the waist width
#         if waist_height_min <= vertex[1] <= waist_height_max:
#             vertex[0] *= waist_factor
        
#         # Scale the entire pant length by stretching along the Z-axis
#         if vertex[2] >= z_min:
#             # Apply proportional stretching based on distance from the bottom
#             vertex[2] = z_min + (vertex[2] - z_min) * vertical_scale_factor

#         # Scale the thigh width
#         if thigh_height_min <= vertex[1] <= thigh_height_max:
#             vertex[0] *= thigh_factor

#     return vertices

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/lower_5.obj'
# output_file = 'modified_lower_5.obj'

# # Load the original OBJ
# vertices, faces = load_obj(input_file)

# # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 32
# current_length = 60
# desired_length = 42
# current_thighs = 24
# desired_thighs = 25

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Save the modified model
# save_obj(output_file, modified_vertices, faces)


#---------------------------------------


# import numpy as np

# def load_obj(filename):
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(int(f.split('/')[0]))
#                     faces.append(face)
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx) for idx in f) + '\n')

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Adjust these ranges based on your model specifics
#     waist_height_min, waist_height_max = 0.8, 1.2
#     thigh_height_min, thigh_height_max = 0.2, 0.6

#     # Determine the current min and max height (Z-axis) of the pants
#     z_min = np.min(vertices[:, 2])
#     z_max = np.max(vertices[:, 2])
#     height = z_max - z_min

#     # Apply scaling factors for waist, thighs, and length
#     for vertex in vertices:
#         # Scale the waist width
#         if waist_height_min <= vertex[1] <= waist_height_max:
#             vertex[0] *= waist_factor
        
#         # Scale the thigh width
#         if thigh_height_min <= vertex[1] <= thigh_height_max:
#             vertex[0] *= thigh_factor

#         # Adjust the length (Z-axis) by scaling vertices above the waist proportionally
#         if vertex[2] > z_min:
#             vertex[2] = z_min + (vertex[2] - z_min) * length_factor

#     return vertices

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/lower_5.obj'
# output_file = 'modified_lower_5.obj'

# # Load the original OBJ
# vertices, faces = load_obj(input_file)

# # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 43
# current_length = 40
# desired_length = 45
# current_thighs = 24
# desired_thighs = 30

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Save the modified model
# save_obj(output_file, modified_vertices, faces)


#--------------------------------------------------------------------------------------------
# import numpy as np

# def load_obj(filename):
#     vertices = []
#     texture_coords = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'vt':
#                     texture_coords.append(list(map(float, parts[1:3])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(f.split('/'))
#                     faces.append(face)
#     return np.array(vertices), texture_coords, faces

# def save_obj(filename, vertices, texture_coords, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for vt in texture_coords:
#             file.write(f'vt {vt[0]} {vt[1]}\n')
#         for face in faces:
#             face_str = ' '.join([f'{f[0]}/{f[1]}' for f in face])
#             file.write(f'f {face_str}\n')

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Find the center of the waist (x-coordinate) for symmetrical scaling
#     waist_center_x = np.mean(vertices[:, 0])
#     thigh_center_x = waist_center_x  # Typically the same as the waist for pants

#     # Determine the current min and max height (Z-axis) of the pants
#     z_min = np.min(vertices[:, 2])
#     z_max = np.max(vertices[:, 2])
    
#     # Apply scaling factors for waist, thighs, and length
#     for vertex in vertices:
#         # Scale the waist width symmetrically
#         if 0.8 <= vertex[1] <= 1.2:
#             vertex[0] = waist_center_x + (vertex[0] - waist_center_x) * waist_factor
        
#         # Scale the thigh width symmetrically
#         if 0.2 <= vertex[1] <= 0.6:
#             vertex[0] = thigh_center_x + (vertex[0] - thigh_center_x) * thigh_factor

#         # Adjust the length (Z-axis) by scaling vertices above the waist proportionally
#         if vertex[2] > z_min:
#             vertex[2] = z_min + (vertex[2] - z_min) * length_factor

#     return vertices

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/M-lower_5.obj'
# output_file = 'lower_5.obj'

# # Load the original OBJ
# vertices, texture_coords, faces = load_obj(input_file)

# # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 42
# current_length = 40
# desired_length = 45
# current_thighs = 24
# desired_thighs = 28

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Save the modified model
# save_obj(output_file, modified_vertices, texture_coords, faces)

#-------------------------------------------------------------------------

# import numpy as np

# def load_obj(filename):
#     vertices = []
#     texture_coords = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'vt':
#                     texture_coords.append(list(map(float, parts[1:3])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(f.split('/'))
#                     faces.append(face)
#     return np.array(vertices), texture_coords, faces

# def save_obj(filename, vertices, texture_coords, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for vt in texture_coords:
#             file.write(f'vt {vt[0]} {vt[1]}\n')
#         for face in faces:
#             face_str = ' '.join([f'{f[0]}/{f[1]}' for f in face])
#             file.write(f'f {face_str}\n')

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Find the center of the pants in X and Z directions
#     center_x = np.mean(vertices[:, 0])
#     z_min = np.min(vertices[:, 2])

#     # Apply scaling factors for waist, thighs, and length
#     for vertex in vertices:
#         # Scale the waist width symmetrically
#         if 0.8 <= vertex[1] <= 1.2:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * waist_factor
        
#         # Scale the thigh width symmetrically
#         if 0.2 <= vertex[1] <= 0.6:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * thigh_factor

#         # Adjust the length (Z-axis) by scaling vertices above the base proportionally
#         if vertex[2] > z_min:
#             vertex[2] = z_min + (vertex[2] - z_min) * length_factor

#     return vertices

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/M-lower_5.obj'
# output_file = 'lower_5.obj'

# # Load the original OBJ
# vertices, texture_coords, faces = load_obj(input_file)

# # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 42
# current_length = 40
# desired_length = 45
# current_thighs = 24
# desired_thighs = 28

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Save the modified model
# save_obj(output_file, modified_vertices, texture_coords, faces)


#-------------------------------------------------------------------

# import numpy as np

# def load_obj(filename):
#     vertices = []
#     texture_coords = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'vt':
#                     texture_coords.append(list(map(float, parts[1:3])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(f.split('/'))
#                     faces.append(face)
#     return np.array(vertices), texture_coords, faces

# def save_obj(filename, vertices, texture_coords, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for vt in texture_coords:
#             file.write(f'vt {vt[0]} {vt[1]}\n')
#         for face in faces:
#             face_str = ' '.join([f'{f[0]}/{f[1]}' for f in face])
#             file.write(f'f {face_str}\n')

# def calculate_centroid(vertices):
#     """Calculate the centroid of the vertices."""
#     centroid = np.mean(vertices, axis=0)
#     return centroid

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Find the center of the pants in X and Z directions
#     center_x = np.mean(vertices[:, 0])
#     z_min = np.min(vertices[:, 2])

#     # Apply scaling factors for waist, thighs, and length
#     for vertex in vertices:
#         # Scale the waist width symmetrically
#         if 0.8 <= vertex[1] <= 1.2:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * waist_factor
        
#         # Scale the thigh width symmetrically
#         if 0.2 <= vertex[1] <= 0.6:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * thigh_factor

#         # Adjust the length (Z-axis) by scaling vertices above the base proportionally
#         if vertex[2] > z_min:
#             vertex[2] = z_min + (vertex[2] - z_min) * length_factor

#     return vertices

# def translate_to_original(vertices, original_centroid):
#     """Translate vertices to match the original centroid position."""
#     new_centroid = calculate_centroid(vertices)
#     translation_vector = original_centroid - new_centroid
    
#     # Apply translation to each vertex
#     for vertex in vertices:
#         vertex += translation_vector

#     return vertices

# # # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/M-lower_5.obj'
# output_file = 'lower_5.obj'

# # Load the original OBJ
# vertices, texture_coords, faces = load_obj(input_file)

# # Calculate the original centroid before modifications
# original_centroid = calculate_centroid(vertices)

# # # Path to the original and output OBJ files
# # input_file = './test_data/meshes/pants/M-lower_5.obj'
# # output_file = 'lower_5.obj'

# # # Load the original OBJ
# # vertices, texture_coords, faces = load_obj(input_file)

# # # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 42
# current_length = 40
# desired_length = 45
# current_thighs = 24
# desired_thighs = 28

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Translate the modified pants back to their original position
# translated_vertices = translate_to_original(modified_vertices, original_centroid)

# # Save the modified model
# save_obj(output_file, translated_vertices, texture_coords, faces)


#------------------------------------------------------------------------------

# import numpy as np

# def load_obj(filename):
#     vertices = []
#     texture_coords = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'vt':
#                     texture_coords.append(list(map(float, parts[1:3])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(f.split('/'))
#                     faces.append(face)
#     return np.array(vertices), texture_coords, faces

# def save_obj(filename, vertices, texture_coords, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for vt in texture_coords:
#             file.write(f'vt {vt[0]} {vt[1]}\n')
#         for face in faces:
#             face_str = ' '.join([f'{f[0]}/{f[1]}' for f in face])
#             file.write(f'f {face_str}\n')

# def calculate_centroid(vertices):
#     """Calculate the centroid of the vertices."""
#     centroid = np.mean(vertices, axis=0)
#     return centroid

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Find the center of the pants in X and Z directions
#     center_x = np.mean(vertices[:, 0])
#     z_min = np.min(vertices[:, 2])

#     # Apply scaling factors for waist, thighs, and length
#     for vertex in vertices:
#         # Scale the waist width symmetrically
#         if 0.8 <= vertex[1] <= 1.2:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * waist_factor
        
#         # Scale the thigh width symmetrically
#         if 0.2 <= vertex[1] <= 0.6:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * thigh_factor

#         # Adjust the length (Z-axis) by scaling vertices above the base proportionally
#         if vertex[2] > z_min:
#             vertex[2] = z_min + (vertex[2] - z_min) * length_factor

#     return vertices

# def translate_to_original(vertices, original_centroid, waist_factor):
#     """Translate vertices to match the original centroid position, with slight backward adjustment if necessary."""
#     new_centroid = calculate_centroid(vertices)
#     translation_vector = original_centroid - new_centroid

#     # Adjust the Z-coordinate to move it slightly backward when the waist is expanded
#     adjustment_factor = (waist_factor - 1) * 0.05  # Proportional adjustment based on waist scaling
#     translation_vector[2] += adjustment_factor  # Move the pants slightly backward if scaled up

#     # Apply translation to each vertex
#     for vertex in vertices:
#         vertex += translation_vector

#     return vertices

# # Path to the original and output OBJ files

# input_file = './test_data/meshes/pants/M-lower_5.obj'
# output_file = './test_data/meshes/pants/lower_5.obj'


# # Load the original OBJ
# vertices, texture_coords, faces = load_obj(input_file)

# # Calculate the original centroid before modifications
# original_centroid = calculate_centroid(vertices)

# # Example current and desired measurements in inches
# current_waist = 30
# desired_waist = 50
# current_length = 40
# desired_length = 45
# current_thighs = 24
# desired_thighs = 28

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Translate the modified pants back to their original position, with a slight backward adjustment if needed
# translated_vertices = translate_to_original(modified_vertices, original_centroid, desired_waist / current_waist)

# # Save the modified model
# save_obj(output_file, translated_vertices, texture_coords, faces)

#---------------------------------------------------------------


# import numpy as np

# def load_obj(filename):
#     vertices = []
#     texture_coords = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'vt':
#                     texture_coords.append(list(map(float, parts[1:3])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(f.split('/'))
#                     faces.append(face)
#     return np.array(vertices), texture_coords, faces


# def save_obj(filename, vertices, texture_coords, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for vt in texture_coords:
#             file.write(f'vt {vt[0]} {vt[1]}\n')
#         for face in faces:
#             face_str = ' '.join([f'{f[0]}/{f[1]}' for f in face])
#             file.write(f'f {face_str}\n')

# def calculate_centroid(vertices):
#     """Calculate the centroid of the vertices."""
#     centroid = np.mean(vertices, axis=0)
#     return centroid

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Find the center of the pants in X and Z directions
#     center_x = np.mean(vertices[:, 0])
#     z_min = np.min(vertices[:, 2])

#     # Apply scaling factors for waist, thighs, and length
#     for vertex in vertices:
#         # Scale the waist width symmetrically
#         if 0.8 <= vertex[1] <= 1.2:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * waist_factor
        
#         # Scale the thigh width symmetrically
#         if 0.2 <= vertex[1] <= 0.6:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * thigh_factor

#         # Adjust the length (Z-axis) by scaling vertices above the base proportionally
#         if vertex[2] > z_min:
#             vertex[2] = z_min + (vertex[2] - z_min) * length_factor

#     return vertices

# def translate_to_original(vertices, original_centroid, waist_factor):
#     """Translate vertices to match the original centroid position, with backward adjustment if necessary."""
#     new_centroid = calculate_centroid(vertices)
#     translation_vector = original_centroid - new_centroid

#     # Adjust the Z-coordinate to move it backward when the waist is expanded
#     adjustment_factor = (waist_factor - 1) * 0.05  # Proportional adjustment based on waist scaling
#     translation_vector[2] -= adjustment_factor  # Move the pants backward if scaled up

#     # Apply translation to each vertex
#     for vertex in vertices:
#         vertex += translation_vector

#     return vertices

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/M-lower_5.obj'
# output_file = './test_data/meshes/pants/lower_5.obj'

# # Load the original OBJ
# vertices, texture_coords, faces = load_obj(input_file)

# # Calculate the original centroid before modifications
# original_centroid = calculate_centroid(vertices)

# # Example current and desired measurements in inches
# current_waist = 30
# current_thighs = 40
# current_length = 30


# desired_length = 100
# desired_thighs = 30
# desired_length = 45


# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Translate the modified pants back to their original position, with backward adjustment if needed
# translated_vertices = translate_to_original(modified_vertices, original_centroid, desired_waist / current_waist)

# # Save the modified model
# save_obj(output_file, translated_vertices, texture_coords, faces)


#--------------------------------------------------------------------


# import numpy as np


# def load_obj(filename):
#     vertices = []
#     texture_coords = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'vt':
#                     texture_coords.append(list(map(float, parts[1:3])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(f.split('/'))
#                     faces.append(face)
#     return np.array(vertices), texture_coords, faces


# def save_obj(filename, vertices, texture_coords, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for vt in texture_coords:
#             file.write(f'vt {vt[0]} {vt[1]}\n')
#         for face in faces:
#             face_str = ' '.join([f'{f[0]}/{f[1]}' for f in face])
#             file.write(f'f {face_str}\n')

# def calculate_centroid(vertices):
#     """Calculate the centroid of the vertices."""
#     centroid = np.mean(vertices, axis=0)
#     return centroid

# def modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs):
#     waist_factor = desired_waist / current_waist
#     length_factor = desired_length / current_length
#     thigh_factor = desired_thighs / current_thighs
    
#     # Find the center of the pants in X and Z directions
#     center_x = np.mean(vertices[:, 0])
#     z_min = np.min(vertices[:, 2])

#     # Apply scaling factors for waist, thighs, and length
#     for vertex in vertices:
#         # Scale the waist width symmetrically
#         if 0.8 <= vertex[1] <= 1.2:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * waist_factor
        
#         # Scale the thigh width symmetrically
#         if 0.2 <= vertex[1] <= 0.6:  # Adjust these values based on your model specifics
#             vertex[0] = center_x + (vertex[0] - center_x) * thigh_factor

#         # Adjust the length (Z-axis) by scaling vertices above the base proportionally
#         if vertex[2] > z_min:
#             vertex[2] = z_min + (vertex[2] - z_min) * length_factor
        
#         # Make adjustments along the Y-axis to make the model wider
#         vertex[1] *= waist_factor

#     return vertices

# def translate_to_original(vertices, original_centroid, waist_factor):
#     """Translate vertices to match the original centroid position, with backward adjustment if necessary."""
#     new_centroid = calculate_centroid(vertices)
#     translation_vector = original_centroid - new_centroid

#     # Adjust the Z-coordinate to move it backward when the waist is expanded
#     adjustment_factor = (waist_factor - 1) * 0.05  # Proportional adjustment based on waist scaling
#     translation_vector[2] -= adjustment_factor  # Move the pants backward if scaled up

#     # Translate vertically to position the model slightly higher
#     translation_vector[1] += 0.1  # Adjust this value as needed

#     # Apply translation to each vertex
#     for vertex in vertices:
#         vertex += translation_vector

#     return vertices

# # Assume `load_obj` and `save_obj` are defined functions for loading and saving OBJ files.
# # These functions should handle the file I/O operations with OBJ format specifics.

# # Path to the original and output OBJ files
# input_file = './test_data/meshes/pants/M-lower_5.obj'
# output_file = './test_data/meshes/pants/lower_5.obj'

# # Load the original OBJ
# vertices, texture_coords, faces = load_obj(input_file)

# # Calculate the original centroid before modifications
# original_centroid = calculate_centroid(vertices)

# # Modify the pants according to specified inch measurements
# modified_vertices = modify_pants(vertices, current_waist, desired_waist, current_length, desired_length, current_thighs, desired_thighs)

# # Translate the modified pants back to their original position, with backward and upward adjustment
# translated_vertices = translate_to_original(modified_vertices, original_centroid, desired_waist / current_waist)

# # Save the modified model
# save_obj(output_file, translated_vertices, texture_coords, faces)







#-----------------------------



# import numpy as np

# def load_obj(filename):
#     vertices = []
#     texture_coords = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             if parts:
#                 if parts[0] == 'v':
#                     vertices.append(list(map(float, parts[1:4])))
#                 elif parts[0] == 'vt':
#                     texture_coords.append(list(map(float, parts[1:3])))
#                 elif parts[0] == 'f':
#                     face = []
#                     for f in parts[1:]:
#                         face.append(f.split('/'))
#                     faces.append(face)
#     return np.array(vertices), texture_coords, faces

# def save_obj(filename, vertices, texture_coords, faces):
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for vt in texture_coords:
#             file.write(f'vt {vt[0]} {vt[1]}\n')
#         for face in faces:
#             face_str = ' '.join(['/'.join(f) for f in face])
#             file.write(f'f {face_str}\n')

# def calculate_centroid(vertices):
#     return np.mean(vertices, axis=0)

# def modify_pants(vertices, desired_waist, desired_length, desired_thighs):
#     z_min = np.min(vertices[:, 2])
#     z_max = np.max(vertices[:, 2])
#     height = z_max - z_min
#     waist_start = z_max - 0.3 * height
#     thighs_end = z_min + 0.6 * height

#     for vertex in vertices:
#         z_position = vertex[2]
#         if z_position >= waist_start:
#             # Scale waist area
#             vertex[0] *= desired_waist / 30
#             vertex[1] *= desired_waist / 30
#         elif z_position <= thighs_end:
#             # Scale thigh area
#             vertex[0] *= desired_thighs / 24
#             vertex[1] *= desired_thighs / 24
#         # Scale the entire length
#         vertex[2] = z_min + (vertex[2] - z_min) * (desired_length / 40)

#     return vertices

# def translate_to_original(vertices, original_centroid):
#     new_centroid = calculate_centroid(vertices)
#     translation_vector = original_centroid - new_centroid
#     for vertex in vertices:
#         vertex += translation_vector
#     return vertices

# # Desired measurements
# desired_waist = 38
# desired_thighs = 12
# desired_length = 42

# # File paths
# input_file = './test_data/meshes/pants/M-lower_5.obj'
# output_file = './test_data/meshes/pants/lower_5.obj'

# # Load the original OBJ
# vertices, texture_coords, faces = load_obj(input_file)

# # Calculate the original centroid before modifications
# original_centroid = calculate_centroid(vertices)

# # Modify the pants according to specified desired measurements
# modified_vertices = modify_pants(vertices, desired_waist, desired_length, desired_thighs)

# # Translate the modified pants back to their original position
# translated_vertices = translate_to_original(modified_vertices, original_centroid)

# # Save the modified model
# save_obj(output_file, translated_vertices, texture_coords, faces)



#------------------------------------------


# import numpy as np

# def load_obj(filename):
#     """Load an OBJ file into vertices and faces."""
#     vertices = []
#     faces = []
#     with open(filename, 'r') as file:
#         for line in file:
#             if line.startswith('v '):
#                 parts = line.split()
#                 vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
#             elif line.startswith('f '):
#                 parts = line.split()
#                 faces.append([int(p.split('/')[0]) - 1 for p in parts[1:]])
#     return np.array(vertices), faces

# def save_obj(filename, vertices, faces):
#     """Save vertices and faces back to an OBJ file."""
#     with open(filename, 'w') as file:
#         for v in vertices:
#             file.write(f'v {v[0]} {v[1]} {v[2]}\n')
#         for f in faces:
#             file.write('f ' + ' '.join(str(idx + 1) for idx in f) + '\n')

# def modify_dimensions(vertices, width_scale, height_scale, depth_scale):
#     """Scale the pants' dimensions based on provided factors."""
#     scaled_vertices = vertices.copy()
#     scaled_vertices[:, 0] *= width_scale  # Scale width along the x-axis
#     scaled_vertices[:, 1] *= depth_scale  # Scale depth along the y-axis
#     scaled_vertices[:, 2] *= height_scale  # Scale height along the z-axis
#     return scaled_vertices

# # Define your desired scaling factors here
# width_scale = 1.2  # e.g., increase width by 20%
# height_scale = 1.1  # e.g., increase height by 10%
# depth_scale = 1.05  # e.g., increase depth by 5%
# input_file = './test_data/meshes/pants/M-lower_5.obj'

# # Load the original OBJ file
# # input_file = 'lower_5.obj'
# vertices, faces = load_obj(input_file)

# # Modify the dimensions of the pants
# modified_vertices = modify_dimensions(vertices, width_scale, height_scale, depth_scale)

# output_file = './test_data/meshes/pants/lower_5.obj'
# # # Define the output file path
# # output_file = 'modified_lower_5.obj'

# # Save the modified model
# save_obj(output_file, modified_vertices, faces)



#-------------------------------------------

import numpy as np

def load_obj(filename):
    """ Load an OBJ file into vertices, UVs, and faces. """
    vertices = []
    texture_coords = []
    faces = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('v '):
                parts = line.split()
                vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif line.startswith('vt '):
                parts = line.split()
                texture_coords.append([float(parts[1]), float(parts[2])])
            elif line.startswith('f '):
                parts = line.split()
                # Faces can include vertex/texture/normal indices; only vertex and texture are handled here.
                face = [p.split('/') for p in parts[1:]]
                faces.append([(int(f[0]) - 1, int(f[1]) - 1) if len(f) > 1 and f[1] != '' else (int(f[0]) - 1, -1) for f in face])
    return np.array(vertices), np.array(texture_coords), faces

def save_obj(filename, vertices, texture_coords, faces):
    """ Save vertices, UVs, and faces back to an OBJ file. """
    with open(filename, 'w') as file:
        for v in vertices:
            file.write(f'v {v[0]} {v[1]} {v[2]}\n')
        for vt in texture_coords:
            file.write(f'vt {vt[0]} {vt[1]}\n')
        for f in faces:
            face_line = 'f '
            for v in f:
                # Adding 1 because OBJ format is 1-indexed
                face_line += f'{v[0]+1}/{v[1]+1} ' if v[1] != -1 else f'{v[0]+1} '
            file.write(face_line.strip() + '\n')

def modify_dimensions(vertices, width_scale, height_scale, depth_scale):
    """ Scale the pants' dimensions based on provided factors. """
    scaled_vertices = vertices.copy()
    scaled_vertices[:, 0] *= width_scale  # Scale width along the x-axis
    scaled_vertices[:, 1] *= depth_scale  # Scale depth along the y-axis
    scaled_vertices[:, 2] *= height_scale  # Scale height along the z-axis
    return scaled_vertices

# Define your desired scaling factors here
width_scale = 1  # e.g., increase width by 20%
height_scale = 1  # e.g., increase waist by 10%
depth_scale = 1 # e.g., increase length by 5%

import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument('length', type=float, help='A numeric value 1')
parser.add_argument('waist', type=float, help='A numeric value 2')

# Parse the arguments
args = parser.parse_args()

# Access the arguments directly
print(f"Numeric Value 1 in modify ,py: {args.length}")
print(f"Numeric Value 2 in modify.py: {args.waist}")


# Define your desired scaling factors here
width_scale =  1 if args.waist == 1.10 else args.waist-0.12  # e.g., increase width by 20%
 
height_scale =  1 if args.waist == 1.10 else args.waist-0.09  # e.g., increase waist by 10%
depth_scale = 1  if args.length == 0.95 else args.length # e.g., increase length by 5%



# Define your desired scaling factors here
# width_scale = 1  # e.g., increase width by 20%
# height_scale = 1  # e.g., increase waist by 10%
# depth_scale = 1 # e.g., increase length by 5%


# Load the original OBJ file
#/Users/phun/Downloads/3D-Human-Body-Generator/p_m_c/pix2surf/test_data/meshes/pants/M-lower_5.obj
input_file = '/Users/phun/Downloads/3D-Human-Body-Generator/p_m_c/pix2surf/test_data/meshes/pants/M-lower_5.obj'
vertices, texture_coords, faces = load_obj(input_file)

# Modify the dimensions of the pants
modified_vertices = modify_dimensions(vertices, width_scale, height_scale, depth_scale)

# Define the output file path
output_file = '/Users/phun/Downloads/3D-Human-Body-Generator/p_m_c/pix2surf/test_data/meshes/pants/lower_5.obj'

# Save the modified model
save_obj(output_file, modified_vertices, texture_coords, faces)
