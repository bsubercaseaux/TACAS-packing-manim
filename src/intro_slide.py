from manim import *
from manim_slides import Slide 
from subgraphs import Grid, to_3d
import config
import numpy as np
from empty import EmptyAnimation

class IntroSlide(Slide):
    def construct(self): 
        grid_for_title = Grid(5, 19, node_constructor=Square, scale=0.7, color=BLACK).center().shift(0.7*UP)
        
        authors = Text("Bernardo Subercaseaux and Marijn Heule", font_size=36).next_to(grid_for_title, DOWN, buff=MED_LARGE_BUFF)
        email = Tex(r"\texttt{bsuberca@cs.cmu.edu}", font_size=28, color=BLUE).next_to(authors, DOWN)
        self.play(FadeIn(authors), Write(email), run_time=0.8)
        self.next_slide()
        
      
        text = ["THE PACKING", "CHROMATIC NUMBER OF", " ", "THE INFINITE SQUARE", "GRID IS 15"]
        for row, line in enumerate(text):
            text[row] = line + " " * (19 - len(line))
        
        C = [
                [2, 1, 3, 1, 2, 1, 4, 1, 7, 1, 3, 1, 2, 1, 3, 1, 2, 1, 5],
                [1, 4, 1, 5, 1, 3, 1, 2, 1, 8, 1, 5, 1, 4, 1, 9, 1, 6, 1],
                [3, 1, 2, 1, 6, 1, 9, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2],
                [1, 8, 1, 7, 1, 2, 1, 5, 1, 4, 1, 6, 1, 7, 1, 5, 1, 8, 1],
                [2, 1, 3, 1, 4, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3]
            ]

        anim_group = []
        for row, line in enumerate(text):
            for i, c in enumerate(line):
                anim_group.append(grid_for_title.ColorNode(len(C)-1-row, i, C[row][i], label_text=c))
       
        self.play(FadeIn(grid_for_title), run_time=0.3)
        #print("anim_group", anim_group, *anim_group)
       
        self.play(Succession(*anim_group, lag_ratio=2, run_time=4))
        self.play(EmptyAnimation())
        self.next_slide()
        
        self.start_loop()
        self.play(Indicate(grid_for_title.nodes[(0, 8)]),
                            Indicate(grid_for_title.nodes[(0, 9)]),
                            Indicate(grid_for_title.labels[(0, 8)],color=BLUE),
                            Indicate(grid_for_title.labels[(0, 9)],color=BLUE))
        self.end_loop()
        self.play(EmptyAnimation())
        self.next_slide()
       