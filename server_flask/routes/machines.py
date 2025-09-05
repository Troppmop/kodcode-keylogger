from flask import Blueprint, jsonify
import os

machines_bp = Blueprint('machines', __name__)

@machines_bp.route('/api/get_machines', methods=['GET'])
def get_machines():
    if not os.path.exists("logs"):
        return jsonify([]), 200
    
    machines = [name for name in os.listdir("logs") if os.path.isdir(os.path.join("logs", name))]
    return jsonify(machines), 200