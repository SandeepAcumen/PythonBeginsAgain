import argparse

parser = argparse.ArgumentParser(description="Simple calculation")

parser.add_argument("num1",type=float,help="first number")
parser.add_argument("num2",type=float,help="Second number")
parser.add_argument("Operation",choices=["add","sub","div","mul"],help="Operation to perform")

args = parser.parse_args()

print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")

if(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")

if(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")

if(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")

else:
    print("Some error occured")

