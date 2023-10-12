import numpy as np
from flask import Flask, render_template, request
from database import load_tickets_from_db, add_ticket_to_db

app = Flask(__name__)


@app.route('/')
def show_homepage():
  return render_template('home.html')


@app.route('/create_new')
def show_form():
  return render_template('create_new.html')


@app.route('/tickets')
def show_tickets():
  tickets = load_tickets_from_db()
  return render_template('my_tickets.html', tickets=tickets)

@app.route("/ticket/submit", methods=['POST'])
def write_submit():
  data = request.form
  add_ticket_to_db(data)
  return "you ticket has been submitted!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
