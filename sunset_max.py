#!/usr/bin/python

import subprocess
from time import sleep


def running_from_cli(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()


if __name__ == "__main__":
    running_from_cli('/var/www/rfoutlet/codesend 4478268')
    sleep(1)
    running_from_cli('/var/www/rfoutlet/codesend 4478268')
    sleep(1)
    running_from_cli('/var/www/rfoutlet/codesend 4478268')
    running_from_cli('/var/www/rfoutlet/codesend 4480268')
    sleep(1)
    running_from_cli('/var/www/rfoutlet/codesend 4480268')
    sleep(1)
    running_from_cli('/var/www/rfoutlet/codesend 4480268')
