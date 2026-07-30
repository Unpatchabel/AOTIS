from datetime import datetime
import ipaddress
import re
import os

# ---------------- COLOURS ----------------
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def is_ipv4(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

def is_domain(value):
    pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, value) is not None

def hash_type(value):
    if len(value) == 32:
        return "MD5"
    elif len(value) == 40:
        return "SHA1"
    elif len(value) == 64:
        return "SHA256"
    else:
        return None
    
# ---------------- AOTIS START ----------------
print(WHITE + "\nAOTIS INVESTIGATION WORKFLOW\n" + RESET)

ioc = input("Enter IOC: ").strip().lower()

ioc_type = None

if is_ipv4(ioc):
    ioc_type = "IPv4 Address"

elif is_domain(ioc):
    ioc_type = "Domain"

else:
    detected_hash = hash_type(ioc)
    if detected_hash:
        ioc_type = detected_hash

# ---------------- VALIDATION RESULT ----------------

if ioc_type:
    print(GREEN + "\nVALID IOC DETECTED" + RESET)
    print("Type:", ioc_type)
    print("Value:", ioc)

    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    file_timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{file_timestamp}_{ioc}.txt"

    report = f"""
============================
AOTIS INVESTIGATION REPORT
============================

IOC: {ioc}
Type: {ioc_type}
Timestamp: {timestamp}

Status: Investigation Created
"""

    with open(filename, "w") as file:
        file.write(report)

    print(CYAN + f"\nReport saved: {filename}" + RESET)

else:
    print(RED + "\nINVALID IOC" + RESET)
    print("No report created.")
