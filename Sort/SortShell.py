# Улучшенный Insertion
def shell_sort(lst):
    gap = len(lst) // 2

    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value
            print("######")
            print(current_value)
            print(position)
            print(gap)
            print("######")

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value
                print("******")
                print(current_value)
                print(position)
                print(gap)
                print("******")

        gap //= 2
    return lst


lst = [22, 34, 25, 15, 67, 23, 11, 86]
print("Исходный массив: ", lst)
result = shell_sort(lst)
print("Результат сортировки: ", result)