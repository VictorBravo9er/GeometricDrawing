from figures.base import base
from Drawables.Drawable import Drawable as dw

for i in range(100):
    if i % 10 != 0:
        continue
    a = base.modify(i)
    dw.draw(
        a, _show=False,_store=True,
        _storageName=f"./data/store{i}"
    )