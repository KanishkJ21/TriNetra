#--------------------------------
#config.py

#Central configuration module for hte TriNetra Application

#This module stores application metadata, directory paths, scanner defaults, logging configuration, GUI settings, and other constants used throughtout the project.

#Author: Kanishk Jha
#--------------------------------

from pathlib import Path

APP_NAME = "TriNetra"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Kanishk Jha"
APP_DESCRIPTION = (
    "A network reconnaissance and security scanning tool"
    "Built with python and Nmap, it provides a comprehensive set of features for network discovery, vulnerability assessment, and security auditing."
)

#-------------------------------
# Directory paths              -
#-------------------------------
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGS_DIR = BASE_DIR / "logs"
DATABASE_DIR = BASE_DIR / "database"
SCANS_DIR = BASE_DIR / "scans"
REPORTS_DIR = BASE_DIR / "reports"

#-------------------------------
# Scanner Configurations       -
#-------------------------------
DEFAULT_TIMEOUT = 10    #seconds
DEFAULT_PING_TIMEOUT = 2  #seconds
DEFAULT_THREADS = 20
DEFAULT_SCAN_PROFILE = "Quick Scan"
DEFAULT_PORT_RANGE = "1-1000"

#-------------------------------
# Export Configurations        -
#-------------------------------
DEFAULT_EXPORT_FORMAT = "json"  # Options: html, pdf, txt
SUPPORTED_EXPORT_FORMATS = (
       "csv",
       "json",
       "txt",
       "html",
       "pdf"
)

#-------------------------------
# Logging Configuration        -    
#-------------------------------
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = LOGS_DIR / "trinetra.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

#-------------------------------
# GUI Settings                 -
#-------------------------------
WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
DEFAULT_THEME = "dark"  # Options: light, dark

#-------------------------------
# DATABASE                     -
#-------------------------------
DATABASE_NAME = "trinetra.db"
DATABASE_PATH = DATABASE_DIR / DATABASE_NAME
DATABASE_TIMEOUT = 5  # seconds