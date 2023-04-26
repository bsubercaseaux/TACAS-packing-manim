from manim import *
        
class Test(Scene):
    def construct(self):
        self.nodes = []
        for i in range(6):
            self.nodes.append(Square(side_length=1, stroke_width=i*3))

        group = VGroup(*self.nodes).arrange(RIGHT, buff=1)
        for node in self.nodes:
            self.play(FadeIn(node))
        
        for node in self.nodes:
            print(node.get_height())
            
        center = self.nodes[0].get_center()
        last_center = self.nodes[-1].get_center()
        l = Line(start=(center + UP*0.5), end=(last_center+UP*0.5), color=RED)
        l2 = Line(start=(center + DOWN*0.5), end=(last_center+ DOWN*0.5), color=RED)
        
        self.play(Create(l), Create(l2))
        self.wait()
    

        