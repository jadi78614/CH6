import flask
from flask import jsonify, request, render_template,send_from_directory
from flask_cors import CORS
import blenderinvoker
import json
from pygltflib import GLTF2
import logging

# app = flask.Flask(__name__)
# CORS(app)

# # Serve static files from the 'projectexports' directory
# @app.route('/pythonscripts/projectexports/<path:filename>')
# def serve_project_exports(filename):
#     # You can provide the absolute or relative path to the directory
#     directory = '/Users/phun/Downloads/3D-Human-Body-Generator/pythonscripts/projectexports'
#     return send_from_directory(directory, filename)

# # Enable logging to track errors
# logging.basicConfig(level=logging.DEBUG)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         if not request.is_json:
#             return "Invalid JSON", 400

#         obj = request.json
#         print(f"Received data: {obj}")
        
#         # Accessing torso (make sure 'torso' exists in the object)
#         if 'torso' in obj:
#             print(f"Torso: {obj['torso']}")
#         else:
#             return "Missing 'torso' field", 400

#         # Pass data to Blender invoker
#         blenderinvoker.execute(obj)
#         return "done"  # Return response for POST request

#     # Render the index.html template for GET requests
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)




# import flask
# from flask import jsonify, request, render_template, send_from_directory
# from flask_cors import CORS
# import subprocess
# import os
# import sys
# import logging
# import threading

# app = flask.Flask(__name__)
# CORS(app)

# # Set up logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Serve static files from the 'projectexports' directory
# @app.route('/pythonscripts/projectexports/<path:filename>')
# def serve_project_exports(filename):
#     directory = '/Users/phun/Downloads/3D-Human-Body-Generator/pythonscripts/projectexports'
#     return send_from_directory(directory, filename)

# def run_script(script_path, script_args=[]):
#     """Function to run a script with arguments and log outputs."""
#     python_executable = sys.executable  # Use the same Python executable that's running Flask
#     try:
#         full_command = [python_executable, script_path] + script_args
#         logging.info(f"Executing script: {full_command}")
#         result = subprocess.run(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if result.stdout:
#             logging.info(f"Script output: {result.stdout}")
#         if result.stderr:
#             logging.error(f"Script error: {result.stderr}")
#         return result
#     except subprocess.CalledProcessError as e:
#         logging.error(f"Script execution failed: {e.stderr}")
#         return None

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         if not request.is_json:
#             return jsonify({"error": "Invalid JSON"}), 400

#         obj = request.json
#         logging.info(f"Received data: {obj}")

#                 # Accessing torso (make sure 'torso' exists in the object)
#         if 'torso' in obj:
#             print(f"Torso: {obj['torso']}")
#         else:
#             return "Missing 'torso' field", 400

#         # Pass data to Blender invoker
#         blenderinvoker.execute(obj)
#         # Return response for POST request

#         required_fields = ['torso', 'legs', 'arms']
#         if not all(field in obj for field in required_fields):
#             missing = [field for field in required_fields if field not in obj]
#             return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400
        
#           # Convert numbers to strings to pass as arguments
#         script_args = [str(obj['height']), str(obj['hips'])]

#         scripts_base_path = '/Users/phun/Downloads/3D-Human-Body-Generator/p_m_c/pix2surf'
#         modifypants_script = os.path.join(scripts_base_path, 'modifypants.py')
#         demo_script = os.path.join(scripts_base_path, 'demo.py')

#         # Start scripts asynchronously
#         threading.Thread(target=run_script, args=(modifypants_script,script_args)).start()
#         threading.Thread(target=run_script, args=(demo_script, [
#             '--gpus', '-1', '--pose_id', str(obj.get('pose_id', '5')),
#             '--img_id', str(obj.get('img_id', '6')),
#             '--low_type', obj.get('low_type', 'pants'),
#             '--output', './output_pants'
#         ])).start()

        

#     return {"message": "Scripts are being processed"}, 202

#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)










import flask
from flask import jsonify, request, render_template, send_from_directory
from flask_cors import CORS
import subprocess
import os
import sys
import logging

app = flask.Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Serve static files from the 'projectexports' directory
@app.route('/pythonscripts/projectexports/<path:filename>')
def serve_project_exports(filename):
    directory = '/Users/phun/Downloads/3D-Human-Body-Generator/pythonscripts/projectexports'
    return send_from_directory(directory, filename)

def run_script(script_path, script_args=[]):
    """Function to run a script with arguments and log outputs."""
    python_executable = sys.executable  # Use the same Python executable that's running Flask
    try:
        full_command = [python_executable, script_path] + script_args
        logging.info(f"Executing script: {full_command}")
        result = subprocess.run(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout:
            logging.info(f"Script output: {result.stdout}")
        if result.stderr:
            logging.error(f"Script error: {result.stderr}")
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f"Script execution failed: {e.stderr}")
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Invalid JSON"}), 400

        obj = request.json
        logging.info(f"Received data: {obj}")

        # Check for required fields
        required_fields = ['torso', 'legs', 'arms']
        if not all(field in obj for field in required_fields):
            missing = [field for field in required_fields if field not in obj]
            return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400
         # Pass data to Blender invoker
        blenderinvoker.execute(obj)
        # Convert numbers to strings to pass as arguments
        script_args = [str(obj['height']), str(obj['hips'])]

        scripts_base_path = '/Users/phun/Downloads/3D-Human-Body-Generator/p_m_c/pix2surf'
        modifypants_script = os.path.join(scripts_base_path, 'modifypants.py')
        demo_script = os.path.join(scripts_base_path, 'demo.py')

        # Run the scripts synchronously
        modifypants_result = run_script(modifypants_script, script_args)
        demo_result = run_script(demo_script, [
            '--gpus', '-1', '--pose_id', str(obj.get('pose_id', '5')),
            '--img_id', str(obj.get('img_id', '5')),
            '--low_type', obj.get('low_type', 'pants'),
            '--output', './output_pants'
        ])

        # Check results and prepare response
        if modifypants_result is None or modifypants_result.returncode != 0:
            return jsonify({"error": "Failed to run modifypants.py"}), 500
        if demo_result is None or demo_result.returncode != 0:
            return jsonify({"error": "Failed to run demo.py"}), 500

    return jsonify({"message": "Scripts executed successfully"}), 202

    

if __name__ == "__main__":
    app.run(debug=True)
