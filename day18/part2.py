math = open("input.txt").read().split("\n")
summa = 0

def calculator(lista):
    while len(lista) != 1:
        while "+" in lista:
            for xc, nc in enumerate(lista):
                if nc == "+":
                    tmp = eval(' '.join(map(str, lista[xc-1:xc+2])))
                    del lista[xc-1:xc+2]
                    lista.insert(xc - 1, str(tmp))
                    break
        while "*" in lista:
            for xc, nc in enumerate(lista):
                if nc == "*":
                    tmp = eval(' '.join(map(str, lista[xc-1:xc+2])))
                    del lista[xc-1:xc+2]
                    lista.insert(xc - 1, str(tmp))
                    break
    return(int(lista[0]))

def decoupler(line):
    while "(" in line:
        count = 0
        for x, n in enumerate(line):
            if (n == "(" and count == 0):
                start = x
                count += 1
            elif n == "(" and count == 1:
                start_2 = x
                count += 1
            elif n == ")" and count == 2:
                end_2 = x
                tmp = calculator([i for i in line[start_2 + 1:end_2]])
                del line[start_2:end_2 + 1]
                line.insert(start_2, str(tmp))
                count -= 1
                break
            elif n == ")" and count == 1:
                end = x
                #Replace our () with a sum in the list
                tmp = calculator([i for i in line[start + 1:end]])
                del line[start:end + 1]
                line.insert(start, str(tmp))
                count -= 1
                break
    return(line)

for line in math:
    line = [c for word in line.split() for c in word]
    res = decoupler(line)
    summa += calculator(res)

print(summa)
