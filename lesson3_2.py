lst = []
print(lst)
if lst == []:
    print(lst)
else:
    x = lst.pop()
    lst.insert(0,x)
    print(lst)
