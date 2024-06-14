from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/payments/pix", methods=["POST"])
def create_payment_pix():
    return jsonify({"message": "Payment created with success!"})


@app.route("/payments/pix/confirmation", methods=["POST"])
def confirm_payment_pix():
    return jsonify({"message": "Payment confirmed with success!"})


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_pagamento(payment_id):
    return "pagamento pix"


if __name__ == "__main__":
    app.run(debug=True)
