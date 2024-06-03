theA = ["Bougainvillea", "Orchids", "Hibiscus", "Frangipani", "Honeysuckle"]

theA1 = []
theA2 = []

for w in theA:
    if w[0] == "H":
        theA1.append(w)
    else:
        theA2.append(w)


theA3 = sorted(theA1) + sorted(theA2)
print(theA3)
