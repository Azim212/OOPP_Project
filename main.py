from flask import Flask, render_template, request, flash
from simData import *
import shelve
app = Flask(__name__)
app.config['SECRET_KEY'] = 'iufnaofiLKE'
#simStorage = shelve.open('simStorage')
#calc.led.data = simStorage['ledNum']
#calc.cfl.data = simStorage['cflNum']
#calc.inc.data = simStorage['incNum']
#calc.toish.data = simStorage['toiletNum']
#calc.toitype.data = simStorage['toiletType']
#simStorage.close()

@app.route('/')
def index():
    return render_template("SmartLivingHomepage.html")


@app.route('/Sim.html', methods=['GET', 'POST'])
def sim():
    calc = simData(request.form)
    error = None
    if request.method == 'POST':
        if calc.validate():
            return render_template("SimResults.html", calc=calc)
        else:
            error = 'Please enter numbers only.'
            return render_template("Sim.html", calc=calc, error=error)
    else:
        return render_template("Sim.html", calc=calc, error=error)


if __name__ == '__main__':
    app.run()


