from manim import *
from manim_slides import Slide 
import config 
import numpy as np
from curved_edge import CurvedEdge

def to_3d(x, y):
    return np.array([x, y, 0])

class Grid(VMobject):
    def __init__(self, m, n, scale=0.2, node_constructor=Circle, infinite_rows=False, infinite_columns=False, color=WHITE, toroidal=False, stroke_width=2, assignment=None, chebyshev=False, **kwargs):
        super().__init__()
        
        self.nodes = {}
        self.edges = {}
        self.labels = {}
        vdirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if chebyshev:
            vdirs += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.m = m
        self.n = n
        for i in range(m):
            for j in range(n):
                if node_constructor is Circle:
                    node_object = node_constructor(radius=scale, color=color, stroke_width=stroke_width).move_to(to_3d(4*j*scale, 4*i*scale))
                    for vdir in vdirs:
                        vi, vj = i + vdir[0], j + vdir[1]
                        if toroidal:
                            if m > 1: vi = vi % m
                            if n > 1: vj = vj % n
                        if min(vi, vj) >= 0 and vi < m and vj < n:
                            if toroidal and ((abs(vi - i)  == m-1 and m > 1) or (abs(vj - j) == n-1 and n > 1)):
                                if vj < j: continue
                                edge_object = CurvedEdge(start=to_3d(4*j*scale, 4*i*scale), end=to_3d(4*vj*scale, 4*vi*scale), color=RED, angle=TAU/8, buff=scale)
                            else:
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
                    node_object = node_constructor(side_length=scale, color=color, stroke_width=stroke_width).move_to([to_3d(j*scale, i*scale)])
                    for vdir in vdirs:
                        vi, vj = i + vdir[0], j + vdir[1]
                        di, dj = vdir[0], vdir[1]
                        if infinite_rows and (vi == m or vi == -1):
                            edge_object = DashedLine(to_3d(j*scale + scale/2*dj, i*scale+scale/2*di), to_3d(j*scale + scale*dj, i*scale + scale*di), buff=scale)
                            self.edges[((i, j), (vi, vj))] = edge_object
                            self.add(edge_object)
                        if infinite_columns and (vj == n or vj == -1):
                            edge_object = DashedLine(to_3d(j*scale + scale/2*dj, i*scale + scale/2*di), to_3d(j*scale + scale*dj, i*scale + scale*di), buff=scale)
                            self.edges[((i, j), (vi, vj))] = edge_object
                            self.add(edge_object)
              
                self.nodes[(i, j)] = node_object
                self.add(self.nodes[(i, j)])
                if assignment is not None and (i, j) in assignment:
                    self.colorNode(i, j, assignment[(i, j)])
        
    def ColorNode(self, i, j, color_number, label_text=None, label_color=BLACK):
        color = config.MY_COLORS[color_number]
        if label_text is None:
            label = Tex(str(color_number)).move_to(self.nodes[(i, j)])
        else:
            label = Text(label_text, font_size=36, color=label_color,  weight=HEAVY).move_to(self.nodes[(i, j)])
        label.scale_to_fit_height(0.75*self.nodes[(i, j)].get_height())
        def color_node(node):
            # node.set_color(color)
            fill_opacity = 1 if label_text != ' ' else 0.35
            stroke_opacity = 1 if label_text is None else 0.35
            node.set_fill(color=color, opacity=fill_opacity)
            node.set_stroke(opacity=stroke_opacity)
            return node
     
        self.labels[(i, j)] = label
        self.nodes[(i, j)].add(label)
        return  AnimationGroup(ApplyFunction(color_node, self.nodes[(i, j)]),
                              Write(label), run_time=0.5)
                              
    def colorNode(self, i, j, color_number, label_text=None, label_color=BLACK, label_num_color=WHITE):
        color = config.MY_COLORS[color_number]
        if label_text is None:
            label = Tex(str(color_number), color=label_num_color).move_to(self.nodes[(i, j)])
        else:
            label = Text(label_text, font_size=36, color=label_color,  weight=HEAVY).move_to(self.nodes[(i, j)])
        
        node = self.nodes[(i, j)]
        
        label_scale = 0.85 if isinstance(node, Circle) else 0.6
        label.scale_to_fit_height(label_scale*self.nodes[(i, j)].get_height())
        
        
        # node.set_color(color)
        fill_opacity = 1 if label_text != ' ' else 0.35
        stroke_opacity = 1 if label_text is None else 0.35
        node.set_fill(color=color, opacity=fill_opacity)
        # node.set_stroke(opacity=stroke_opacity)
     
        self.labels[(i, j)] = label
        self.nodes[(i, j)].add(label)
        return None




