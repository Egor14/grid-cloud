import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloudtask.settings')
import django
django.setup()
from cloudtask import settings

from worker.models import Task
import time

while True:
    if len(Task.objects.filter(status=False)) >= 5:
        os.system(f'az login -u {settings.azure_username} -p {settings.azure_password}')
        os.system('az vm start --name MyVm1 --resource-group MyResourceGroup')
        while(len(Task.objects.all()) > 0):
            time.sleep(5)
        else:
            os.system(f'az login -u {settings.azure_username} -p {settings.azure_password}')
            os.system('az vm stop --resource-group MyResourceGroup --name MyVm1')

    time.sleep(60)
