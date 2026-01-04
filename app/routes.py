from flask import Blueprint, jsonify, request


claims_bp = Blueprint("claims", __name__)

@claims_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status" : "ok"}), 200

from app.models import create_claim
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

from app.models import get_all_claims
@claims_bp.route("/claims", methods=["GET"])
def list_claims():
    return jsonify(get_all_claims()), 200

from app.models import get_claim
@claims_bp.route("/claims/<claim_id>", methods=["GET"])
def fetch_claim(claim_id):
    claim = get_claim(claim_id)

    if not claim:
        return jsonify({"error" : "Claim not found"}), 404

    return jsonify(claim), 200

from app.models import update_status
@claims_bp.route("/claims/<claim_id>/update", methods=["PATCH"])
def patch_status(claim_id):
    data = request.get_json()

    if not data or "status" not in data:
        return jsonify({"error" : "Status not found"}), 400

    claim = update_status(claim_id, data["status"])
    if not claim:
        return jsonify({"error" : "Invalid status or claim not found"}), 400
    return jsonify(claim)
