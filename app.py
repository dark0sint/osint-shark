# Flask application setup for OSINT SHARK.

from flask import Flask
import routes  # Import routes to register them

app = Flask(__name__)

# Register routes
app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/data', 'get_data', routes.get_data)

if __name__ == '__main__':
    app.run()
