list = [3,6,8,10,11,15,17,18,19,20]
comparison = 0

for i in list:
    comparison += 1
    if i == 12:
        print(comparison)
        break
    
print(comparison)