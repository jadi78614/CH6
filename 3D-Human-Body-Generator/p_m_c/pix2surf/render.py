import bpy
import sys
import os
import argparse

class Renderer():
    def __init__(self):
        self.get_args()
        self.make_dirs()
        self.setup_scene()
        self.setup_lights()
        self.setup_objects()
        self.export_model()  # Export the model as a .glb file

    def get_args(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("--up_mesh", type=str, help="location of upper mesh")
        ap.add_argument("--up_text", type=str, help="location of upper texture")
        ap.add_argument("--low_mesh", type=str, help="location of lower mesh")
        ap.add_argument("--low_text", type=str, help="location of lower texture")
        ap.add_argument("--body_mesh", type=str, help="location of body mesh")
        ap.add_argument("--body_text", type=str, help="location of body texture")
        ap.add_argument("--renderfolder", type=str, help="Location to save the exported model")
        
        self.args = ap.parse_args(self.extract_args())

    def make_dirs(self):
        if not os.path.isdir(self.args.renderfolder):
            os.makedirs(self.args.renderfolder)

    def setup_scene(self):
        self.scene = bpy.context.scene
        self.scene.render.film_transparent = True
        # Remove the default cube, camera, and light (if needed)
        bpy.ops.object.select_all(action='DESELECT')  # Deselect everything
        if "Cube" in bpy.data.objects:
            bpy.data.objects['Cube'].select_set(True)
            bpy.ops.object.delete()  # Delete the cube

    def setup_lights(self):
        lamp_data = bpy.data.lights.new(name="New Lamp", type='AREA')
        lamp_data.energy = 1
        lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)
        self.scene.collection.objects.link(lamp_object) 
        lamp_object.location = (15.0, 0.0, 15.0)

    def insert_object(self, gar_loc, tex_loc,val):
        # Import the OBJ file
        bpy.ops.wm.obj_import(filepath=gar_loc)
       
        #print("Location : ",gar_loc)

        #bpy.ops.import_scene.obj(filepath=gar_loc)
        obj_object = bpy.context.selected_objects[0]  # Imported object gets id 0

        # Scale the object
        obj_object.scale = (4.0, 4.0, 4.0)

        # Load the image for the texture
        img = bpy.data.images.load(tex_loc)
        #print("Location Texture: ",tex_loc)

        # Create a new material
        mat = bpy.data.materials.new(name='object')
        mat.use_nodes = True  # Enable the use of nodes for the material

        # Clear default nodes
        nodes = mat.node_tree.nodes
        for node in nodes:
            nodes.remove(node)

        # if val == "low":
        #     obj_object.location.y += 0.1

        # Create a new image texture node
        tex_image_node = nodes.new(type='ShaderNodeTexImage')
        tex_image_node.image = img  # Assign the loaded image to the texture node

        # Create a Principled BSDF node
        bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')

        # Create a Material Output node
        output_node = nodes.new(type='ShaderNodeOutputMaterial')

        # Link the nodes together
        links = mat.node_tree.links
        links.new(tex_image_node.outputs['Color'], bsdf_node.inputs['Base Color'])  # Link texture color output to BSDF input
        links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])  # Link BSDF output to material output

        # Assign the material to the object
        if len(obj_object.data.materials) > 0:
            obj_object.data.materials[0] = mat  # If the object already has a material, replace it
        else:
            obj_object.data.materials.append(mat)  # Otherwise, add the new material
        
     


    def setup_objects(self):
        dirs = ['low', 'up', 'body']
        for val in dirs:
            mesh_pth = getattr(self.args, val + '_mesh')
            text_pth = getattr(self.args, val + '_text')
            print(f"test ting  {val,mesh_pth, text_pth}")
            self.insert_object(mesh_pth, text_pth,val)

    def export_model(self):
        # Construct output file path for .glb
        output_file_path = os.path.join(self.args.renderfolder, 'exported_model.glb')
        output_file_path = "/Users/phun/Downloads/3D-Human-Body-Generator/pythonscripts/projectexports/model.glb"
        print(f"Export file path: {output_file_path}")  # Debug print to check the output path
        
        # Use Blender's export operators to export the model to .glb file
        bpy.ops.export_scene.gltf(filepath=output_file_path, export_format='GLB')  # Export as GLB
        print(f"Model exported to {output_file_path}")

    def extract_args(self, input_argv=None):
        if input_argv is None:
            input_argv = sys.argv
        output_argv = []
        if '--' in input_argv:
            idx = input_argv.index('--')
            output_argv = input_argv[(idx + 1):]
        return output_argv

if __name__ == "__main__":
    renderer = Renderer()




# import bpy
# import sys
# import os
# import argparse

