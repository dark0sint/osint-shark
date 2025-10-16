# Defines routes for the Flask web interface.

from flask import render_template, jsonify
from app import app  # Import the Flask app instance
import database

def index():
    """Render the main page."""
    return "Welcome to OSINT SHARK! Visit /data to see monitored data."

def get_data():
    """Endpoint to retrieve data from the database."""
    conn = database.sqlite3.connect(database.DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM osint_data ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)  # Return data as JSON
