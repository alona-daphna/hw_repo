import  random
from datetime import datetime
CURRENT_YEAR = datetime.now().year
CURRENT_MONTH = datetime.now().month
month = random.randint(1,12)
year = random.randint(1980,CURRENT_YEAR)

flag = False
if year == CURRENT_YEAR:
    if month < CURRENT_MONTH:
        hefresh_months = CURRENT_MONTH - month
        hefresh_years = 0
    elif month == CURRENT_MONTH:
        hefresh_months = 0
        hefresh_years = 0
    else:
        hefresh_months = month - CURRENT_MONTH
        hefresh_years = 0
        flag = True
elif month < CURRENT_MONTH:
    hefresh_months = CURRENT_MONTH - month
    hefresh_years = CURRENT_YEAR - year
elif month == CURRENT_MONTH:
    hefresh_months = 0
    hefresh_years = CURRENT_YEAR - year
else:
    hefresh_months = 12 + CURRENT_MONTH - month
    hefresh_years = CURRENT_YEAR - year - 1

print('Rand Year: {0}\nRand Month: {1}'.format(year, month))
if flag:
    if hefresh_months == 1:
        print("The Rand date will be {0} month from now".format(hefresh_months))
    else:
        print("The Rand date will be {0} months from now".format(hefresh_months))
else:
    print(str(hefresh_months)+'/'+str(hefresh_years))
