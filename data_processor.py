# Module to process collected OSINT data.
# Filters data based on keywords from config.

from config import KEYWORD_FILTER

def process_data(raw_data):
    """Process and filter the raw data."""
    filtered_data = [line for line in raw_data.split('\n') if any(keyword in line.lower() for keyword in KEYWORD_FILTER)]
    return filtered_data  # Return a list of filtered lines
