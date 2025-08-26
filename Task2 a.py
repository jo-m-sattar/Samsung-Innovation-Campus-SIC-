a = int(input("1st num "))
b = int(input("2nd num "))
for i in range(a,b):
    if i % 5 == 0 and i % 7 ==0:
        print(i)
    else:
        continue
