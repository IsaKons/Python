import sys
from collections import Counter

cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']
NewCities = []

mynumber_list = list(range(0, 10))      # Creates array 0-10
visited = [[] for _ in range(10)]      # Empty array create
graph = {key: [] for key in range(10)}  # empty dickt create
new_list = [[None for _ in range(x+1)] for x in range(numRows)]  # Creade empty 2d matrix
l[x] = [0] * (i + 1)                    # Create llist inside list


sys.argv                                # array of args provided
print(len(cities))                      # lenght of array
cities[2] = 'Tula'                      # set with exchange
cities.append('Kursk')                  # add to the end
cities.insert(2, 'Feodosiya')           # insert in position without exchange
del cities[-1]                          # remove by ID
cities.remove('Tula')                   # remove by name
cities.reverse()                        # Reverse
cities[::-1]                            # also reverse and can be done with STR!!
cities[:] = cities[::-1]                # for cases when need to change inside function and also have change outside
print(cities[-4:-1])                    # From -4 includet to -1 not includet
cities.pop(1)                           # Delete and show deleted(can be saved in var)
NewCities.append(cities.copy())         # Create a COPY of array
x = Counter(cities)
y = Counter(NewCities)                  # Combines similar elements
z = x & y                               # общие элементы в словарях с наименьшим значением

#dictionary
enemy = {
          'loc_x':  70,
          'loc_y':  50,
          'color':  'green',
          'health': 100,
          'name': 'Zed',
}
#Create array of many copies of dictionary
all_enemies = []
for x in range(0, 10):
    all_enemies.append(enemy.copy())
# How to change values in separate dictionary
all_enemies[5]['health'] = 30
all_enemies[8]['name'] = "Kozel"
all_enemies[2]['loc_x'] += 10

# 2d arrays
# magic, rotate it for 180 and remowe first line
# zip - make from 123 456 = 14 25 36, *matrix send each x in matrix as argument, ::-1 slicer to get reverse
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = []
while matrix:
    result += matrix.pop(0)
    matrix = (list(zip(*matrix)))[::-1]
print(result)