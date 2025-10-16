import string
lst1 = (string.punctuation)
lst = input("Введіть рядок:")
lst = lst.title()
for x in lst:
    lst2 = "".join(x for x in lst if x not in string.punctuation)
for x in lst2:
    lst3 = lst2.replace(" ", "")
print(lst3[:140])
