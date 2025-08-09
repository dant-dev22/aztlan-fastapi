from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from app.schemas.participant import ParticipantBase, ParticipantOut, PaymentProofUpdate
# from app.database import get_db  # función que devuelve la sesión de DB
from app.crud import participant as crud_participant

router = APIRouter(prefix="/participants")

@router.get("", response_model=List[ParticipantOut])
def get_participants( 
    # db: Session = Depends(get_db)
):
    # return crud_participant.get_all_participants(db)
    print("GET /participants called")
    return []

@router.post("", response_model=ParticipantOut)
def create_participant(
    participant: ParticipantBase,
    # db: Session = Depends(get_db)
):
    # return crud_participant.create_participant(db, participant)
    print(f"POST /participants called with: {participant}")
    return participant

@router.patch("/{participant_id}/payment-proof", response_model=ParticipantOut)
def update_payment_proof(
    participant_id: int,
    file: UploadFile = File(...),
    # db: Session = Depends(get_db)
):
    try:
        # file_url = crud_participant.upload_payment_proof_to_s3(file, db)
        file_url = f"https://fake-s3-url/{file.filename}"
        print(f"Simulated upload of file {file.filename} for participant {participant_id} -> {file_url}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

    # updated = crud_participant.update_payment_proof(db, participant_id, file_url)
    updated = {
        "aztlan_id": f"aztlan-{participant_id}",
        "name": "Test Participant",
        "birth_date": "2000-01-01",
        "experience": 1,
        "belt_color": "white",
        "club": "Test Club",
        "biological_sex": "M",
        "payment_proof_url": file_url
    }
    # if not updated:
    #     raise HTTPException(status_code=404, detail="Participant not found")
    return updated

@router.put("/{participant_id}/mark-paid")
def mark_paid(
    participant_id: int,
    # db: Session = Depends(get_db)
):
    # updated = crud_participant.mark_as_paid(db, participant_id)
    # if not updated:
    #     raise HTTPException(status_code=404, detail="Participant not found")
    print(f"PUT /participants/{participant_id}/mark-paid called")
    return {"message": f"Participant {participant_id} marked as paid (simulated)"}