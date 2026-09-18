vars = []
base_name = input("Enter variable base name: ")  # User types 'Calc'
total_vars = int(input("How many variables? "))  # User types '3'

var_counter = 1
for i in range(total_vars):
    # Construct the variable name as a string
    var_name = f"{base_name}{var_counter}"
    
    # Force Python to create a real variable with this name
    globals()[var_name] = i
    var_counter += 1

    #Saves the variable names into an array to know what to call back later
    vars.append(var_name)


# Because globals() was modified, these variables now literally exist in the code:
for var in vars:
    print(globals()[var])  # Outputs variable using array of variable names 