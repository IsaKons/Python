#n^2 Сравнивает пары и менят местами и так по кругу
def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item-z):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist


oldlist = [10, 75, 43, 15, 25, -4, 27]
print("Old List: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("New List: ", newlist)