

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
