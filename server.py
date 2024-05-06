from flask import Flask, render_template, request
from ExecuteAndPdfNotebook import runNotebook
from weather import get_current_weather
from waitress import serve
from datetime import datetime

app = Flask(__name__)


# Define some global variables to track last time of run for each 
global lastRunCreditAggs
lastRunCreditAggs = 0


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/creditAggregates')
def get_creditAggs():

    global lastRunCreditAggs

    #Almost certainly will have been run before
    if lastRunCreditAggs:

        #print('Last run triggered')

        timeDelta = datetime.now() - lastRunCreditAggs

        secondsTimeDelta = timeDelta.days*24*60*60 + timeDelta.seconds

        #Run again if was run more than 100 seconds ago
        if secondsTimeDelta > 100:

             a = runNotebook("CreditAggregatesExample.ipynb")

             lastRunCreditAggs = datetime.now()
    
             with open('creditAggregates.html', 'w') as f:
                 f.write(a)
        else:
            #Get last run from file
            #print('Not running again, looking for existing html')
            with open('creditAggregates.html', 'r') as f:
                a = f.read()
            
    else:
        a = runNotebook("CreditAggregatesExample.ipynb")
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


if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port = 8000)


