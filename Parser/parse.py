"""Parser Module."""
import __init__
from Parser.collect import *
from math import degrees, radians


class Parser:
    """Parser Class."""

    _objId:int = 0
    _callerObj:int = 1
    _constr:int = 2
    _paramLst:int = 3

    _new:str = "new"

    _printError:str = "errorLog"
    _printObject:str="printDesc"
    _subplots:str="subplot"

    _desc:str = "description"
    _val:str = "value"

    _idLexicon:str = "^[A-Za-z_]\\w*$"
    def __init__(self) -> None:
        """Construct default configuration. Initializes components."""
        super().__init__()
        self.rules = Collector().getDS()
        self.symtab = {}
        self.errorLog = []

    @staticmethod
    def help(rules:dict=..., _print:bool=True):
        """Provide documentation of Library."""
        _tab = " " * 4
        var = []
        if not isinstance(rules, dict):
            rules = Collector().getDS()
        for obj, content in rules.items():
            var.append(f"Drawable: {obj.__name__}")
            for ops, content in content.items():
                try:
                    if ops == Parser._new:
                        ops = "Constructor"
                    var.append(
                        f"\n{_tab}{ops}\n{_tab * 2}returns -> {content[retVal].__name__}"
                    )
                except:
                    print(obj)
                    print(ops)
                    print(content)
                for argTypes, content in content.items():
                    if argTypes == retVal:
                        continue
                    target   = content[trgt]
                    argList  = content[args]
                    try:
                        if len(argList) == 0:
                            argTypes = (
                                f"{_tab * 3}Expected args{_tab}: None"
                            )
                        else:
                            argTypes = (
                                f"{_tab * 3}Expected args{_tab}: "+", ".join(argList)+
                                f"\n{_tab * 3}Of Types     {_tab}: "+
                                " , ".join([x.__name__ for x in argTypes])+"."
                            )
                    except:
                        print(obj.__name__)
                        print(ops)
                        print(target.__name__)
                        print(argList)
                        print(argTypes)
                    var.append(
                        f"{_tab * 2}{target.__doc__}\n"+
                        argTypes
                    )
            var.append("\n")
        printable = "\n".join(var)
        if _print:
            print(printable)
        return printable

    @staticmethod
    def parse(
        fileName:str=..., inputList:list=...,
        inputString:str=...,
        _show:bool=False, _store:bool=True,
        _storageName:str="./data/store",
        _print:bool=False, _error:bool=False
    ):
        """Standalone parsing Operation. Returns Descrpition."""
        ops = Parser()
        ops.initParse(
            fileName=fileName, inputList=inputList,
            inputString=inputString, _printErrors=_error
        )
        ops.draw(_show, _store, _storageName, _print)
        return {
            Parser._printObject:ops.print(_print),
            Parser._printError:ops.errorLog
        }

    @staticmethod
    def angleConversion(paramDict):
        """Convert Degrees to radians."""
        for key in paramDict:
            if "angle" in key:
                paramDict[key] = radians(paramDict[key])

    def inputTokenizer(
        self, fileName:str=..., inputList:list=...,
        inputString:str=..., _error:bool=False
    ):
        """Read in file and tokenizes it."""
        fileContent = ...
        if isinstance(inputList, list):
            fileContent = inputList
        elif isinstance(inputString, str):
            fileContent = inputString.split("\n")
        elif isinstance(fileName, str):
            with open(fileName) as file:
                fileContent = file.read()
                fileContent = fileContent.split("\n")
        else:
            raise ValueError(
                "No acceptable input received."
            )
        line = 0
        for content in fileContent:
            line += 1
            if isinstance(content, str):
                content = content.split()
            try:
                content = {
                    self._objId:content[0],
                    self._callerObj:content[1],
                    self._constr:content[2],
                    self._paramLst:content[3:]
                }
            except:
                l = len(content)
                if not _error:
                    continue
                if l == 0:
                    print(
                        f"Line {line}. \tEmpty"
                    )
                else:
                    print(
                        f"Line {line}. \tSyntaxError:",
                        f"\tExpected atleast 3 tokens, received {l}"
                    )
                continue
            yield (line, content)

    def processConstruction(
        self, _ref:str, _constr:str, _id:str, _param:list
    ):
        """Deals with construction per instruction."""
        if _ref == self._new:
            try:
                obj = objectADT[_constr]
            except:
                raise Exception(
                    f"TypeError:\tExpected a subclass of Drawable,"+
                    f" received {_constr}"
                )
            if issubclass(obj, initOrder):
                return self.newConstruction(_constr, self.rules[obj][self._new],_id, _param)
            raise Exception(
                f"TypeError:\tExpected a subclass of Drawable,"+
                f" received {obj.__name__}"
            )
        try:
            obj = self.symtab[_ref][self._val]
        except:
            raise Exception(
                f"ValueError:\tObject {_ref} not declared before."
            )
        tp = type(obj)
        if issubclass(tp, initOrder):
            try:
                methodDict:dict = self.rules[tp][_constr]
            except:
                raise Exception(
                    f"OpsError:\tOperation {tp.__name__}->{_constr} not available."
                )
            return self.objectConstruction(obj, _constr, methodDict, _id, _ref, _param)
        raise Exception(
            f"TypeError:\tExpected a subclass of Drawable,"+
            f" received {tp.__name__}"
        )

    def resolveParameters(
        self, paramList:list, forConstructor:bool=False
    ):
        """Resolve parameters according to types."""
        paramValue = list()
        paramType  = list()
        for item in paramList:
            try:
                val = self.symtab[item][self._val ]
                tp  = type(val)
            except:
                try:
                    val = float(item)
                    tp  = float
                except:
                    val = item
                    tp  = str
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

    def newConstruction(
        self, constr:str, constructorDict:dict,
        _id:str, param:list
    ):
        """Construct brand 'new' Drawable object."""
        types, values = self.resolveParameters(param, forConstructor=True)
        try:
            target = constructorDict[types]
        except:
            raise ValueError(
                f"ValueError:\tParameter list: {param} of "+
                f"types: {types} doesn't match with any "+
                f"parameter list for construction of {constr}"
            )
        values = dict(zip(target[args], values))
        self.angleConversion(values)
        target = target[trgt]
        values = target(**values)
        types = type(values).__name__
        if len(param) == 0:
            constr = "no parameters"
        else:
            constr = "parameters: "+", ".join(param)
        return {
            #self._type  :types,
            self._desc  :f"{_id} is {types} using {target.__name__}"+
                         f" with {constr}",
            self._val   :values
        }

    def objectConstruction(
        self, ref, constr, methodDict:dict,
        _id:str, _refid:str, param:list
    ):
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
        values = dict(zip(target[args], values))
        self.angleConversion(values)
        target = target[trgt]
        values = target(ref, **values)
        types = type(values).__name__
        target = target.__name__
        if "angle" in constr and isinstance(values, (float, int)):
            values = degrees(values)
        if len(param) == 0:
            constr = "no parameters"
        else:
            constr = "parameters: "+", ".join(param)
        return {
            #self._type  :types,
            self._desc  :f"{_id} is {types} {target}"+
                         f" on {_refid} with {constr}",
            self._val   :values
        }

    def initParse(
        self, fileName:str=..., inputList:list=...,
        inputString:str=..., _printErrors:bool=False
    ):
        """Start point of operations."""
        self.symtab.clear()
        self.errorLog.clear()
        from re import match
        instStruct = ...
        if isinstance(inputList, list):
            instStruct = self.inputTokenizer(inputList=inputList)
        elif isinstance(inputString, str):
            instStruct = self.inputTokenizer(inputString=inputString)
        elif isinstance(fileName, str):
            instStruct = self.inputTokenizer(fileName)
        else:
            raise ValueError(
                "FATAL ERROR - No acceptable input detected."
            )
        for (line, instruction) in instStruct:
            _id:str = instruction[self._objId]
            if match(self._idLexicon, _id) == None and _printErrors:
                print(
                    f"Line {line}. \tIDError:",
                    "\tIdentifier doesn't follow naming convension."
                )
                continue
            if _id in self.symtab and _printErrors:
                print(
                    f"Line {line}. \tObject exists with same id.",
                    "Can't proceed without overwriting.",
                    "Skipping"
                )
                continue
            try:
                retStructure = self.processConstruction(
                    instruction[self._callerObj],
                    instruction[self._constr],
                    _id,
                    instruction[self._paramLst]
                )
                self.symtab[_id] = retStructure
                retStructure = retStructure[self._val]
                if isinstance(retStructure, initOrder):
                    retStructure.extendLimits()
            except Exception as e:
                error = f"Line {line}. \t{e.args[0]}"
                if _printErrors:
                    print(error)
                self.errorLog.append(error)

    def print(self, _print:bool=False):
        """Print drawable item's list."""
        drawableList = []
        for x,value in self.symtab.items():
            desc, value = value[self._desc], value[self._val]
            if issubclass(type(value), initOrder):
                drawableList.append(desc)
                if _print:
                    print(desc)
                continue
            x = f"{desc}, {x}: {round(value, 4)}"
            drawableList.append(x)
            if _print:
                print(x)
        return drawableList

    def draw(
        self, _show:bool=False, _store:bool=True,
        _storageName:str="./data/store", _print:bool=False
    ):
        """Stage DS to be drawable under Drawable library specification."""
        drawableList = []
        for x in self.symtab.values():
            desc, x = x[self._desc], x[self._val]
            if issubclass(type(x), initOrder):
                drawableList.append(x)
                continue
            drawableList.append((desc, x))
        figure = Drawable.draw(
            drawables=drawableList, _storageName=_storageName,
            _store=_store, _show=_show, _print=_print
        )
        return (drawableList, figure)
