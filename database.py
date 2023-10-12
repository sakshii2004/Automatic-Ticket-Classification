from sqlalchemy import create_engine, text
import os
from datetime import date

current_date = date.today()

connection_info = os.environ['connection_info']

engine = create_engine(connection_info,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_tickets_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tickets ORDER BY `date` DESC"))
    tickets = []
    for row in result.all():
      tickets.append(dict(row._asdict()))
  return tickets


def add_ticket_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO tickets (zip_code, issue, date, state, product, company, complaint_what_happened, tags) VALUES(:zip_code, :issue, :date, :state, :product, :company, :complaint_what_happened, :tags)")
    variables = {"zip_code":data['zip_code'], "issue":data['issue'], "date":current_date, "state":data['state'], "product":data['product'], "company":data['company'],"complaint_what_happened":data['complaint_what_happened'], "tags":data['tags']}
    conn.execute(query, variables)
