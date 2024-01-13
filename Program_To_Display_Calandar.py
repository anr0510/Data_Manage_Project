import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)

# To get the calendar we have to import calendar module from python
# It is an inbuilt module of python