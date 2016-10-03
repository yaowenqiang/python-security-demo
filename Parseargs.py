import argparse
parser = argparse.ArgumentParser(description="This is our description")
parser.add_argument('-i',type=str,help="This is the help you get to describe the parameter",required=True)
parser.add_argument('-o',type=str,help="This is Optional",required=False)

# cmdargs ends up being a dictionary/hash

cmdargs = parser.parse_args()

# access the parameter based on the flag

ivar = cmdargs.i
ovar = cmdargs.o
print(ivar)
print(ovar)
