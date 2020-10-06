pipeline {
  agent any
  stages {
    stage('Checkout Scm') {
      steps {
        git(credentialsId: '31a3b92c-a374-4e40-89fc-0051cea58a76', url: 'https://github.com/AsaphNoam/Covid19Statistics')
      }
    }

    stage('Shell script 0') {
      steps {
        sh '''C:\\\\Users\\\\Asaph\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python37\\\\python.exe --version
C:\\\\Users\\\\Asaph\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python37\\\\python.exe -m pip install requests
C:\\\\Users\\\\Asaph\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python37\\\\python.exe -m pip install flask
export FLASK_APP=main.py
flask run &
C:\\\\Users\\\\Asaph\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python37\\\\python.exe main.py
curl localhost:5000/status
curl localhost:5000/newCasesPeak?country=israel
curl localhost:5000/newCasesPeak?country=canada
curl localhost:5000/deathsPeak?country=united%20kingdom
curl localhost:5000/recoveredPeak?country=germany
curl localhost:5000/newCasesPeak?country=fakeCountry
curl localhost:5000/recoveredPeak?country=australia
curl localhost:5000/deathsPeak?country=China
curl localhost:5000/newCasesPeak?country=new%20zeland
curl localhost:5000/newCasesPeak?country=us
curl localhost:5000/deathsPeak?country=us
'''
      }
    }

  }
}
