from abc import ABC , abstractmethod
from dataclasses import dataclass

class Order:
    customer_name : str
    total_price: float
    status: str = "open"\
    
# Abstraksi (kontak untuk OCP/DIP)
class IPaymentProcessor(ABC):
    """kontrak: semua prosesor pembayaran harus punya method 'proses'"""
    @abstractmethod
    def process(self, order: Order,) -> bool:
        pass

class INotificationService(ABC):
    """Kontrrak: semua layanan notifikasi harus puya method 'send'"""
    @abstractmethod
    def send(self,order:Order):
        pass

# IMPLEMENTASI KONKIRT (PLUG-IN)    
class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order)-> bool:
        print("payment: Memproses kartu kredit.")
        return True
    
class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Notif: Mengirim Email konfirmasi ke {order.customer_name}.")


# Kelas koordinator(SRP & DIP)
class checkoutservice:
    def __init__(self,payment_processort: IPaymentProcessor, notifier: INotificationService):
        self.payment_processor = payment_processort
        self.notifier = notifier

    def run_checkout(self, order: Order):
        payment_success = self.payment_processor.process(order)

        if payment_success:
            order.status = "paid"
            self.notifier.send(order)
            print("CHeckout Sukses.")
            return True
        return False
    
# Program Utama

andi_order = Order("Andi", 500000)
email_service = EmailNotifier()

# 1. Inject implementasi Credit Card
cc_processor = CreditCardProcessor()
checkout_cc = checkoutservice(payment_processort= cc_processor, notifier= email_service)
print("--- Skenario 1: Credit card ---")
checkout_cc.run_checkout(andi_order)

# 2 Pembuktian OCP: Menambah Metode Pembayaran QRIS (Tanpa Mengubah Checkoutservice )
class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order)-> bool:
        print("Payment : Memproses Qris.")
        return True

budi_order = Order("Budi", 100000)
qris_processor = QrisProcessor()

# Inject im0lementasi QRIS yang baru dibuat
checkout_qris = checkoutservice(payment_processort=qris_processor, notifier=email_service)
print("\n--- Skenario 2: Pembuktian OCP (QRIS) ---")
checkout_qris.run_checkout(budi_order)