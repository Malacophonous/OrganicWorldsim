#TODO: Still need to test negative inputs
#for various arguments in the add/sub methods

class Time():
    def __init__(self, _minute, _day, _year):
        self.minute = _minute
        self.day = _day
        self.year = _year

    @classmethod
    def fromInt(self,arg):
        #converts integer argument into a date/time object
        if isinstance(arg, int):
            if arg>=1440:
                a = arg%1440
                b = int(arg/1440)
                if b >=365:
                    b = b%365
                    c = int(b/365)
                else:
                    c = 0
            else:
                a = arg
                b = 0
                c = 0
            return Time(a,b,c)

    def __add__(self,amount):
        if isinstance(amount,Time):
            a = amount.minute
            b = amount.day
            c = amount.year
        elif isinstance(amount,int) and amount>=0:
            t = Time.fromInt(amount)
            a = t.minute
            b = t.day
            c = t.year
        else:
            raise TypeError
        d = self.minute+a
        e = self.day+b
        f = self.year+c
        if d>=1440:
            d = d%1440
            e = e + int(d/1440)
        if e>=365:
            e = e%365
            f = f + int(e/365)
        return Time(d,e,f)

    def __sub__(self, amount):
        if isinstance(amount,Time):
            a = amount.minute
            b = amount.day
            c = amount.year
        elif isinstance(amount,int) and amount>=0:
            t = Time.fromInt(amount)
            a = t.minute
            b = t.day
            c = t.year
        else:
            raise TypeError
        d = self.minute - a
        e = self.day - b
        f = self.year - c
        if d<=0:
            e = e - 1
            d=1440+d
        if e<=0:
            f = f-1
            e = 365+e
        return Time(d,e,f)

    def toString(self):
        temp = 'minute: ' + str(self.minute) + ', day: '+ str(self.day) + ', year: ' + str(self.year)
        return temp