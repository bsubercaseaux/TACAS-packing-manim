from manim import *
from manim_slides import Slide
from subgraphs import Diamond
import numpy as np
import config

class SymmetryBreaking(Slide):
    def construct(self):
        title = Text("Symmetry Breaking", color=YELLOW, font_size=72)
        title.to_edge(UP)
        d_6 = Diamond(6, scale=0.4, node_constructor=Square, color=WHITE).next_to(title, DOWN, buff=LARGE_BUFF)
        
        self.play(FadeIn(title), FadeIn(d_6))
        self.next_slide()

        arrows = [Arrow(start=d_6.get_center()+3.2*DOWN, end=d_6.get_center()+3.5*UP, color=BLUE),
                Arrow(start=d_6.get_center()+3.2*LEFT, end=d_6.get_center()+3.5*RIGHT, color=BLUE), 
                Arrow(start=d_6.get_center()+1.8*DOWN+1.8*LEFT, end=d_6.get_center()+2*UP+2*RIGHT, color=BLUE)]
                
        d_6_arrows = VGroup(d_6, *arrows)
        
        rotation_axes = [[0, 1, 0], [1, 0, 0], [1, 1, 0]]
        
        for i, arrow in enumerate(arrows):
            self.play(FadeIn(arrow))
            self.next_slide()
            self.play(Rotate(d_6, axis=rotation_axes[i]))
            self.next_slide()
        
        
        eightfold_symmetry = Tex(r"$D_r$ has an inherent ",r"$\times 8$", r"-symmetry!", font_size=36)
        eightfold_symmetry.set_color_by_tex("8", PINK)
        eightfold_symmetry.next_to(d_6_arrows, RIGHT)
        eightfold_symmetry.shift(3.5*LEFT+2*UP)
        
        
        self.play(d_6_arrows.animate.shift(3.5*LEFT), Write(eightfold_symmetry))
        
        d_6_plus =  Diamond(6, scale=0.4, node_constructor=Square, color=WHITE).next_to(title, DOWN, buff=MED_LARGE_BUFF)
        
        plus_centers = [(0, 0), (1, -2), (-2, -1), (2, 1), (-1, 2), (-1, -3), (1, 3), (3, -1), (-3, 1), (0, 5), (0, -5), (5, 0), (-5, 0)]
        vdirs = [(0,0), (-1, 0), (1, 0), (0, 1), (0, -1)]
        for i, cell in enumerate(plus_centers):
            for vdir in vdirs:
                ncell = (cell[0] + vdir[0], cell[1] + vdir[1])
                d_6_plus.nodes[ncell].set_fill(config.MY_COLORS[i+2], opacity=0.85)
                d_6_plus.nodes[ncell].set_stroke(WHITE, opacity=1, width=4)
                
        d_6_plus.move_to(d_6)
        
        self.next_slide()
        self.play(Transform(d_6, d_6_plus))
        
        self.next_slide()
        
        plus_no_longer = Tex(r"But the Plus encoding only has a ",r"$\times 4$", r"-symmetry \frownie", font_size=36)
        plus_no_longer.set_color_by_tex("4", RED)
        plus_no_longer.next_to(eightfold_symmetry, DOWN, buff=MED_SMALL_BUFF)
        
        self.play(arrows[2].animate.set_color(RED), Write(plus_no_longer))
        self.next_slide()
        
        solution = Tex(r"Therefore we need to break symmetry\\", r"before", r" re-encoding uses Pluses!", color=YELLOW, font_size=36)
        solution.set_color_by_tex("before", PINK)
        solution.next_to(plus_no_longer, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(solution))
        self.next_slide()
        
        encode = Text("How do we encode this symmetry breaking?", font_size=36)
        encode.next_to(title, DOWN, buff=MED_SMALL_BUFF)
        
        self.play(FadeOut(solution), FadeOut(plus_no_longer), FadeOut(eightfold_symmetry), FadeOut(d_6_arrows), FadeOut(d_6),
                FadeIn(encode))
        
        
        
        d_6 = Diamond(6, scale=0.4, node_constructor=Square, color=WHITE).next_to(encode, DOWN, buff=MED_SMALL_BUFF)
        for i in range(-5, 6):
            for j in range(-5, 6):
                if abs(i) + abs(j) <= 5:
                    d_6.nodes[(i, j)].set_fill(config.MY_COLORS[1], opacity=0.65)
        d_6.shift(3*LEFT)
        
        d_6.colorNode(3, 1, 10)
                    
        observation = Tex(r"Observation: ", r"in any sub-$D_5$\\ there can be at most one $10$!", font_size=36)
        observation.set_color_by_tex("Observation", YELLOW)
        observation.next_to(d_6, RIGHT, buff=MED_LARGE_BUFF)
        observation.shift(2*UP + 1*RIGHT)
        
        self.next_slide()
        self.play(FadeIn(d_6), Write(observation))
        
        force = Tex(r"Therefore we can enforce that:\\", r"if a 10 appears in the central sub-$D_5$,\\", "at position $(a, b)$, then ", r"$a \geq 0 \land b \geq a$", font_size=36)
        force.set_color_by_tex(r"a \geq 0", GREEN)
        
        force.next_to(observation, DOWN, buff=MED_LARGE_BUFF)
        
        self.next_slide()
        
        
        for i in range(-6, 7):
            for j in range(-6, 7):
                if abs(i) + abs(j) <= 5:
                    if j >= 0 and i >= j:
                        if i == 3 and j == 1: continue
                        d_6.nodes[(i, j)].set_fill(config.MY_COLORS[2], opacity=0.65)
                        
        self.play(Write(force))
        
        we_do_this = Tex(r"We do this by adding ", r"negative units\\", r"for color 10 in the remaining positions \smiley", font_size=36)
        we_do_this.set_color_by_tex("negative units", RED)
        
        
                        
        we_do_this.next_to(force, DOWN, buff=1.3*MED_SMALL_BUFF)
        self.next_slide()
        self.play(FadeIn(we_do_this))
        
        if_no_ten = Tex(r"If no 10s in the central sub-$D_5$, then\\", r"break symmetry on the", r" 9s ",  r"in the sub-$D_4$,\\ and so on...", font_size=36)
        if_no_ten.set_color_by_tex("9s", PINK)
        if_no_ten.next_to(we_do_this, DOWN, buff=1.3*MED_SMALL_BUFF)
        
        self.next_slide()
        self.play(FadeIn(if_no_ten))
        
        self.next_slide()