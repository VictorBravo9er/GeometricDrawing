import __init__

with open("input.txt") as file:
    inp = file.read()
print(inp)

from Parser.Preprocessing_Parsing import parseNaturalInput as pni

inter_rep = pni(text=inp)
for inst in inter_rep:
    print(inst)


from Parser.parse import Parser

data = Parser.parse(inputList=inter_rep, _show=True, _error=True)
print(data[Parser._printObject])
print(data[Parser._printError])