class Diamond(VMobject):
    def __init__(self, r, scale=0.2, node_constructor=Circle, assignment=None, color=PINK, stroke_width=2, **kwargs):
        super().__init__()

        self.nodes = {}
        self.edges = {}
        self.labels = {}
        vdirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(-r, r+1):
            for j in range(-r, r+1):
                if abs(i) + abs(j) <= r:
                    if node_constructor is Circle:
                        node_object = node_constructor(radius=scale, color=color, stroke_width=stroke_width).move_to(to_3d(4*j*scale, 4*i*scale))
                        for vdir in vdirs:
                            vi, vj = i + vdir[0], j + vdir[1]
                            if abs(vi) + abs(vj) <= r:
                                edge_object = Line(to_3d(4*j*scale, 4*i*scale), to_3d(4*vj*scale, 4*vi*scale), buff=scale)
                                self.edges[((i, j), (vi, vj))] = edge_object
                                self.add(edge_object)
                    elif node_constructor is Square:
                        node_object = node_constructor(side_length=scale, color=color, stroke_width=stroke_width).move_to(to_3d(j*(scale+0.0), i*(scale+0.0)))
                    self.nodes[(i, j)] = node_object
                    self.add(self.nodes[(i, j)])
                    if assignment is not None and (i, j) in assignment:
                        self.colorNode(i, j, assignment[(i, j)])
                    
    def ColorNode(self, i, j, color_number, label_text=None, label_color=BLACK, label_num_color=WHITE):
        color = config.MY_COLORS[color_number]
        if label_text is None:
            label = Tex(str(color_number), color=label_num_color).move_to(self.nodes[(i, j)])
        else:
            label = Text(label_text, font_size=36, color=label_color,  weight=HEAVY).move_to(self.nodes[(i, j)])
        label.scale_to_fit_height(0.85*self.nodes[(i, j)].get_height())
        
        def color_node(node):
            # node.set_color(color)
            fill_opacity = 1 if label_text != ' ' else 0.35
            stroke_opacity = 1 if label_text is None else 0.35
            node.set_fill(color=color, opacity=fill_opacity)
            node.set_stroke(opacity=stroke_opacity)
            return node
     
        self.labels[(i, j)] = label
        self.nodes[(i, j)].add(label)
        return  AnimationGroup(ApplyFunction(color_node, self.nodes[(i, j)]),
                              Write(label), run_time=0.5)
        
    def colorNode(self, i, j, color_number, label_text=None, label_color=BLACK, label_num_color=WHITE):
        color = config.MY_COLORS[color_number]
        if label_text is None:
            label = Tex(str(color_number), color=label_num_color).move_to(self.nodes[(i, j)])
        else:
            label = Text(label_text, font_size=36, color=label_color,  weight=HEAVY).move_to(self.nodes[(i, j)])
        
        node = self.nodes[(i, j)]
        
        label_scale = 0.85 if isinstance(node, Circle) else 0.6
        label.scale_to_fit_height(label_scale*self.nodes[(i, j)].get_height())
        
        
        # node.set_color(color)
        fill_opacity = 1 if label_text != ' ' else 0.35
        stroke_opacity = 1 if label_text is None else 0.35
        node.set_fill(color=color, opacity=fill_opacity)
        # node.set_stroke(opacity=stroke_opacity)
     
        self.labels[(i, j)] = label
        self.nodes[(i, j)].add(label)
        return None

