# Custom error handling module.

class OSINTError(Exception):
    """Custom exception for OSINT SHARK errors."""
    pass

def handle_error(error_message):
    """Handle and log errors."""
    import logger
    log = logger.setup_logger()
    log.error(f"Application error: {error_message}")
    raise OSINTError(error_message)
