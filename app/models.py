import uuid
from enum import Enum
from datetime import datetime, timezone
import sqlite3

DATABASE = "claims.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute('''
            CREATE TABLE IF NOT EXISTS claims (
                claim_id TEXT PRIMARY KEY,
                veteran_id TEXT NOT NULL,
                claim_type TEXT NOT NULL,
                status TEXT NOT NULL,
                submitted_at TEXT NOT NULL
            )
        ''')
    conn.commit()
    conn.close()

# What does a claim contain
# - claim_id
# - veteran_id
# - claim_type
# - status
# - submitted_date

#CLAIMS_DB = {} # Old list used as temp db

class ClaimStatus(Enum):
    RECEIVED = "RECEIVED"
    IN_REVIEW = "IN_REVIEW"
    APPROVED = "APPROVED"
    DENIED = "DENIED"

def create_claim(veteran_id, claim_type):
    claim_id = str(uuid.uuid4())
    submitted_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    claim = {
        "claim_id" : claim_id,
        "veteran_id" : veteran_id,
        "claim_type" : claim_type,
        "status" : ClaimStatus.RECEIVED.value,
        "submitted_at" : submitted_at,
    }
    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO claims VALUES (?,?,?,?,?)",(claim_id, veteran_id, claim_type, ClaimStatus.RECEIVED.value, submitted_at))
    conn.commit()
    conn.close()
    return claim

def get_claim(claim_id):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.execute("SELECT * FROM claims WHERE claim_id = ?", (claim_id,))
    row = cur.fetchone()
    conn.close()

    return dict(row) if row else None
    #return CLAIMS_DB.get(claim_id)

def get_all_claims():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.execute("SELECT * FROM claims")
    claims = [dict(row) for row in cur.fetchall()]
    conn.close()
    return claims
    #return list(CLAIMS_DB.values())

def update_status(claim_id, status):
    try:
        new_status = ClaimStatus(status).value
    except ValueError:
        return None
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute(
        'UPDATE claims SET status = ? WHERE claim_id = ?',
        (new_status, claim_id)
    )
    if cur.rowcount == 0:
        conn.close()
        return None
    conn.commit()
    conn.close()
    return get_claim(claim_id)

    # claim = CLAIMS_DB.get(claim_id)
    # if not claim:
    #     return None
    #
    # claim["status"] = new_status
    # return claim