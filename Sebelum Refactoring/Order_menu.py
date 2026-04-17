class Order:
    customer_name : str
    total_price: float
    status: str = "open"\

# kode sebelum refactoring
class OrderManager: # melanggar SRP, OCP, dan DIP
    def process_checkout(self, order: Order, payment_method: str):
        print(f"Memulai checkout untuk {order.customer_name}. . .")
        
        # Logika permbayaran yang melanggar OCP/DIP
        if payment_method == "credit_card":
            print("Processing credit card...")

        elif payment_method == "bank_transfer":
            print("Processing transfer bank...")
            
        else:
            print("Metode tidak valid")
            return False
        
        # logika Modifikasi (pelanggaran SRP)
        print(f"mengirim notifiksi ke {order.customer_name}...")
        order.status = "paid"
        return True