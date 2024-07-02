from sqlalchemy.orm import Session
from models.event import Event
from models.participant import Participant
from models.registration import Registration

def add_event(db: Session, name: str, date: str, location: str, description: str, type: str):
    event = Event(name=name, date=date, location=location, description=description, type=type)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def list_events(db: Session):
    return db.query(Event).all()

def update_event(db: Session, event_id: int, name: str = None, date: str = None, location: str = None, description: str = None, type: str = None):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event:
        if name:
            event.name = name
        if date:
            event.date = date
        if location:
            event.location = location
        if description:
            event.description = description
        if type:
            event.type = type
        db.commit()
        db.refresh(event)
        return event
    return None

def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event:
        db.delete(event)
        db.commit()
        return event
    return None
