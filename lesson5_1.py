import string
import keyword
lst = input("Введіть рядок:")
answer = True
x = lst[0]
lst1 = (string.punctuation)
lst3 = (keyword.kwlist)
char = "__"
count = lst.count(char)
lst2 = lst1.replace(char, "")
if  (x.isalpha() and x.islower()) and x not in lst2 and x not in lst3 and char != "__":
    answer = True
else:
    answer = False
count = lst1.count(char)
print(answer)