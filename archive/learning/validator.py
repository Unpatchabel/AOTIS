import ipaddress
import re

#COLOUR CODES
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RESET = "\033[0m"
#----------------------#

#create reusable function
def is_ipv4(value):
    try : 
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False
    
#add domain validation
def is_domain(value):
    pattern =  r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern,value) is not None

#Add hash detection
def is_hash(value):
    if len(value) == 32:
        return "MD5"
    elif len(value) == 40:
        return "SHA1"
    elif len(value) == 64:
        return "SHA256"
    else:
        return None


print(WHITE + "AOTIS IOC VALIDATOR STARTING..." + RESET)

#User input
ioc = input("Enter IOC: ").strip().lower()



print(YELLOW + "\nAOTIS VALIDATION RESULT" + RESET)
print("IOC:", ioc)

hash_result = is_hash(ioc)

if is_ipv4(ioc):
    print("Type: IP ADDRESS")
    print(BLUE + "VALID" + RESET)

elif is_domain(ioc):
    print("Type: DOMAIN")
    print(BLUE + "VALID" + RESET)

elif is_hash(ioc):
    print("Type: HASH")
    print(BLUE + "VALID" + RESET)

else:
    print(RED + "INVALID" + RESET)

