lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
lst1 = []
zero_count = 0
for x in lst:
    if x == 0:
        zero_count += 1
    else:
        lst1.append(x)
for x in range (zero_count):
    lst1.append(0)
print(lst1)



