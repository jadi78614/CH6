from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Assuming the script is named 'your_script.py'
        # You can also pass arguments to the script if needed
        result = subprocess.run(['python', 'app.py'], capture_output=True, text=True)
        return jsonify({'output': result.stdout, 'error': result.stderr}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
