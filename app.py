import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")

    # Add positional arguments for the operation and the numbers
    parser.add_argument("operation", choices=["add", "subtract"], help="Operation to perform: add or subtract")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    # Parse the arguments
    args = parser.parse_args()

    # Perform the appropriate calculation
    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "subtract":
        result = subtract(args.num1, args.num2)

    # Print the result using format()
    print("The result is: {}".format(result))
