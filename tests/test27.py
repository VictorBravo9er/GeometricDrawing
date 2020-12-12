import __init__
from Drawables.Drawable import Drawable
from Drawables.Point import Point
from Drawables.Arc import  Arc

drawables = []

p1 = Point.fromCoOrdinates(0,0)
drawables.append(p1)
p2 = Point.fromCoOrdinates(0,2)
drawables.append(p2)
p3 = Point.fromCoOrdinates(0,1.5)
drawables.append(p3)
c = Arc.formArc(centre=p1, radius=3, startAngle=2, endAngle=0)
drawables.append(c)
c = Arc.formArc(centre=p1, radius=1, startAngle=0, endAngle=2)
drawables.append(c)
c = Arc.formArc(centre=p1, point=p2, angle=2)
drawables.append(c)
c = Arc.formArc(centre=p1, point=p3, angle=-1)
drawables.append(c)



Drawable.draw(drawables)

