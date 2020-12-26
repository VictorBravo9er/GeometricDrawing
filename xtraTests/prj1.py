import __init__
from Parser.parse import Parser

d = Parser.parse("inp4.file", _show=False, _error=True)

print("\n".join(d[Parser._printObject]))
print()
print("\n".join(d[Parser._printError]))

