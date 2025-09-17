#!/usr/bin/env python3
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/customers', methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        all_customers = Customer.query.all()
        return make_response(jsonify([c.to_dict() for c in all_customers]), 200)

    if request.method == 'POST':
        data = request.get_json()
        try:
            customer = Customer(
                name=data.get("name"),
                email=data.get("email"),
                age=data.get("age")
            )
            db.session.add(customer)
            db.session.commit()
            return make_response(customer.to_dict(), 200)
        except Exception as e:
            return make_response({"error": str(e)}, 400)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
