import subprocess
import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open('README.md', 'w') as file:
        file.write(f'## Current Hour: {current_time}\n')

    subprocess.run(['git', 'config', '--global', 'user.email', 'my-bot@example.com'])
    subprocess.run(['git', 'config', '--global', 'user.name', 'my-bot'])
    subprocess.run(['git', 'commit', '-am', 'README updated'])
    subprocess.run(['git', 'push'])

    time.sleep(10)
