
from Parser.parse import Parser

with open("rule.txt", "w") as file:
    file.write(Parser.help())
