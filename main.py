from resources import binary

# Will throw errors if given more than one ASCII character - currently working on a fix


def main():
    target = get_str_value("Single character of ASCII : ")  # Get input from user
    binary_dict = binary.get(target)  # Call list of binary values
    output = target.replace(target, binary_dict)  # Replaces target value with binary
    return output


def get_str_value(prompt):  # Check if input from user is a string
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Please enter a string.")


def printer():
    print(f"Resulting binary : {main()}")


printer()
