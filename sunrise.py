#!/usr/bin/python3
from base_action import run_event
from Confidential.switch_table import switch1off
from Confidential.switch_table import switch2off
run_event([switch1off, switch2off])