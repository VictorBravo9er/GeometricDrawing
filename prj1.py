from Drawables.Drawable import Drawable
import __init__
from Parser.parse import Parser


d = Parser.parse("inp.file", _show=True)

print("\n".join(d[Parser._printObject]))
print()
# print("\n".join(d[Parser._printError]))

