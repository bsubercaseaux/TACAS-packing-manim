# Animates the raise of lower bounds for a function. 
# The function is f(x) = packing chromatic number of the infinite square grid
from manim import *
from manim.utils.commands import run
from manim_slides import Slide
import numpy as np
from empty import EmptyAnimation


def normalize_3d(point, axes):
    point_2d = axes.coords_to_point(*point)
    return np.array([point_2d[0], point_2d[1], 0.0])

class L1Geodesic(VMobject):
    def __init__(self, p1, p2, line_color, **kwargs):
        super().__init__(**kwargs)
        self.l1 = Line(p1, (p2[0], p1[1], 0), color=line_color) # type: ignore
        self.l2 = Line((p2[0], p1[1], 0), p2, color=line_color) # type: ignore
        self.add(self.l1, self.l2)
        

class AppearingLineGraph(Mobject):
    def __init__(self, points, labels, ax, label_pos, line_color=RED, label_color=PINK,  **kwargs):
        super().__init__(**kwargs)

        self.ax = ax

        self.add(self.ax)
        

        self.points = list(map(lambda p: normalize_3d(p, self.ax), points.items()))

        self.labels = labels

        self.point_objects = []
        for point in self.points:
            self.point_objects.append(Dot().move_to(point).set_color(PINK).scale(1.2))
            self.point_objects[-1].set_z_index(1)

        self.add(*self.point_objects)

        self.line_segments = []
        for i in range(1, len(self.points)):
            self.line_segments.append(L1Geodesic(self.points[i-1], self.points[i], line_color=line_color))


        self.add(*self.line_segments)

        self.point_labels = []
        for i in range(len(self.points)):
            self.point_labels.append(Text(labels[i])
                                     .set_color(label_color)
                                     .scale(0.5)
                                     .move_to(label_pos[i]))

        self.add(*self.point_labels)

    def get_anims(self, run_time=1.4, **kwargs):
        succ = []
        text_run_time = 0.8
        for i in range(len(self.points)):
            if self.point_labels[i].text != '':
                if i > 0:
                    succ.append(AnimationGroup(Create(self.line_segments[i-1], run_time=run_time),
                                               FadeIn(self.point_objects[i], run_time=text_run_time), 
                                               Write(self.point_labels[i], run_time=text_run_time)))

                else:
                    succ.append(AnimationGroup(FadeIn(self.point_objects[i], run_time=text_run_time),
                                               Write(self.point_labels[i], run_time=text_run_time)))
            else:
                if i > 0:
                    succ.append(Create(self.line_segments[i-1], run_time=run_time))
                else:
                    succ.append(EmptyAnimation())
        return succ


class HistoricalSummary(Slide):
    def construct(self):
        # self.camera.background_color = WHITE
        
        title = Text("Historical Progress", font_size=60, color=YELLOW).to_edge(UP)
   

        self.play(Write(title))

        ax = Axes(
                x_range=[1999, 2024, 1],
                y_range=[5, 25, 1],
                axis_config={"include_numbers":True, "font_size": 18, "tip_width": 0.2, "decimal_number_config": {"group_with_commas": False, "num_decimal_places": 0}},
                x_axis_config={"numbers_to_include": [2002, 2003, 2009, 2010, 2015, 2017, 2022, 2023]},
                y_axis_config={"numbers_to_include": [9, 10, 12, 13, 14, 15, 16, 17, 22, 23]},
                ).shift(0.6*DOWN).scale_to_fit_width(11.5).shift(0.2*DOWN)
        # ax.set_color(BLACK)
        x_label = ax.get_x_axis_label(r'\text{Year}')
        y_label = ax.get_y_axis_label(r'\text{Bounds on }\textcolor{red}{\chi_\rho(\mathbb{Z}^2)}')
        
        self.next_slide()
        self.play(FadeIn(ax), Write(x_label), Write(y_label))

        upper_points = { 2002: 23, 2003: 22, 2009: 22, 2010: 17, 2015: 16, 2017: 15, 2022: 15, 2023: 15}
        upper_labels = ['Goddard et al.', 'Schwenk',  '', 'Soukal and Holub', 'Martin et al.', 'Martin et al.', '', '']

        label_pos_upper = [(-4, 1.8, 0), (-3.7, 0.8, 0), (-0.8, -0.5, 0), (-0.8, -0.5, 0), (1.7, 0.0, 0), (3.5, -0.5, 0), (7, 0, 0), (8, 0, 0)]
        upper_bounds = AppearingLineGraph(upper_points, upper_labels, ax, line_color=BLUE, label_color=BLUE, label_pos=label_pos_upper)

        lower_points = { 2002: 9, 2003: 9, 2009: 10, 2010: 12, 2015: 13, 2017:13, 2022: 14, 2023: 15}
        lower_labels = ['Goddard et al.', '', 'Fiala et al.', 'Ekstein et al.', 'Martin et al.', '', 'Subercaseaux and Heule (S&H)', 'S&H']

        label_pos_lower = [(-4, -2.8, 0), (-3.7, -2.8, 0), (-1.4, -2.8, 0), (-0.8, -1.3, 0), (1.5, -2, 0), (3, -1, 0), (4.7, -1.6, 0), (6, -0.75, 0)]
        lower_bounds = AppearingLineGraph(lower_points, lower_labels, ax, label_pos=label_pos_lower)
        #lower_bounds.point_labels[-1].set_color(YELLOW).set_weight(BOLD)
        
        for lower_anim, upper_anim in zip(upper_bounds.get_anims(), lower_bounds.get_anims()):
            self.next_slide()
            self.play(lower_anim, upper_anim)
            
        shaded_rectangle = Rectangle(height=6, width=3.7, color=GREEN, fill_opacity=0.4, stroke_width=0).shift(3.32*RIGHT + 0.6*DOWN) 
        sat_label = Text("SAT proofs", font_size=44, color=WHITE).move_to([3.3, 1.5,0])
        
        self.next_slide()
        self.play(FadeIn(shaded_rectangle), Write(sat_label))
        

        self.next_slide()

