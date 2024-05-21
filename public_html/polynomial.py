#!/usr/bin/python3
print("Content-Type: text/html\n\n")
PAGE_TITLE = "My Favorite Polynomial - Dua Baig"
page = '''
<!DOCTYPE html>
<html>
    <head>
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>
</html>
'''
page = page[len('\n'):(len(page)-len('\n'))]

def makePolyTable(start, end):
    tableColumn = '<th>x</th><th>y=x^3+4x^2+18x+27</th>' 
    bodyData = ''
    tab = ' ' * 4
    table = '''
        <table>
            <thead>
                <tr>_COLUMNS_</tr>
            </thead>
            <tbody>
                _TBODY_
            </tbody>
        </table>
    '''
    table = table[:len(table) - (len(tab)+len('\n'))]
    for i in range (start, (end+1)):
        bodyData += '<tr><td>'+ str(i)+'</td><td>' + str((i**3) + 5*(i**2) + 18*i + 27) +'</td></tr>\n' + (tab * 4)
    bodyData = bodyData[: len(bodyData)-(len(tab) * 4 + len('\n'))]
    table = table.replace('_COLUMNS_', tableColumn)
    table = table.replace('_TBODY_', bodyData)
    return table

def generateBody():
    tab = ' ' * 4
    body = '<h1>My Favorite Polynomial</h1>\n'
    body += tab * 2 + '<p>\n'
    body += tab * 3 + 'My favorite Polynomial is y=x^3+4x^2+18x+27. I like this polynomial because I think 3 is a pretty satisfying number(hence x being cubed). As they say "Good things come in threes" - like the flavors in Neopolitan icecream, and the components of a nucleotide (phosphate, base, and deoxyribose). I suppose my feelings towards three also extend to the number 27, as 27 is a multiple of 3 and is also a perfect cube(9 x 9 x 9). I also like the numbers 4 and 18, since they make me think of my birthday.\n'
    body += tab * 2 + '</p>'
    body += makePolyTable(-20, 50)
    return body

page = page.replace('_TITLE_', PAGE_TITLE)
page = page.replace('_BODY_', generateBody())
print (page)