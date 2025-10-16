# Custom logging module.

import logging

def setup_logger():
    """Set up and return a logger."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger('OSINT_SHARK')
