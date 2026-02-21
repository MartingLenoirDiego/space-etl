from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date, timedelta
from main import run_pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scheduler = BlockingScheduler()

@scheduler.scheduled_job("cron", hour=6, minute=0)
def scheduled_pipeline():
    logger.info("⏰ Lancement automatique du pipeline...")
    end = date.today()
    start = end - timedelta(days=1)
    run_pipeline(start, end)

if __name__ == "__main__":
    logger.info("🚀 Scheduler démarré - pipeline tous les jours à 6h00")
    scheduler.start()