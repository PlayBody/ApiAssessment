from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
db = SQLAlchemy(app)

class Receivable(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  reference = db.Column(db.String(255), nullable=False)
  currencyCode = db.Column(db.String(10), nullable=False)
  issueDate = db.Column(db.String(10), nullable=False)
  openingValue = db.Column(db.Float, nullable=False)
  paidValue = db.Column(db.Float, nullable=False)
  dueDate = db.Column(db.String(10), nullable=False)
  closedDate = db.Column(db.String(10))
  cancelled = db.Column(db.Boolean, default=False)
  debtorName = db.Column(db.String(255), nullable=False)
  debtorReference = db.Column(db.String(255), nullable=False)
  debtorAddress1 = db.Column(db.String(255))
  debtorAddress2 = db.Column(db.String(255))
  debtorTown = db.Column(db.String(255))
  debtorState = db.Column(db.String(255))
  debtorZip = db.Column(db.String(255))
  debtorCountryCode = db.Column(db.String(10), nullable=False)
  debtorRegistrationNumber = db.Column(db.String(255))

@app.route('/api/receivables', methods=['POST'])
def store_receivables():
  data = request.get_json()
  try:
    for item in data:
      receivable = Receivable(**item)
      db.session.add(receivable)
    db.session.commit()
    return jsonify({'message': 'Receivables data stored successfully'})
  except IntegrityError:
    db.session.rollback()
    return jsonify({'error': 'Invalid payload'}), 400

@app.route('/api/receivables/summary', methods=['GET'])
def get_summary():
  open_invoices = db.session.query(db.func.sum(Receivable.openingValue)).filter(Receivable.closedDate == None).scalar()
  closed_invoices = db.session.query(db.func.sum(Receivable.openingValue)).filter(Receivable.closedDate != None).scalar()
  return jsonify({'openInvoices': open_invoices or 0, 'closedInvoices': closed_invoices or 0})

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run()