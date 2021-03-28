formulas = ["1) Find force: F = ma",
            "2) Find power: P = IV",
            "3) Find density: D = m/v"]
choice = int(input("input number of the formula you would like to use"))
if choice == 1:
    m = int(input("input mass (m)"))
    a = int(input("input acceleration (a)"))
    print("the force is:",m*a,"N")
elif choice == 2:
    i = int(input("input current (I)"))
    v = int(input("input voltage (V)"))
    print("the power is:",i*v,"W")
elif choice == 3:
    m = int(input("input mass (m)"))
    v = int(input("input volume (v)"))
    print("the density is:",m/v,"g/cm^2")
else:
    print("Sorry! We're working on adding more formulas :)")