import numpy as np
from flask import Flask, render_template, request
from database import load_tickets_from_db, load_tickets_from_db_user, add_ticket_to_db, load_tickets_0, load_tickets_1, load_tickets_2, load_tickets_3, load_tickets_4, load_one_complaint_from_db
from classifier import preprocess, predict

app = Flask(__name__)


@app.route('/')
def show_homepage():
  return render_template('home.html')


@app.route('/create_new')
def show_form():
  return render_template('create_new.html')


@app.route('/tickets')
def show_tickets():
  tickets = load_tickets_from_db_user()
  return render_template('my_tickets.html', tickets=tickets)


@app.route("/ticket/submit", methods=['POST'])
def write_submit():
  data = request.form
  text = preprocess(data['complaint_what_happened'])
  topic = predict(text)
  add_ticket_to_db(data, topic)
  return render_template('submitted.html')

@app.route("/support")
def support_page():
  return render_template('support.html')


@app.route('/all-tickets')  #ALL THE TICKETS FOR SUPPORT SIDE
def show_all_tickets():
  tickets = load_tickets_from_db()
  return render_template('all_tickets.html', tickets=tickets)


@app.route('/loans')
def show_loan_tickets():
  tickets = load_tickets_0()
  return render_template('loans.html', tickets=tickets)


@app.route('/account-services')
def show_account_tickets():
  tickets = load_tickets_1()
  return render_template('account_services.html', tickets=tickets)


@app.route('/credit-prepaid')
def show_credit_tickets():
  tickets = load_tickets_2()
  return render_template('credit_prepaid.html', tickets=tickets)


@app.route('/theft-fraud')
def show_theft_tickets():
  tickets = load_tickets_3()
  return render_template('theft_fraud.html', tickets=tickets)


@app.route('/booking-refund')
def show_booking_tickets():
  tickets = load_tickets_4()
  return render_template('booking_refund.html', tickets=tickets)


@app.route("/tickets/<complaint_id>")
def show_complaint(complaint_id):
  complaint = load_one_complaint_from_db(complaint_id)
  return render_template('support_complaint.html', ticket=complaint)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
