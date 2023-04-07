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

class AppearingLineGraph(Mobject):
    def __init__(self, points, labels, ax, line_color=RED, label_dir=DOWN, label_color=PINK, **kwargs):
        super().__init__(**kwargs)

        self.ax = ax

        self.add(self.ax)
        

        self.points = list(map(lambda p: normalize_3d(p, self.ax), points.items()))

        self.labels = labels

        self.point_objects = []
        for point in self.points:
            self.point_objects.append(Dot().move_to(point).set_color(PINK).scale(1.2))

        self.add(*self.point_objects)

        self.line_segments = []
        for i in range(1, len(self.points)):
            self.line_segments.append(Line(self.points[i-1], self.points[i], color=line_color))


        self.add(*self.line_segments)

        self.point_labels = []
        for i in range(len(self.points)):
            self.point_labels.append(Text(labels[i])
                                     .set_color(label_color)
                                     .scale(0.5)
                                     .move_to(self.points[i] + 0.4*label_dir + 0.4*RIGHT*(i > 0)))

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


class LineGraphExample(Slide):
    def construct(self):

        
        title = Text("Summary of Historical Progress", color=YELLOW).scale(1.2).to_edge(UP)
        title.scale_to_fit_width(13)

        self.play(Write(title))

        ax = Axes(
                x_range=[1999, 2024, 1],
                y_range=[5, 25, 1],
                axis_config={"include_numbers":True, "font_size": 22, "tip_width": 0.3},
                x_axis_config={"numbers_to_include": [2002, 2003, 2009, 2010, 2015, 2017, 2022, 2023]},
                y_axis_config={"numbers_to_include": [9, 10, 12, 13, 14, 15, 16, 17, 22, 23]},
                ).shift(0.6*DOWN).scale_to_fit_width(11)

        x_label = ax.get_x_axis_label(r'\text{Year}')
        y_label = ax.get_y_axis_label(r'\text{Bounds for }\chi_r(\mathbb{Z}^2)')
        
        self.next_slide()
        self.play(FadeIn(ax), Write(x_label), Write(y_label))

        upper_points = { 2002: 23, 2003: 22, 2009: 22, 2010: 17, 2015: 16, 2017: 15, 2022: 15, 2023: 15}
        upper_labels = ['Goddard et al.', 'Schwenk',  '', 'Soukal and Holub', 'Martin et al.', 'Martin et al.', '', '']

        upper_bounds = AppearingLineGraph(upper_points, upper_labels, ax, line_color=BLUE, label_dir=UP, label_color=BLUE)

        lower_points = { 2002: 9, 2003: 9, 2009: 10, 2010: 12, 2015: 13, 2017:13, 2022: 14, 2023: 15}
        lower_labels = ['Goddard et al.', '', 'Fiala et al.', 'Ekstein et al.', 'Martin et al.', '', 'Our work', 'This work']

        lower_bounds = AppearingLineGraph(lower_points, lower_labels, ax)
        
        for lower_anim, upper_anim in zip(upper_bounds.get_anims(), lower_bounds.get_anims()):
            self.next_slide()
            self.play(lower_anim, upper_anim)

        self.next_slide()

