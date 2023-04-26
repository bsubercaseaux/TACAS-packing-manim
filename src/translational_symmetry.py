from manim import *
from manim_slides import Slide
from subgraphs import Grid, Diamond


class Translational(Slide):
    def construct(self):
        title = Text("Translational Symmetry: forcing the center", font_size=48, t2c={
                     'forcing the center': YELLOW}).to_edge(UP)
        self.play(FadeIn(title))
        self.next_slide()

        ekstein_case = Tex(
            r"When Ekstein et al. proved $\chi_\rho(\mathbb{Z}^2) \geq 12$")
        ekstein_case.next_to(title, DOWN, buff=MED_SMALL_BUFF)

        g_9_15 = Grid(9, 15, scale=0.35*4,
                      node_constructor=Square).scale(0.375)
        g_9_15.next_to(ekstein_case, DOWN, buff=MED_SMALL_BUFF)

        self.play(Write(ekstein_case), FadeIn(g_9_15))

        ekstein_force = Tex(r"they forced vertex ",
                            r"$(5,5)$",  r" to get color ", r"$9$.")
        ekstein_force.set_color_by_tex("5", BLUE)
        ekstein_force.set_color_by_tex("9", YELLOW)
        ekstein_force.next_to(g_9_15, DOWN, buff=MED_SMALL_BUFF)

        self.next_slide()
        self.play(Write(ekstein_force), g_9_15.ColorNode(4, 4, 9))

        self.next_slide()
        d_14 = Diamond(14, scale=0.2*4, node_constructor=Square).scale(0.23)

        our_force = Tex(r"We force the central vertex to get color ", r"$6$.").next_to(
            d_14, DOWN, buff=MED_SMALL_BUFF)
        our_force.set_color_by_tex("6", YELLOW)
        self.play(FadeOut(g_9_15), FadeIn(d_14), FadeOut(
            ekstein_case), Transform(ekstein_force, our_force))
        self.play(d_14.ColorNode(0, 0, 6, label_num_color=BLACK))

        self.next_slide()

        center_is_better = Text("The center is the best vertex to force,\n as it participates in the most clauses!", font_size=26, t2c={
                                'center': YELLOW, 'best vertex to force': BLUE}).next_to(d_14, RIGHT, buff=MED_SMALL_BUFF)
        center_is_better.shift(2*LEFT)

        self.play(d_14.animate.shift(2*LEFT), Write(center_is_better))

        self.next_slide()

        why = Text("Why can we do this?", font_size=48, t2c={'Why': YELLOW})
        why.next_to(title, DOWN, buff=MED_SMALL_BUFF)

        self.play(FadeOut(d_14), FadeOut(center_is_better),
                  FadeOut(ekstein_force), FadeIn(why))

        self.next_slide()

        no_13 = Tex(
            r"1.", r" There's no solution with 13 colors (Subercaseaux and Heule 2022).", font_size=36)
        if_sol_6 = Tex(r"2.",  r" If a solution with colors ", r"$\{1, \ldots, 14\} \setminus \{6 \}$", r" were to exist, we could map it to ", r"$\{1, \ldots, 13\}$.",
                       font_size=36)
        therefore = Tex(r"3.", r" Therefore a solution, if it exists, must use color ", r"$6$.",
                        font_size=36)
        center = Tex(r"4.", r" We can safely assume it's in the center by considering a ", r"$D_{14}$ around it.",
                     font_size=36)
        no_13.set_color_by_tex("1.", BLUE)
        if_sol_6.set_color_by_tex("2.", BLUE)
        if_sol_6.set_color_by_tex("6", YELLOW)
        if_sol_6.set_color_by_tex("13", PINK)
        therefore.set_color_by_tex("3.", BLUE)
        therefore.set_color_by_tex("6", YELLOW)
        center.set_color_by_tex("4.", BLUE)
        center.set_color_by_tex("D_{14}", GREEN)

        steps = VGroup(no_13, if_sol_6, therefore, center).arrange(
            DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
        steps.next_to(why, DOWN, buff=MED_SMALL_BUFF)

        self.play(Write(no_13))
        self.next_slide()
        self.play(Write(if_sol_6))
        self.next_slide()

        assignment_14 = {(0, 0): 5,
                         (0, 1): 1,
                         (0, -1): 1,
                         (1, 0): 1,
                         (-1, 0): 1,
                         (1, 2): 1,
                         (2, 1): 1,
                         (-1, 2): 1,
                         (-2, 1): 1,
                         (1, -2): 1,
                         (2, -1): 1,
                         (-1, -2): 1,
                         (-2, -1): 1,
                         (0, 3): 1,
                         (3, 0): 1,
                         (-3, 0): 1,
                         (0, -3): 1,
                         (1, 1): 2,
                         (-1, -1): 2,
                         (-1, 1): 3,
                         (1, -1): 3,
                         (0, 4): 3,
                         (4, 0): 3,
                         (-4, 0): 3,
                         (0, -4): 3,
                         (-1, 3): 2,
                         (1, -3): 2,
                         (3, -1): 2,
                         (-3, 1): 2,
                         (-2, -2): 3,
                         (2, 2): 3,
                         (2, 0): 7,
                         (-2, 0): 8,
                         (0, 2): 9,
                         (0, -2): 10,
                         (1, 3): 4,
                         (-1, -3): 4,
                         (3, 1): 11,
                         (-3, -1): 12,
                         (-2, 2): 13,
                         (2, -2): 14
                         }

        d_4 = Diamond(4, scale=0.2*4, node_constructor=Square,
                      assignment=assignment_14, color=WHITE).scale(0.4)
        d_4.next_to(if_sol_6, DOWN, buff=MED_SMALL_BUFF)
        d_4.shift(2*LEFT)

        assignment_13 = {}
        for k in assignment_14:
            assignment_13[k] = assignment_14[k]
            if assignment_14[k] > 6:
                assignment_13[k] -= 1

        d_4_2 = Diamond(4, scale=0.2*4, node_constructor=Square,
                        assignment=assignment_13, color=WHITE).scale(0.4)
        d_4_2.next_to(d_4, RIGHT, buff=2*LARGE_BUFF)

        arr = Arrow(d_4.get_corner(RIGHT), d_4_2.get_corner(LEFT), buff=0.5)

        self.play(FadeIn(d_4), FadeIn(d_4_2), FadeIn(arr))

        self.next_slide()

        self.play(FadeOut(d_4), FadeOut(d_4_2), FadeOut(arr), Write(therefore))
        self.next_slide()

        self.play(Write(center))

        assignment_6_28 = {
            (0, 0): 1,
            (0, 1): 5,
            (0, 2): 1,
            (0, 3): 2,
            (0, 4): 1,
            (0, 5): 3,
            (0, 6): 1,
            (0, 7): 2,
            (0, 8): 1,
            (0, 9): 4,
            (0, 10): 1,
            (0, 11): 3,
            (0, 12): 1,
            (0, 13): 2,
            (0, 14): 1,
            (0, 15): 3,
            (0, 16): 1,
            (0, 17): 4,
            (0, 18): 1,
            (0, 19): 2,
            (0, 20): 1,
            (0, 21): 3,
            (0, 22): 1,
            (0, 23): 2,
            (0, 24): 1,
            (0, 25): 3,
            (0, 26): 1,
            (0, 27): 2,
            (1, 0): 3,
            (1, 1): 1,
            (1, 2): 6,
            (1, 3): 1,
            (1, 4): 8,
            (1, 5): 1,
            (1, 6): 13,
            (1, 7): 1,
            (1, 8): 3,
            (1, 9): 1,
            (1, 10): 6,
            (1, 11): 1,
            (1, 12): 5,
            (1, 13): 1,
            (1, 14): 10,
            (1, 15): 1,
            (1, 16): 2,
            (1, 17): 1,
            (1, 18): 3,
            (1, 19): 1,
            (1, 20): 5,
            (1, 21): 1,
            (1, 22): 4,
            (1, 23): 1,
            (1, 24): 9,
            (1, 25): 1,
            (1, 26): 5,
            (1, 27): 1,
            (2, 0): 1,
            (2, 1): 2,
            (2, 2): 1,
            (2, 3): 3,
            (2, 4): 1,
            (2, 5): 2,
            (2, 6): 1,
            (2, 7): 5,
            (2, 8): 1,
            (2, 9): 2,
            (2, 10): 1,
            (2, 11): 11,
            (2, 12): 1,
            (2, 13): 3,
            (2, 14): 1,
            (2, 15): 9,
            (2, 16): 1,
            (2, 17): 7,
            (2, 18): 1,
            (2, 19): 8,
            (2, 20): 1,
            (2, 21): 2,
            (2, 22): 1,
            (2, 23): 3,
            (2, 24): 1,
            (2, 25): 2,
            (2, 26): 1,
            (2, 27): 6,
            (3, 0): 9,
            (3, 1): 1,
            (3, 2): 7,
            (3, 3): 1,
            (3, 4): 10,
            (3, 5): 1,
            (3, 6): 4,
            (3, 7): 1,
            (3, 8): 14,
            (3, 9): 1,
            (3, 10): 3,
            (3, 11): 1,
            (3, 12): 12,
            (3, 13): 1,
            (3, 14): 2,
            (3, 15): 6,
            (3, 16): 3,
            (3, 17): 1,
            (3, 18): 2,
            (3, 19): 1,
            (3, 20): 3,
            (3, 21): 1,
            (3, 22): 11,
            (3, 23): 1,
            (3, 24): 7,
            (3, 25): 1,
            (3, 26): 3,
            (3, 27): 1,
            (4, 0): 1,
            (4, 1): 3,
            (4, 2): 1,
            (4, 3): 2,
            (4, 4): 1,
            (4, 5): 3,
            (4, 6): 1,
            (4, 7): 2,
            (4, 8): 1,
            (4, 9): 7,
            (4, 10): 1,
            (4, 11): 2,
            (4, 12): 1,
            (4, 13): 4,
            (4, 14): 1,
            (4, 15): 5,
            (4, 16): 1,
            (4, 17): 13,
            (4, 18): 1,
            (4, 19): 4,
            (4, 20): 1,
            (4, 21): 6,
            (4, 22): 1,
            (4, 23): 2,
            (4, 24): 1,
            (4, 25): 14,
            (4, 26): 1,
            (4, 27): 2,
            (5, 0): 2,
            (5, 1): 1,
            (5, 2): 4,
            (5, 3): 1,
            (5, 4): 5,
            (5, 5): 1,
            (5, 6): 6,
            (5, 7): 1,
            (5, 8): 3,
            (5, 9): 1,
            (5, 10): 5,
            (5, 11): 1,
            (5, 12): 8,
            (5, 13): 1,
            (5, 14): 3,
            (5, 15): 1,
            (5, 16): 2,
            (5, 17): 1,
            (5, 18): 3,
            (5, 19): 1,
            (5, 20): 2,
            (5, 21): 1,
            (5, 22): 5,
            (5, 23): 1,
            (5, 24): 3,
            (5, 25): 1,
            (5, 26): 4,
            (5, 27): 1,
        }

        infinite = Grid(6, 28, scale=0.8, infinite_rows=True, infinite_columns=True,
                        node_constructor=Square, color=WHITE, assignment=assignment_6_28).scale(0.4)
        infinite.next_to(center, DOWN, buff=MED_SMALL_BUFF)

        d_2 = Diamond(2, scale=0.8, node_constructor=Square,
                      color=YELLOW, stroke_width=4).scale(0.4)
        d_2.next_to(center, DOWN, buff=MED_SMALL_BUFF)
        d_2.shift(0.32*10.5*LEFT + 0.32*0.5*DOWN)

        self.play(FadeIn(infinite), FadeIn(d_2))

        path = [np.array([2, 0, 0]),
                np.array([1, -1, 0]),
                np.array([3, 0, 0]),
                np.array([2, 1, 0]),
                np.array([4, 0, 0])]

        self.next_slide()
        for movement in path:
            self.play(d_2.animate.shift(0.32*movement), run_time=1)

        self.next_slide()

        self.play(FadeOut(infinite), FadeOut(d_2), FadeOut(steps))

        axes = Axes(x_range=[0, 14, 1],
                    y_range=[-1, 2],
                    axis_config={"include_numbers": True},
                    y_axis_config={"scaling": LogBase(custom_labels=True)},)
        axes.next_to(why, DOWN, buff=0.1)
        axes.shift(0.3*UP)
        axes.scale_to_fit_width(10)
        vals = [(1, 16.7111),
                (2, 11.644),
                (3, 1.56254),
                (4, 1.10246),
                (5, 0.347961),
                (6, 0.343833),
                (7, 0.343433),
                (8, 0.541108),
                (9, 0.629939),
                (10, 0.795033),
                (11, 0.869528),
                (12, 0.870236),
                (13, 5.15691)]
        x = [val[0] for val in vals]
        y = [val[1] for val in vals]
        line = axes.plot_line_graph(x, y,
                                    add_vertex_dots=True,
                                    vertex_dot_radius=0.05,
                                    line_color=RED)
        dot6 = line["vertex_dots"][5]
        dot6.scale(2)
        dot6.set_color(YELLOW)

        x_label = axes.get_x_axis_label(r'\text{Color to force}').scale(0.7)
        y_label = axes.get_y_axis_label(r'\text{Runtime [hours]}').scale(
            0.7).shift(0.25*DOWN + 0.5*LEFT)
        new_text = Tex(r"What color", r" to force in order to show ",
                       r"$\chi_\rho(D_{12}) \geq 14$").move_to(why)
        new_text.set_color_by_tex(r"color", YELLOW)
        new_text.set_color_by_tex(r"12", PINK)
        self.play(FadeIn(axes), FadeIn(line), Transform(why, new_text),
                  Write(x_label), Write(y_label))

        self.next_slide()
