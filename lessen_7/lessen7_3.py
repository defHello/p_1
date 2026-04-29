palidrom = ['level', 'car', 'auto', 'Radar']

for palidrom_new in palidrom:
    if palidrom_new.lower() == palidrom_new.lower()[::-1]:
        print(palidrom_new)

palidromes = list(filter(lambda x: x.lower() == x.lower()[::-1], palidrom))
print(palidromes)