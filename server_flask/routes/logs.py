from flask import Blueprint, jsonify
import os

logs_bp = Blueprint('logs', __name__)

@logs_bp.route('/api/get_logs/<machine>', methods=['GET'])
def get_logs(machine):
    machine_folder = os.path.join("logs", machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404
    
    logs = []
    for file_name in sorted(os.listdir(machine_folder)):
        file_path = os.path.join(machine_folder, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read()

            try:
                ts_str = file_name.replace("log_", "").replace(".txt", "")
                timestamp = float(ts_str)
            except ValueError:
                timestamp = None
            logs.append({
                "file": file_name,
                "timestamp": timestamp,
                "content": content})
    
    return jsonify(logs), 200