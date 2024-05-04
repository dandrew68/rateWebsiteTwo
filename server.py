from flask import Flask, render_template, request
from ExecuteAndPdfNotebook import runNotebook
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/creditAggregates')
def get_creditAggs():
    #city = request.args.get('city')
    #weather_data = get_current_weather(city)
    #a = runNotebook("LabourForceExample.ipynb")
    a = runNotebook("CreditAggregatesExample.ipynb")
    #return htmlOutput
    return a
    #                       title=weather_data["name"],
    #                       status=weather_data["weather"][0]["description"].capitalize(),
    #                       temp=f"{weather_data['main']['temp']:.1f}",
    #                       feels_like=f"{weather_data['main']['feels_like']:.1f}")


@app.route('/labourForce')
def get_labourForce():
    #city = request.args.get('city')
    #weather_data = get_current_weather(city)
    #a = runNotebook("LabourForceExample.ipynb")
    a = runNotebook("LabourForceExample.ipynb")
    #return htmlOutput
    return a
    #                       title=weather_data["name"],
    #                       status=weather_data["weather"][0]["description"].capitalize(),
    #                       temp=f"{weather_data['main']['temp']:.1f}",
    #                       feels_like=f"{weather_data['main']['feels_like']:.1f}")


if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port = 8000)


