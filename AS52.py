#e1b
import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2012)

#e1c
import calendar
cal = calendar.TextCalendar()
cal.setfirstweekday(calendar.THURSDAY)
month = int(input("Input Number of Birthday Month"))
year = int(input("Input Birthday Year"))
cal.prmonth(year,month)

#e1d
1) When they work, the months are translated into the new language
2) For certain languages (using pictorial symbols), the unicode comes out garbled and nonsensical

#e1e
Argument = Year
Result = Boolean (True or False: depending on if year input is a leap year or not)

#e2a
50 functions

#e2b
math.ceil = returns value rounded up
math.floor = returns value rounded down

#e2c
set value to power of 0.5 (**0.5)

#e3
deepcopy: creates new object, adds copies of nested object from original element

#e4
import mymodule1
import mymodule2

print((mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year))

#e5
import mymodule1
import mymodule2

print((mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year))
print("My name is",__name__)

#e6
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

#e7
s = "If we took the bones out, it wouldn't be crunchy, would it?"
print(s.split())
print(type(s.split()))
print(s.split("o"))
print(s.split("i"))
print("0".join(s.split("o")))

