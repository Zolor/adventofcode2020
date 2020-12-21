include = {"apple", "banana", "cherry"}
exclude = {"apple", "banana", "cherry"}
include.add("allergen")
ingredients_dct = {}
ingredients_dct["key"] = {"incl": include, "excl":exclude}

ingredients_dct["key"].get("excl").add("lol")

print(ingredients_dct)

#print(dct.get("key")[include])