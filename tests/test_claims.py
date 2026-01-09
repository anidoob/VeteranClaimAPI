import pytest
from app import create_app
import sqlite3
#from app.models import CLAIMS_DB


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    conn = sqlite3.connect('claims.db')
    conn.execute('DELETE FROM claims')
    conn.commit()
    conn.close()
    #CLAIMS_DB.clear()


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'


def test_create_claim(client):
    response = client.post('/claims', json={
        'veteran_id': '123',
        'claim_type': 'disability'
    })
    assert response.status_code == 201
    assert 'claim_id' in response.json


def test_create_claim_missing_fields(client):
    response = client.post('/claims', json={'veteran_id': '123'})
    assert response.status_code == 400


def test_get_claim(client):
    create_response = client.post('/claims', json={
        'veteran_id': '123',
        'claim_type': 'disability'
    })
    claim_id = create_response.json['claim_id']

    response = client.get(f'/claims/{claim_id}')
    assert response.status_code == 200
    assert response.json['veteran_id'] == '123'


def test_get_nonexistent_claim(client):
    response = client.get('/claims/fake-id')
    assert response.status_code == 404


def test_update_status(client):

    create_response = client.post('/claims', json={
        'veteran_id': '123',
        'claim_type': 'disability'
    })
    claim_id = create_response.json['claim_id']


    response = client.patch(f'/claims/{claim_id}/update', json={
        'status': 'APPROVED'
    })
    assert response.status_code == 200
    assert response.json['status'] == 'APPROVED'


def test_update_invalid_status(client):
    create_response = client.post('/claims', json={
        'veteran_id': '123',
        'claim_type': 'disability'
    })
    claim_id = create_response.json['claim_id']

    response = client.patch(f'/claims/{claim_id}/update', json={
        'status': 'INVALID'
    })
    assert response.status_code == 400