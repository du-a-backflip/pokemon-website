#! /usr/bin/python3
print("Content-Type: text/html\n\n")
site = '''
<DOCTYPE HTML>
<html>
    <head>
        <title>
            ?TITLE?
        </title>
        <style>
            ?STYLE?
        </style>
        _OTHER_
    </head>
    <body>
        ?BODY?
    </body>
</html>'''

#Style for homepage, top10 pokemon, and all pokemon
mainstyle = '''
            h1 {
                text-align: center;
                background-color: #bd8f8f;
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
                background-image: url('graphpaper.jpg');
                 }
            .favpokemon {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 20%;
                }
            p {
                text-align: center;
                background-color: #ddabab;
                padding-top: 20px;
                padding-bottom: 20px;
                margin-left: 20px;
                margin-right: 20px;
                }
            .navbar {
                width: 100%;
                height: 50px;
                padding: 0;
                text-align: center;
                font-weight: 100;
                }
            table {
                margin-left: auto;
                margin-right: auto;
                width: 99%;
                }
            th, td {
                text-align: center;
                padding: 4px;
                }
            .navbar li {
                height: auto;
                width: 25%;
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
            td {
                min-width: 75px;
                border: 2px solid black;
                }
            .Legendary td {
                border-color: #E4CA67;
                }
            .Normal td:nth-child(odd) {
                background-color: #c2c3a3;
                }
            .Normal1 td:nth-child(even) {
                background-color: #b1b187;
                }
            .Fire td:nth-child(odd) {
                background-color: #f2a56b;
                }
            .Fire1 td:nth-child(even) {
                background-color: #ee8d47;
                }
            .Water td:nth-child(odd) {
                background-color: #9cacd7;
                }
            .Water1 td:nth-child(even) {
                background-color: #8198c3;
                }
            .Grass td:nth-child(odd) {
                background-color: #a2d385;
                }
            .Grass1 td:nth-child(even) {
                background-color: #8ac865;
                }
            .Electric td:nth-child(odd) {
                background-color: #f9de72;
                }
            .Electric1 td:nth-child(even) {
                background-color: #f8d344;
                }
            .Ice td:nth-child(odd) {
                background-color: #b6e5e0;
                }
            .Ice1 td:nth-child(even) {
                background-color: #a2dada;
                }
            .Fighting td:nth-child(odd) {
                background-color: #d2726b;
                }
            .Fighting1 td:nth-child(even) {
                background-color: #d55d5d;
                }
            .Poison td:nth-child(odd) {
                background-color: #bc7cb6;
                }
            .Poison1 td:nth-child(even) {
                background-color: #b168ac;
                }
            .Ground td:nth-child(odd) {
                background-color: #e9d494;
                }
            .Ground1 td:nth-child(even) {
                background-color: #e1c771;
                }
            .Flying td:nth-child(odd) {
                background-color: #bbb0d8;
                }
            .Flying1 td:nth-child(even) {
                background-color: #dfc5fe;
                }
            .Psychic td:nth-child(odd) {
                background-color: #f58bac;
                }
            .Psychic1 td:nth-child(even) {
                background-color: #f46994;
                }
            .Bug td:nth-child(odd) {
                background-color: #c6cd77;
                }
            .Bug1 td:nth-child(even) {
                background-color: #b5c252;
                }
            .Rock td:nth-child(odd) {
                background-color: #cebd6e;
                }
            .Rock1 td:nth-child(even) {
                background-color: #c6b359;
                }
            .Ghost td:nth-child(odd) {
                background-color: #cebd6e;
                }
            .Ghost1 td:nth-child(even) {
                background-color: #c6b359;
                }
            .Fairy td:nth-child(odd) {
                background-color: #f7dae8;
                }
            .Fairy1 td:nth-child(even) {
                background-color: #f5cee4;
                }
            .Dragon td:nth-child(odd) {
                background-color: #9289be;
                }
            .Dragon1 td:nth-child(even) {
                background-color: #8379b6;
                }
            .Steel td:nth-child(odd) {
                background-color: #ccccdf;
                }
            .Steel1 td:nth-child(even) {
                background-color: #b7b7d0;
                }
    '''
            
mainstyle = mainstyle[12:]
site = site[1:]

#open text file
with open('pokemon.csv', 'r') as text:
    text = text.read()
    text = text[:len(text)-1]

