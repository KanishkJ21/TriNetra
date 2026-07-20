"""
exporter.py

Provides exporting functionality for the application

This module exports scan results into various file formats
such as TXT, CSV, JSON and HTML.

"""

import csv
import json

from config import REPORTS_DIR
from core.logger import get_logger

logger = get_logger(__name__)


#------------------------------
# Export txt                  -
#------------------------------
def _export_txt(results, output_path):
    try:
        with open(output_path, "w") as file:
            file.write("TriNetra Scan Report\n")
            file.write("-" * 40 + "\n\n")

            for port, status in results:
                file.write(f"Port: {port} | Status: {status}\n")
            
        return True
    
    except Exception as err:
        logger.error(f"TXT export failed: {err}")
        return False
    

#------------------------------
# Export csv                  -
#------------------------------
def _export_csv(results, output_path):
    try:
        with open(output_path, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["port", "status"])

            for port, status in results:
                writer.writerow([port, status])
        
        return True
    
    except Exception as err:
        logger.error(f"CSV export failed: {err}")
        return False
    

#-------------------------------
# Export json                  -
#-------------------------------
def _export_json(results, output_path):
    try:
        data = []

        for port, status in results:
            data.append(
                {
                    "port": port,
                    "status": status
                }
            )
        with open(output_path, "w") as file:
            json.dump(data, file, indent=4)

        return True
    except Exception as err:
        logger.error(f"JSON export failed: {err}")
        return False
    

#--------------------------------
# Export html                   -
#--------------------------------
def _export_html(results, output_path):
    try:
        with open(output_path, "w") as file:
            file.write("<html>\n")
            file.write("<head><title>TriNetra Report</title></head>\n")
            file.write("<body>\n")
            file.write("<h1>TriNetra Scan Report</h1>\n")
            file.write("<table border='1'>\n")
            file.write("<tr><th>Port</th><th>Status</th></tr>\n")

            for port, status in results:
                file.write(f"<tr><td>{port}</td><td>{status}</td></tr>\n")

            file.write("</table>\n")
            file.write("</body>\n")
            file.write("</html>\n")

        return True

    except Exception as err:
        logger.error(f"HTML export failed: {err}")
        return False


#----------------------------------
# Export Main                     -
# ---------------------------------
def export(results, export_format, filename):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORTS_DIR / f"{filename}.{export_format}"
    logger.info(f"Exporting Report as {export_format.upper()}")

    if export_format == "txt":
        success = _export_txt(results, output_path)

    elif export_format == "csv":
        success = _export_csv(results, output_path)
    
    elif export_format == "json":
        success = _export_json(results, output_path)

    elif export_format == "html":
        success = _export_html(results, output_path)

    else:
        logger.error("Unsupported Export Format.")
        return False
    
    if success:
        logger.info(f"Report exported to {output_path}")

    return success


#---------------------------------
# Testing Block                  -
#---------------------------------
if __name__ == "__main__":

    sample_results = [
        (22, "Open"),
        (80, "Closed"),
        (443, "Open"),
        (8000, "Closed")
    ]

    export(sample_results, "txt", "sample_report")
    export(sample_results, "csv", "sample_report")
    export(sample_results, "json", "sample_report")
    export(sample_results, "html", "sample_report")