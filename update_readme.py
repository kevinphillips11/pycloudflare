import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open('README.md', 'w') as file:
        file.write(f'## Current Hour: {current_time}\n')
    time.sleep(10)
