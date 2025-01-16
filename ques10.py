import sys

if len(sys.argv) != 3:
    print("Please provide two numbers as command-line arguments.")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        result = num1 + num2

        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please provide valid numbers.")
        
#10.2
if len(sys.argv) != 2:
    print("Please provide a string as a command-line argument.")
else:
    input_string = sys.argv[1]

    string_length = len(input_string)

    print(f"The length of the string '{input_string}' is: {string_length}")