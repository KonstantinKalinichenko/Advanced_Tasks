from collections import defaultdict


class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = int(quantity)

def generate_product_report(data):
    records = data.split(';')
    items = [Item(*record.split(':')) for record in records]
    full_report = defaultdict(lambda: defaultdict(int))
    for item in items:
        full_report[item.product][item.date] += item.quantity

    result = []
    for product, dates in full_report.items():
        product_report = f'{product}:'
        for date, quantity in dates.items():
            product_report += f' - {date}: {quantity}'
        result.append(product_report)
    return result


if __name__ == "__main__":
    input_data =  input()
    product_report_generator = generate_product_report(input_data)
    for report in product_report_generator:
        print(report)