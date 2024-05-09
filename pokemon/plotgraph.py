# import matplotlib.pyplot
import matplotlib.pyplot as plt
# g = [10, 14, 19, 40]
# plt.plot(g)
# plt.show()

#plt.show() - display the current plot in a new window
#plt.plot(data) Create a line graph - If data is a single list, the elements are considered y values, while the list indices will be x values. If you provide 2 lists the first will be x values and the second will be y values.
#plt.bar(xdata, ydata) - Create a bar graph
#plt.hist(data, bins) - Create a histogram based on the frequencies of the elements in data. It will create bins amount of bars.

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