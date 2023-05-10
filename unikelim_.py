list = [1, 2, 3, 4, 2, 5, 6, 7, 8, 5, 3, 4, 7]
def unique_list(lst):
    lst.sort()
    unique = []
    for i in lst:
        if lst.count(i) == 1:
            unique.append(i)
    return unique
print(unique_list(list))
