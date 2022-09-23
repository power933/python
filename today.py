from datetime import *
today = datetime.now()

day = today.date()
time = today.time()
print(today.replace(microsecond=0))