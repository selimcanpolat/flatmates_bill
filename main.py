class Bill:
    """
    Object that contains data about a bill, such as total amount
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        return bill.amount * (self.days_in_house / (flatmate2.days_in_house + self.days_in_house))


class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names,
    their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

the_bill = Bill(amount=120, period=30)
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary",days_in_house=25)

print("Mary pays:",mary.pays(bill=the_bill, flatmate2=john))
print("John pays:", john.pays(bill=the_bill,flatmate2=mary))
