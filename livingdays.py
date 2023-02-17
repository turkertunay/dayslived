import datetime
from datetime import date

day = input("enter the day you were born: " )
month = input("enter the month you were born: ")
year = input("enter the year you were born: ")


t_bd = datetime.date(int(year), int(month), int(day))
print(t_bd)
today = date.today()
print("Today's date:", today)
days_lived = today - t_bd
print("you are on this world for", days_lived, "days")