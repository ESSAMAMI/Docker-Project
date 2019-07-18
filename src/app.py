from flask import Flask, render_template, request
import pandas as pd
import random
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
        why = ['SORRY NOT TODAY',  'AUDI A1', 'SORRY NOT TODAY', 'SORRY NOT TODAY','AUDI A5']
        win = why[random.randint(0,4)]
        setPerson(surname, name, age, address, win)
        person = getPerson()
        return render_template('crud.html', person=person)
