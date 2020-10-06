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
from_date = cur_date - timedelta(days=30)

# Drop hours/minutes/seconds from date
cur_date = str(cur_date).split(" ")[0]
from_date = str(from_date).split(" ")[0]

'''Find the peak attribute by attribute name and country'''


def find_peak_attribute(attr_name, country):
    # Create the request from the API
    response = requests.get(
        f"https://api.covid19tracking.narrativa.com/api/country/{country}?date_from={from_date}&date_to={cur_date}")
    data = response.json()
    max_value, max_day = 0, ""
    # Find the max value and day from all days
    for day in data["dates"]:
        # Created a special case since there are many ways to spell the US, and it's likely to be queried
        if country.lower() in ["usa", "us", "united states", "america"]:
            day_data = data["dates"][day]["countries"]["US"]
        else:
            day_data = data["dates"][day]["countries"][country.title()]
        attr_value = day_data[attr_name]
        max_value = max(attr_value, max_value)
        if max_value == attr_value:
            max_day = day

    return max_value, max_day


'''Format the result as a JSON string'''


def format_response(country, method, val, date):
    res = {"country": country, "method": method, "date": date, "value": val}
    return json.dumps(res)


@app.route('/status')
def status():
    # Check today's data for israel as a status check
    response = requests.get(f"https://api.covid19tracking.narrativa.com/api/{cur_date}/country/Israel")
    code = response.status_code
    # If the result returned a 2xx code, return success, otherwise failure
    result = "success" if 200 <= code < 300 else "failure"
    res = {"status": result}
    return json.dumps(res)


@app.route('/newCasesPeak')
def new_cases_peak():
    # Get the requested country and the peak date and value
    country = request.args.get("country")
    val, date = find_peak_attribute(NEW_CASES, country)
    res = format_response(country, "newCasesPeak", val, date)
    return res


@app.route('/recoveredPeak')
def recovered_peak():
    # Get the requested country and the peak date and value
    country = request.args.get("country")
    val, date = find_peak_attribute(RECOVERED, country)
    res = format_response(country, "recoveredPeak", val, date)
    return res


@app.route('/deathsPeak')
def deaths_peak():
    # Get the requested country and the peak date and value
    country = request.args.get("country")
    val, date = find_peak_attribute(DEATHS, country)
    res = format_response(country, "deathsPeak", val, date)
    return res


@app.errorhandler(404)
def page_not_found(error):
    return "{}"


@app.errorhandler(500)
def page_not_found(error):
    return "{}"
