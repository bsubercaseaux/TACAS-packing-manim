from manim import *
from manim_slides import Slide 
import config 
import numpy as np

def to_3d(x, y):
    return np.array([x, y, 0])

class Grid(Mobject):
    def __init__(self, m, n, scale=0.2, node_constructor=Circle):
        super().__init__()
        
        self.nodes = {}
        self.edges = {}
        vdirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if node_constructor is Circle:
                    node_object = node_constructor(radius=scale, color=PINK).move_to(to_3d(4*i*scale, 4*j*scale))
                    for vdir in vdirs:
                        vi, vj = i + vdir[0], j + vdir[1]
                        if min(vi, vj) >= 0 and vi < m and vj < n:
                            edge_object = Line(to_3d(4*i*scale, 4*j*scale), to_3d(4*vi*scale, 4*vj*scale), buff=scale)
                            self.edges[((i, j), (vi, vj))] = edge_object
                            self.add(edge_object)
                elif node_constructor is Square:
                    node_object = node_constructor(side_length=scale, color=PINK).move_to([to_3d(i*scale, j*scale)])
                self.nodes[(i, j)] = node_object
                self.add(self.nodes[(i, j)])

#        self.add(Circle(radius=1).move_to([0,0,0]))
 #       self.add(Square(side_length=2).move_to([0,0,0]))
        

class Diamond(Mobject):
    def __init__(self, r, scale=0.2, node_constructor=Circle):
        super().__init__()

        self.nodes = {}
        self.edges = {}
        vdirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(-r, r+1):
            for j in range(-r, r+1):
                if abs(i) + abs(j) <= r:
                    if node_constructor is Circle:
                        node_object = node_constructor(radius=scale, color=PINK).move_to(to_3d(4*i*scale, 4*j*scale))
                        for vdir in vdirs:
                            vi, vj = i + vdir[0], j + vdir[1]
                            if abs(vi) + abs(vj) <= r:
                                edge_object = Line(to_3d(4*i*scale, 4*j*scale), to_3d(4*vi*scale, 4*vj*scale), buff=scale)
                                self.edges[((i, j), (vi, vj))] = edge_object
                                self.add(edge_object)
                    elif node_constructor is Square:
                        node_object = node_constructor(side_length=scale, color=PINK).move_to(to_3d(i*scale, j*scale))
                    self.nodes[(i, j)] = node_object
                    self.add(self.nodes[(i, j)])

class Subgraphs(Slide):
    def construct(self):
        
        title = Text("Finite Subgraphs for Lower Bounds", color=YELLOW).scale_to_fit_width(11)
        title.to_edge(UP)
        self.play(Write(title))

        self.next_slide()
        
        # self.next_slide()

        g_66 = Grid(6, 6, scale=0.25).scale(0.5).next_to(title, DOWN, buff=LARGE_BUFF)
        g_94 = Grid(9, 4, scale=0.25).scale(0.5).next_to(g_66, RIGHT, buff=1.0)
        d_4 = Diamond(4, scale=0.25).scale(0.5).next_to(g_66, LEFT, buff=1.0)

        # self.play(FadeIn(g_66), FadeIn(g_94), FadeIn(d_4))
        self.play(FadeIn(g_66))

        s_g_66 = Grid(6, 6, scale=1, node_constructor=Square).scale(0.5).next_to(title, DOWN, buff=LARGE_BUFF)
        s_g_94 = Grid(9, 4, scale=1, node_constructor=Square).scale(0.5).next_to(s_g_66, RIGHT, buff=1.0)
        s_d_4 = Diamond(4, scale=1, node_constructor=Square).scale(0.5).next_to(s_g_66, LEFT, buff=1.0)

        self.next_slide()
        # self.play(TransformFromCopy(g_66, s_g_66),
                  # TransformFromCopy(g_94, s_g_94),
                  # TransformFromCopy(d_4, s_d_4))
        self.play(Transform(g_66, s_g_66, run_time=1))

        self.next_slide()

