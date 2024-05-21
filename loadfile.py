def tallyText():
    with open('Text2.txt', 'r') as text:
        txt = text.read()
        txt = txt.lower()
        d = {}
        wordlst = ''
        val = ''
        for i in range (len(txt)):
            if txt[i].isalpha() or txt[i] == ' ' or txt[i] == '-':
                wordlst += txt[i]
        print(wordlst)
        wordlst = wordlst.split()
        for i in range (len(wordlst)):
            if wordlst[i] in d:
                val = d.get(wordlst[i])
                val += '|' 
                d.pop(wordlst[i])
                d[wordlst[i]] = val
            else:
                d[wordlst[i]] = '|'
        print(d)
