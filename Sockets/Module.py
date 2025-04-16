import my_function

def main():
    my_function.message("python")

if __name__ == '__main__':
    main()

# Passing an argument using argparse in Python module argparse
import argparse

parser = argparse.ArgumentParser(description="Example")
parser.add_argument("-n", "--number", type=int, help="An integer number is needed")
args = parser.parse_args()

print("The number is:", args.number)

# ---------------------------------------------------------------------------------
# Using a Class to Store Parameters
# If we have multiple parameters, we can use a class to keep things organized.

class Parameters:
    """Store multiple parameters"""
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

def view_parameters(params):
    print("Parameter 1:", params.param1)
    print("Parameter 2:", params.param2)

# Set up argparse
parser = argparse.ArgumentParser(description="Testing Parameters")
parser.add_argument("-p1", "--param1", help="First parameter")
parser.add_argument("-p2", "--param2", help="Second parameter")

# Parse arguments
args = parser.parse_args()

# Create a Parameters object
params = Parameters(param1=args.param1, param2=args.param2)

# View the parameters
view_parameters(params)
##########################################################
#########################################################
"----------------------------------------------------------------------------\n"
# #QUESTION
# #How can we use the argparse module in Python to manage parameters for a port scanning script? The script should allow users to specify:

#     A target IP address
#     Ports to scan (default: 80,8080)
#     A verbosity level (-v, -vv, -vvv for different levels of detail)
#     An option to display only open ports (--open)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanning Tool")
    
    # Required target argument
    parser.add_argument("-target", metavar="TARGET", dest="target",
                        help="Target IP address to scan", required=True)
    
    # Optional ports argument (default: 80,8080)
    parser.add_argument("-ports", dest="ports",
                        help="Specify target ports, separated by commas",
                        default="80,8080")
    
    # Verbosity argument (-v, -vv, -vvv for different levels)
    parser.add_argument("-v", dest="verbosity", default=0, action="count",
                        help="Verbosity level: -v, -vv, -vvv")
    
    # Only show open ports flag
    parser.add_argument("--open", dest="only_open", action="store_true",
                        help="Only display open ports", default=False)

    # Parse arguments
    args = parser.parse_args()

    # Print results
    print("Target:", args.target)
    print("Verbosity:", args.verbosity)
    print("Only show open ports:", args.only_open)

    # Process port list
    portlist = args.ports.split(',')
    for port in portlist:
        print("Port:", port)
