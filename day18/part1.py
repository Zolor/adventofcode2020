math = open("input.txt").read().split("\n")
summa = 0

def calculator(lista):
    while len(lista) != 1:
        tmp = eval(' '.join(map(str, lista[0:3])))
        del lista[0:3]
        lista.insert(0, tmp)
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
                tmp = calculator([i for i in line[start + 1:end]])
                del line[start:end + 1]
                line.insert(start, str(tmp))
                count -= 1
                break
    return(line)

for lina in math:
    lina = [c for word in lina.split() for c in word]
    res = decoupler(lina)
    summa += calculator(res)

print(summa)
