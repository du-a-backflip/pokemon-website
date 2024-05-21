#! /usr/bin/python3
print("Content-Type: text/html\n\n")

import matplotlib.pyplot as plt

templatePage = '''
<!DOCTYPE html>
<html>
    <head>
        <!-- the stylesheet for the html -->
        <link href="stylesheet.css" rel="stylesheet">
        <!-- The title for the tables -->
        <title>Data Table Page</title>
    </head>
    <body>
        <!-- Heading -->
            <h1> _HEADING_ </h1>
        <!-- Where the navbar is replaced on all the files -->
        _NAVBAR_
        <!-- Where the files get there own unique bodies -->
        _IMG_
        <!-- Where we put the statistical calculations -->
         _STATS_
    </body>
</html>
'''


templatePage = templatePage[1:len(templatePage)-1]
Home_Desc = '''Hello! We analyzed global data about economic trends in countries across the globe. We hope this will prove to be an insightful lesson on overall global economic trends.</br>
We analyzed the GDPs, the gross domestic product, of different countries for our project. It shows the overall value of the goods and services from a country, and a higher GDP correlates to </br>
a healthier economy, in turn providing a higher standard of living.'''

navbar = '''<ul class = "navbar">
            <li><a href="http://marge.stuy.edu/~dbaig50/countryGDP/GDPWebsite.py">Home</a></li>
            <li><a href="Danny.html">Standard Deviations</a></li>
            <li><a href="David.html">Frequency of Percentages</a></li>
            <li><a href="Dua.html">Sector Contributions to GDP</a></li>
            <li><a href="Seth.html">GDP Growth Rate</a></li>
        </ul>'''

Home = ((templatePage.replace('_IMG_', '<img src="./Economy.PNG">')).replace('_HEADING_', 'Home').replace('_STATS_', f'<p>{Home_Desc}</p>')).replace('_NAVBAR_', navbar).replace('Data Table Page', 'Home')
print(Home)

files = ['us.csv', 'russia.csv', 'japan.csv','china.csv', 'india.csv']

#Opens the CSV files and makes lists out of the data
def openCoolData(filename):
    with open(filename,"r") as filename:
        dataList = filename.read().strip()
        dataList = dataList.split('\n')
        for i in range(len(dataList)):
            dataList[i] = dataList[i].split(',')
    return dataList

#This returns a list with just the years and rates
def stripTheStupidSets(dataList):
    for i in dataList:
        if i == '' or i == ' ':
            dataList.remove(i)
    for i in range(0,16):
        dataList.pop(0)
    return dataList

#gets the data from the year 1990 and up
def gain1990s(dataList):
    dataList = dataList[1:]
    i = 0
    while int(dataList[i][0][:4]) < 1990:
        dataList.pop(i)
    return dataList

def createWList(filename):
    dataList = openCoolData(filename)
    dataList = stripTheStupidSets(dataList)
    dataList = gain1990s(dataList)
    return dataList

#Make all the data lists for the countries
US = createWList(files[0])
Russia = createWList(files[1])
Japan = createWList(files[2])
China = createWList(files[3])
India = createWList(files[4])

######################################################################################################################################################
#Seth's code - GDP Growth from 1990 - 2021
######################################################################################################################################################
#Make lists of all the x values (the years) of the data
def returnXAxis(dataList):
    XList = []
    for i in range (len(dataList)):
        XList.append(int(dataList[i][0][:4]))
    return XList

#Make lists of all the y values (the 
def returnYAxis(dataList):
    YList = []
    for i in range (len(dataList)):
        YList.append(float(dataList[i][1]))
    return YList

#Make all the lists for the X and Y values of each country
UsX = returnXAxis(US)
UsY = returnYAxis(US)
russiaX = returnXAxis(Russia)
russiaY = returnYAxis(Russia)
japanX = returnXAxis(Japan)
japanY = returnYAxis(Japan)
chinaX = returnXAxis(China)
chinaY = returnYAxis(China)
indiaX = returnXAxis(India)
indiaY = returnYAxis(India)

