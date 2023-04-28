import math


def daraja():
    d = int(input("Sonni kirit: "))
    u = int(input("Darajani kirit: "))
    print(pow(d, u))


def ildiz():
    l = int(input())
    print(math.ceil(math.sqrt(l)))


def sum():
    a = int(input())
    sum = 0
    for i in range(a):
        a = int(input())
        sum += a
    print(sum)


def qoshish():
    x = int(input())
    y = int(input())
    print(x + y)


def minus():
    x = int(input())
    y = int(input())
    print(x - y)


def kopaytir():
    x = int(input())
    y = int(input())
    print(x * y)


def bolish():
    x = int(input())
    y = int(input())
    print(x // y)


a = input()
if a[0] == '+':
    qoshish()
elif a[0] == '-':
    minus()
elif a[0] == '*':
    kopaytir()
elif a[0] == '/':
    bolish()
elif a[0] == '^':
    daraja()
elif a[0] == '~':
    ildiz()
elif a == "sum":
    sum()