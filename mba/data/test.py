fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()

inp = inp.upper()
print(inp.rstrip())
