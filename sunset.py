#!/usr/bin/python3
from base_action import run_event
from Confidential.switch_table import switch1on
from Confidential.switch_table import switch2on

run_event([switch1on, switch2on])