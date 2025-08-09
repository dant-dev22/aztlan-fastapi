from pydantic import BaseModel
from datetime import date

class ParticipantBase(BaseModel):
    name: str
    birth_date: date
    experience: int
    belt_color: str
    club: str
    biological_sex: str

    class Config:
        orm_mode = True

class ParticipantOut(ParticipantBase):
    aztlan_id: str  # Solo aquí está incluido para la respuesta

class PaymentProofUpdate(BaseModel):
    payment_proof_url: str