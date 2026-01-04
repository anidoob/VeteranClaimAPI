import uuid
from enum import Enum
from datetime import datetime, timezone

# What does a claim contain
# - claim_id
# - veteran_id
# - claim_type
# - status
# - submitted_date

CLAIMS_DB = {}

class ClaimStatus(Enum):
    RECEIVED = "RECEIVED"
    IN_REVIEW = "IN_REVIEW"
    APPROVED = "APPROVED"
    DENIED = "DENIED"

def create_claim(veteran_id, claim_type):
    claim_id = str(uuid.uuid4())

    claim = {
        "claim_id" : claim_id,
        "veteran_id" : veteran_id,
        "claim_type" : claim_type,
        "status" : ClaimStatus.RECEIVED.value,
        "submitted_at" : datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    CLAIMS_DB[claim_id] = claim
    return claim

def get_claim(claim_id):
    return CLAIMS_DB.get(claim_id)

def get_all_claims():
    return list(CLAIMS_DB.values())

def update_status(claim_id, status):
    try:
        new_status = ClaimStatus(status)
    except ValueError:
        return None

    claim = CLAIMS_DB.get(claim_id)
    if not claim:
        return None

    claim["status"] = new_status
    return claim