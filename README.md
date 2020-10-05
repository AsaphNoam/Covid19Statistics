# Covid19Statistics

Useage:
localhost:5000/"method"?country="country"

Example - curl localhost:5000/newCasesPeak?country=canada

Methods - 

newCasesPeak - Returns the date (and value) of the highest peak of new Covid-19 cases in the last 30 days for a required country.

recoveredPeak - Returns the date (and value) of the highest peak of recovered Covid-19 cases in the last 30 days for the required country.

deathsPeak - Returns the date (and value) of the highest peak of death Covid-19 cases in the last 30 days for a required country.

status - Returns a value of success / fail to contact the backend API
