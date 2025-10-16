# Simple data models for the application.
# Using dictionaries for simplicity; in a real app, use an ORM like SQLAlchemy.

def create_osint_entry(timestamp, data):
    """Create a data entry model."""
    return {
        'timestamp': timestamp,
        'data': data
    }
