from flask import Blueprint, request, jsonify
import os
from utils.file_utils import make_file_name

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/api/upload', methods=['POST'])
def upload_file():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400
    
    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join("logs", machine)
    os.makedirs(machine_folder, exist_ok=True)

    file_name = make_file_name()
    file_path = os.path.join(machine_folder, file_name)

    with open(file_path, 'w') as f:
        f.write(str(log_data))

    return jsonify({"status": "success", "file": file_path}), 200
