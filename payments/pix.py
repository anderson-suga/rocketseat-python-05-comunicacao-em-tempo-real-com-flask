import uuid
import qrcode


class Pix:
    def __init__(self) -> None:
        pass

    def create_payment(self):
        bank_payment_id = str(uuid.uuid4())

        bash_payment = f"hash_payment_{bank_payment_id}"

        img = qrcode.make(bash_payment)

        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}",
        }
