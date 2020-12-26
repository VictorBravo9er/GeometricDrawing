from Drawables.Drawable import Drawable
import __init__
from Parser.parse import Parser

d = Parser.parse("inp3.file", _show=False, _error=False)

print("\n".join(d[Parser._printObject]))
print()
print("\n".join(d[Parser._printError]))

