# Module to collect OSINT data from a source.
# This is a simulation; in a real app, this would fetch from APIs like Twitter.

import requests
from config import DUMMY_DATA_SOURCE

def collect_data():
    """Simulate fetching OSINT data from a public source."""
    try:
        response = requests.get(DUMMY_DATA_SOURCE, timeout=5)
        response.raise_for_status()  # Check for HTTP errors
        return response.text  # Return raw data as string
    except requests.RequestException as e:
        raise ValueError(f"Error collecting data: {e}")
