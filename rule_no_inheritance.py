
from Parser.parse import Parser, Collector

rules = Collector(inheritance=False).getDS()
with open("rule_no_inheritance.txt", "w") as file:
    file.write(Parser.help(rules=rules))