class Subgraphs(Slide):
    def construct(self):
        
        title = Tex(r"Finite subgraphs for lower bounds on ", r"$\chi_\rho(\mathbb{Z}^2)$", color=YELLOW).scale_to_fit_width(12)
        title.set_color_by_tex("chi", BLUE)
        
        title.to_edge(UP)
        self.play(Write(title))

        self.next_slide()
        
        # self.next_slide()

        
        g_14_14 = Grid(14, 14, scale=0.17, color=PINK).scale(0.25)
        g_9_15 = Grid(9, 15, scale=0.17, color=PINK).scale(0.25)
        d_14 = Diamond(14, scale=0.17).scale(0.25)
        
        g_graphs = VGroup(g_9_15, g_14_14, d_14).arrange(RIGHT, buff=1.4*LARGE_BUFF).next_to(title, DOWN, buff=MED_SMALL_BUFF)
        g_graphs.shift(0.6*RIGHT)

        caption_9_15 = Tex(r"$9 \times 15$", " grid").set_color_by_tex("9", YELLOW).next_to(g_9_15, DOWN, buff=MED_SMALL_BUFF)    
        caption_14_14 = Tex(r"$14 \times 14$", " grid").set_color_by_tex("14", YELLOW).next_to(g_14_14, DOWN, buff=MED_SMALL_BUFF)    
        caption_d14 = Tex(r"$D_{15}$", " diamond").set_color_by_tex("D", YELLOW).next_to(d_14, DOWN, buff=MED_SMALL_BUFF)    
        
        detail_9_15 = Tex(r"Ekstein et al. ", r"$\chi_\rho(\mathbb{Z}^2) \geq 12$", font_size=28).set_color_by_tex("chi", BLUE).next_to(caption_9_15, DOWN, buff=SMALL_BUFF)
        detail_14_14 = Tex(r"Martin et al. ", r"$\chi_\rho(\mathbb{Z}^2) \geq 13$", font_size=28).set_color_by_tex("chi", BLUE).next_to(caption_14_14, DOWN, buff=SMALL_BUFF)
        detail_d14 = Tex(r"This work ", r"$\chi_\rho(\mathbb{Z}^2) = 15$", font_size=28).set_color_by_tex("chi", ORANGE).next_to(caption_d14, DOWN, buff=SMALL_BUFF)
        
        
        self.play(FadeIn(g_9_15), Write(caption_9_15), Write(detail_9_15))
        self.next_slide()
        self.play(FadeIn(g_14_14), Write(caption_14_14), Write(detail_14_14))
        self.next_slide()
        self.play(FadeIn(d_14), Write(caption_d14), Write(detail_d14))

        s_g_9_15 = Grid(9, 15, scale=0.68, node_constructor=Square, color=PINK).scale(0.25)
        s_g_14_14 = Grid(14, 14, scale=0.68, node_constructor=Square, color=PINK).scale(0.25)
        s_d_15 = Diamond(15, scale=0.68, node_constructor=Square).scale(0.25)
        
        g_grids = VGroup(s_g_9_15, s_g_14_14, s_d_15).arrange(RIGHT, buff=1.4*LARGE_BUFF).next_to(title, DOWN, buff=MED_SMALL_BUFF)
        g_grids.shift(0.6*RIGHT)

        self.next_slide()
        self.play(Transform(g_graphs, g_grids),
                  caption_9_15.animate.shift(0.0*DOWN),
                  caption_14_14.animate.shift(0.0*DOWN),
                  caption_d14.animate.shift(0.0*DOWN))

        self.next_slide()

