print('')
print('[17.1 Object_oriented features]','-'*70)

print('')
print('[17.2 Printing objects]','-'*70)

def int_to_time(i):
    time = Time()
    time.hour,reminder = divmod(i,3600)
    time.minute,time.second = divmod(reminder,60)
    return time

class Time:
    """attribute: hour, minute, second"""

    def __init__(self,hour=0,mintue=0,second=0):
        self.hour = hour
        self.minute = mintue
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other,Time):
            seconds = self.time_to_int() + other.time_to_int()
            return int_to_time(seconds)
        if isinstance(other,int):
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)


    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))

    def time_to_int(self):
        second = self.hour*3600 + self.minute*60 + self.second
        return second

    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self,other):
        return self.time_to_int() > other.time_to_int()

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

start.print_time()

print('')
print('[17.3 Another example]','-'*70)

start.increment(10000).print_time()


print('')
print('[17.4 A more complicated example]','-'*70)

end = Time()
end.hour = 13
end.minute = 22
end.second = 0

print(end.is_after(start))

print('')
print('[17.5 The init method]','-'*70)
now = Time(16,21)
now.print_time()

print('')
print('[17.6 The __str__ method]','-'*70)
now = Time(16,21)
print(now)

print('')
print('[17.7 Operator overloading]','-'*70)
duration = Time(1,30)
print(start+duration)

print('')
print('[17.8 Type_based dispatch]','-'*70)
print(2000+now)

print('')
print('[17.9 Polymorphism]','-'*70)
total = sum([start,duration,now,end])
print(total)

print('')
print('[17.10 Debugging]','-'*70)
print(hasattr(now,'hour'))
print(vars(now),'\nType is:',type(vars(now)))
def print_attrs(obj):
    for attr in vars(obj):
        print(attr,getattr(obj,attr))

print_attrs(now)

print('')
print('[17.11 Interface and implementation ]','-'*70)

print('')
print('[17.13 Exercise ]','-'*70)
print('[Ex17.1 ]','-'*70)
class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        self.seconds_from_mid = hour*3600 + minute*60 + second############Changed###########

    def __str__(self):
        """Returns a string representation of the time."""
        hour, ex_second= divmod(self.seconds_from_mid,3600)############Changed###########
        minute,second = divmod(ex_second,60)############Changed###########
        return '%.2d:%.2d:%.2d' % (hour, minute, second)############Changed###########

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.seconds_from_mid############Changed###########

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        return self.seconds_from_mid >= 0 and self.seconds_from_mid < 24*60*60 ############Changed###########

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    # end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()

print('')
print('[Ex17.1 ]','-'*70)
class Kangaroo:
    def __init__(self,name,contents=[]):
        self.name = name
        self.pouch_contents = contents

    def put_in_pouch(self,obj):
        self.pouch_contents.append(obj)
        return self.pouch_contents

    def __str__(self):
        t = [' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)


kanga = Kangaroo('kanga')
roo = Kangaroo('roo')
kanga.put_in_pouch(roo)
print(kanga)


