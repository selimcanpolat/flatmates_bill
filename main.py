import webbrowser
from fpdf import FPDF


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

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Helvetica", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label & value
        pdf.set_font(family="Helvetica", size=16, style="B")
        pdf.cell(w=0, h=20, txt="Period", border=0, align="C", ln=1)
        pdf.cell(w=0, h=20, txt=bill.period, border=0, align="C", ln=1)

        # Insert name and the due amount of the first flatmate
        pdf.set_font(family="Helvetica", size=16, style="B")
        pdf.cell(w=0, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=0, h=20, txt=flatmate1_pay, border=0, align="C",ln=1)

        # Insert name and the due amount of the second flatmate
        pdf.set_font(family="Helvetica", size=16, style="B")
        pdf.cell(w=0, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=0, h=20, txt=flatmate2_pay, border=0, align="C")

        pdf.output(self.filename)

        webbrowser.open(self.filename) # Automatically open the PDF

amount = float(input("Hey user, enter the bill amount: "))
period = input("Please enter the period, eg. Mar 2021: ")

name_1 = input("Please enter the name of the first flatmate: ")
days_1 = int(input(f"How many days did {name_1} stay in the house? "))

name_2 = input("Please enter the name of the second flatmate: ")
days_2 = int(input(f"How many days did {name_2} stay in the house? "))


the_bill = Bill(amount=amount, period=period)
first_flatmate = Flatmate(name=name_1, days_in_house=days_1)
second_flatmate = Flatmate(name=name_2, days_in_house=days_2)

print(f"{first_flatmate.name} pays:", second_flatmate.pays(the_bill, flatmate2=first_flatmate))
print(f"{second_flatmate.name} pays:",first_flatmate.pays(the_bill, flatmate2=second_flatmate))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(first_flatmate, second_flatmate, the_bill)