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
        "status" : ClaimStatus.RECEIVED,
        "submitted_at" : datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    CLAIMS_DB[claim_id] = claim
    return claim