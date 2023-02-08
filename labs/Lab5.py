import datetime

print("What is your birthday?")
Year = input("Year: ")
Month = input("Month (1-12): ")
Day = input("Date: ")


birthday = datetime.datetime(int(Year), int(Month), int(Day))
tday = datetime.datetime.today()
timedelta = (tday - birthday).total_seconds()
print("You are", timedelta, "seconds old" )
