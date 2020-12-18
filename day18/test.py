import re, ast
math = open("testinput.txt").read().split("\n")

 
for line in math:
    lista = [c for word in line.split() for c in word]
    while len(lista) != 1:
        tmp = eval(' '.join(map(str, lista[0:3])))
        del lista[0:3]
        lista.insert(0, tmp)
        print(lista)
print(int(lista[0]))
"""
while "(" in lista:
    print(lista.count("("))
    print(lista)

del lista[4:9]
lista.insert(4, "20")
print(lista)
print(eval(' '.join(map(str, lista[0:3]))))

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# using list comprehension 
listToStr = ' '.join(map(str, s)) """

