i = 0
while i <= 5:
    i+=1 #contador
    print(f"imprimiendo el valor de i {i}")
print("\n================================")

i = 0
while i <= 5:
    i+=1 #contador
    if i == 1:
        continue #probando continue
    print(f"imprimiendo el valor de i {i}")
print("\n================================")

i = 0
while i <= 5:
    i+=1 #contador
    if i == 4:
        break #probando break
    print(f"imprimiendo el valor de i {i}")