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

the_bill = Bill(amount=120, period="April 2021")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary",days_in_house=25)

print("Mary pays:",mary.pays(bill=the_bill, flatmate2=john))
print("John pays:", john.pays(bill=the_bill,flatmate2=mary))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(john, mary, the_bill)