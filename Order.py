class Order:
    def __init__(self, no, customer_id, product_dict, time, total_price=0, payment_status=0):
        self.order_no = no
        self.item = product_dict  # {Product: (qty, unit)}
        self.customer_id = customer_id
        self.time = time
        self.total_price = total_price
        self.payment_status = payment_status

    def get_order_no(self):
        return self.order_no

    def get_item(self, product=None):
        return self.item if product is None else self.item[product]

    def get_customer_id(self):
        return self.customer_id

    def get_time(self):
        return self.time

    def get_total_price(self):
        return self.total_price

    def get_payment_status(self):
        return self.payment_status

    def calculate_total_price(self):
        self.total_price = 0
        for p in self.item:
            self.total_price += p.price * p.unit
        return self.total_price

    def change_payment_status(self, status):
        self.payment_status = status

    def pay_bill(self):
        pass

    def __len__(self):
        return len(self.item)

    def __iter__(self):
        return iter(self.item)

    def __delitem__(self, key):
        del self.item[key]

    def __setitem__(self, key, value):
        self.item[key] = value

    def __str__(self):
        return '{},{},{},{},{},{}'.format(self.order_no, self.item, self.customer_id, self.time, self.total_price, self.payment_status)