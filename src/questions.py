from manim import *
from manim_slides import Slide 

import config
import numpy as np
from empty import EmptyAnimation


class Questions(Slide):
    def construct(self):
        questions = Text("Questions?", color=YELLOW, font_size=72)
        self.play(FadeIn(questions))
        self.next_slide()
        
        
        
        