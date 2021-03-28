gp = float(input("input gross profit"))
np = float(input("input net profit"))
s = int(input("sales"))
gpm,npm = (gp/s)*100, (np/s)*100
print("Gross Profit Margin:",gpm,"%")
print("Net Profit Margin:",npm,"%")