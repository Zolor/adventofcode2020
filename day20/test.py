img = ['#..#','..##','.###','..#.#']

for line in ([''.join(list(i)[::-1]) for i in zip(*img)]):
    print(line)

x = "ABC"
y = "DEF"

for a, b in zip(img, img):
    print(a + b)