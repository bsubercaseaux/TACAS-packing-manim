from manim import *
from manim_slides import Slide 
import config 
import numpy as np

def to_3d(x, y):
    return np.array([x, y, 0])

class Grid(Mobject):
    def __init__(self, m, n, scale=0.2, node_constructor=Circle, infinite_rows=False, infinite_columns=False, color=PINK):
        super().__init__()
        
        self.nodes = {}
        self.edges = {}
        self.labels = {}
        vdirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.m = m
        self.n = n
        for i in range(m):
            for j in range(n):
                if node_constructor is Circle:
                    node_object = node_constructor(radius=scale, color=color).move_to(to_3d(4*j*scale, 4*i*scale))
                    for vdir in vdirs:
                        vi, vj = i + vdir[0], j + vdir[1]
                        if min(vi, vj) >= 0 and vi < m and vj < n:
                            edge_object = Line(to_3d(4*j*scale, 4*i*scale), to_3d(4*vj*scale, 4*vi*scale), buff=scale)
                            self.edges[((i, j), (vi, vj))] = edge_object
                            self.add(edge_object)
                        if infinite_rows and (vi == m or vi == -1):
                            edge_object = DashedLine(to_3d(4*j*scale, 4*i*scale), to_3d(4*vj*scale, 4*vi*scale), buff=scale)
                            self.edges[((i, j), (vi, vj))] = edge_object
                            self.add(edge_object)
                        if infinite_columns and (vj == n or vj == -1):
                            edge_object = DashedLine(to_3d(4*j*scale, 4*i*scale), to_3d(4*vj*scale, 4*vi*scale), buff=scale)
                            self.edges[((i, j), (vi, vj))] = edge_object
                            self.add(edge_object)
                elif node_constructor is Square:
                    node_object = node_constructor(side_length=scale, color=color).move_to([to_3d(j*scale, i*scale)])
                self.nodes[(i, j)] = node_object
                self.add(self.nodes[(i, j)])
        
    def ColorNode(self, i, j, color_number, label_text=None):
        color = config.MY_COLORS[color_number]
        label = None
        if label_text is None:
            label = Tex(str(color_number)).move_to(self.nodes[(i, j)])
        else:
            label = Text(label_text, font_size=36, color=BLACK,  weight=HEAVY).move_to(self.nodes[(i, j)])
        def color_node(node):
            node.set_fill(color, opacity=1 if label_text != ' ' else 0.25)
            node.set_stroke_opacity(1 if label_text is None else 0.75)
            return node
        self.labels[(i, j)] = label
        return  AnimationGroup(ApplyFunction(color_node, self.nodes[(i, j)]),
                              Write(label))


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
                        node_object = node_constructor(radius=scale, color=PINK).move_to(to_3d(4*j*scale, 4*i*scale))
                        for vdir in vdirs:
                            vi, vj = i + vdir[0], j + vdir[1]
                            if abs(vi) + abs(vj) <= r:
                                edge_object = Line(to_3d(4*j*scale, 4*i*scale), to_3d(4*vj*scale, 4*vi*scale), buff=scale)
                                self.edges[((i, j), (vi, vj))] = edge_object
                                self.add(edge_object)
                    elif node_constructor is Square:
                        node_object = node_constructor(side_length=scale, color=PINK).move_to(to_3d(j*scale, i*scale))
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
        g_94 = Grid(9, 4, scale=0.25).scale(0.5).next_to(g_66, LEFT, buff=LARGE_BUFF)
        d_4 = Diamond(4, scale=0.25).scale(0.5).next_to(g_66, RIGHT, buff=LARGE_BUFF)

        caption_66 = Tex(r"$6 \times 6$", " grid").set_color_by_tex("6", YELLOW).next_to(g_66, DOWN, buff=MED_SMALL_BUFF)    
        caption_94 = Tex(r"$9 \times 4$", " grid").set_color_by_tex("9", YELLOW).next_to(g_94, DOWN, buff=MED_SMALL_BUFF)    
        caption_d4 = Tex(r"$D_4$", " diamond").set_color_by_tex("D", YELLOW).next_to(d_4, DOWN, buff=MED_SMALL_BUFF)    
        
        self.play(FadeIn(g_66), Write(caption_66))
        self.next_slide()
        self.play(FadeIn(g_94), Write(caption_94))
        self.next_slide()
        self.play(FadeIn(d_4), Write(caption_d4))

        s_g_66 = Grid(6, 6, scale=1, node_constructor=Square).scale(0.5).next_to(title, DOWN, buff=LARGE_BUFF)
        s_g_94 = Grid(9, 4, scale=1, node_constructor=Square).scale(0.5).next_to(s_g_66, LEFT, buff=MED_LARGE_BUFF)
        s_d_4 = Diamond(4, scale=1, node_constructor=Square).scale(0.5).next_to(s_g_66, RIGHT, buff=MED_LARGE_BUFF)

        self.next_slide()
        self.play(Transform(g_66, s_g_66, run_time=1),
                  Transform(g_94, s_g_94, run_time=1),
                  Transform(d_4, s_d_4, run_time=1),
                  caption_66.animate.shift(0.5*DOWN),
                  caption_94.animate.shift(0.5*DOWN),
                  caption_d4.animate.shift(0.5*DOWN))

        self.next_slide()

