from flask import request, Flask, jsonify
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running"

def make_file_name():
    return f"log_{str(time.time())}.txt"

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid data"}), 400

    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join("logs", machine)
    os.makedirs(machine_folder, exist_ok=True)

    file_name = make_file_name()
    file_path = os.path.join(machine_folder, file_name)

    with open(file_path, "w") as f:
        f.write(str(log_data))

    return jsonify({"status": "success", "file": file_name}), 200

@app.route('/api/get_machines', methods=['GET'])
def get_machines():
    if not os.path.exists("logs"):
        return jsonify([])

    machines = [d for d in os.listdir("logs") if os.path.isdir(os.path.join("logs", d))]
    return jsonify(machines)

@app.route('/api/get_logs/<machine>', methods=['GET'])
def get_logs(machine):
    machine_folder = os.path.join("logs", machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404

    logs = []
    for file_name in sorted(os.listdir(machine_folder)):
        file_path = os.path.join(machine_folder, file_name)
        with open(file_path, "r") as f:
            content = f.read()

        # try to extract timestamp from filename: "log_<timestamp>.txt"
        try:
            ts_str = file_name.replace("log_", "").replace(".txt", "")
            timestamp = float(ts_str)
        except ValueError:
            timestamp = None

        logs.append({
            "file": file_name,
            "timestamp": timestamp,
            "content": content
        })

    return jsonify(logs)


if __name__ == "__main__":
    app.run(debug=True)
