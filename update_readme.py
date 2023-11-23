import subprocess
import time
from datetime import datetime
import os

github_token = os.environ.get('GH_TOKEN')

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open('README.md', 'w') as file:
        file.write(f'## Current Hour: {current_time}\n')

    subprocess.run(['git', 'config', '--global', 'user.email', 'my-bot@example.com'])
    subprocess.run(['git', 'config', '--global', 'user.name', 'my-bot'])
    subprocess.run(['git', 'commit', '-am', 'README updated'])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])

    # Use the GitHub token for authentication
    subprocess.run(['git', 'push', '-u', 'origin', 'main'], env={'GITHUB_TOKEN': github_token})

    time.sleep(10)
