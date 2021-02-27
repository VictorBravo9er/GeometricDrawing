"""App."""
import __init__
from figures.base import base
from Drawables.Drawable import Drawable as dw
import streamlit as st

@st.cache(persist=True, allow_output_mutation=True)
def getParser(input:int):
    """Get Parser."""
    return base.modify(input)

st.title("Number")
inp: int = st.number_input("Input a Number", min_value=0, max_value=(1<<53-1), value=0, step=1)


if st.button("Go"):
    items = base.modify(inp)
    a = st.pyplot(dw.draw(items, _show=False), clear_figure=False)
    