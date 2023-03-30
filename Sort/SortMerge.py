# Делит на кучу массивов затем собирая назад передвигает наименьшее в начало
# принты для наглядности процесса
def merge_sort(lst):
    print(1)
    print(lst)
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left_list = lst[:middle]
    print(2)
    print(left_list)
    right_list = lst[middle:]
    print(3)
    print(right_list)
    
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    print(4)
    print(left_list)
    print(5)
    print(right_list)

    return list(merge(left_list, right_list))


def merge(left_half, right_half):
    print(6)
    print(left_half)
    print(7)
    print(right_half)
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res += right_half
    else:
        res += left_half
    print(8)
    print(res)
    return res


lst = [12, 34, 25, 15, 67, 23, 11, 5, 86]
print("Исходный массив: ", lst)
result = merge_sort(lst)
print("Результат сортировки: ", result)


      
