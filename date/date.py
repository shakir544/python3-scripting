import datetime

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.day)
print(currentDate.month)
print(currentDate.year)


# default date format is YYYY-MM-DD
# %b - for Month in chars
# %B - for Month in all chars
# %y - for year in two number
# %a - day of the week
# %A - day of the week (full)
print(currentDate.strftime("%d-%b-%y"))
print(currentDate.strftime("%a - %A"))

# calculate number of days to your birthdate

birthdate = "1987-08-23"
print(datetime.datetime.strptime(birthdate,"%Y-%m-%d").date())