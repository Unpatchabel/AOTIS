from datetime import datetime

print("AOTIS CASE LOGGER")
ioc = input("Enter IOC: ").strip().lower()
current_time = datetime.now()

timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

file_timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"reports/{file_timestamp}_{ioc}.txt"

report = f"""
============================
AOTIS INVESTIGATION REPORT
============================

IOC: {ioc}
Timestamp: {timestamp}

Status: Investigation Created
"""
with open(filename, "w") as file:
    file.write(report)


print("Report saved:", filename)
