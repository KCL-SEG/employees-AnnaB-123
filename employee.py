"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, bonus, com_rate , num_contracts):
        self.name = name
        self.num_contracts = num_contracts

        if bonus != None:
            self.bonus = bonus
        else:
            self.bonus = None

        if com_rate != None:
            self.com_rate = com_rate
        else:
            self.com_rate = None

    def getCommission(self):
        total = 0
        if (self.bonus != None):
            # recieves a fixed bonus
            total += self.bonus
        elif (self.com_rate != None):
            # recieves commission
            total += self.com_rate * self.num_contracts

        return total

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Salary(Employee):
    def __init__(self, name, bonus, com_rate , num_contracts, monthly):
        super().__init__(name, bonus, com_rate , num_contracts)
        self.monthly = monthly

    def __str__(self):
        if (self.bonus != None):
            # recieves a fixed bonus
            return(f"{self.name} works on a monthly salary of {self.monthly} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}.")
        elif (self.com_rate != None):
            # recieves commission
            return(f"{self.name} works on a monthly salary of {self.monthly} and receives a commission for {self.num_contracts} contract(s) at {self.com_rate}/contract. Their total pay is {self.get_pay()}.")
        else:
            # no bonus or commission
            return(f"{self.name} works on a monthly salary of {self.monthly}. Their total pay is {self.get_pay()}.")

    def get_pay(self):
        return self.monthly + super().getCommission()


class Hourly(Employee):
    def __init__(self, name, bonus, com_rate , num_contracts, rate, hours):
        super().__init__(name, bonus, com_rate , num_contracts)
        self.rate = rate
        self.hours = hours

    def __str__(self):
        if (self.bonus != None):
            # recieves a fixed bonus
            return(f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}.")
        elif (self.com_rate != None):
            # recieves commission
            return(f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.num_contracts} contract(s) at {self.com_rate}/contract. Their total pay is {self.get_pay()}.")
        else:
            # no bonus or comission
            return(f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {self.get_pay()}.")

    def get_pay(self):
        return (self.rate * self.hours) + super().getCommission()

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary('Billie', None, None, 0, 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly('Charlie', None, None, 0, 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary('Renee', None, 200, 4, 3000)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly('Jan', None, 220, 3, 25, 150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary('Robbie', 1500, None, 0, 2000)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly('Ariel', 600, None, 0, 30, 120)

# print(billie.__str__())
# print(billie.get_pay())
# print(billie.monthly)
