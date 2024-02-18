from latex2sympy2 import latex2sympy, latex2latex
from sympy import *
import llm_bridge


def evaluate(tmp):
    latex = tmp.replace('\x0c','\\f')
    latex = llm_bridge.get_response("gpt-4", llm_bridge.build_prompt_correct(latex))
    print(latex)
    return(latex2sympy(latex).doit())

