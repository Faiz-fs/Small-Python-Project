from  datetime import date as d
sdat=int(input('enter the starting date'))
smonth=int(input('enter the starting month'))
syear=int(input('enter the starting year'))
d1=d(year=syear,month=smonth,day=sdat)
edat=int(input('enter the ending date'))
emonth=int(input('enter the ending month'))
eyear=int(input('enter the ending year'))
d2=d(year=eyear,month=emonth,day=edat)
print(d2-d1)
