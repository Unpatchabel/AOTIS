from datetime import datetime

###---------------------------###

###THE CODE###

#colour codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RESET = "\033[0m"

#starting line of text
AOTIS = int(input("START AOTIS 1=YES 0=NO: "))

if AOTIS == 1:
    #to set the date and time
    current_time = datetime.now()
    #to format the date and time into readable format
    formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
    banner = f"""
    {YELLOW}
    ====================================
       AOTIS - AI-DRIVEN OSINT SYSTEM
    ====================================
    {RESET}"""
    print(GREEN +"AOTIS IS STARTING..."+ RESET)

    print("Current date and time is:", CYAN + formatted_time + RESET)
    print(banner)
    print(WHITE +" OPERATOR : TONY" + RESET)
else: 
    print(RED + "GET tf OUTTA HERE!!!" + RESET)


