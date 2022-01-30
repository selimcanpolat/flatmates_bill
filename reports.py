import webbrowser

from fpdf import FPDF


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