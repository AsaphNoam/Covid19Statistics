from datetime import datetime, timedelta

import requests
from flask import Flask
from flask import request
import json

NEW_CASES = "today_new_confirmed"
RECOVERED = "today_new_recovered"
DEATHS = "today_new_deaths"
app = Flask(__name__)
# Get the current date and the date 30 days ago, and keep them as strings
cur_date = datetime.now()
from_date = cur_date - timedelta(days=3)
# Drop hours/minutes/seconds from date
cur_date = str(cur_date).split(" ")[0]
from_date = str(from_date).split(" ")[0]
response = requests.get(f"https://api.covid19tracking.narrativa.com/api?date_from={from_date}&date_to={cur_date}")


def find_peak_attribute(attr_name, country):
    data = response.json()
    m, max_day = 0, ""
    for day in data["dates"]:
        day_data = data["dates"][day]["countries"][country.capitalize()]
        attr_value = day_data[f"{attr_name}"]
        m = max(attr_value, m)
        # if m == attr_value:
        #     max_day = day

    return m


def format_response(country, method, val):
    date = cur_date
    res = {"country": country, "method": method, "date": date, "value": val}
    return json.dumps(res)


@app.route('/')
def hello_world():
    return response.json()


@app.route('/status')
def status():
    code = response.status_code
    result = "success" if 200 <= code < 300 else "failure"
    res = {"status": result}
    return json.dumps(res)


@app.route('/newCasesPeak')
def new_cases_peak():
    country = request.args.get("country")
    val = find_peak_attribute(NEW_CASES, country)
    res = format_response(country, "newCasesPeak", val)
    return res


@app.route('/recoveredPeak')
def recovered_peak():
    country = request.args.get("country")
    val = find_peak_attribute(RECOVERED, country)
    res = format_response(country, "recoveredPeak", val)
    return res


@app.route('/deathsPeak')
def deaths_peak():
    country = request.args.get("country")
    val = find_peak_attribute(DEATHS, country)
    res = format_response(country, "deathsPeak", val)
    return res


@app.errorhandler(404)
def page_not_found(error):
    return "{}"

@app.errorhandler(500)
def page_not_found(error):
    return "{}"