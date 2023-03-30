#FOR####
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

for x in range(100, 10, -2):
    print("Number x = " + str(x))

for x in range(1, 6):
    print(x)

#WHILE####
while True:
    print(x)
    x = x + 1
    if x == 100:
        break
import sys

filename = "/Users/isakonst/Learn1/Python/justfile.txt"
while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding="Latin-1")
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1])  #mmodule sys for that
        filename = input("ENter Correct file name! :")
    else:
        print("Indise ELSE")
        print(myfile.read())
        break


#IF####
def bool_to_word(bool):
    return "Yes" if bool else "No"

age = 14
if (age <= 4):
    print("You are baby!")
elif (age > 4) and (age < 12):
    print("You age kid")
else:
    print("You are old!")

