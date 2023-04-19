from manim import *

class Node(Mobject):
    def __init__(self):
        super().__init__()
        self.circle = Circle(radius=1)
        self.add(self.circle)
        
    def ColorNode(self, color, label_text:str = ''):
        def color_circle(circle):
            circle.set_fill(color, opacity=1)
            circle.set_stroke(color, opacity=1)
            return circle
        
        label = Text(label_text)
        label.move_to(self.circle)
        #self.circle.add(label)
        return AnimationGroup(ApplyFunction(color_circle, self.circle),
                              Write(label))
        

class Test(Scene):
    def construct(self):
        self.nodes = []
        for i in range(5):
            self.nodes.append(Node())
            self.nodes[-1].move_to([i*2, 0, 0])
      
        self.play(*[FadeIn(node) for node in self.nodes])
        anim_group = []
        for i in range(5):
            anim_group.append(self.nodes[i].ColorNode(RED, str(i)))
        
        self.play(Succession(*anim_group, lag_ratio=2, run_time=4))
        