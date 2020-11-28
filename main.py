import sys
import os
import time
import datetime
import settings as sets

if __name__ == "__main__":
    pass
else:
    print("UNAVAILABLE")
    sys.exit(999)

print("Initialzing ORWTMC Data Manager...")
boottime = time.time()
try:
    open("config.json")
except FileNotFoundError:
    print("You are the first time using ORWTMC Data Manager.")
    print("Sending you to Settings/index...")
    sets.index()
    print("Please restart the application.")
    sys.exit(1)

print("Reading config...")
print("Initialzed.")
print("\n\n")
print("This is a data manager based on Python.")