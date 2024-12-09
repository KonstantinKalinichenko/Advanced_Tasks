class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = int(quantity)

def generate_product_report(data):
    """Ваш код"""



input_data =  input()
product_report_generator = generate_product_report(input_data)
for report in product_report_generator:
    print(report)