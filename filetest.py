
totalData = 2 #Number of variables in file

########################################################################################################

file = open("data.txt", "r")

lines = file.readlines()

file.close()

########################################################################################################
"""
file = open("data.txt", "w") #Open the file to make modifications



file.writelines(lines)

file.close() #Close the file to save modifications
"""
########################################################################################################

while len(lines) < totalData:
    lines.append("\n")

if lines[0].strip() == "":
    initialIncome = float(input("Initial income missing, enter initial income: "))
else:
    initialIncome = float(lines[0].strip())

if lines[1].strip() == "":
    initialSavings = float(input("Initial savings missing, enter initial savings: "))
else:
    initialSavings = float(lines[1].strip())

########################################################################################################

file = open("data.txt", "w")

lines[0] = str(initialIncome) + "\n"
lines[1] = str(initialSavings) + "\n"

file.writelines(lines)

file.close()

########################################################################################################

file = open("data.txt") #Open the file to read it

lines = file.readlines()

print(lines[1])

file.close() #Close at the end