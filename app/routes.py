from flask import Blueprint, jsonify

claims_bp = Blueprint("claims", __name__)

@claims_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status" : "ok"}), 200