import datetime
a = input("input date 1 (day/month/year, ex 03 04 2004)")
a = a.split()
a = list(map(int, a))
fdate = datetime.date(a[2],a[1],a[0])
b = input("input date 2")
b = b.split()
b = list(map(int, b))
ldate = datetime.date(b[2],b[1],b[0])
temp = ldate - fdate
print(temp.days)