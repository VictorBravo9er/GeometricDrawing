import __init__

from Parser.parse import Parser, Collector

with open("rule_no_inheritance.txt", "w") as file:
    file.write(Parser.help())
