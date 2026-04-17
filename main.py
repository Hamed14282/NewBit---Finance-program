isCube = False
calcType = 0
count = 0
product = 1
sum = 0
values = []

print("Calculating using operators\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
option = int(input("Select an option: "))
match option:
    case 1:
        print("Addition")
        calcType = 1
    case 2:
        print("Subtraction")
        calcType = 2
    case 3:
        print("Multiplication")
        calcType = 3
    case 4:
        print("Division")
        calcType = 4 
    case 5:
        print("Finance app")
        calcType = 5

valuesNum = int(input("How many numbers do you want to calculate?: "))

for i in range(valuesNum):
    count += 1
    values.append(int(input("Input number {}: ".format(count))))

match calcType: #Addition
    case 1:
        for num in values:
            sum += num
    case 2: #Subtraction
        sum = values[0]
        for num in values[1:]:
            sum -= num
    case 3: #Multiplication
        for num in values:
            product *= num
    case 4: #Division
        product = values[0]
        for num in values[1:]:
            product /= num


# if (valuesNum == 2):
#     if (values[0] == values[1]):
#         isCube = True
#         print("Shape is a square")
#     else:
#         print("Not a square")
# elif (valuesNum == 3):
#     if (values[0] == values[1] == values[2]):
#         isCube = True
#         print("Shape is a cube")
#     else:
#         print("Not a cube")

print("Count: {}".format(count))
match calcType:
    case 1:
        print("Sum: {}".format(sum))
    case 2:
        print("Sum: {}".format(sum))
    case 3:
        print("Product: {}".format(product))
    case 4:
        print("Product: {}".format(product))

