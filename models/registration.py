from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    participant_id = Column(Integer, ForeignKey("participants.id"))
