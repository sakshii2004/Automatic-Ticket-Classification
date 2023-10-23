from sqlalchemy import create_engine, text
import os
from datetime import date

current_date = date.today()

connection_info = os.environ['connection_info']

engine = create_engine(connection_info,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_tickets_from_db_user():
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from final_db_tickets ORDER BY `date` DESC LIMIT 6"))
    tickets = []
    for row in result.all():
      tickets.append(dict(row._asdict()))
  return tickets


def load_tickets_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from final_db_tickets ORDER BY `date` DESC"))
    tickets = []
    for row in result.all():
      tickets.append(dict(row._asdict()))
  return tickets


def load_tickets_0():
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from final_db_tickets where Dominant_Topic=0 ORDER BY `date` DESC"))
    tickets = []
    for row in result.all():
      tickets.append(dict(row._asdict()))
  return tickets

def load_tickets_1():
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from final_db_tickets where Dominant_Topic=1 ORDER BY `date` DESC"))
    tickets = []
    for row in result.all():
      tickets.append(dict(row._asdict()))
  return tickets

def load_tickets_2():
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from final_db_tickets where Dominant_Topic=2 ORDER BY `date` DESC"))
    tickets = []
    for row in result.all():
      tickets.append(dict(row._asdict()))
  return tickets

def load_tickets_3():
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from final_db_tickets where Dominant_Topic=3 ORDER BY `date` DESC"))
    tickets = []
    for row in result.all():
      tickets.append(dict(row._asdict()))
  return tickets

def load_tickets_4():
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from final_db_tickets where Dominant_Topic=4 ORDER BY `date` DESC"))
  tickets = []
  for row in result.all():
    tickets.append(dict(row._asdict()))
  return tickets


def add_ticket_to_db(data, topic):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO final_db_tickets (zip_code, issue, date, state, product, company, complaint_what_happened, tags, Dominant_Topic) VALUES(:zip_code, :issue, :date, :state, :product, :company, :complaint_what_happened, :tags, :topic)"
    )
    variables = {
      "zip_code": data['zip_code'],
      "issue": data['issue'],
      "date": current_date,
      "state": data['state'],
      "product": data['product'],
      "company": data['company'],
      "complaint_what_happened": data['complaint_what_happened'],
      "tags": data['tags'],
      "topic": topic
    }
    conn.execute(query, variables)
