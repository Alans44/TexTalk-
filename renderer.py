import matplotlib.pyplot as plt
from PIL import Image
from pdf2image import convert_from_path

import numpy as np
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os



def format_str(input_str):
    result = ""
    for char in input_str:
        if char == '\\':
            result += '\\\\'
        else:
            result += char
    return result

def render(formula, path="resources/result.png"):
    fig = plt.figure()
    plt.axis("off")
    #formula = format_str(formula)
    plt.text(0.5, 0.5, f"${formula}$", size=50, ha="center", va="center")

    pdf_path = "resources/.result.pdf"
    png_path = path

    plt.savefig(pdf_path, format="pdf", bbox_inches="tight", pad_inches=0.4)
    plt.close(fig)

    images = convert_from_path(pdf_path)
    images[0].save(png_path, "PNG")

    return png_path

if __name__ == "__main__":
    latex_formula = r"\int_{0}^{2} 3x \, dx"
    render(latex_formula)


