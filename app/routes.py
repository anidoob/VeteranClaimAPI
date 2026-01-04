from flask import Blueprint, jsonify, request
from app.models import create_claim

claims_bp = Blueprint("claims", __name__)

@claims_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status" : "ok"}), 200

@claims_bp.route("/claims", methods=["POST"])
def submit_claim():
    data = request.get_json()

    if not data or "veteran_id" not in data or "claim_type" not in data:
        return jsonify({"error": "veteran_id and claim_type are required"}), 400

    try:
        claim = create_claim(
            veteran_id=data["veteran_id"],
            claim_type=data["claim_type"]
        )
        return jsonify(claim), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500