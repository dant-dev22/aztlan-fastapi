# app/models/participant.py

# from sqlalchemy import Column, Integer, String, Date, Boolean
# from app.database import Base

class Participant:
    # __tablename__ = "participants"

    # id = Column(Integer, primary_key=True, index=True)
    # aztlan_id = Column(String, unique=True, index=True, nullable=False)
    # name = Column(String, nullable=False)
    # birth_date = Column(Date, nullable=False)
    # experience = Column(Integer, nullable=False)
    # belt_color = Column(String, nullable=False)
    # club = Column(String, nullable=False)
    # biological_sex = Column(String, nullable=False)
    # payment_proof_url = Column(String, nullable=True)
    # is_paid = Column(Boolean, default=False)
    
    # Opcional: puedes definir atributos normales para pruebas sin DB
    id = None
    aztlan_id = None
    name = None
    birth_date = None
    experience = None
    belt_color = None
    club = None
    biological_sex = None
    payment_proof_url = None
    is_paid = False