def bank(x,y):
    x = int(x)
    y = int(y)
    z = x*(1 + 0.1/1)**y
    print(z)
bank(10000,4)