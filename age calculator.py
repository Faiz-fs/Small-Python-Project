from  datetime import date as d
sdat=int(input('enter the starting date'))
smonth=int(input('enter the starting month'))
syear=int(input('enter the starting year'))
d1=d(year=syear,month=smonth,day=sdat)
d2=d.today()
age=(d2-d1)//365
print('age=',age)