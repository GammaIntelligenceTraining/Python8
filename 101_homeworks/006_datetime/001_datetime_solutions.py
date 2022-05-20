"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object
import datetime

sample1 = 'Jan 1 2014 2:43PM'
print(datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p'))
sample2 = '14:20 10/12/22'  # YY/MM/DD
print(datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d'))
sample3 = 'Tuesday, September 24, 2019'
print(datetime.datetime.strptime(sample3, '%A, %B %d, %Y'))
sample4 = '01.01.1970 - 00:00:01'
print(datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S'))



# Write a program to print yesterdays, today and tomorrow dates
difference = datetime.timedelta(days=1)
print('Yesterday', datetime.date.today() - difference)
print('Yesterday', datetime.date.today())
print('Yesterday', datetime.date.today() + difference)

# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
print(datetime.datetime.strftime(datetime.datetime.fromtimestamp(some_day), '%d.%m.%Y'))


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)
def two_weeks_ago(timestamp):
    difference = datetime.timedelta(weeks=2)
    result = datetime.datetime.timestamp(datetime.datetime.fromtimestamp(timestamp) - difference)
    return result

print(two_weeks_ago(1014163200))