from Drawables.Drawable import Drawable
import __init__
from matplotlib import pyplot as plt
from Parser.parse import Parser
from p import a

Parser.parse(inputList=a, _show=False, _store=True, _error=True)

#help(plt.savefig)