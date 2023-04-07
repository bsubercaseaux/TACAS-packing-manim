from manim import *

font = 'Palatino'
Text.set_default(font=font)

tex_template = TexTemplate()
tex_template.add_to_preamble(r"""\usepackage{booktabs}
                             \usepackage[dvipsnames]{xcolor}
                             \usepackage{amsmath}
                             \usepackage{mathtools}
                             \usepackage{newpxmath}
                             \usepackage{newpxtext}
                             \newcommand{\ptime}{\textrm{PTIME}}
                             \newcommand{\np}{\textrm{NP}}
                             \newcommand{\shp}{\textrm{\#P}}
                             \newcommand{\complete}{\text{complete}}""")

Tex.set_default(tex_template=tex_template)
MathTex.set_default(tex_template=tex_template)



