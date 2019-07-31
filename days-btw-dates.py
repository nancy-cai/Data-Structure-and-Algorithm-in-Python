def daysInMonth(y,m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    else:
        if m == 2:
            if isLeapYear(y):
                return 29
            else: 
                return 28
    return 30

def nextDay(y,m,d):
    if d < daysInMonth(y,m):
        return y,m,d+1
    else:
        if m < 12:
            return y,m+1,1
        else:
            return y+1,1,1

def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    
def dateIsBefore(y1,m1,d1,y2,m2,d2):
    if y1 > y2:
        return False
    elif y1 == y2:
        if m1 > m2:
            return False
        elif m1 == m2:
            return d1 < d2
    return True
          
def daysBetweenDates(y1,m1,d1,y2,m2,d2):
    days = 0
    assert not dateIsBefore(y2,m2,d2,y1,m1,d1)
    # keepd adding the number of days while date1 is before date2
    while dateIsBefore(y1,m1,d1,y2,m2,d2):
        y1,m1,d1 = nextDay(y1,m1,d1)
        days +=1
    return days
          
print daysBetweenDates(2008,2,28,2008,3,1)
print daysBetweenDates(2011,2,22,2019,2,20)
print daysBetweenDates(2019,2,22,2009,2,20)