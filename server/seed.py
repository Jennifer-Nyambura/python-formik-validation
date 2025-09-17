#!/usr/bin/env python3
from app import app, db, Customer

with app.app_context():
    print("Seeding database...")

    Customer.query.delete()

    c1 = Customer(name="Alice", email="alice@example.com", age=25)
    c2 = Customer(name="Bob", email="bob@example.com", age=32)
    c3 = Customer(name="Charlie", email="charlie@example.com", age=40)

    db.session.add_all([c1, c2, c3])
    db.session.commit()

    print("Done seeding!")
