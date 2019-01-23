from flask import Flask, render_template, request, flash
from simData import *
import shelve
import AdaptedSimulationCode as simCode
app = Flask(__name__)
app.config['SECRET_KEY'] = 'iufnaofiLKE'

@app.route('/')
def index():
    return render_template("SmartLivingHomepage.html")


@app.route('/Sim.html', methods=['GET', 'POST'])
def sim():
    calc = simData(request.form)
    error = None
    if request.method == 'POST':
        if calc.validate():
            with shelve.open('simStorage') as simStorage:
                simStorage['ledNum'] = int(calc.led.data)
                simStorage['cflNum'] = int(calc.cfl.data)
                simStorage['incNum'] = int(calc.inc.data)
                simStorage['toiletNum'] = int(calc.toish.data)
                simStorage['toiletType'] = calc.toitype.data
            finalWatt = simCode.calcWatt()
            finalPrice = simCode.calcWattPrice()
            cubmtrperday = simCode.calcCubmtr()
            cubmtrPrice = simCode.calcCubmtrPrice()
            dailyWatt = round(finalWatt/30, 2)
            dailyPrice = round(finalPrice/30, 2)
            dailyCubmtr = round(cubmtrperday/30, 2)
            dailyCubmtrPrice = round(cubmtrPrice/30, 2)
            yearlyWatt = round(finalWatt * 12, 2)
            yearlyPrice = round(finalPrice * 12, 2)
            yearlyCubmtr = round(cubmtrperday * 12, 2)
            yearlyCubmtrPrice = round(cubmtrPrice * 12, 2)
            openTab = True
            return render_template("Sim.html", openTab=openTab, yearlyCubmtrPrice=yearlyCubmtrPrice, yearlyCubmtr=yearlyCubmtr, yearlyPrice=yearlyPrice, yearlyWatt=yearlyWatt, dailyCubmtrPrice=dailyCubmtrPrice, dailyCubmtr=dailyCubmtr, dailyPrice=dailyPrice, dailyWatt=dailyWatt, finalPrice=finalPrice, cubmtrperday=cubmtrperday, cubmtrPrice=cubmtrPrice, finalWatt=finalWatt, calc=calc)
        else:
            error = 'Only numbers lower than 100 are allowed.'
            return render_template("Sim.html", calc=calc, error=error)
    else:
        return render_template("Sim.html", calc=calc, error=error)


if __name__ == '__main__':
    app.run()


