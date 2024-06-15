import os
from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix

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

    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment()

    new_payment.bank_payment_id = data_payment_pix["bank_payment_id"]
    new_payment.qr_code = data_payment_pix["qr_code_path"]

    db.session.add(new_payment)
    db.session.commit()

    return jsonify(
        {"message": "Payment created with success!", "payment": new_payment.to_dict()}
    )


@app.route("/payments/pix/qr_code/<file_name>", methods=["GET"])
def get_image(file_name):
    return send_file(f"static/img/{file_name}.png", mimetype="image/png")


@app.route("/payments/pix/confirmation", methods=["POST"])
def confirm_payment_pix():
    return jsonify({"message": "Payment confirmed with success!"})


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_pagamento(payment_id):
    return render_template("payment.html")


if __name__ == "__main__":
    # Create folder to save images if not exists
    path_img = "./static/img/"
    if not os.path.exists(path_img):
        os.makedirs(path_img)

    app.run(debug=True)
