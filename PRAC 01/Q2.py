from Q1 import CreditCard
# NOTE BALANCE = AMT OWED TO THE BANK!


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit):
        super().__init__(customer, bank, acnt, limit)
        self._charge_calls = 0
        self._apr = 0.0825  # annual percentage rate (APR) for interest

    def charge(self, price):
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self._balance += price
            self._charge_calls += 1
            if self._charge_calls > 10:
                surcharge = self._charge_calls - 10
                self._balance += surcharge
            return True

    def process_month(self):
        if self._balance > 0:
            monthly_rate = pow(1 + self._apr, 1/12)
            monthly_interest = self._balance * (monthly_rate - 1)
            self._balance += monthly_interest
            self._charge_calls = 0
