#Jamie Hilton
#30/09/2014
#Date Converter

date= input("Please enter the date in the form; ##/##/##(I.E 02/12/98): ")

day_number= date[0:3]

month_number = date[3:5]

if month_number == "01":
    month = "January"

elif month_number == "02":
    month = "Febuary"

elif month_number == "03":
    month = "March"

elif month_number == "04":
    month = "April"

elif month_number == "05":
    month = "May"

elif month_number == "06":
    month = "June"

elif month_number == "07":
    month = "July"

elif month_number == "08":
    month = "August"

elif month_number == "09":
    month = "September"

elif month_number == "10":
    month = "October"

elif month_number == "11":
    month = "November"

elif month_number == "12":
    month = "December"
else:
    print("That is an invalid Number-Please try again")

year_number = date[6:]

if year_number > 29 and year_number < 99:
    year = "19{0}".format(year_number)
elif year number < 30:
    year = "20{0}".format(year_number)

print("The date you entered is the {0}th {1} {
