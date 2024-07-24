class Stationary:
    def __init__(self, prod_id, prodname, category, brand, supp_year, stock):
        self.prod_id = prod_id
        self.prodname = prodname
        self.category = category
        self.brand = brand
        self.supp_year = supp_year
        self.stock = stock

    def get_prod_id(self):
        return self.prod_id

    def set_prod_id(self, prod_id):
        self.prod_id = prod_id

    def get_prodname(self):
        return self.prodname

    def set_prodname(self, prodname):
        self.prodname = prodname

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_supp_year(self):
        return self.supp_year

    def set_supp_year(self, supp_year):
        self.supp_year = supp_year

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock


class RestockDetail:
    def __init__(self, prod_id, quantity):
        self.prod_id = prod_id
        self.quantity = quantity


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)