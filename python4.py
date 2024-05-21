def mySwap(text):
    new = ''
    for i in text:
        if i.isupper():
            new += i.lower()
        else:
            new += i.upper()
    text = new
    print (text)