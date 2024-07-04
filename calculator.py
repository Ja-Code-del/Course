#greet
print("Welcome")
#ask for first number
number_one = float(input("first number"))
#ask for operator
operator = input("operator : ")
#ask for second
number_two = float(input("second number"))
#print the result
result = 0.0
if operator == "+":
    result = number_one + number_two
elif operator == "x":
    result = number_one * number_two
elif operator == "/":
    result = number_one / number_two
elif operator == "-":
    result = number_one - number_two
else:
    print("operator not taken in charge")

print(f"{number_one} {operator} {number_two} = {result}")