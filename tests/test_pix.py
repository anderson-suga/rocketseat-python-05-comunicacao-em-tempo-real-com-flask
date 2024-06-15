import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "payments"))
)

import pytest
from pix import Pix


def test_pix_create_payment():
    pix_instance = Pix()

    # create a payment
    payment_info = pix_instance.create_payment()

    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info

    qr_code_path = payment_info["qr_code_path"]

    folder_img = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "static/img")
    )
    assert os.path.isfile(f"{folder_img}/{qr_code_path}.png")
