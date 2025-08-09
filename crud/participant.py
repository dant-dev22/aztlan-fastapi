import random
from sqlalchemy.orm import Session
from models.participant import Participant
from schemas.participant import ParticipantBase
from config import AWS_ACCESS_KEY_ID, S3_BUCKET_NAME, AWS_SECRET_ACCESS_KEY, AWS_REGION
from fastapi import UploadFile
import boto3 
import uuid

S3_BASE_URL = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com"

s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def generate_unique_aztlan_id(db: Session):
    while True:
        random_number = random.randint(100000, 999999)
        aztlan_id = f"aztlan-{random_number}"
        existing = db.query(Participant).filter_by(aztlan_id=aztlan_id).first()
        if not existing:
            return aztlan_id

def get_all_participants(db: Session):
    return db.query(Participant).all()

def create_participant(db: Session, participant_data: ParticipantBase):
    aztlan_id = generate_unique_aztlan_id(db)
    db_participant = Participant(**participant_data.dict(), aztlan_id=aztlan_id)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant


def upload_payment_proof_to_s3(file: UploadFile, aztlan_id: str) -> str:
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"payment_proofs/{aztlan_id}.{file_extension}"
    s3.upload_fileobj(
        file.file,
        S3_BUCKET_NAME,
        unique_filename
    )
    return f"{S3_BASE_URL}/{unique_filename}"

def update_payment_proof(db: Session, aztlan_id: str, file_url: str):
    participant = db.query(Participant).filter(Participant.aztlan_id == aztlan_id).first()
    if not participant:
        return None

    participant.payment_proof_url = file_url
    db.commit()
    db.refresh(participant)
    return participant

def mark_as_paid(db: Session, aztlan_id: str):
    participant = db.query(Participant).filter(Participant.aztlan_id == aztlan_id).first()
    if not participant:
        return None
    participant.is_paid = True
    db.commit()
    db.refresh(participant)
    return participant