# class Renderer():
#     def __init__(self):
#         self.get_args()
#         self.make_dirs()
#         self.setup_scene()
#         self.setup_lights()
#         self.setup_objects()
#         self.export_model()  # Export the model as a .glb file

#     def get_args(self):
#         ap = argparse.ArgumentParser()
#         ap.add_argument("--up_mesh", type=str, help="Location of upper mesh")
#         ap.add_argument("--up_text", type=str, help="Location of upper texture")
#         ap.add_argument("--low_mesh", type=str, help="Location of lower mesh")
#         ap.add_argument("--low_text", type=str, help="Location of lower texture")
#         ap.add_argument("--body_mesh", type=str, help="Location of body mesh")
#         ap.add_argument("--body_text", type=str, help="Location of body texture")
#         ap.add_argument("--renderfolder", type=str, help="Location to save the exported model")
        
#         self.args = ap.parse_args(self.extract_args())

#     def make_dirs(self):
#         if not os.path.isdir(self.args.renderfolder):
#             os.makedirs(self.args.renderfolder)

#     def setup_scene(self):
#         self.scene = bpy.context.scene
#         self.scene.render.film_transparent = True
#         bpy.ops.object.select_all(action='DESELECT')  # Deselect everything
#         # Remove the default cube, camera, and light if present
#         for obj in bpy.data.objects:
#             if obj.type in ['MESH', 'LIGHT', 'CAMERA']:
#                 bpy.data.objects.remove(obj, do_unlink=True)

#     def setup_lights(self):
#         lamp_data = bpy.data.lights.new(name="New Lamp", type='AREA')
#         lamp_data.energy = 1000  # Adjust light intensity
#         lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)
#         self.scene.collection.objects.link(lamp_object) 
#         lamp_object.location = (15.0, 0.0, 15.0)

#     def insert_object(self, gar_loc, tex_loc):
#         # Import the OBJ file
#         bpy.ops.import_scene.obj(filepath=gar_loc)
#         print("Location: ", gar_loc)

#         # Get the imported object
#         if len(bpy.context.selected_objects) == 0:
#             print(f"Error: No objects imported from {gar_loc}")
#             return
#         obj_object = bpy.context.selected_objects[0]

#         # Scale the object
#         obj_object.scale = (4.0, 4.0, 4.0)

#         # Load the image for the texture
#         if tex_loc and os.path.exists(tex_loc):
#             img = bpy.data.images.load(tex_loc)
#             print("Location Texture: ", tex_loc)

#             # Create a new material
#             mat = bpy.data.materials.new(name='object')
#             mat.use_nodes = True  # Enable the use of nodes for the material

#             # Get nodes and clear default
#             nodes = mat.node_tree.nodes
#             for node in nodes:
#                 nodes.remove(node)

#             # Create a new image texture node
#             tex_image_node = nodes.new(type='ShaderNodeTexImage')
#             tex_image_node.image = img  # Assign the loaded image to the texture node

#             # Create a Principled BSDF node
#             bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')

#             # Create a Material Output node
#             output_node = nodes.new(type='ShaderNodeOutputMaterial')

#             # Link the nodes together
#             links = mat.node_tree.links
#             links.new(tex_image_node.outputs['Color'], bsdf_node.inputs['Base Color'])
#             links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])

#             # Assign the material to the object
#             if len(obj_object.data.materials) > 0:
#                 obj_object.data.materials[0] = mat
#             else:
#                 obj_object.data.materials.append(mat)

#     def setup_objects(self):
#         # Directories for different parts of the model
#         dirs = ['low', 'up', 'body']
#         for val in dirs:
#             mesh_pth = getattr(self.args, val + '_mesh')
#             text_pth = getattr(self.args, val + '_text')
#             self.insert_object(mesh_pth, text_pth)

#     def export_model(self):
#         # Construct output file path for .glb
#         output_file_path = os.path.join(self.args.renderfolder, 'exported_model.glb')
#         print(f"Export file path: {output_file_path}")  # Debug print to check the output path
        
#         # Use Blender's export operators to export the model to .glb file
#         bpy.ops.export_scene.gltf(filepath=output_file_path, export_format='GLB')  # Export as GLB
#         print(f"Model exported to {output_file_path}")

#     def extract_args(self, input_argv=None):
#         if input_argv is None:
#             input_argv = sys.argv
#         output_argv = []
#         if '--' in input_argv:
#             idx = input_argv.index('--')
#             output_argv = input_argv[(idx + 1):]
#         return output_argv

# if __name__ == "__main__":
#     renderer = Renderer()


# import bpy
# import sys
# import os
# import argparse

