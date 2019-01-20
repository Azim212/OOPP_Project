from flask import Flask, render_template, request, flash
from simData import *
import shelve
import AdaptedSimulationCode as simCode
app = Flask(__name__)
app.config['SECRET_KEY'] = 'iufnaofiLKE'
simStorage = shelve.open('simStorage')


@app.route('/')
def index():
    return render_template("SmartLivingHomepage.html")


@app.route('/Sim.html', methods=['GET', 'POST'])
def sim():
    calc = simData(request.form)
    error = None
    if request.method == 'POST':
        if calc.validate():
            simStorage['ledNum'] = int(calc.led.data)
            simStorage['cflNum'] = int(calc.cfl.data)
            simStorage['incNum'] = int(calc.inc.data)
            simStorage['toiletNum'] = int(calc.toish.data)
            simStorage['toiletType'] = calc.toitype.data
            return render_template("SimResults.html", calc=calc)
        else:
            error = 'Please enter numbers only.'
            return render_template("Sim.html", calc=calc, error=error)
    else:
        return render_template("Sim.html", calc=calc, error=error)


@app.route('/SimCalculation.html')
def calc():
    led = simStorage['ledNum']
    cfl = simStorage['cflNum']
    inc = simStorage['incNum']
    toi = simStorage['toiletNum']
    toitype = simStorage['toiletType']
    finalPrice = simCode.calcPrice()
    return render_template("SimCalculation.html", led=led, cfl=cfl, inc=inc, toi=toi, toitype=toitype, finalPrice=finalPrice)


if __name__ == '__main__':
    app.run()


