from datetime import datetime

year = 2015
month = 6
day = 16

date = datetime(year, month, day)
week_number = date.isocalendar()[1]

print("Week number:", week_number)
                                            
