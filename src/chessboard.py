from manim import *
from manim_slides import Slide
from subgraphs import Diamond
from empty import EmptyAnimation

class Chessboard(Slide):
    def construct(self):
        title = Tex(r"Chessboard Conjecture", color=YELLOW, font_size=64).to_edge(UP)
        
        before = Tex(r"Before we optimized enough the final instance,\\ we considered the following idea:", font_size=36)
        before.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        
        self.play(FadeIn(title))
        
        self.next_slide()
        self.play(Write(before))
        
        self.next_slide()
        
        d_7 =  Diamond(7, scale=0.4, node_constructor=Square, color=WHITE).next_to(title, DOWN, buff=MED_LARGE_BUFF)
        d_7.scale(0.8)
        d_7.next_to(before, DOWN, buff=0.8*MED_SMALL_BUFF)
        
        d_7.colorNode(0, 0, 6, label_num_color=BLACK)
        self.play(FadeIn(d_7))
        self.next_slide()
        
        
        ones = []
        for i in range(-7, 8):
            for j in range(-7, 8):
                if abs(i) + abs(j) <= 7 and (i + j)%2 == 1:
                    ones.append((i, j))
                    
        anims = [d_7.ColorNode(*cell, 1) for cell in ones]
        self.play(*anims)
        self.next_slide()
        
        can_we = Text("Can we always assume this chessboard pattern?", t2c={'chessboard pattern': YELLOW}, font_size=26)
        can_we.next_to(d_7, RIGHT, buff=MED_LARGE_BUFF)
        can_we.shift(1.5*UP + 0.5*LEFT)
        self.play( FadeIn   (can_we), can_we.animate.shift(3.8*LEFT), d_7.animate.shift(3.8*LEFT))
        self.next_slide()
        speed_up = Tex(r"If true", r": dramatical performance speed-up!", font_size=36)
        speed_up[0].set_color(BLUE)
        speed_up.next_to(can_we, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(speed_up))
        self.next_slide()
        
        solved = Tex(r"It's not too hard to prove that\\", r"Chessboard Conjecture $\implies \chi_\rho(\mathbb{Z}^2) = 15$", font_size=36)
        solved.set_color_by_tex_to_color_map({'Chessboard Conjecture': PINK})
        
        detail = Tex(r"$\textrm{UNSAT}$", r"$\left(D_{14} + \text{14 colors} + \textsc{Chessboard} + 6 \text{ in the center}\right)$", font_size=36)
        detail.set_color_by_tex_to_color_map({r'\textrm{UNSAT}': RED, r'\textsc{Chessboard}': YELLOW})
        solved.next_to(speed_up, DOWN, buff=LARGE_BUFF)
        detail.next_to(solved, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(solved))
        self.next_slide()
        self.play(Write(detail))
        
        self.next_slide()
        self.play(FadeOut(speed_up), FadeOut(can_we), FadeOut(before), FadeOut(d_7), FadeOut(solved), FadeOut(detail))
        
        turns_out = Text("But it turns out the conjecture is false!", t2c={'false': RED}, font_size=42)
        turns_out.next_to(title, DOWN, buff=MED_SMALL_BUFF)
        self.next_slide()
        self.play(Write(turns_out))
        
        assignment = {(-14, 0): 2, (-13, -1): 3, (-13, 0): 1, (-13, 1): 7, (-12, -2): 8, (-12, -1): 1, (-12, 0): 9, (-12, 1): 1, (-12, 2): 2, (-11, -3): 3, (-11, -2): 1, (-11, -1): 2, (-11, 0): 1, (-11, 1): 3, (-11, 2): 1, (-11, 3): 10, (-10, -4): 2, (-10, -3): 1, (-10, -2): 6, (-10, -1): 1, (-10, 0): 5, (-10, 1): 1, (-10, 2): 12, (-10, 3): 1, (-10, 4): 2, (-9, -5): 3, (-9, -4): 1, (-9, -3): 4, (-9, -2): 1, (-9, -1): 3, (-9, 0): 1, (-9, 1): 2, (-9, 2): 1, (-9, 3): 3, (-9, 4): 1, (-9, 5): 7, (-8, -6): 2, (-8, -5): 1, (-8, -4): 14, (-8, -3): 1, (-8, -2): 2, (-8, -1): 1, (-8, 0): 11, (-8, 1): 1, (-8, 2): 4, (-8, 3): 1, (-8, 4): 5, (-8, 5): 1, (-8, 6): 9, (-7, -7): 3, (-7, -6): 1, (-7, -5): 9, (-7, -4): 1, (-7, -3): 5, (-7, -2): 1, (-7, -1): 7, (-7, 0): 1, (-7, 1): 3, (-7, 2): 1, (-7, 3): 2, (-7, 4): 1, (-7, 5): 3, (-7, 6): 1, (-7, 7): 2, (-6, -8): 8, (-6, -7): 1, (-6, -6): 4, (-6, -5): 1, (-6, -4): 2, (-6, -3): 1, (-6, -2): 3, (-6, -1): 1, (-6, 0): 2, (-6, 1): 1, (-6, 2): 6, (-6, 3): 1, (-6, 4): 13, (-6, 5): 1, (-6, 6): 8, (-6, 7): 4, (-6, 8): 1, (-5, -9): 3, (-5, -8): 1, (-5, -7): 2, (-5, -6): 1, (-5, -5): 3, (-5, -4): 1, (-5, -3): 10, (-5, -2): 1, (-5, -1): 4, (-5, 0): 1, (-5, 1): 5, (-5, 2): 1, (-5, 3): 3, (-5, 4): 1, (-5, 5): 2, (-5, 6): 1, (-5, 7): 3, (-5, 8): 2, (-5, 9): 1, (-4, -10): 2, (-4, -9): 1, (-4, -8): 7, (-4, -7): 1, (-4, -6): 5, (-4, -5): 1, (-4, -4): 6, (-4, -3): 1, (-4, -2): 2, (-4, -1): 1, (-4, 0): 3, (-4, 1): 1, (-4, 2): 2, (-4, 3): 1, (-4, 4): 4, (-4, 5): 1, (-4, 6): 5, (-4, 7): 1, (-4, 8): 11, (-4, 9): 12, (-4, 10): 2, (-3, -11): 5, (-3, -10): 1, (-3, -9): 4, (-3, -8): 1, (-3, -7): 3, (-3, -6): 1, (-3, -5): 2, (-3, -4): 1, (-3, -3): 3, (-3, -2): 1, (-3, -1): 8, (-3, 0): 1, (-3, 1): 9, (-3, 2): 1, (-3, 3): 7, (-3, 4): 1, (-3, 5): 3, (-3, 6): 1, (-3, 7): 2, (-3, 8): 1, (-3, 9): 3, (-3, 10): 1, (-3, 11): 5, (-2, -12): 2, (-2, -11): 1, (-2, -10): 3, (-2, -9): 1, (-2, -8): 2, (-2, -7): 1, (-2, -6): 13, (-2, -5): 1, (-2, -4): 4, (-2, -3): 1, (-2, -2): 5, (-2, -1): 1, (-2, 0): 2, (-2, 1): 1, (-2, 2): 3, (-2, 3): 1, (-2, 4): 2, (-2, 5): 1, (-2, 6): 6, (-2, 7): 1, (-2, 8): 4, (-2, 9): 1, (-2, 10): 7, (-2, 11): 1, (-2, 12): 2, (-1, -13): 3, (-1, -12): 1, (-1, -11): 6, (-1, -10): 1, (-1, -9): 9, (-1, -8): 1, (-1, -7): 11, (-1, -6): 1, (-1, -5): 3, (-1, -4): 1, (-1, -3): 2, (-1, -2): 1, (-1, -1): 3, (-1, 0): 1, (-1, 1): 4, (-1, 2): 1, (-1, 3): 5, (-1, 4): 1, (-1, 5): 10, (-1, 6): 1, (-1, 7): 3, (-1, 8): 1, (-1, 9): 2, (-1, 10): 1, (-1, 11): 3, (-1, 12): 1, (-1, 13): 4, (0, -14): 8, (0, -13): 1, (0, -12): 4, (0, -11): 1, (0, -10): 2, (0, -9): 1, (0, -8): 3, (0, -7): 1, (0, -6): 2, (0, -5): 1, (0, -4): 7, (0, -3): 1, (0, -2): 12, (0, -1): 1, (0, 0): 6, (0, 1): 1, (0, 2): 2, (0, 3): 1, (0, 4): 3, (0, 5): 1, (0, 6): 2, (0, 7): 1, (0, 8): 5, (0, 9): 1, (0, 10): 8, (0, 11): 1, (0, 12): 13, (0, 13): 1, (0, 14): 2, (1, -13): 2, (1, -12): 1, (1, -11): 3, (1, -10): 1, (1, -9): 10, (1, -8): 1, (1, -7): 4, (1, -6): 1, (1, -5): 5, (1, -4): 1, (1, -3): 3, (1, -2): 1, (1, -1): 2, (1, 0): 1, (1, 1): 3, (1, 2): 1, (1, 3): 14, (1, 4): 1, (1, 5): 4, (1, 6): 1, (1, 7): 9, (1, 8): 1, (1, 9): 3, (1, 10): 1, (1, 11): 2, (1, 12): 1, (1, 13): 3, (2, -12): 5, (2, -11): 1, (2, -10): 7, (2, -9): 1, (2, -8): 2, (2, -7): 1, (2, -6): 3, (2, -5): 1, (2, -4): 2, (2, -3): 1, (2, -2): 4, (2, -1): 1, (2, 0): 5, (2, 1): 1, (2, 2): 11, (2, 3): 1, (2, 4): 2, (2, 5): 1, (2, 6): 3, (2, 7): 1, (2, 8): 2, (2, 9): 1, (2, 10): 4, (2, 11): 1, (2, 12): 5, (3, -11): 2, (3, -10): 1, (3, -9): 3, (3, -8): 1, (3, -7): 6, (3, -6): 1, (3, -5): 8, (3, -4): 1, (3, -3): 9, (3, -2): 1, (3, -1): 3, (3, 0): 1, (3, 1): 2, (3, 2): 1, (3, 3): 3, (3, 4): 1, (3, 5): 5, (3, 6): 1, (3, 7): 7, (3, 8): 1, (3, 9): 6, (3, 10): 1, (3, 11): 3, (4, -10): 4, (4, -9): 1, (4, -8): 5, (4, -7): 1, (4, -6): 2, (4, -5): 1, (4, -4): 3, (4, -3): 1, (4, -2): 2, (4, -1): 1, (4, 0): 7, (4, 1): 1, (4, 2): 4, (4, 3): 1, (4, 4): 8, (4, 5): 1, (4, 6): 2, (4, 7): 1, (4, 8): 3, (4, 9): 1, (4, 10): 2, (5, -9): 2, (5, -8): 1, (5, -7): 3, (5, -6): 1, (5, -5): 4, (5, -4): 1, (5, -3): 5, (5, -2): 1, (5, -1): 10, (5, 0): 1, (5, 1): 3, (5, 2): 1, (5, 3): 2, (5, 4): 1, (5, 5): 3, (5, 6): 1, (5, 7): 4, (5, 8): 1, (5, 9): 5, (6, -8): 14, (6, -7): 1, (6, -6): 7, (6, -5): 1, (6, -4): 2, (6, -3): 1, (6, -2): 3, (6, -1): 1, (6, 0): 2, (6, 1): 1, (6, 2): 13, (6, 3): 1, (6, 4): 6, (6, 5): 1, (6, 6): 12, (6, 7): 1, (6, 8): 2, (7, -7): 2, (7, -6): 1, (7, -5): 3, (7, -4): 1, (7, -3): 6, (7, -2): 1, (7, -1): 4, (7, 0): 1, (7, 1): 5, (7, 2): 1, (7, 3): 3, (7, 4): 1, (7, 5): 2, (7, 6): 1, (7, 7): 3, (8, -6): 5, (8, -5): 1, (8, -4): 11, (8, -3): 1, (8, -2): 2, (8, -1): 1, (8, 0): 3, (8, 1): 1, (8, 2): 2, (8, 3): 1, (8, 4): 4, (8, 5): 1, (8, 6): 5, (9, -5): 2, (9, -4): 1, (9, -3): 3, (9, -2): 1, (9, -1): 8, (9, 0): 1, (9, 1): 9, (9, 2): 1, (9, 3): 7, (9, 4): 1, (9, 5): 3, (10, -4): 4, (10, -3): 1, (10, -2): 5, (10, -1): 1, (10, 0): 2, (10, 1): 1, (10, 2): 3, (10, 3): 1, (10, 4): 2, (11, -3): 7, (11, -2): 1, (11, -1): 3, (11, 0): 1, (11, 1): 6, (11, 2): 1, (11, 3): 5, (12, -2): 2, (12, -1): 1, (12, 0): 4, (12, 1): 1, (12, 2): 2, (13, -1): 12, (13, 0): 1, (13, 1): 3, (14, 0): 5}
        d_14 = Diamond(14, scale=0.4, node_constructor=Square, color=WHITE, assignment=assignment).next_to(turns_out, DOWN, buff=MED_SMALL_BUFF)
        d_14.scale(0.5)
        d_14.shift(3*UP)
        
        self.play(FadeIn(d_14))
        self.next_slide()
        
        
        detail_unsat = Tex(r"$\textrm{UNSAT}$", r"$\left(D_{14} + \text{14 colors} + \textsc{Chessboard} + 6 \text{ in the center}\right)$", font_size=34)
        detail_sat = Tex(r"$\textrm{SAT}$", r"$\left(D_{14} + \text{14 colors} + 6 \text{ in the center}\right)$", font_size=34)
        detail_unsat.set_color_by_tex_to_color_map({r'\textrm{UNSAT}': RED, r'\textsc{Chessboard}': WHITE})
        detail_sat.set_color_by_tex_to_color_map({r'\textrm{SAT}': GREEN, r'center': WHITE})
        group_sat = VGroup(detail_unsat, detail_sat).arrange(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF).next_to(d_14, RIGHT, buff=MED_LARGE_BUFF)
        group_sat.shift(5.0*LEFT + 2*UP)
        self.play(d_14.animate.shift(3.5*LEFT), FadeIn(detail_unsat), FadeIn(detail_sat))
        
        assignment_ones = {}
        for k in assignment:
            if k == (0, 0) or assignment[k] == 1:
                assignment_ones[k] = assignment[k]
        d_14_ones = Diamond(14, scale=0.4, node_constructor=Square, color=WHITE, assignment=assignment_ones)
        d_14_ones.move_to(d_14)
        d_14_ones.scale_to_fit_width(d_14.get_width())
        self.next_slide()
        self.remove(d_14)
        self.add(d_14_ones)
        self.play(EmptyAnimation())
        self.next_slide()
        
          # Set the coordinates and radius of the circular area
        circle_center = d_14.nodes[(4, 8)].get_center() + 1.8*DOWN
        circle_radius = 0.8

        # Create the circular area
        focus_circle = Circle(radius=circle_radius, color=YELLOW, fill_opacity=0.2, fill_color=YELLOW)
        focus_circle.move_to(circle_center)

        # Create the background overlay
        background_overlay = Rectangle(height=config['frame_height'], width=config['frame_width'], fill_opacity=0.7, fill_color=BLACK, stroke_opacity=0)
    
           # Create a hole in the overlay using a VDict object
        hole = focus_circle.copy()
        hole.set_fill(color=BLACK, opacity=0)
        hole.set_stroke(color=BLACK, opacity=0)
        
        unfocus = Difference(background_overlay, hole)
        unfocus.set_stroke(color=BLACK, opacity=0)
        unfocus.set_fill(color=BLACK, opacity=0.7)
        
        self.play(
            FadeIn(unfocus),
            #Create(focus_circle)
        )
        
        self.next_slide()

        # Remove the focus effect
        self.play(
            FadeOut(unfocus)
        )
        
        self.next_slide()
        self.clear()
        # self.play(FadeOut(d_14_ones), FadeOut(detail_unsat), FadeOut(detail_sat), FadeOut(title)) # ?

        # math art
        title = Text("We liked this counter-example too much!", font_size=42).to_edge(UP)

        painting1 = ImageMobject("img/painting1.jpg").scale(0.7).shift(1.5*LEFT)
        painting2 = ImageMobject("img/painting2.jpg").next_to(painting1, RIGHT, buff=SMALL_BUFF).scale(0.5)
        self.play(FadeIn(title))
        self.next_slide()
        self.play(FadeIn(painting1), FadeIn(painting2))
        self.next_slide()
