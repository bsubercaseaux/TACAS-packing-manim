from manim import *
from manim_slides import Slide 
from subgraphs import Grid, to_3d
import config
import numpy as np


class Motivation(Slide):
    def construct(self):
        title = Text("Motivation", font_size=72)
        title.to_edge(UP)

        self.play(Write(title))

        self.next_slide()

        santiago = SVGMobject('img/Comunas_de_Santiago_2.svg', should_center=True, color=BLUE, fill_color=RED, opacity=1)
        #santiago.generate_mobject()
        santiago.scale(2.5)

        santiago_title = Text("Old map of the districts of Santiago, Chile", font_size=28)
        santiago_title.next_to(santiago, DOWN)

        self.play(FadeIn(santiago))
        self.play(Write(santiago_title))
        
        dots = {
                0: to_3d(0.2, -0.1),
                1: to_3d(0.6, 0),
                2: to_3d(0.5, 0.5),
                3: to_3d(1.2, 0.8),
                4: to_3d(1.3, 0.3),
                5: to_3d(1.3, 1.5),
                6: to_3d(1.7, 2.3),
                7: to_3d(1.0, 1.9),
                8: to_3d(0.8,-0.7),
                9: to_3d(1.0,-1.6),
                10:to_3d(0.1, -1.5),
                11:to_3d(-0.35, -1.4),
                12:to_3d(-0.7, -1.8),
                13:to_3d(0.35, 1),
                14:to_3d(-0.2, 0.6),
                15:to_3d(-0.1, 1.5),
                16:to_3d(-0.4, 1.3),
                17:to_3d(-0.5, 1.8),
                18:to_3d(-0.85, 1.45),
                19:to_3d(-1.3, 2.1),
                20:to_3d(-0.9, 1.0),
                21:to_3d(-1.35, 1.05),
                22:to_3d(-1.55, 0.75),
                23:to_3d(-1.15, 0.65),
                24:to_3d(-0.8, 0.4),
                25:to_3d(-0.5, -0.1),
                26:to_3d(-0.15, -0.2),
                27:to_3d(-0.65, -0.65),
                28:to_3d(-0.3, -0.7),
                29:to_3d(0.03,-1),
                30:to_3d(0.3,-0.8),
                31:to_3d(-1.65, -0.6),
                32:to_3d(-1.1, -0.25),
                33:to_3d(-1.35, 0.15),
                34:to_3d(-1.45,0.35),
                35:to_3d(-1.9, -1.4),
                36:to_3d(-0.03, 2.0),
                37:to_3d(0.3,1.8),
            }

        antenna = ImageMobject('img/radio_antenna.png').set_color(WHITE).scale(0.5).move_to(to_3d(0.2, -0.1))

        self.play(FadeIn(antenna))
        # dot_objects = {}
        # for id, pos in dots.items():
        #     print(id, pos)
        #     dot_objects[id] = Dot().move_to(pos)
        # 
        edges = []
        for u in range(38):
            for v in range(u+1, 38):
                if np.linalg.norm(np.array(dots[u])-np.array(dots[v])) < 0.8:
                    edges.append((u, v))

        g = Graph(dots.keys(), edges, layout=dots, edge_config={'color': BLUE, 'stroke_width': 2})

        self.next_slide()
        graph_title = Text("Graph of old Santiago's districts", font_size=28).move_to(santiago_title)
        self.play(*[Create(g.vertices[v]) for v in g.vertices], ReplacementTransform(santiago_title, graph_title))




        self.next_slide()
        self.play(FadeOut(santiago), run_time=1.5)
        self.play(*[Create(g.edges[e]) for e in g.edges])
        # self.play(*[FadeIn(d) for d in dot_objects.values()])

        subgraph = [0,1,2,3,4,5,7,8,13, 30]
        not_subgraph = list(filter(lambda x: x not in subgraph, g.vertices.keys()))
        induced_edges = list(filter(lambda x: x[0] in subgraph and x[1] in subgraph, g.edges.keys()))
        not_induced_edges = list(filter(lambda x: x not in induced_edges,  g.edges.keys()))

        sub_dots = {k: v for k, v in dots.items() if k in subgraph}
        subg = Graph(subgraph, induced_edges, layout=sub_dots, edge_config={'color': BLUE, 'stroke_width': 2}).scale(1.5)
        subgraph_title = Text("Subgraph of old Santiago's districts", font_size=28).move_to(graph_title)
        self.next_slide()

        self.play(FadeOut(g), ReplacementTransform(graph_title, subgraph_title), FadeIn(subg), subg.animate.scale(2.25), subg.animate.move_to([0,0,0]))


        self.next_slide()
