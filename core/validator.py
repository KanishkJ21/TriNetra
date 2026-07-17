

import ipaddress  #Inbuilt module to validate IP addresses

#---------------------------
# Validate IP              -
#---------------------------
def validate_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return (True,None)
        
    except ValueError:
        if ":" in ip_address and "." not in ip_address:
            return (False,"Invalid IPv6 address format.")
        elif "." in ip_address and ":" not in ip_address:
            return (False,"Invalid IPv4 address format.")
        else:
            return (False,"Invalid IP address format.")


#---------------------------
# Validate Port            -
#---------------------------
def validate_port(port):
    if not isinstance(port, int):
        return (False,"Port must be an Integer")
    if not 1 <= port <= 65535:
        return (False,"Port must be an integer between 1 and 65535.")
    else:
        return (True, None)
    

#---------------------------
# Validate Port List       -   
#---------------------------
def validate_port_list(port_list):
    if not isinstance(port_list, list):                   #can be modified later to accept other iterable types like tuple, set, etc.
        return (False,"Input is not in the list format.")

    for port in port_list:
        is_valid, error = validate_port(port)

        if not is_valid:
            return False, f"Invalid port {port}: {error}"
    
    return (True, None)


#---------------------------
#Optional Testing          -
#---------------------------
if __name__ == "__main__":
    print(validate_ip("192.168.1.1"))
    print(validate_ip("256.1.1.1"))

    print(validate_port(8080))
    print(validate_port(70000))
    
    print(validate_port_list([22, 80, 443]))
    print(validate_port_list([22, 70000, 443]))