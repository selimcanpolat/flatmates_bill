from flat import Bill, Flatmate
from reports import PdfReport

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