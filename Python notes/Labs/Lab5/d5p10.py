# 10. Print current date in YYYY-MM-DD H:M format
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))