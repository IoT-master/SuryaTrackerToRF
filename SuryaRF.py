from pathlib import Path
import json
from datetime import datetime, timedelta


def read_file(file_location):
    path = Path.cwd().joinpath(file_location)
    sundata_json = json.loads(path.read_text())
    return sundata_json


def fill_month_text(month):
    unformatted_month = str(month)
    return unformatted_month if len(unformatted_month) == 2 else "0" + unformatted_month


def get_sunrise_sunset_times(sundata):
    now = datetime.now()
    current_month = fill_month_text(now.month)
    daydata_json = sundata[current_month][str(now.day)]
    sunrise = (
        daydata_json["Sunrise/Sunset"]["Sunrise"]
        .replace("am", "AM")
        .replace("pm", "PM")
    )
    sunset = (
        daydata_json["Sunrise/Sunset"]["Sunset"].replace("am", "AM").replace("pm", "PM")
    )
    sunrise = datetime.strptime(sunrise, "%I:%M %p \u2191").strftime("%M %H")
    sunset = datetime.strptime(sunset, "%I:%M %p \u2191").strftime("%M %H")
    print(f"Sunrise: {sunrise} Sunset: {sunset}")


def test_calendar_is_leap_year(sundata):
    day_counter = {}
    for k, v in sundata.items():
        day_counter[k] = len(v)
    assert day_counter == {
        "01": 31,
        "02": 28,
        "03": 31,
        "04": 30,
        "05": 31,
        "06": 30,
        "07": 31,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }


def test_calendar_is_not_leap_year(sundata):
    day_counter = {}
    for k, v in sundata.items():
        day_counter[k] = len(v)
    assert day_counter == {
        "01": 31,
        "02": 29,
        "03": 31,
        "04": 30,
        "05": 31,
        "06": 30,
        "07": 31,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }

def get_extreme_sunrise(sundata, sunrise=True):
    now = datetime.now()
    last_month = str((now - timedelta(weeks=4)).month)
    this_month = str((now).month)
    next_month = str((now + timedelta(weeks=4)).month)
    recent_three_months = map(
        lambda x: fill_month_text(x), [last_month, this_month, next_month]
    )
    min_time = 1e6
    max_time = 0
    for each_month in recent_three_months:
        for _, e_val in sundata[each_month].items():
            if sunrise:
                sun_time = datetime.strptime(
                    e_val["Sunrise/Sunset"]["Sunrise"].replace("am", "AM").replace("pm", "PM"),
                    "%I:%M %p \u2191",
                )
            else:
                sun_time = datetime.strptime(
                    e_val["Sunrise/Sunset"]["Sunset"].replace("am", "AM").replace("pm", "PM"),
                    "%I:%M %p \u2191",
                )

            if (sun_time.timestamp()) < min_time:
                min_time = sun_time.timestamp()
            if (sun_time.timestamp()) > min_time:
                max_time = sun_time.timestamp()

    print(datetime.fromtimestamp(min_time), datetime.fromtimestamp(max_time))

sundata = read_file("Confidential/Sundata.json")
get_extreme_sunrise(sundata, False)
