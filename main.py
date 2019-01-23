from flask import Flask, render_template, request
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
    '''if request.method == 'POST':
        if request.form['form'] == 'electric' and request.form['form'] == 'water':
            if calcElectric.validate() and calcWater.validate() is False:
                errorWater = 'Only numbers lower than 100 are allowed.'
                errorElectric = 'Only numbers lower than 100 are allowed.'
                return render_template("Sim.html", errorWater=errorWater, errorElectric=errorElectric,
                                        calcElectric=calcElectric, calcWater=calcWater)
            if calcElectric.validate() and calcWater.validate():
                with shelve.open('simStorage') as simStorage:
                    simStorage['ledNum'] = int(calcElectric.led.data)
                    simStorage['cflNum'] = int(calcElectric.cfl.data)
                    simStorage['incNum'] = int(calcElectric.inc.data)
                    simStorage['toiletNum'] = int(calcWater.toish.data)
                    simStorage['toiletType'] = calcWater.toitype.data
                finalWatt = simCode.calcWatt()
                finalPrice = simCode.calcWattPrice()
                dailyWatt = round(finalWatt / 30, 2)
                dailyPrice = round(finalPrice / 30, 2)
                yearlyWatt = round(finalWatt * 12, 2)
                yearlyPrice = round(finalPrice * 12, 2)
                cubmtrperday = simCode.calcCubmtr()
                cubmtrPrice = simCode.calcCubmtrPrice()
                dailyCubmtr = round(cubmtrperday / 30, 2)
                dailyCubmtrPrice = round(cubmtrPrice / 30, 2)
                yearlyCubmtr = round(cubmtrperday * 12, 2)
                yearlyCubmtrPrice = round(cubmtrPrice * 12, 2)
                openTab = True
                return render_template("Sim.html", openTab=openTab, cubmtrPrice=cubmtrPrice, cubmtrperday=cubmtrperday,
                                       yearlyCubmtrPrice=yearlyCubmtrPrice, yearlyCubmtr=yearlyCubmtr,
                                       dailyCubmtrPrice=dailyCubmtrPrice, dailyCubmtr=dailyCubmtr,
                                       yearlyPrice=yearlyPrice, yearlyWatt=yearlyWatt, dailyPrice=dailyPrice,
                                       dailyWatt=dailyWatt, finalPrice=finalPrice, finalWatt=finalWatt,
                                       calcElectric=calcElectric, calcWater=calcWater)'''
    if request.method == 'POST':
            if calc.validate():
                with shelve.open('simStorage') as simStorage:
                    simStorage['ledNum'] = int(calc.led.data)
                    simStorage['cflNum'] = int(calc.cfl.data)
                    simStorage['incNum'] = int(calc.inc.data)
                    simStorage['toiletNum'] = int(calc.toish.data)
                    simStorage['toiletType'] = calc.toitype.data
                    led = simStorage['ledNum']
                    cfl = simStorage['cflNum']
                    inc = simStorage['incNum']
                    toitype = simStorage['toiletType']
                finalWatt = simCode.calcWatt()
                finalPrice = simCode.calcWattPrice()
                dailyWatt = round(finalWatt / 30, 2)
                dailyPrice = round(finalPrice / 30, 2)
                yearlyWatt = round(finalWatt * 12, 2)
                yearlyPrice = round(finalPrice * 12, 2)
                cubmtrperday = simCode.calcCubmtr()
                cubmtrPrice = simCode.calcCubmtrPrice()
                dailyCubmtr = round(cubmtrperday / 30, 2)
                dailyCubmtrPrice = round(cubmtrPrice / 30, 2)
                yearlyCubmtr = round(cubmtrperday * 12, 2)
                yearlyCubmtrPrice = round(cubmtrPrice * 12, 2)
                tipElc = simCode.tipsElc()
                tipWtr = simCode.tipsWtr()
                global replaceInc
                global replaceCfl
                global saveSmartE
                global saveSmartW
                global replaceOldorConv
                replaceInc = False
                replaceCfl = False
                saveSmartE = False
                saveSmartW = False
                replaceOldorConv = False
                for i in tipElc:
                    if i == 'replaceInc':
                        replaceInc = True
                    if i == 'replaceCfl':
                        replaceCfl = True
                    if i == 'saveSmartE':
                        saveSmartE = True
                for i in tipWtr:
                    if i == 'replaceOldorConv':
                        replaceOldorConv = True
                    if i == 'saveSmartW':
                        saveSmartW = True
                openTab = True
                return render_template("Sim.html", toitype=toitype, inc=inc, cfl=cfl, led=led, replaceOldorConv=replaceOldorConv, saveSmartW=saveSmartW, saveSmartE=saveSmartE, replaceCfl=replaceCfl, replaceInc=replaceInc, openTab=openTab, cubmtrPrice=cubmtrPrice, cubmtrperday=cubmtrperday,
                                       yearlyCubmtrPrice=yearlyCubmtrPrice, yearlyCubmtr=yearlyCubmtr,
                                       dailyCubmtrPrice=dailyCubmtrPrice, dailyCubmtr=dailyCubmtr,
                                       yearlyPrice=yearlyPrice, yearlyWatt=yearlyWatt, dailyPrice=dailyPrice,
                                       dailyWatt=dailyWatt, finalPrice=finalPrice, finalWatt=finalWatt,
                                       calc=calc)
            else:
                error = 'Only numbers lower than 100 are allowed.'
                return render_template("Sim.html", error=error, calc=calc)
    else:
        return render_template("Sim.html", calc=calc)


if __name__ == '__main__':
    app.run()


