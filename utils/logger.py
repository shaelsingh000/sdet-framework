from loguru import logger
import sys
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = LOG_DIR / f"test_run_{timestamp}.log"
logger.remove()
#console logging
logger.add(sys.stdout,level="INFO",format="{time}| {level} | {message}")
#file logging
logger.add(
    log_file,
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {message}",
    rotation="10 MB",
    retention="7 days",
    compression="zip"
)

def get_logger():
    return logger