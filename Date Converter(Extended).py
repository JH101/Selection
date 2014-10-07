#Jamie Hilton
#30/09/2014
#Date Converter

date= input("Please enter the date in the form; ##/##/##(I.E 02/02/98): ")

day_number = date[0:2]

if day_number == "01":
    day = "1st"

if int(day_number) % 10 == 1 and int(day_number) != 11:
    day = "{0}st".format(day_number)

elif day_number == "02":
    day = "2nd"

if int(day_number) % 10 == 2 and int(day_number) != 12:
    day = "{0}nd".format(day_number)

elif int(day_number)> 31:
    print("That is an invalid date, try again")

else:
    day = "{0}th".format(day_number)

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
    print("That is an invaild Month, please try again")

year_number = int(date[6:])

if year_number < 30:
    year = year_number + 2000

else:
    year = year_number + 1900

if year % 4 == 0:
    print("The date you entered is the {0} {1} {2} Which is also a leap year".format(day, month, year))
    
else:
    print("The date you entered is the {0} {1} {2}".format(day, month, year))
