from matplotlib import pyplot as plt
import __init__
from sys import argv
from Parser.parse import Parser
from Parser.Preprocessing_Parsing import parseNaturalInput as pni

with open(argv[1]) as file:
    a = pni(file.read())
    Parser.parse(inputList=a, _show=False, _store=False, _error=False)
    # plt.show()
#help(plt.savefig)