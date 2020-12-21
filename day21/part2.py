from typing import NamedTuple
from copy import deepcopy
import collections

data = open("input.txt").read().split("\n")

allergens_dct = {}
all_ingredients = set()

for line in data:
    tmp_set = set()
    tmp_lista = []
    ingredients, allergens = line.split(" (contains ")
    ingredients = [i for i in ingredients.split()]
    allergens = [u.strip(")") for u in allergens.split(", ")]
    for allergen in allergens:
        if allergen not in allergens_dct:
            for ingredient in ingredients:
                all_ingredients.add(ingredient)
                tmp_set.add(ingredient)
            allergens_dct[allergen] = deepcopy(tmp_set)
            tmp_set = set()
        else:
            for ingredient in ingredients:
                all_ingredients.add(ingredient)
                if ingredient in allergens_dct[allergen]:
                    tmp_lista.append(ingredient)
            tmp_set = deepcopy(allergens_dct[allergen])
            for item in allergens_dct[allergen]:
                if item not in tmp_lista:
                    tmp_set.remove(item)
            allergens_dct[allergen] = deepcopy(tmp_set)
            tmp_set = set()

while True:
    for k, v in allergens_dct.items():
        if len(v) != 1:
            allergens_dct[k] = v.intersection(all_ingredients)
        if len(v) == 1:
            all_ingredients = all_ingredients.difference(v)
            continue
            
    tmp_set = set()
    #Check to make sure all allergens have only one ingredient in it's value and break while loop if True
    check = 0
    for value in allergens_dct.values():
        if len(value) == 1 and list(value)[0] not in all_ingredients:
            check += 1
    if check == len(allergens_dct):
        break

ordered_allergens_dct = collections.OrderedDict(sorted(allergens_dct.items()))

summa = ""
tmp_lista = []
for v in ordered_allergens_dct.values():
    tmp_lista.append(list(v)[0])
for i in tmp_lista:
    summa += i + ","
print(summa[:-1])
