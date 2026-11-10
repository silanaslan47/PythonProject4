vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

vuodenaika = vuodenajat[(kuukausi % 12) // 3]

print(vuodenaika)