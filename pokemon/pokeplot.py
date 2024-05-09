import matplotlib.pyplot as plt

with open('pokemon.csv', 'r') as text:
    text = text.read()
    text = text[:len(text)-1]

def makeTypeList(data):
    data = data.split('\n')
    typeslist = []
    for i in range(len(data)):
        data[i] = data[i].split(',')
        typeslist.append(data[i][2])
        typeslist.append(data[i][3])
    return(typeslist)

typesdata = makeTypeList(text)
types = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Fairy', 'Dragon', 'Steel']

def typecounter():
    data = []
    for i in range(len(types)):
        x = typesdata.count(types[i])
        data.append(x)
    return data

quantype = typecounter()
plt.bar(types, quantype, color = ['red', 'blue', 'green'])
plt.xlabel("Type")
plt.ylabel("Number of Pokemon")
plt.title("Pokemon Types")
plt.show()