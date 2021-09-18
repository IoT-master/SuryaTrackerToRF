from pathlib import Path
import re
from SuryaRF import *


def rewrite_cron(cron_loc, sunset_min, sunrise, sunset, sunset_max):
    path = Path(cron_loc)
    text_in_cron = path.read_text()
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*on2switch1\.py.*)", sunset_min + r" \1", text_in_cron
    )
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*sunrise\.py.*)", sunrise + r" \1", text_in_cron
    )
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*sunset\.py.*)", sunset + r" \1", text_in_cron
    )
    text_in_cron = re.sub(
        r"[0-9]+ [0-9]+ (\* .*off1switch1\.py.*)", sunset_max + r" \1", text_in_cron
    )

    path.write_text(text_in_cron)


if __name__ == "__main__":
    CRON_LOCATION = "/var/spool/cron/crontabs/pi"
    sundata = read_file("Confidential/Sundata.json")
    sunrise, sunset = get_sunrise_sunset_times(sundata)
    sunset_min, sunset_max = get_other_action(sundata, 60)
    print(sunset_min, sunrise, sunset, sunset_max)
    rewrite_cron("CRON_LOCATION", sunset_min, sunrise, sunset, sunset_max)
