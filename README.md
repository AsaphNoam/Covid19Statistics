# Covid19Statistics

Serves 3 endpoints for extracting covid19 data from the past 30 days.

Useage:
localhost:5000/"method"?country="country"

Example - curl localhost:5000/newCasesPeak?country=canada

Methods - 

newCasesPeak - Returns the date (and value) of the highest peak of new Covid-19 cases in the last 30 days for a required country.

recoveredPeak - Returns the date (and value) of the highest peak of recovered Covid-19 cases in the last 30 days for the required country.

deathsPeak - Returns the date (and value) of the highest peak of death Covid-19 cases in the last 30 days for a required country.

status - Returns a value of success / fail to contact the backend API



All data is pulled from API by https://covid19tracking.narrativa.com/index_en.html
