# Module to manage scheduled tasks using APScheduler.

from apscheduler.schedulers.background import BackgroundScheduler
from data_collector import collect_data
from data_processor import process_data
from database import save_data, init_db
from utils import get_current_timestamp
from config import MONITOR_INTERVAL
import logger

log = logger.setup_logger()

def monitoring_job():
    """Job to run periodically for monitoring."""
    try:
        raw_data = collect_data()
        processed_data = process_data(raw_data)
        timestamp = get_current_timestamp()
        for item in processed_data:
            save_data(timestamp, item)
        log.info("Monitoring job completed successfully.")
    except Exception as e:
        log.error(f"Error in monitoring job: {e}")

def start_scheduler():
    """Start the background scheduler."""
    init_db()  # Ensure database is initialized
    scheduler = BackgroundScheduler()
    scheduler.add_job(monitoring_job, 'interval', seconds=MONITOR_INTERVAL)
    scheduler.start()
    log.info("Scheduler started.")
