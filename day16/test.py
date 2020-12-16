lista = []

for i in range(1,4+1):
    lista.append(i)
#print(i)


lista = [[7,3,47], [40,4,50], [55,2,20], [38,6,12]]

#print(lista[0][1])

""" for i in range(0, len(lista[0])):
    print(i) """


from collections import defaultdict

ticket_dct2 = defaultdict(list)

ticket_dct2["test"].append(3)
ticket_dct2["test"].append(4)
print(ticket_dct2)