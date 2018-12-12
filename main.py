from flask import Flask, render_template, request, flash
from simData import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'iufnaofiLKE'


@app.route('/')
def index():
    return render_template("SmartLivingHomepage.html")


@app.route('/Sim.html', methods=['GET', 'POST'])
def sim():
    calc = simData()
    if request.method == 'GET':
        return render_template("Sim.html", calc=calc)
    elif request.method == 'POST':
        return render_template("SimResults.html", calc=calc)


if __name__ == '__main__':
    app.run()
