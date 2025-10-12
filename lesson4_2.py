lst = [1,2,3,4,5,6,7,8,12,34,100]
sum_elements = 0
for x in lst:
    ind = lst.index(x)
    if ind % 2 == 0:
         sum_elements += x
print("сума елементів з парими індексами:",sum_elements)
last_element = lst[-1]
result = sum_elements * last_element
print("Рузультат:",result)