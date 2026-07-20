"""
logger.py

Purpose:
    Configure and provide a centralized logging system
    for the TriNetra application.

Responsibilities:
    - Configure application logging
    - Create log directory if needed
    - Return configured loggers to other modules

Does NOT:
    - Perform network scanning
    - Validate input
    - Generate reports
"""

#---------------------------
#Import Statements     
#---------------------------
import logging
from config import LOG_FILE, LOG_LEVEL,LOG_FORMAT


#---------------------------
#Logging Configuration
#---------------------------
def configure_logging():

    LOG_FILE.parent.mkdir(parents = True, exist_ok = True)  # Ensure log directory exists
    logging.basicConfig(
        level = LOG_LEVEL,
        format = LOG_FORMAT,
        filename = LOG_FILE,
    )


def get_logger(name):       #Return a configured logger
    return logging.getLogger(name)


if __name__ == "__main__":
    configure_logging()
    logger = get_logger(__name__)
    logger.info("Logger configured successfully.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    
    


