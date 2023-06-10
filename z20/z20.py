import string
d = {}

for letter in string.ascii_uppercase:
    d[letter] = 0


for (k,v) in d.items():
    if k in ('D', 'G'):
        d[k] = 2
    elif k in ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'):
        d[k] = 1
    elif k in ('B', 'C', 'M', 'P'):
        d[k] = 3
    elif k in ('F', 'H', 'V', 'W', 'Y'):
        d[k] = 4
    elif k in ('K'):
        d[k] = 5
    elif k in ('J', 'X'):
        d[k] = 8
    elif k in ('Q', 'Z'):
        d[k] = 10

print(d)

word = input('Введите слово на английском языке').upper()
my_list = list(word)
print(my_list)
cost = 0
for (k,v) in d.items():
    if k in my_list:
        cost +=d[k]
print(cost)

