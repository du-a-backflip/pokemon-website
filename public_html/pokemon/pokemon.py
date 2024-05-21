#! /usr/bin/python3
print("Content-Type: text/html\n\n")
with open('home.html', 'r') as text:
    text = text.read()

print(text)