#Seth's Graph - Line graph of GDP Growth
plt.title("Some Really Cool National GDP Data On A Line Graph")
plt.plot(indiaX,indiaY, label='India')
plt.plot(UsX,UsY, label='US')
plt.plot(japanX,japanY, label='Japan')
plt.plot(chinaX,chinaY, label='China')
plt.plot(russiaX,russiaY, label='Russia')
plt.xlabel('Year')
plt.ylabel('GDP Growth (in %)')
plt.legend()
plt.savefig("GDPSethData")
plt.close()
#######################################################################################################################################################

#Basic mean function
def genMean(dataSet):
    return (sum(dataSet) // len(dataSet))

#Basic median function
def genMedian(lists):
    lists.sort()
    z = (len(lists))
    if z % 2 == 0:
        return (lists[((z // 2))] + lists[z // 2 - 1]) / 2
    else:
        return (z // 2)

#function that returns mean, median, and standard deviation
def statistics(listOfData):
    a = genMean(listOfData)
    k = 0
    for i in listOfData:
        k += (abs(a - i)**2)
    c = (k / len(listOfData))**0.5
    b = genMedian(listOfData)
    return [a,b,c]

#Find mean, median, and standard deviation for each countries
russiaMean,russiaMedian,russiaSD = statistics(russiaY)
UsMean,UsMedian,UsSD = statistics(UsY)
chinaMean,chinaMedian,chinaSD = statistics(chinaY)
japanMean,japanMedian,japanSD = statistics(japanY)
indiaMean,indiaMedian,indiaSD = statistics(indiaY)


###############################################################################################################################
# Danny - Bar graph of Standard Deviation per Country
###############################################################################################################################
names = ['United-States', 'Russia', 'Japan','China', 'India']

def dataDictGrab(data):
    new = []
    for file in data:
        temp = open(file, 'r').read().strip()
        temp = [[i.strip() for i in x.split(',')][:3] for x in temp.split('\n')][16:]
        new0 = [x[0] for x in temp]
        find = new0.index('1990-12-31')
        new.append(temp[find:])
    newdict = {}
    for i in range(len(names)):
        newdict.update({names[i]: new[i]})
    return newdict

dictionary = dataDictGrab(files)

def countrySD():
    SDdict = {}
    for country, data in dictionary.items():
        a, b, SD = statistics([float(x[1]) for x in data])
        SDdict.update({country: SD})
    return SDdict

def countryMean():
    Meandict = []
    for country, data in dictionary.items():
        mean, b, c = statistics([float(x[1]) for x in data])
        Meandict.append(mean)
    return Meandict

def SDGrapher():
    data = countrySD()
    plt.barh(list(data.keys()), list(data.values()))
    for key, items in data.items():
        plt.text(items, key, str(round(items, 3)))
    plt.title('SD values by Country')
    plt.savefig("GDPDannyData")
    plt.close()

SDGrapher()

#############################################################################################################################################################################
# David - Histogram documenting the frequency of certain GDP percentage growths
#############################################################################################################################################################################
def readData(data):
    with open(data,"r") as data:
                df = [x.split(',') for x in data.read().strip().split('\n') if x]
                for x in df:
                    try:
                        x[2]
                    except:
                        x.append(0)
                df = df[[x[0] for x in df].index('1990-12-31'):]
    return df

def create_histogram(data, column, bin_ranges):
    column_data = [float(x[column]) for x in data]
    plt.hist(column_data, bins=bin_ranges)
    plt.xlabel('Ranges')
    plt.ylabel('Frequency')
    plt.title('Histogram of Growth Percentages')
    plt.savefig('GDPDavidData')
    plt.close()
    

filedata = []
for country_name in files:
    filedata += readData(country_name)

column = 1
bin_ranges = range(-15, 16)

create_histogram(filedata, column, bin_ranges)

###########################################################################################################################################################
#Dua's Data - Pie Charts of Sector contributions to GDP
###########################################################################################################################################################
countriesList = ['United States', 'Russian Federation', 'Japan','China', 'India']

with open('piedata.txt', 'r') as piedata:
    piedata = piedata.read()
    piedata = piedata.split('\n')
    piedata.remove('')

#split the data in the document into a list
for i in range(len(piedata)):
    piedata[i] = piedata[i].split(',')
    for j in piedata[i]:
        if j == '':
            piedata[i].remove(j)          

sectors = piedata[0][1:]

#filter through list to get the data for each country
def getCountryStats(dataList):
    newList = []
    for i in range(len(piedata)):
        if piedata[i][0] in dataList:
            newList.append(piedata[i])
    return newList

piedata = getCountryStats(countriesList)

#get percentages for 2020 for each industry for each country
def getPercentages(dataList):
    for i in range(len(piedata)):
        country = []
        country.append(piedata[i][0])
        for j in range(4, 11, 2):
            country.append(float(piedata[i][j]))
        piedata[i] = country
    return piedata

piedata = getPercentages(piedata)
chinaval = piedata[0][1:]
indiaval = piedata[1][1:]
japanval = piedata[2][1:]
russiaval = piedata[3][1:]
usval = piedata[4][1:]

#make the pie graph for each country
plt.title(names[0] + ' GDP by Sector (2020)')
plt.pie(usval, labels = sectors, autopct='%1.1f%%')
plt.savefig('USPie')
plt.close()

plt.title(names[1] + ' GDP by Sector (2020)')
plt.pie(russiaval, labels = sectors, autopct='%1.1f%%')
plt.savefig('RussiaPie')
plt.close()

plt.title(names[2] + ' GDP by Sector (2020)')
plt.pie(japanval, labels = sectors, autopct='%1.1f%%')
plt.savefig('JapanPie')
plt.close()

plt.title(names[3] + ' GDP by Sector (2020)')
plt.pie(chinaval, labels = sectors, autopct='%1.1f%%')
plt.savefig('ChinaPie')
plt.close()

plt.title(names[4] + ' GDP by Sector (2020)')
plt.pie(indiaval, labels = sectors, autopct='%1.1f%%')
plt.savefig('IndiaPie')
plt.close()
#####################################################################################################

#Generating Webpages
List = ''
for i in range(len(names)):
    List += f'\t    <li class="means">{names[i]} : {countryMean()[i]}</li>\n'

Danny_Desc = "For my graph, I decided to see how consistent each country's GDP grew compared to their respective mean growth from 1990-2023. This was done by comparing each country's SD values, with a higher SD vlaue meaning more variability and thus less consistency to their mean growth. Here is a list of growth averages for reference:"
Danny = ((templatePage.replace('_IMG_', '<img src="GDPDannyData.png">')).replace('_HEADING_', 'Standard Deviations').replace('_STATS_', f'<p>{Danny_Desc}</p>\n\t<ul class="meanul">\n{List[:-1]}\n\t</ul>')).replace('_NAVBAR_', navbar).replace('Data Table Page', 'Country SD')


David_Desc = 'I analyzed and plotted the growth percentages of all countries from the 1990s and onwards to today into a histogram. This is helpful for determining the average global trend of world economies, as the graph is left skewed in the positive direction, so the world economy is increasing overall.'
David = ((templatePage.replace('_IMG_', '<img src="GDPDavidData.png">')).replace('_HEADING_', 'Frequency of Percentages').replace('_STATS_', f'<p>{David_Desc}</p>')).replace('_NAVBAR_', navbar).replace('Data Table Page', 'Country Histogram')


Dua_Desc = "The above pie charts demonstrate, for each country, the contribution from each of the four sectors: Agriculture, Industry, Manufacturing, and Services. Across the board, it seems like a good percentage (about 50% or more) of each country's GDP, comes from the Services sector, with the Industry sector being the second largest contribution."
pielist = ['USPie', 'RussiaPie', 'JapanPie', 'ChinaPie', 'IndiaPie']
imglist = ''
for i in pielist:
    imglist += f'\t<img src="./{i}.png">\n'
Dua = ((templatePage.replace('_IMG_', imglist[1:-1])).replace('_HEADING_', 'Sector Contributions to GDP').replace('_STATS_', f'<p>{Dua_Desc}</p>')).replace('_NAVBAR_', navbar).replace('Data Table Page', 'Country Pie Chart')

Seth_Desc = "Each line shows a different country and the graph shows the year along with the corresponding GDP%. From here we can see major points of recession and growth in the global economy when the line rises or falls sharply. Here is a list of growth averages for reference:"
Seth = ((templatePage.replace('_IMG_', '<img src="./GDPSethData.png">')).replace('_HEADING_', 'GDP Growth Rate').replace('_STATS_', f'<p>{Seth_Desc}</p>\n\t<ul class="meanul">\n{List[:-1]}\n\t</ul>')).replace('_NAVBAR_', navbar).replace('Data Table Page', 'Country Line Graph')


# Writing
with open('Home.html', 'w') as text:
        text.write(Home)
        text.close()

with open('Danny.html', 'w') as text1:
        text1.write(Danny)
        text1.close()

with open('David.html', 'w') as text2:
        text2.write(David)
        text2.close()

with open('Dua.html', 'w') as text3:
        text3.write(Dua)
        text3.close()

with open('Seth.html', 'w') as text4:
        text4.write(Seth)
        text4.close()
        
css = '''
/* navbar Styling */
    .navbar {
        position: sticky;
        top: 0px;
        width: 100%;
        margin-top: -40px;
        margin-left: -48px
        }
    .navbar li {
        height: auto;
        width: 20%;
        float: left;
        text-align: center;
        list-style: none;
        padding: 0;
        margin: 0;
        background-color: #9e9c9c;
        text-decoration: dotted #E4CA67;
        }
    .navbar a {
        padding: 20px 0;
        border-left: 3px dotted #E4CA67;
        text-decoration: none;
        color: black;
        display: block;
        }
     .navbar li:hover, a:hover {
        background-color: #bfbcbc;
        }
     .navbar li ul {
        display: none;
        height: 20px;
        margin: 0;
        padding: 0;
        }
     .navbar li:hover ul {
        display: block;
        position: absolute;
        }
     .navbar li ul li {
        background-color: #bfbcbc;
        }
     .navbar li ul li a {
        border-left: 1px solid #bfbcbc;
        border-right: 1px solid #bfbcbc;
        border-top: 1px solid #c9d4d8;
        border-bottom: 1px solid #bfbcbc;
        }
    .navbar li ul li a:hover {
        background-color: #E4CA67;
        }
        
/* Body Styling */
    h1 {
        text-align: center;
        background-color: #008000;
        padding-top: 50px;
        padding-bottom: 50px;
        color: white;
        border-style: dotted;
        border-width: 10px;
        border-color: #E4CA67;
        text-decoration: underline dotted white
        margin-top: 10px
         }
    body {
        background-image: url("./Dollars.JPG");
        margin-top: 40px
        background-color: #ffeeed;
        }
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        margin-top: 40px;
        }
    p{
        color: white;
        font-size: 24px;
        font-weight: 4px;
        border: 5px solid Green;
        background: Gray;
        padding: 15px;
        text-align: center;
        }
    .means{
        color: white;
        font-size: 18px;
        font-weight: 4px;
        border: 5px solid Green;
        background: Black;
        padding: 15px;
        text-align: center;
        }
    .meanul {
        list-style:none;
        padding-left:0;
        }
            '''
with open('stylesheet.css', 'w') as text5:
        text5.write(css)
        text5.close()



