from pathlib import Path
import re
from SuryaRF import *


def rewrite_cron(cron_loc, sunrise_min, sunrise, sunset, sunset_max):
    path = Path(cron_loc)
    text_in_cron = path.read_text()
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*sunrise_min\.py.*)", sunrise_min + r" \1", text_in_cron
    )
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*sunrise\.py.*)", sunrise + r" \1", text_in_cron
    )
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*sunset\.py.*)", sunset + r" \1", text_in_cron
    )
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*sunset_max\.py.*)", sunset_max + r" \1", text_in_cron
    )

    path.write_text(text_in_cron)


if __name__ == "__main__":
    CRON_LOCATION = "/var/spool/cron/crontabs/pi"
    sundata = read_file("Confidential/Sundata.json")
    sunrise, sunset = get_sunrise_sunset_times(sundata)
    sunrise_min, sunset_max = get_other_action(sundata, 60)
    print(sunrise_min, sunrise, sunset, sunset_max)
    rewrite_cron(CRON_LOCATION, sunrise_min, sunrise, sunset, sunset_max)
    # rewrite_cron(Path.cwd().joinpath('Confidential/crontab.txt'), sunrise_min, sunrise, sunset, sunset_max)
