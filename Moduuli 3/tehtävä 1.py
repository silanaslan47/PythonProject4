pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    print("Laske kuha takaisin järveen.")
    print("Kuhasta puuttuu", 37 - pituus, "cm sallitusta pyyntimitasta.")
else:
    print("Kuha on sallitun pyyntimitan mukainen.")