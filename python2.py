def twoThrough20():
    n = 0
    total = 0
    while n <= 18:
        n = n + 2
        total += n
        print(n)
    return(total)

x = -1

while x <= 0:
    x = int(input("Number: "))
    if x <= 0:
        print("Must be Positive")