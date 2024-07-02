import click
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from business_logic import add_event, list_events, update_event, delete_event

@click.group()
def cli():
    """Tech Events Manager CLI"""
    pass

@cli.command()
@click.option('--name', prompt='Event name')
@click.option('--date', prompt='Event date (YYYY-MM-DD)')
@click.option('--location', prompt='Event location')
@click.option('--description', prompt='Event description')
@click.option('--type', prompt='Event type')
def add_event_cmd(name, date, location, description, type):
    """Add a new event"""
    db: Session = SessionLocal()
    event = add_event(db, name, date, location, description, type)
    click.echo(f"Event '{event.name}' added successfully!")
    db.close()

@cli.command()
def list_events_cmd():
    """List all events"""
    db: Session = SessionLocal()
    events = list_events(db)
    for event in events:
        click.echo(f"ID: {event.id}, Name: {event.name}, Date: {event.date}, Location: {event.location}, Type: {event.type}")
    db.close()

@cli.command()
@click.argument('event_id')
@click.option('--name', prompt='New event name', required=False)
@click.option('--date', prompt='New event date (YYYY-MM-DD)', required=False)
@click.option('--location', prompt='New event location', required=False)
@click.option('--description', prompt='New event description', required=False)
@click.option('--type', prompt='New event type', required=False)
def update_event_cmd(event_id, name, date, location, description, type):
    """Update an existing event"""
    db: Session = SessionLocal()
    event = update_event(db, event_id, name, date, location, description, type)
    if event:
        click.echo(f"Event '{event.name}' updated successfully!")
    else:
        click.echo("Event not found.")
    db.close()

@cli.command()
@click.argument('event_id')
def delete_event_cmd(event_id):
    """Delete an event"""
    db: Session = SessionLocal()
    event = delete_event(db, event_id)
    if event:
        click.echo(f"Event '{event.name}' deleted successfully!")
    else:
        click.echo("Event not found.")
    db.close()

if __name__ == '__main__':
    init_db()
    cli()
