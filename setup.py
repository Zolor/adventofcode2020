import os, sys
#Verify we're getting input
if len(sys.argv) != 2:
    print('Missing day number. Run e.g:')
    print('python setup.py 13')
    sys.exit(2)
#Create folder from input
path = str(os.getcwd()) + "/day" + str(sys.argv[1])
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
 
#Create 4 empty files
lista = ["/part2.py", "/test.py", "/input.txt", "/testinput.txt"]
for i in lista:
    open(path + i, 'a').close()

#Create and Write to part1.py
part1 = path + "/part1.py"
f = open(part1, "a")
f.write('data = open("input.txt").read().split("\\n")')
f.close()

#Success?!
print(str(path) + " and adjacent files created!")