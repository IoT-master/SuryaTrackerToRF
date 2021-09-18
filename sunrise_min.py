#!/usr/bin/python
from Confidential.switch_table import switch1on
import subprocess
from time import sleep


def running_from_cli(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()


if __name__ == "__main__":
    running_from_cli(f'/var/www/rfoutlet/codesend {switch1on}')
    sleep(1)
    running_from_cli(f'/var/www/rfoutlet/codesend {switch1on}')
    sleep(1)
    running_from_cli(f'/var/www/rfoutlet/codesend {switch1on}')
