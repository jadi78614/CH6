import subprocess

blenderPath = r"/Applications/Blender.app/Contents/MacOS/blender"
projectPath = r"/Users/phun/Downloads/3D-Human-Body-Generator/pythonscripts/blenderfiles/humanproject.blend"
scriptPath = r"bodyEditor.py"


def run_blender(blenderPath, projectPath, scriptPath, measures):
    subprocess.run([blenderPath,
                    projectPath,
                    '--background',
                    '--python', scriptPath,
                    '--', measures['head'], measures['torso'], measures['legs'], measures['calves'],
                    measures['shoulders'], measures['arms'], measures['forearms'], measures['hips'],
                    measures['height']])

def execute(measures):
    run_blender(blenderPath, projectPath, scriptPath, measures)

