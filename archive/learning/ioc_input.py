BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RESET = "\033[0m"





ioc_type= input("Enter IOC type (IP/domain/hash): ")
ioc = input("Enter IOC = ")
clean_ioc = ioc.strip().lower()
analyst = input("Analyst ID: ")
if analyst == "TONY":
    print("============================")
    print("AOTIS IOC SUMMARY")
    print("============================")


    print("Type: ", ioc_type)
    print("Value: ", clean_ioc)
else: 
    print(RED + "INVALID IDENTITY" + RESET)






 