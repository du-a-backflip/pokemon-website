from tkinter import Tk, simpledialog, messagebox

the_world = {}

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            line1 = line.split()
            country = line1[0]
            city = line1[1]
            the_world[country] = city

def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '   ' + city_name)
    file.close

print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()

read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country:')
    query_country = query_country[0].upper() + query_country[1:len(query_country)].lower()
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer ' ,
                            'The captial city of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach me',
                                          'I don\'t know!' +
                                          'What is the capital city of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop
