"""App."""
import __init__
from Parser.parse import Parser
from Parser.Preprocessing_Parsing import parseNaturalInput as pni
import streamlit as st


@st.cache(persist=True, allow_output_mutation=True)
def getParser():
    """Get Parser."""
    return Parser()


inStr, inLst = ..., ...
options = ("Plain text", "Geometry script")
parser = getParser()


def process(inpLst=..., inpStr=...):
    """Process input text and return results."""
    parser.initParse(
        inputList=inpLst, inputString=inpStr,
        _printErrors=False
    )
    _, figure = parser.draw(_store=False)
    return (
        figure,
        "\n".join(parser.print()),
        "\n".join(parser.errorLog)
    )


st.title("App")
inp = st.text_area("InputText", "Enter here")
i = options.index(st.radio("Input Type", options=options))
_print = st.checkbox("Print objects")
_error = st.checkbox("Print Errors")
try:
    if st.button("Go"):
        if i == 0:
            inLst = pni(text=inp)
        if i == 1:
            inStr = inp
        fig, printLog, errLog = process(inpLst=inLst, inpStr=inStr)
        st.pyplot(fig)
        if _print:
            st.text(f"Objects:\n{printLog}")
        if _error:
            st.text(f"Errors:\n{errLog}")
except Exception as e:
    errors = "\n".join(e.args)
    st.write(f"Error:\t{errors}")