#make table out of data
def generatePokeTable(data):
    tbody = ''
    tab = ' ' * 4
    header = ''
    table = '''
        <table>
            <thead>
                _THEADER_
            </thead>
            <tbody>
                _TBODY_
            </tbody>
        </table>'''
    data = data.split('\n')
    for i in range(len(data)):
        data[i] = data[i].split(',')
        tbody += '\n' + tab*4 + '<tr'
        tbody += ' class = "' + data[i][2]
        if data[i][3] != '':
            tbody += ' ' + data[i][3] + str(1)
        else:
            tbody += ' ' + data[i][2] + str(1)
        if 'True' in data[i]:
            tbody += ' Legendary">'
        else:
            tbody += '">'
        for j in range(len(data[i])):
            if data[i][j] == '':
                data[i][j] = 'N/A'
            if i >= 1 and j == 0:
                tbody += '\n' + tab*5 + '<td>'
                tbody += '\n' + tab*6 + data[i][j]
                tbody += '\n' + tab*6 + '<br>'
                tbody += '\n' + tab*6 + '<img src ="./pokemon/img/front/' + str(data[i][j]) + '.png">'
                tbody += '\n' + tab*6 + '<img src ="./pokemon/img/back/' + str(data[i][j]) + '.png">'
                tbody += '\n' + tab*5 + '</td>'
            else:
                tbody += '\n' + tab*5 + '<td>'+ data[i][j] + '</td>'
        tbody += '\n' + tab*4 + '</tr>'
        if i == 0:
            header = tbody
            tbody = ''
    tbody = tbody[(1+len(tab)*4):]
    header = header[1+len(tab)*4:]
    header = header.replace('<tr>', '<th>')
    header = header.replace('</tr>', '</th>')
    table = table.replace('_TBODY_', tbody)
    table = table.replace('_THEADER_', header)
    table = table[1:]
    return(table)

#Top 10 Pokemon List for function
top10list = ['Magneton', 'Magnemite', 'Cloyster', 'Ditto', 'Horsea', 'Squirtle', 'Dragonair', 'Rapidash', 'Ninetales', 'Ivysaur']

#filter text by type of pokemon or by top 10 and make table out of filtered list
def generateTypeText(data, poketype):
    data = data.split('\n')
    typelist = []
    typelist.append(data[0].split(','))
    for i in range(len(data)):
        data[i] = data[i].split(',')
        if data[i][1] in poketype or data[i][2] == poketype or data[i][3] == poketype:
            typelist.append(data[i])
    for j in range(len(typelist)):
        typelist[j] = ','.join(typelist[j])
    typelist = '\n'.join(typelist)
    typetable = generatePokeTable(typelist)
    return(typetable)
    
#lists for navbar
pageList = ['Home', 'Types', 'All Pokemon', 'Top 10']
pagefiles = ['home.html', '', 'allpokemon.html', 'top10pokemon.html']
typeList = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Fairy', 'Dragon', 'Steel']
typefiles = ['normalpokemon.html', 'firepokemon.html', 'waterpokemon.html', 'grasspokemon.html', 'electricpokemon.html', 'icepokemon.html', 'fightingpokemon.html', 'poisonpokemon.html', 'groundpokemon.html', 'flyingpokemon.html', 'psychicpokemon.html', 'bugpokemon.html', 'rockpokemon.html', 'ghostpokemon.html', 'fairypokemon.html', 'dragonpokemon.html', 'steelPokemon.html']

#generate navbar
def createnavbar():
    lst = pageList
    sublst = typeList
    lstfiles = pagefiles
    sublstfiles = typefiles
    navbody = ''
    tab = ' ' * 4
    navbar = '''
        <ul class = "navbar">
            _LIST_
        </ul>'''
    for i in range(len(lst)):
        navbody += '\n' + tab*3 + '<li>' + '\n' + tab*4 + '<a href="' + lstfiles[i] + '">' + lst[i] + '</a>'
        if i == 1:
            navbody += '\n' + tab*4 + '<ul>'
            for j in range(len(sublst)):
                navbody += '\n' + tab*5 + '<li>' + '<a href="' + sublstfiles[j] + '">' + sublst[j] + '</a></li>'
            navbody += '\n' + tab*4 + '</ul>'
        else:
            navbody += '\n' + tab*3 +'</li>'
    navbody = navbody[1+(len(tab)*3):]
    navbar = navbar.replace('_LIST_', navbody)
    navbar = navbar[1:]
    return(navbar)

navbar = createnavbar()

