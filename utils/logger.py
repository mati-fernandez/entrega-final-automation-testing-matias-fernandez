import logging
from pathlib import Path
from datetime import datetime

nombre = datetime.now().strftime("log_%Y-%m-%d.log")

LOGS_DIR = Path("reports/logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / nombre,
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s: [%(levelname)s] %(name)s - %(message)s",
    force=True  
)

logger = logging.getLogger("talento_tech")