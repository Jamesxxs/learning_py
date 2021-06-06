print('')
print('[16.1 Time]','-'*70)
class Time:
    """Represents the time of day

    attributes: hour, minute, second"""

time1 = Time()
time1.hour = 1
time1.minute = 59
time1.second = 30

def print_time(time):
    print('%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second))

print_time(time1)

def is_after(time1,time2):
    return (time1.hour,time1.minute,time1.second) > (time2.hour,time2.minute,time2.second)

time2 = Time()
time2.hour = 4
time2.minute = 20
time2.second = 30

print(is_after(time1,time2))


print('')
print('[16.2 Pure function]','-'*70)

print('')
print('[16.3 Modifiers]','-'*70)
def increment(start,duration):
    end = Time()
    end.hour = start.hour + duration.hour
    end.mintue = start.minute + duration.minute
    end.second = start.second + duration.second

    ex_minute, second = divmod(end.second, 60)
    end.minute = start.minute + ex_minute
    end.second = second
    ex_hour, minute = divmod(end.minute, 60)
    end.minute = minute
    end.hour = end.hour + ex_hour
    return end

t1 = Time()
t1.hour = 1
t1.minute = 59
t1.second = 30

t2 = Time()
t2.hour = 0
t2.minute = 0
t2.second = 700

print('start:')
print_time(t1)
print('duration:')
print_time(t2)
print('end:')
print_time(increment(t1,t2))



print('')
print('[16.4 Prototyping VS planning]','-'*70)

def time_to_int(t):
    second = t.second + t.minute*60 + t.hour*3600
    return second

def int_to_time(i):
    time = Time()
    time.hour,reminder = divmod(i,3600)
    time.minute,time.second = divmod(reminder,60)
    return time

def add_time(t1,t2):
    second = time_to_int(t1) + time_to_int(t2)
    return int_to_time(second)

print_time(add_time(t1,t2))
s1 = time_to_int(t1)
s2 = time_to_int(t2)
print(s1,s2)


print('')
print('[16.5 Debugging]','-'*70)
def valid_time(t):
    if t.hour<0 or t.minute<0 or t.second<0:
        return False
    if t.minute>=60 or t.second>=60:
        return False
    return True



print('')
print('[16.7 Exercise]','-'*70)

print('[Ex16.1]','-'*70)
def mul_time(t,num):
    assert valid_time(t)
    second = time_to_int(t) * num
    return int_to_time(second)


print('')
print('[Ex16.1]','-'*70)

from datetime import datetime

birthday = Time()
birthday.month = 11
birthday.day = 26

def birthday(birthday):
    today = datetime.today()
    next_birthday = datetime(today.year,birthday.month,birthday.day)
    if today > next_birthday:
        next_birthday = datetime(today.year+1,birthday.month,birthday.day)
    d = next_birthday-today

    print('you are %.2d years old' %(today.year-birthday.year))
    print('your next birthday is ',d.days,'days later')
    
my_birthday = datetime(1999,11,26)
birthday(my_birthday)

print(datetime.today())