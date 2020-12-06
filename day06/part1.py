forms = open("input.txt").read().split("\n\n")
result = 0

for form in forms:
    form_count = set()
    lista = form.split("\n")
    for i in lista:
        for x in i:
            form_count.add(x)
    result += len(form_count)

print(result)