lst = [1,2,3,4,5,6,7,8,9,10]
size_list = len(lst)
div, mod = divmod(size_list, 2)
if size_list != 0 and mod != 0:
    div = div + 1
    lst1 = lst[:div]
    lst2 = lst[div:]
    print(lst1, lst2)
elif size_list != 0 and mod == 0:
    lst1 = lst[:div]
    lst2 = lst[div:]
    print(lst1, lst2)
else:
    lst1 = []
    lst2 = []
    print(lst1, lst2)

