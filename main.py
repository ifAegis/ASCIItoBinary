from resources import binary


def main():
    target = check_value("Input ASCII : ")  # Get input from user
    output = ""
    for x in target:  # Loop over target
        if x in binary:  # Check if value from target is in the binary dictionary
            binary_dict = binary.get(x)
            output += binary_dict + " "  # Append loop to output
        else:
            print("Error, please enter only non-special characters.")
            continue
    return output


def check_value(prompt):  # Check if input from user is a string
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Please enter a string.")


def printer():
    print(f"Resulting binary : {main()}")


printer()
