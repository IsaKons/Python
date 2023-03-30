import re

name = " ..My big string.."
print(name.title())
print(name.upper())
print(name.lower())

print("Privet stroka nomer1\nPrivet stroka N2\n\nStroka N3")
print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND")
print("Lower name: " + name.lower())

print(name.rstrip())
print(name.lstrip())
print(name.strip())        # Udalenie probelov
print(name.strip("."))     # Udalenie to4ek

mylist = []
msg =""
while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)
print(mylist)

mytext = "Vasya aaaaaaaa 1972,  Kolya - 19727777: Olesya 1981, aaaaaa@intel.com," \
         "bbbbbbbbbb@intel.com, Petya ggggggggg, 1992,cccccccccc@yahoo.com,  " \
         "ddddddddddd@intel.com, vasya@yandex.net, hello hello, Misha #43 1984, " \
         "Vladimir 1977, Irina , 2001,  annnnnnn@intel.com, eeeeeeee@yandex.com," \
         "ooooooooooo@hotmai.gov, gggggggggggg@gov.gov, tututut@giv.hot"

"""
\d   = Any Digit 0-9
\D   = Any non DIGIT
\w   = Any Alphabet symbol  [A-Z a-z]
\W   = Any non Alphabet symbol
\s   = breakspace
\S   = non breakspace
[0-9]{3}
[A-Z][a-z]+
"""

textlookfor = r"@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)