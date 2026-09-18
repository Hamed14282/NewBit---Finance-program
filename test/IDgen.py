import random

ids = ["122123423", "jfiameisnt", "1234567890"]
id = ""

def gen_id(r):

    id = ""

    set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for i in range(r):
        random_num = random.randint(0, len(set)-1)
        id += str(set[random_num])

    return id

def check_id(id):
    global ids

    for name in ids:
        if name == id:
            return True

        return False

id = gen_id(15)
print("new ID: " + id)


while check_id(id) == True:
    id = gen_id(15)

    print("repeat new ID: " + id)
    