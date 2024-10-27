import bpy
import sys

# Get output path from command line arguments
output_path = sys.argv[sys.argv.index("--") + 1]

# Configure rendering settings
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = output_path

# Optionally, set the camera and scene if needed
# bpy.context.scene.camera = bpy.data.objects['Camera'] # Example camera

# Render the scene and save the image
bpy.ops.render.render(write_still=True)

print("Rendered image saved to {}".format(output_path))
