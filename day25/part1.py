data = open("input.txt").read().split("\n")

def loop_cracker(num):
    loop = 0
    val = 1
    subject_number = 7
    dividing_value = 20201227
    while True:
        val *= subject_number
        val %= dividing_value
        loop += 1
        if val == num:
            return(loop)

def encryption(loop_size, pub_key):
    loop = 0
    encryption_key = 1
    dividing_value = 20201227
    while loop < loop_size:
        encryption_key *= pub_key
        encryption_key %= dividing_value
        loop += 1
    return(encryption_key)

card_pub_key = int(data[0])
door_pub_key = int(data[1])

card_loop_size = loop_cracker(card_pub_key)
door_loop_size = loop_cracker(door_pub_key)

print(encryption(door_loop_size, card_pub_key))
print(encryption(card_loop_size, door_pub_key))