#About me section for homepage
aboutme = '''
        <p>
            Hello! My name is Dua! I like to draw, listen to music, and play video games like Animal Crossing.
            In all honesty, I've never played a Pokemon game before. It's always seemed like to play, you need
            to know all the pokemon and all their stats - and there are a lot of those things. It gets overwhelming
            very quickly. So, I hope my website can help you with that!
        </p>
        <p>
            Despite me never playing a Pokemon game, I do have a favorite pokemon! My favorite is Magneton.
            Do I know whether it's a bad or good pokemon - nope!, but I like it anyways.
            (I'm sorry if that offends anybody.)'
        </p>
        <img class = "favpokemon"
            src = "./pokemon/img/front/82.png">
        <img class = "favpokemon"
            src = "./pokemon/img/back/82.png">'''
aboutme = aboutme[1:]

#Reasoning for top 10 pokemon chosen
Top10pokemon = '''
        <p>
            DISCLAMER: I chose these pokemon mainly due to aesthetics, and not strength.
        </p>
        <p>
                The reason why I chose Ivysaur is because I like the color combination. The green and pinks chosen
            are very pleasing to the eye, and i also like the bud on its back - it's very pretty. I chose Squirtle
            because I think its cute, and because I like the memes with it in it (the one where a squirtle is meeting
            another group of squirtles and they're all happy to see each other). I also chose Rapidash and Ninetails since
            I think they look elegant, and because Rapidash reminds me of a toy my sister had at one point (it was a
            small white horse figure with a mane made of what looked to be blue fire). Magnemite is on the list since I like
            how round it is, and I think it's cool how it kind of looks like a robot. Magneton is here for the same reasons,
            but I like it more because there's more to love (since it's basically 3 magnemites joined together). Cloyster and
            Ditto are here because I like their faces - Cloyster looks very smug, and I find its face satisfying to look at
            due to how clean and sharp it is. Also, its kind of expression is my favorite to draw. Last of all we have
            Dragonair, who is on this list because I like their color and headfins (headwings? I don't know what they're called).
        </p> '''

def generatepage(Title, heading, table, text, style):
    tab = 4 * ' '
    page = site.replace('?TITLE?', Title)
    page = page.replace('_OTHER_', '<meta charset="UTF-8">')
    body = '\n' + tab*2 + '<h1>' + "Dua's Pokemon Website: " + heading + '</h1>'
    body += '\n' + tab*2 + navbar[len(tab*2):]
    body += '\n' + table
    body += text
    page = page.replace('?BODY?', body)
    page = page.replace('?STYLE?', style)
    return page

#Tables for other pages
allPokemon = generatePokeTable(text)
normalPokemon = generateTypeText(text, 'Normal')
firePokemon = generateTypeText(text, 'Fire')
waterPokemon = generateTypeText(text, 'Water')
grassPokemon = generateTypeText(text, 'Grass')
electricPokemon = generateTypeText(text, 'Electric')
icePokemon = generateTypeText(text, 'Ice')
fightingPokemon = generateTypeText(text, 'Fighting')
poisonPokemon = generateTypeText(text, 'Poison')
groundPokemon = generateTypeText(text, 'Ground')
flyingPokemon = generateTypeText(text, 'Flying')
psychicPokemon = generateTypeText(text, 'Psychic')
bugPokemon = generateTypeText(text, 'Bug')
rockPokemon = generateTypeText(text, 'Rock')
ghostPokemon = generateTypeText(text, 'Ghost')
fairyPokemon = generateTypeText(text, 'Fairy')
dragonPokemon = generateTypeText(text, 'Dragon')
steelPokemon = generateTypeText(text, 'Steel')
top10 = generateTypeText(text, top10list)

#Create homepage
homePage = generatepage("Dua's Pokemon Website - Home", 'About Me', '', aboutme, mainstyle) 
with open('home.html', 'w') as home_html:
    home_html.write(homePage)
    home_html.close

#generate all pokemon page
allPokemonPage = generatepage("Dua's Pokemon Website - All Pokemon", "All Pokemon", allPokemon, '', mainstyle)
allPokemon_html = open('allpokemon.html', 'w')
allPokemon_html.write(allPokemonPage)
allPokemon_html.close

#generate normal pokemon page
normalPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Normal", "Normal Pokemon", normalPokemon, '', mainstyle)
normalPokemon_html = open('normalpokemon.html', 'w')
normalPokemon_html.write(normalPokemonPage)
normalPokemon_html.close

#generate fire pokemon page
firePokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Fire", "Fire Pokemon", firePokemon, '', mainstyle)
firePokemon_html = open('firepokemon.html', 'w')
firePokemon_html.write(firePokemonPage)
firePokemon_html.close

