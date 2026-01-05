# Veteran Claims Service API

A RESTful API for managing veteran disability claims built with Flask and SQLite. This service provides endpoints for creating, retrieving, and updating claim statuses with built-in validation and error handling.

## Features

- **CRUD Operations**: Create, read, and update veteran claims
- **Status Management**: Track claim lifecycle (RECEIVED, IN_REVIEW, APPROVED, DENIED)
- **Data Persistence**: SQLite database for reliable data storage
- **Input Validation**: Comprehensive error handling and status validation
- **RESTful Design**: Standard HTTP methods and status codes

## Tech Stack

- **Backend**: Flask (Python 3)
- **Database**: SQLite
- **Testing**: pytest
- **Deployment**: AWS EC2

## API Endpoints

### Health Check
```
GET /health
```
Returns API health status.

**Response (200)**:
```json
{
  "status": "ok"
}
```

### Create Claim
```
POST /claims
```
Submit a new veteran claim.

**Request Body**:
```json
{
  "veteran_id": "12345",
  "claim_type": "disability"
}
```

**Response (201)**:
```json
{
  "claim_id": "08804dab-c27e-4c5d-a6ca-279df98c3157",
  "veteran_id": "12345",
  "claim_type": "disability",
  "status": "RECEIVED",
  "submitted_at": "2026-01-04T16:12:31+00:00"
}
```

**Error Response (400)**:
```json
{
  "error": "veteran_id and claim_type are required"
}
```

### Get All Claims
```
GET /claims
```
Retrieve all claims in the system.

**Response (200)**:
```json
[
  {
    "claim_id": "08804dab-c27e-4c5d-a6ca-279df98c3157",
    "veteran_id": "12345",
    "claim_type": "disability",
    "status": "RECEIVED",
    "submitted_at": "2026-01-04T16:12:31+00:00"
  }
]
```

### Get Single Claim
```
GET /claims/{claim_id}
```
Retrieve a specific claim by ID.

**Response (200)**:
```json
{
  "claim_id": "08804dab-c27e-4c5d-a6ca-279df98c3157",
  "veteran_id": "12345",
  "claim_type": "disability",
  "status": "RECEIVED",
  "submitted_at": "2026-01-04T16:12:31+00:00"
}
```

**Error Response (404)**:
```json
{
  "error": "Claim not found"
}
```

### Update Claim Status
```
PATCH /claims/{claim_id}/update
```
Update the status of an existing claim.

**Request Body**:
```json
{
  "status": "APPROVED"
}
```

**Valid Status Values**:
- `RECEIVED`
- `IN_REVIEW`
- `APPROVED`
- `DENIED`

**Response (200)**:
```json
{
  "claim_id": "08804dab-c27e-4c5d-a6ca-279df98c3157",
  "veteran_id": "12345",
  "claim_type": "disability",
  "status": "APPROVED",
  "submitted_at": "2026-01-04T16:12:31+00:00"
}
```

**Error Response (400)**:
```json
{
  "error": "Invalid status or claim not found"
}
```

## Project Structure

```
veteran-claims-service/
│
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # API endpoints
│   ├── models.py            # Database models and logic
│
├── tests/
│   └── test_claims.py       # Unit tests
│
├── application.py           # Application entry point
├── requirements.txt         # Python dependencies
├── claims.db                # SQLite database (generated)
└── README.md
```

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip

### Local Development

1. **Clone the repository**
```bash
git clone <repository-url>
cd veteran-claims-service
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python application.py
```

The API will be available at `http://localhost:5000`

### Running Tests

```bash
pytest tests/
```

## Deployment (AWS EC2)

### Prerequisites
- AWS account
- EC2 instance (t2.micro eligible for free tier)
- Security group allowing inbound traffic on port 5000

### Deployment Steps

1. **SSH into EC2 instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

2. **Install dependencies**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

3. **Clone and setup**
```bash
git clone <repository-url>
cd veteran-claims-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Run with screen (keeps running after disconnect)**
```bash
sudo apt install screen -y
screen -S flask-app
python3 application.py
# Press Ctrl+A then D to detach
```

5. **Access the API**
```
http://your-ec2-ip:5000/health
```

## Live Demo

The API is currently deployed at:
```
http://18.217.57.110:5000
```

Try it:
- Health check: `GET http://18.217.57.110:5000/health`
- Create claim: `POST http://18.217.57.110:5000/claims`

## Future Enhancements

- [ ] Add authentication and authorization
- [ ] Implement claim filtering and pagination
- [ ] Add claim document uploads
- [ ] Integrate with external veteran verification systems
- [ ] Add email notifications for status changes
- [ ] Implement audit logging
- [ ] Deploy with HTTPS/SSL
- [ ] Add Docker containerization

## License

This project is licensed under the MIT License.

## Author

Developed as a portfolio project demonstrating RESTful API design, database integration, and cloud deployment.

## Contact

For questions or feedback, please open an issue in the repository.