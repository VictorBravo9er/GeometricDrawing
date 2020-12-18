"""Parser Module."""
import __init__
from Parser.collect import *

class Parser:
    """Parser Class."""

    _objId:str = "id"
    _refObj:str = "reference"
    _constr:str = "construct"
    _paramLst:str = "parameterList"

    _new:str = "new"

    _type:str = "type"
    _desc:str = "description"
    _val:str = "value"

    def __init__(self) -> None:
        """Construct default configuration. Initializes components."""
        super().__init__()
        self.rules = Collector().getDS()
        self.symtab = {}

    @staticmethod
    def parse(arg):
        if "-h" == arg:
            pass
        

    def inputTokenizer(self, fileName:str):
        """Read in file and tokenizes it."""
        with open(fileName) as file:
            fileContent = file.read()
        line = 0
        fileContent = fileContent.split("\n")
        for content in fileContent:
            line += 1
            content = content.split()
            try:
                content = {
                    self._objId:content[0],
                    self._refObj:content[1],
                    self._constr:content[2],
                    self._paramLst:content[3:]
                }
            except:
                l = len(content)
                if l == 0:
                    print(
                        f"Line {line}. \tEmpty"
                    )
                    continue
                else:
                    print(
                        f"Line {line}. \tSyntaxError:",
                        f"\tExpected atleast 3 tokens, received {l}"
                    )
                continue
            yield (line, content)

    def processConstruction(self, ref:str, constr:str, param:list):
        """Deals with construction per instruction."""
        if ref == self._new:
            try:
                obj = objectADT[constr]
            except:
                raise Exception(
                    f"TypeError:\tExpected a subclass of Drawable,"+
                    f" received {constr}"
                )
            if issubclass(obj, initOrder):
                return self.newConstruction(constr, self.rules[obj][self._new], param)
            raise Exception(
                f"TypeError:\tExpected a subclass of Drawable,"+
                f" received {obj.__name__}"
            )
        try:
            obj = self.symtab[ref]
        except:
            raise Exception(
                f"ValueError:\tObject {ref} not declared before."
            )
        tp, obj = obj[self._type], obj[self._val]
        if issubclass(tp, initOrder):
            try:
                methodDict:dict = self.rules[tp][constr]
            except:
                raise Exception(
                    f"OpsError:\tOperation {tp.__name__}->{constr} not available."
                )
            return self.objectConstruction(obj, constr, methodDict, param)
        raise Exception(
            f"TypeError:\tExpected a subclass of Drawable,"+
            f" received {tp.__name__}"
        )

    def resolveParameters(self, paramList:list, forConstructor:bool=False):
        """Resolve parameters according to types."""
        paramValue = list()
        paramType  = list()
        for item in paramList:
            try:
                val = self.symtab[item][self._val ]
                tp  = self.symtab[item][self._type]
            except:
                try:
                    val = float(item)
                    tp  = float
                except:
                    raise ValueError(
                        f"ValueError:\tValue for {item}"
                        +" couldn't be resolved."
                    )
            paramType.append(tp )
            paramValue.append(val)
        if forConstructor and len(paramList) > 2:
            if   all([x == Point for x in paramType]):
                paramType = (Point,)
                paramValue= (paramValue,)
                return (paramType, paramValue)
            elif all([x == Line  for x in paramType]):
                paramType = (Line,)
                paramValue= (paramValue,)
                return (paramType, paramValue)
        return (tuple(paramType), tuple(paramValue))

    def newConstruction(self, constr:str, constructorDict:dict, param):
        """Construct brand 'new' Drawable object."""
        types, values = self.resolveParameters(param, forConstructor=True)
        try:
            target = constructorDict[types]
            print(target[args])
        except:
            raise ValueError(
                f"ValueError:\tParameter list: {param} of "+
                f"types: {types} doesn't match with any "+
                f"parameter list for construction of {constr}"
            )
        param = dict(zip(target[args], values))
        target = target[trgt]
        #print(f"{param}\n\n{target.__name__}")
        return {
            self._type   :constructorDict[ret],
            self._desc   :f"{constr} {target.__name__} with parameters"+
                    " {values}",
            self._val    :target(**param)
        }

    def objectConstruction(self, ref, constr, methodDict:dict, param):
        """Construct object from existing Drawable object or perform some computation."""
        types, values = self.resolveParameters(param)
        try:
            target = methodDict[types]
        except:
            raise ValueError(
                f"ValueError:\tParameter list: {param} of "+
                f"types: {types} doesn't match with any "+
                f"parameter list for construction of {constr}"
            )
        param = dict(zip(target[args], values))
        target = target[trgt]
        return {
            self._type   :methodDict[ret],
            self._desc   :f"{type(ref).__name__} {target.__name__} with parameters"+
                    " {values}",
            self._val    :target(ref, **param)
        }

    def tokenChecker(self, fileName:str):
        """Start point of operations."""
        from re import match
        for (line, instruction) in self.inputTokenizer(fileName):
            _id:str = instruction[self._objId]
            if match('^[A-Za-z_]\w*$', _id) == None:
                print(
                    f"Line {line}. \tIDError:",
                    "\tIdentifier doesn't follow naming convension."
                )
            if _id in self.symtab:
                print(
                    f"Line {line}. \tObject exists with same id.",
                    "Can't proceed without overwriting.",
                    "Skipping"
                )
                continue
            try:
                self.symtab[_id] = self.processConstruction(
                    instruction[self._refObj  ],
                    instruction[self._constr  ],
                    instruction[self._paramLst]
                )
            except Exception as e:
                print(
                    f"Line {line}. \t",
                    e.args[0]
                )

    def draw(self):
        """Stage DS to be drawable under Drawable library specification."""
        draw = []
        for x in self.symtab.values():
            if issubclass(x[self._type], Drawable):
                draw.append(x[self._val])
                continue
            draw.append((x[self._desc], x[self._val]))
        Drawable.draw(draw)

if __name__ == "__main__":
    # a = processConstruction(_new, "point", ["12", "0.9"])
    from sys import argv
    p = Parser()
    p.tokenChecker(argv[1])
    p.draw()

