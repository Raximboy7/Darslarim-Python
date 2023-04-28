a = int(input('1-son kriting:'))
b = input('matematik operator (^ * / + -) :')
d = int(input('2-son kriting:'))

if b == '-':
    print(a, d, 'ayrilganda', a - d)
elif b == '+':
    print(a, d, 'qoshilganda', a + d)
elif b == '*':
    print(a, d, 'kopaytrilganda', a * d)
elif b == '/':
    print(a, d, 'bolinganda', a / d)
elif b == '^':
    print(a, d, 'darajasi', pow(a, d))