# class Renderer():
#     def __init__(self):
#         self.get_args()
#         self.make_dirs()
#         self.setup_scene()
#         self.setup_lights()
#         self.setup_objects()
#         self.export_model()  # Export the model as a .glb file

#     def get_args(self):
#         ap = argparse.ArgumentParser()
#         ap.add_argument("--up_mesh", type=str, help="location of upper mesh")
#         ap.add_argument("--up_text", type=str, help="location of upper texture")
#         ap.add_argument("--low_mesh", type=str, help="location of lower mesh")
#         ap.add_argument("--low_text", type=str, help="location of lower texture")
#         ap.add_argument("--body_model", type=str, help="location of generated body GLB model")
#         ap.add_argument("--renderfolder", type=str, help="Location to save the exported model")
        
#         self.args = ap.parse_args(self.extract_args())

#     def make_dirs(self):
#         if not os.path.isdir(self.args.renderfolder):
#             os.makedirs(self.args.renderfolder)

#     def setup_scene(self):
#         self.scene = bpy.context.scene
#         self.scene.render.film_transparent = True
#         # Remove the default cube, camera, and light (if needed)
#         bpy.ops.object.select_all(action='DESELECT')  # Deselect everything
#         if "Cube" in bpy.data.objects:
#             bpy.data.objects['Cube'].select_set(True)
#             bpy.ops.object.delete()  # Delete the cube

#     def setup_lights(self):
#         lamp_data = bpy.data.lights.new(name="New Lamp", type='AREA')
#         lamp_data.energy = 1
#         lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)
#         self.scene.collection.objects.link(lamp_object) 
#         lamp_object.location = (15.0, 0.0, 15.0)

#     def insert_object(self, gar_loc, tex_loc):
#         # Import the OBJ file
#         bpy.ops.wm.obj_import(filepath=gar_loc)
#         print("Location : ", gar_loc)

#         # Imported object gets id 0
#         obj_object = bpy.context.selected_objects[0]

#         # Scale the object
#         obj_object.scale = (4.0, 4.0, 4.0)

#         # Load the image for the texture
#         img = bpy.data.images.load(tex_loc)
#         print("Location Texture: ", tex_loc)

#         # Create a new material
#         mat = bpy.data.materials.new(name='object')
#         mat.use_nodes = True  # Enable the use of nodes for the material

#         # Clear default nodes
#         nodes = mat.node_tree.nodes
#         for node in nodes:
#             nodes.remove(node)

#         # Create a new image texture node
#         tex_image_node = nodes.new(type='ShaderNodeTexImage')
#         tex_image_node.image = img  # Assign the loaded image to the texture node

#         # Create a Principled BSDF node
#         bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')

#         # Create a Material Output node
#         output_node = nodes.new(type='ShaderNodeOutputMaterial')

#         # Link the nodes together
#         links = mat.node_tree.links
#         links.new(tex_image_node.outputs['Color'], bsdf_node.inputs['Base Color'])  # Link texture color output to BSDF input
#         links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])  # Link BSDF output to material output

#         # Assign the material to the object
#         if len(obj_object.data.materials) > 0:
#             obj_object.data.materials[0] = mat  # If the object already has a material, replace it
#         else:
#             obj_object.data.materials.append(mat)  # Otherwise, add the new material

#     def insert_glb_body(self, body_glb_loc):
#         # Import the GLB file (generated body)
#         bpy.ops.import_scene.gltf(filepath=body_glb_loc)
#         print(f"Imported GLB model from: {body_glb_loc}")

#     def setup_objects(self):
#         # Insert lower and upper objects with their textures
#         dirs = ['low', 'up']
#         for val in dirs:
#             mesh_pth = getattr(self.args, val + '_mesh')
#             text_pth = getattr(self.args, val + '_text')
#             self.insert_object(mesh_pth, text_pth)

#         # Insert the generated body GLB file
#         self.insert_glb_body(self.args.body_model)

#     def export_model(self):
#         # Construct output file path for .glb
#         output_file_path = os.path.join(self.args.renderfolder, 'exported_model.glb')
#         print(f"Export file path: {output_file_path}")  # Debug print to check the output path
        
#         # Use Blender's export operators to export the model to .glb file
#         bpy.ops.export_scene.gltf(filepath=output_file_path, export_format='GLB')  # Export as GLB
#         print(f"Model exported to {output_file_path}")

#     def extract_args(self, input_argv=None):
#         if input_argv is None:
#             input_argv = sys.argv
#         output_argv = []
#         if '--' in input_argv:
#             idx = input_argv.index('--')
#             output_argv = input_argv[(idx + 1):]
#         return output_argv

# if __name__ == "__main__":
#     renderer = Renderer()
