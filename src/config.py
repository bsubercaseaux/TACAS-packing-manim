from manim import *
from manim.constants import *

font = 'Palatino'
Text.set_default(font=font)

tex_template = TexTemplate()
tex_template.add_to_preamble(r"""\usepackage{booktabs}
                             \usepackage[dvipsnames]{xcolor}
                             \usepackage{amsmath}
                             \usepackage{soul}
                             \usepackage{amssymb}
                             \usepackage{wasysym}
                             \usepackage{booktabs}
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
    1: PURPLE_E,
    2: GREEN_D,
    3: BLUE_E,
    4: GOLD_E,
    5: MAROON_E,
    6: YELLOW_D,
    7: MAROON_A,
    8: GREEN_B,
    9: TEAL_E,
    10: RED_E,
    11: BLUE_A,
    12: BLUE,
    13: GRAY,
    14: ORANGE,
    15: GREEN_E
}



