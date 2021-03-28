import pandas as pd
df = pd.read_excel(r'C:\Users\chloe\Downloads\naughtyornice.xlsx')
mylist = df['strings'].tolist()
nice = 0
nicewords = []
for x in range(len(mylist)):
	a = mylist[x]
	flag1 = False
	flag2 = False
	flag3 = True
	vowels = a.count("a") + a.count("e") + a.count("i") + a.count("o") + a.count("u")
	if vowels >= 3:
		flag1 = True
	if ("aa" in a) or ("bb" in a) or ("cc" in a) or ("dd" in a) or ("ee" in a) or ("ff" in a) or ("gg" in a) or ("hh" in a) or ("ii" in a) or ("jj" in a) or ("kk" in a) or ("ll" in a) or ("mm" in a) or ("nn" in a) or ("oo" in a) or ("pp" in a) or ("qq" in a) or ("rr" in a)or ("ss" in a)or ("tt" in a)or ("uu" in a)or ("vv" in a)or ("ww" in a)or ("xx" in a)or ("yy" in a)or ("zz" in a):
		flag2 = True
	if ("ab" in a) or ("cd" in a) or ("pq" in a) or ("xy" in a):
		flag3 = False
	if (flag1 == True) and (flag2 == True) and (flag3 == True):
		nicewords.append(a)
		nice = nice+1
print(nice)
print(nicewords)