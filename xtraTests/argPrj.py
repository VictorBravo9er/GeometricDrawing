from matplotlib import pyplot as plt
import __init__
from sys import argv
from Parser.parse import Parser
from Parser.Preprocessing_Parsing import parseNaturalInput as pni

with open(argv[1]) as file:
    a = file.read()
    Parser.parse(inputString=a, _show=False, _store=True, _error=True)
    # plt.show()
#help(plt.savefig)