#Jamie Hilton
#30/09/2014
#Date Converter

date= input("Please enter the date in the form; ##/##/##(I.E 02/02/98): ")

day = date[0:2]

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
    month = "Septmeber"

elif month_number == "10":
    month = "October"

elif month_number == "11":
    month = "November"

elif month_number == "12":
    month = "December"

else:
    print("That is an invaild number")

year_number = int(date[6:])

if year_number < 30:
    year = year_number + 2000

else:
    year = year_number + 1900

print("The date you entered is the {0}th {1} {2}".format(day, month, year))
