from flask import Blueprint, request, jsonify
import os
from utils.decypt_script import Decryptor

decrypt_bp = Blueprint('decrypt', __name__)

@decrypt_bp.route('/api/decrypt_logs', methods=['POST'])
def decrypt_file():
    data = request.get_json()
    if not data or "logs" not in data or len(data["logs"]) == 0 or "key" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    encrypted_string = data["logs"][0]
    key = data["key"]  # <-- get key from frontend

    try:
        decryptor = Decryptor(encrypted_string, key, is_string=True)  # <-- use frontend key
        decrypted_string = decryptor.get_decrypted_string()
        print(decrypted_string)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

    return jsonify({"decrypted_data": decrypted_string}), 200
