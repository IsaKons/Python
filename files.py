import json

inputfile = "/Users/isakonst/Learn1/Python/justfile2.txt"
outputfile = "/Users/isakonst/Learn1/Python/justfile.txt"

password_tolookfor = "password"

myfile1 = open(inputfile, mode='r', encoding='latin_1')  # r - read, w- write, a - append, r+
myfile2 = open(outputfile, mode='a', encoding='latin_1')

for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile2.write("Found password:" + line)

myfile1.close()
myfile2.close()

######

filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'awards': ["WT", "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ------------ SAVE by JSON -----------

json.dump(myplayers, myfile)
myfile.close()


# -------- LAOD by JSON --------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name  is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award N1: " + str(user['awards'][0]))
    print("Player Award N2: " + str(user['awards'][1]))
    print("Player Award N3: " + str(user['awards'][2]))
    print("----------------------------------\n\n")