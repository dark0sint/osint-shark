# Main entry point for the OSINT SHARK application.
# This file starts the Flask server and the scheduler.

import app as flask_app  # Import the Flask app
from scheduler import start_scheduler  # Import scheduler

if __name__ == '__main__':
    # Start the scheduler in a background thread
    start_scheduler()
    
    # Run the Flask app on port 5000
    flask_app.app.run(debug=True, host='0.0.0.0', port=5000)
