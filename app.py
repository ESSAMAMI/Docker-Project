from flask import Flask, render_template, request
import pandas as pd
from model.model import getConnection, getPerson, setPerson

app = Flask(__name__)

@app.route('/')
def home():

    person = getPerson()
    if person:
        return render_template('crud.html', person=person)
    else:
        return render_template('crud.html')

@app.route('/add_consumer', methods=['POST'])
def add_consumer():
    pass

    if request.method == 'POST':

        name = request.form['name']
        surname = request.form['surname']
        address = request.form['address']
        age = request.form['age']
        setPerson(surname, name, age, address, 'SORRY NOT TODAY')
        person = getPerson()
        return render_template('crud.html', person=person)