#generate water pokemon page
waterPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Water", "Water Pokemon", waterPokemon, '', mainstyle)
waterPokemon_html = open('waterpokemon.html', 'w')
waterPokemon_html.write(waterPokemonPage)
waterPokemon_html.close

#generate grass pokemon page
grassPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Grass", "Grass Pokemon", grassPokemon, '', mainstyle)
grassPokemon_html = open('grasspokemon.html', 'w')
grassPokemon_html.write(grassPokemonPage)
grassPokemon_html.close

#generate electric pokemon page
electricPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Electric", "Electric Pokemon", electricPokemon, '', mainstyle)
electricPokemon_html = open('electricpokemon.html', 'w')
electricPokemon_html.write(electricPokemonPage)
electricPokemon_html.close

#genetate ice pokemon page
icePokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Ice", "Ice Pokemon", icePokemon, '', mainstyle)
with open('icepokemon.html', 'w') as icePokemon_html:
    icePokemon_html.write(icePokemonPage)
    icePokemon_html.close

#generate fighting pokemon page
fightingPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Fighting", "Fighting Pokemon", fightingPokemon, '', mainstyle)
with open('fightingpokemon.html', 'w') as fightingpokemon_html:
    fightingpokemon_html.write(fightingPokemonPage)
    fightingpokemon_html.close

#generate poison pokemon page
poisonPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Poison", "Poison Pokemon", poisonPokemon, '', mainstyle)
with open('poisonpokemon.html', 'w') as poisonPokemon_html:
    poisonPokemon_html.write(poisonPokemonPage)
    poisonPokemon_html.close

#generate ground pokemon page
groundPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Ground", "Ground Pokemon", groundPokemon, '', mainstyle)
with open('groundpokemon.html', 'w') as groundPokemon_html:
    groundPokemon_html.write(groundPokemonPage)
    groundPokemon_html.close

#generate flying pokemon page
flyingPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Flying", "Flying Pokemon", flyingPokemon, '', mainstyle)
with open('flyingpokemon.html', 'w') as flyingPokemon_html:
    flyingPokemon_html.write(flyingPokemonPage)
    flyingPokemon_html.close

#generate psychic pokemon page
psychicPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Psychic", "Pyschic Pokemon", psychicPokemon, '', mainstyle)
with open('psychicpokemon.html', 'w') as psychicPokemon_html:
    psychicPokemon_html.write(psychicPokemonPage)
    psychicPokemon_html.close

#generate bug pokemon page
bugPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Bug", "Bug Pokemon", bugPokemon, '', mainstyle)
with open('bugpokemon.html', 'w') as bugPokemon_html:
    bugPokemon_html.write(bugPokemonPage)
    bugPokemon_html.close

#generate rock pokemon page
rockPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Rock", "Rock Pokemon", rockPokemon, '', mainstyle)
with open('rockpokemon.html', 'w') as rockPokemon_html:
    rockPokemon_html.write(rockPokemonPage)
    rockPokemon_html.close

#generate ghost pokemon page
ghostPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Ghost", "Ghost Pokemon", ghostPokemon, '', mainstyle)
with open('ghostpokemon.html', 'w') as ghostPokemon_html:
    ghostPokemon_html.write(ghostPokemonPage)
    ghostPokemon_html.close

#generate fairy pokemon
fairyPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Fairy", "Fairy Pokemon", fairyPokemon, '', mainstyle)
with open('fairypokemon.html', 'w') as fairyPokemon_html:
    fairyPokemon_html.write(fairyPokemonPage)
    fairyPokemon_html.close

#generate dragon pokemon page
dragonPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Dragon", "Dragon Pokemon", dragonPokemon, '', mainstyle)
with open('dragonpokemon.html', 'w') as dragonPokemon_html:
    dragonPokemon_html.write(dragonPokemonPage)
    dragonPokemon_html.close

#generate steel pokemon page
steelPokemonPage = generatepage("Dua's Pokemon Website - Pokemon Types: Steel", "Steel Pokemon", steelPokemon, '', mainstyle)
with open('steelPokemon.html', 'w') as steelPokemon_html:
    steelPokemon_html.write(steelPokemonPage)
    steelPokemon_html.close

#generate Top10 page
top10Page = generatepage("Dua's Pokemon Website - Top 10 Pokemon", "My Top 10 Pokemon", top10, Top10pokemon, mainstyle)
top10Page_html = open('top10pokemon.html', 'w')
top10Page_html.write(top10Page)
top10Page_html.close 

with open('home.html', 'r') as home_html:
    home_html = home_html.read()

print(home_html)
    