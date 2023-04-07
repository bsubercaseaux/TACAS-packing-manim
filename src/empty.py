from manim import *

class EmptyAnimation(Animation):
    def __init__(self, **kwargs):
        super().__init__(Mobject(), **kwargs)
    
    def interpolate(self, alpha):
        pass
