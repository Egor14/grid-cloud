import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloudtask.settings')
import django
django.setup()
from cloudtask import settings

from worker.models import Task
import subprocess
import time

while True:
    if len(Task.objects.all()) >= 5:
        subprocess.run(f'az login -u {settings.azure_username} -p {settings.azure_password}')
        subprocess.run('az vm start --name MyVm1 --resource-group MyResourceGroup')
        while(len(Task.objects.all()) > 0):
            time.sleep(5)
        else:
            subprocess.run('az vm stop --resource-group MyResourceGroup --name MyVm1')

    time.sleep(60)
