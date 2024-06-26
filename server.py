from flask import Flask, render_template, request
from ExecuteAndPdfNotebook import runNotebook
from weather import get_current_weather
from waitress import serve
from datetime import datetime

app = Flask(__name__)


# Define some global variables to track last time of run for each 
global lastRunCreditAggs
lastRunCreditAggs = 0

# Set the timezone to Australia
import os, time
os.environ['TZ'] = 'Australia/NSW'
time.tzset()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/creditAggregates')
def get_creditAggs():

    global lastRunCreditAggs

    #Almost certainly will have been run before
    if lastRunCreditAggs:

        timeDelta = datetime.now() - lastRunCreditAggs

        secondsTimeDelta = timeDelta.days*24*60*60 + timeDelta.seconds

        #Run again if was run more than 10 seconds ago
        if secondsTimeDelta > 10:

             a = runNotebook("CreditAggregatesNoTable.ipynb")

             lastRunCreditAggs = datetime.now()
    
             with open('creditAggregates.html', 'w') as f:
                 f.write(a)
        else:
            #Else get last run from file
            #print('Not running again, looking for existing html')
            with open('creditAggregates.html', 'r') as f:
                a = f.read()
            
    else:
        a = runNotebook("CreditAggregatesNoTable.ipynb")
        lastRunCreditAggs = datetime.now()
        with open('creditAggregates.html', 'w') as f:
                 f.write(a)

    return a



@app.route('/labourForce')
def get_labourForce():
    #city = request.args.get('city')
    #weather_data = get_current_weather(city)
    #a = runNotebook("LabourForceExample.ipynb")
    a = runNotebook("LabourForceExample.ipynb")

    with open('labourForce.html', 'w') as f:
        f.write(a)

    #return htmlOutput
    return a
    #                       title=weather_data["name"],
    #                       status=weather_data["weather"][0]["description"].capitalize(),
    #                       temp=f"{weather_data['main']['temp']:.1f}",
    #                       feels_like=f"{weather_data['main']['feels_like']:.1f}")

@app.route('/lendingIndicators')
def get_lendingIndicators():
    #city = request.args.get('city')
    #weather_data = get_current_weather(city)
    #a = runNotebook("LabourForceExample.ipynb")
    a = runNotebook("ABS Lending Indicators Table 1.ipynb")

    with open('lendingIndicators.html', 'w') as f:
        f.write(a)

    #return htmlOutput
    return a
    #                       title=weather_data["name"],
    #                       status=weather_data["weather"][0]["description"].capitalize(),
    #                       temp=f"{weather_data['main']['temp']:.1f}",
    #                       feels_like=f"{weather_data['main']['feels_like']:.1f}")


@app.route('/householdSpendingIndicator')
def get_householdSpendingIndicator():
    #city = request.args.get('city')
    #weather_data = get_current_weather(city)
    #a = runNotebook("LabourForceExample.ipynb")
    a = runNotebook("HouseholdSpendingIndicator.ipynb")

    with open('HouseholdSpendingIndicator.html', 'w') as f:
        f.write(a)

    #return htmlOutput
    return a
    #                       title=weather_data["name"],
    #                       status=weather_data["weather"][0]["description"].capitalize(),
    #                       temp=f"{weather_data['main']['temp']:.1f}",
    #                       feels_like=f"{weather_data['main']['feels_like']:.1f}")



@app.route('/graphingExamples')
def get_graphingExamples():
    #city = request.args.get('city')
    #weather_data = get_current_weather(city)
    #a = runNotebook("LabourForceExample.ipynb")
    a = runNotebook("Graphing Examples.ipynb")

    with open('graphingExamples.html', 'w') as f:
        f.write(a)

    #return htmlOutput
    return a
    #                       title=weather_data["name"],
    #                       status=weather_data["weather"][0]["description"].capitalize(),
    #                       temp=f"{weather_data['main']['temp']:.1f}",
    #                       feels_like=f"{weather_data['main']['feels_like']:.1f}")





if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port = 8000)


