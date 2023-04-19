from manim import *
from manim.constants import *

font = 'Palatino'
Text.set_default(font=font)

tex_template = TexTemplate()
tex_template.add_to_preamble(r"""\usepackage{booktabs}
                             \usepackage[dvipsnames]{xcolor}
                             \usepackage{amsmath}
                             \usepackage{amssymb}
                             \usepackage{mathtools}
                             \usepackage{newpxmath}
                             \usepackage{newpxtext}
                             \newcommand{\ptime}{\textrm{PTIME}}
                             \newcommand{\np}{\textrm{NP}}
                             \newcommand{\shp}{\textrm{\#P}}
                             \newcommand{\complete}{\text{complete}}""")

Tex.set_default(tex_template=tex_template)
MathTex.set_default(tex_template=tex_template)

MY_COLORS = {
    0: BLACK,
    1: PINK,
    2: GREEN_C,
    3: BLUE,
    4: GOLD_E,
    5: ORANGE,
    6: YELLOW_B,
    7: MAROON_A,
    8: GREEN_A,
    9: TEAL_E,
    10: MAROON_E,
    11: BLUE_A,
}



