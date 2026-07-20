"""
scanner.py

Provides the core TCP port scanning functionality for TriNetra.

This module validates user input, performs TCP connect scans, and
returns structured scan results for use by other modules.

"""
import socket

from config import DEFAULT_TIMEOUT
from core.logger import get_logger
from core.validator import validate_ip, validate_port_list

logger = get_logger(__name__)


#------------------------------
# Create Socket               -
#------------------------------
def _create_socket():
    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(DEFAULT_TIMEOUT)
        return s
    except socket.error:
        return None


#------------------------------
# Port Scanner                -
#------------------------------
def _port_scanner(target, port):
    s = _create_socket()
    
    if s is None:
        return port,"Socket Error"
    
    try:
        result = s.connect_ex((target, port))
        if result ==0:
            return port, "Open"
        return port, "Closed"
    
    finally:
        s.close()


#------------------------------
# Scanning Multiple Ports     -
#------------------------------
def _ports_scanner(target, ports):
    results = []

    for port in ports:
        results.append(_ports_scanner(target, port))
    
    return results


#------------------------------
# Scan                        -
#------------------------------
def scan(target, ports):
    
    is_valid, error = validate_ip(target)
    if not is_valid:
        return False, error
    
    is_valid, error = validate_port_list(ports)
    if not is_valid:
        return False, error
    
    logger.info(f"Starting scan on {target}")
    results = _ports_scanner(target, ports)
    logger.info(f"Complete scan on {target}")
    return True, results
    

#-----------------------------
# Testing                    -
# ----------------------------
if __name__ == "__main__":
    target = input("Enter Target: ")

    ports = input("Enter ports (comma separated): ")
    ports = [int(port.strip()) for port in ports.split(",")]

    success, result = scan(target, ports)
    print(result) 