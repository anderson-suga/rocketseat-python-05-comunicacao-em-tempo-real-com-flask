from flask import Flask, jsonify, request
from repository.database import db
from models.payment import Payment
from datetime import datetime, timedelta

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "SECRETE_KEY_WEBSOCKET"

db.init_app(app)


@app.route("/payments/pix", methods=["POST"])
def create_payment_pix():
    data = request.get_json()

    if "value" not in data:
        return jsonify({"message": "Value is required"}), 400

    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(value=data["value"], expiration_date=expiration_date)

    db.session.add(new_payment)
    db.session.commit()

    return jsonify(
        {"message": "Payment created with success!", "payment": new_payment.to_dict()}
    )


@app.route("/payments/pix/confirmation", methods=["POST"])
def confirm_payment_pix():
    return jsonify({"message": "Payment confirmed with success!"})


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_pagamento(payment_id):
    return "pagamento pix"


if __name__ == "__main__":
    app.run(debug=True)
