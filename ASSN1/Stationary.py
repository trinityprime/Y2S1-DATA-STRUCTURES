class Stationary:
    def __init__(self, prod_id, prodname, category, brand, supp_year):
        self.prod_id = prod_id
        self.prodname = prodname
        self.category = category
        self.brand = brand
        self.supp_year = supp_year

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