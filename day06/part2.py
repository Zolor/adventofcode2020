import time
start_time = time.time()

forms = open("input.txt").read().split("\n\n")
result = 0

for form in forms:
    form_count = dict()
    lista = form.split("\n")
    people_in_form = len(lista)
    for i in lista:
        for x in i:
            if not x in form_count:
                form_count[x] = 1
            else:
                form_count[x] += 1
    for y in form_count.values():
        if people_in_form == y:
            result += 1

print(result)
print("--- %s seconds ---" % (time.time() - start_time))