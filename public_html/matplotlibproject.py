import matplotlib as plt

files = ['united-states-gdp-growth-rate.csv', '', '', '', '']
def openCoolData(filename):
    with open(filename,"r") as filename:
        dataList = filename.read()
        dataList = dataList.split('\n')
        for i in range(len(dataList)):
            dataList[i] = dataList[i].split(',')
    return dataList
lst = []

for i in range(len(text)):
    text[i] = text[i].split(',')
    if text[i][1] not in lst:
        lst.append(text[i][1])
print(lst)