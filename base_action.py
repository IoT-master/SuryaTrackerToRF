import subprocess
from time import sleep

def _running_from_cli(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()

def _running_x_times(signal, x=3, secs=1):
    for _ in range(x):
        sleep(secs)
        _running_from_cli(f'/var/www/rfoutlet/codesend {signal}')

def run_event(action_list):
    for event in action_list:
        _running_x_times(event)
