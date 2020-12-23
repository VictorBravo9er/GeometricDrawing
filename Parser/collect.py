"""Collect Everything."""
from io import TextIOWrapper
import __init__
from rules.drawable import *
from rules.point import pointADT
from rules.line import lineADT
from rules.arc import arcADT
from rules.circle import circleADT
from rules.polygon import polygonADT
from rules.triangle import triangleADT
from rules.quad import quadADT
from rules.parallelogram import paralleloADT
from rules.trapezoid import trapezoidADT
from rules.kite import kiteADT


class Collector:
    """Collector exists is to combine all class together."""

    def __init__(self) -> None:
        """Initialize method."""
        super().__init__()
        self.ADT = {}
        self.collect()
        self.processSuper()

    def getDS(self):
        """Provide the Data Structure constructed."""
        return self.ADT

    def processSuper(self):
        """Inherit any remaining methods from base class."""
        backRef = self.ADT
        for key, CLASS in backRef.items():
            BASE = CLASS[is_a]
            del CLASS[is_a]
            if BASE is not None:
                inheritance = [(x, y) for (x, y) in backRef[BASE].items() if x not in CLASS]
                for x, y in inheritance:
                    CLASS[x] = y

    def collect(self):
        """Collect all ADT's together."""
        self.ADT = {
            Point:pointADT,
            Line:lineADT,
            Arc:arcADT,
            Circle:circleADT,
            Polygon:polygonADT,
            Triangle:triangleADT,
            Quadrilateral:quadADT,
            Parallelogram:paralleloADT,
            Trapezoid:trapezoidADT,
            Kite:kiteADT,
            
        }

    def print(self, output:TextIOWrapper=..., toPrint:bool=False):
        """Print ADT."""
        Collector.printDST(self.ADT, output=output, toPrint=toPrint)

    @staticmethod
    def printDST(DST, gap:str="", output:TextIOWrapper=..., toPrint:bool=False):
        """Reccursive printing."""
        try:
            if not isinstance(DST, dict):
                raise Exception
            for x in DST:
                s = ""
                try:
                    s = f"{gap}{x.__name__}"
                except:
                    try:
                        s = f"{gap}("
                        for i in x:
                            s += f"{i.__name__} "
                        s += ")"
                    except:
                        s = f"{gap}{x}"
                if toPrint:
                    print(s)
                if isinstance(output, TextIOWrapper):
                    output.write(s+"\n")
                Collector.printDST(DST[x], gap+"    ", output, toPrint)
        except:
            try:
                s = f"{gap}{DST.__name__}"
            except:
                try:
                    s = f"{gap}("
                    for i in DST:
                        s += f"{i.__name__} "
                    s += ")"
                except:
                    s = f"{gap}{DST}"
            if toPrint:
                print(s)
            if isinstance(output, TextIOWrapper):
                output.write(s+"\n")
