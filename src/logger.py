import logging
import os
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log'
LOG_FOLDER = os.path.join("logs", f'{datetime.now().strftime('%d%m%Y')}')

os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE)

logging.basicConfig(
    format = "[ %(asctime)s ] %(levelname)s %(module)s %(funcName)s %(lineno)d - %(message)s",
    level = logging.INFO,
    handlers = [logging.FileHandler(filename = LOG_FILE_PATH) ,logging.StreamHandler()]
)