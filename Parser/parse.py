"""Parser Module."""
from rules.collect import *

sytab = {}
_id:str = "id"
_ref:str = "reference"
_const:str = "construct"
_param:str = "parameterList"

rules = Collector().getDS()


def tokenizer(fileName:str):
    """Read in file and tokenizes it."""
    with open(fileName) as file:
        fileContent = file.read()
    line = 0
    fileContent = fileContent.split(";")
    for content in fileContent:
        line += 1
        content = content.split()
        try:
            content = {
                _id:content[0],
                _ref:content[1],
                _const:content[2],
                _param:content[3:]
            }
        except:
            print(
                f"SyntaxError: line {line}.",
                f"Expected atleast 3 tokens, received {len(content)}"
            )
            continue
        yield (line, content)

def processConstruction(ref:str, const:str, param:str):
    pass

def newConstruction():
    pass

def tokenChecker(fileName:str):
    dst = {}
    for (line, instruction) in tokenizer(fileName):
        if instruction[_id] in dst:
            print(
                f"Object exists with same id in line {line}.",
                "Can't proceed without overwriting.",
                "Skipping"
            )
            continue
        try:
            dst[instruction[_id]] = processConstruction(
                instruction[_ref], instruction[_const],
                instruction[_param]
            )
        except Exception as e:
            print(
                f"Line {line}.",
                e.args[0]
            )
    return dst
