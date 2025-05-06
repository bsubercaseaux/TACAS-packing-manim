from manim import *
from manim_slides import Slide 
from subgraphs import Grid, to_3d
import config
import numpy as np
from empty import EmptyAnimation


class Motivation(Slide):
    def construct(self):
        # self.play(EmptyAnimation())
        # self.next_slide()
        
        standard_coloring_title = Text("Standard graph coloring", color=BLUE, font_size=48).to_edge(UP)
        self.play(FadeIn(standard_coloring_title))
        self.next_slide()
        
        standard_definition = Tex(r"A graph coloring is a function ", r"$f: V \to \{1, \dots, k\}$", r", such that", font_size=36).next_to(standard_coloring_title, DOWN, buff=MED_SMALL_BUFF)
        standard_condition = Tex(r"if ", r"$f(u) = f(v) = c$", r", then ",  r"$d(u, v) > 1.$", font_size=36).next_to(standard_definition, DOWN)
        standard_definition[1].set_color(YELLOW)
        standard_condition[1].set_color(YELLOW)
        standard_condition[3].set_color(PINK)

        
        self.play(Write(standard_definition))
        self.next_slide()
        
        self.play(Write(standard_condition))
        self.next_slide()
        
        l4 = Grid(1, 4, scale=0.4).next_to(standard_condition, DOWN, buff=MED_SMALL_BUFF)
        
        self.play(FadeIn(l4))
        self.next_slide()
        
        self.play(l4.ColorNode(0, 0, 1))
        self.next_slide()
        self.play(l4.ColorNode(0, 1, 2))
        self.next_slide()
        self.play(l4.ColorNode(0, 2, 1))
        self.next_slide()
        self.play(l4.ColorNode(0, 3, 2))
        
        dividing_line=DashedLine([-6,0,0], [6,0,0]).next_to(l4, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(dividing_line))
        
        broadcast_coloring_title = Text("Packing coloring", color=BLUE, font_size=48).next_to(l4, DOWN, buff=LARGE_BUFF)
        self.play(FadeIn(broadcast_coloring_title))
        self.next_slide()
        
        broadcast_definition = Tex(r"A ", r"packing coloring", r" is a function ", r"$f: V \to \{1, \dots, k\}$", r", such that", font_size=36).next_to(broadcast_coloring_title, DOWN, buff=MED_SMALL_BUFF)
        broadcast_condition = Tex(r"if ", r"$f(u) = f(v) = c$", r", then ",  r"$d(u, v)$", r"$\,> c.$", font_size=36).next_to(broadcast_definition, DOWN)
        broadcast_definition[1].set_color(YELLOW)
        broadcast_definition[3].set_color(YELLOW)
        
        broadcast_condition[1].set_color(YELLOW)
        broadcast_condition[3].set_color(PINK)
        broadcast_condition[4].set_color(YELLOW)
        
        self.play(Write(broadcast_definition))
        self.next_slide()
        
        self.play(Write(broadcast_condition))
        self.next_slide()
        
        l4_2 = Grid(1, 4, scale=0.4).next_to(broadcast_condition, DOWN, buff=MED_SMALL_BUFF)
        
        self.play(FadeIn(l4_2))
        self.next_slide()
        
        self.play(l4_2.ColorNode(0, 0, 1))
        self.next_slide()
        self.play(l4_2.ColorNode(0, 1, 2))
        self.next_slide()
        self.play(l4_2.ColorNode(0, 2, 1))
        self.next_slide()
        self.play(l4_2.ColorNode(0, 3, 3))
        
        self.next_slide()
        
        self.clear()
        
        infinite = Text("Let's look at some infinite graphs!", color=BLUE, font_size=60).to_edge(UP)
        self.play(FadeIn(infinite))
        self.next_slide()
        l14 = Grid(1, 14, scale=0.2, infinite_columns=True).next_to(infinite, DOWN, buff=LARGE_BUFF)
        self.play(FadeIn(l14))
        
        self.next_slide()
        self.play(l14.ColorNode(0, 0, 1))
        self.next_slide()
        self.play(l14.ColorNode(0, 1, 2))
        self.next_slide()
        self.play(l14.ColorNode(0, 2, 1))
        self.next_slide()
        self.play(l14.ColorNode(0, 3, 3))
        self.next_slide()
        self.play(l14.ColorNode(0, 4, 1))
        self.next_slide()
        self.play(l14.ColorNode(0, 5, 2))
        self.next_slide()
        def c(i):
            if i % 2 == 0:
                return 1
            elif i % 4 == 1:
                return 2
            else:
                return 3
        gr = []
        for i in range(6, 14):
            gr.append(l14.ColorNode(0, i, c(i)))
        self.play(*gr)
        
        self.next_slide()
        
        z1_text = Tex(r"$\chi_\rho(\mathbb{Z}) = 3$", ", easy :)")
        z1_text.set_color_by_tex("3", YELLOW)
        z1_text.next_to(l14, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(z1_text))
        
        self.next_slide()
        z12_text = Tex(r"What about ", r"$\chi_\rho(\mathbb{Z} \times P_2)$", r"?").next_to(z1_text, DOWN, buff=0.8*LARGE_BUFF)
        z12_text.set_color_by_tex("Z", YELLOW)
        l2_14 = Grid(2, 14, scale=0.2, infinite_columns=True).next_to(z12_text, DOWN, buff=MED_SMALL_BUFF)
        
        self.play(Write(z12_text), FadeIn(l2_14))
        self.next_slide()
        
        self.play(l2_14.ColorNode(0, 0, 1))
        self.next_slide()
        self.play(l2_14.ColorNode(1, 1, 1))
        self.next_slide()
        self.play(l2_14.ColorNode(0, 2, 1))
        self.next_slide()
        anim_group = []
        for i in range(3, 14):
            anim_group.append(l2_14.ColorNode(i%2, i, 1))
        self.play(*anim_group)
        self.next_slide()
        
        self.play(l2_14.ColorNode(1, 0, 2))
        self.next_slide()
        self.play(l2_14.ColorNode(0, 3, 2))
        self.next_slide()
        anim_group = []
        for i in range(6, 14, 3):
            anim_group.append(l2_14.ColorNode((1-i%2), i, 2))
        self.play(*anim_group)
        self.next_slide()
        
        self.play(l2_14.ColorNode(0, 1, 3))
        self.next_slide()
        anim_group = []
        for i in range(4, 14, 3):
            anim_group.append(l2_14.ColorNode((1-i%2), i, 3))
        self.play(*anim_group)
        self.next_slide()
        
        self.play(l2_14.ColorNode(1, 2, 4), l2_14.ColorNode(1, 8, 4))
        self.next_slide()
        self.play(l2_14.ColorNode(0, 5, 5), l2_14.ColorNode(0, 11, 5))
        self.next_slide()
        z_p2_text = Tex(r"$\chi_\rho(\mathbb{Z} \times P_2) \leq 5$", ", can we do better?")
        z_p2_text.set_color_by_tex("5", YELLOW)
        z_p2_text.next_to(l2_14, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(z_p2_text))
        self.next_slide()
        

        
class SquareGrid(Slide):
    def construct(self):
         
        back = Tex(r"Back to the standard $\mathbb{Z}^2$ grid", font_size=72, color=YELLOW).to_edge(UP)
        self.play(Write(back))   
        
        
        can_we = Text(r"What happens if we try to use the same proof?").next_to(back, DOWN, buff=MED_SMALL_BUFF)
        self.play(FadeIn(can_we))
        
        self.next_slide()
        
        z_4_4 = Grid(4, 4, scale=0.25, infinite_columns=True, infinite_rows=True, chebyshev=False).next_to(can_we, DOWN, buff=MED_LARGE_BUFF).shift(LEFT*3)
        self.play(FadeIn(z_4_4))
        self.next_slide()
        
        self.play(z_4_4.ColorNode(0, 0, 3), z_4_4.ColorNode(1, 3, 3), z_4_4.ColorNode(3, 1, 3))
        
        now_density = Tex(r"Now we can say:", r"$$\textrm{density}_{\mathbb{Z}_{\ell_1}^2}(k) \leq \frac{3}{(k+1)^2}$$").scale(0.8).next_to(z_4_4, RIGHT, buff=MED_LARGE_BUFF)
        now_density[1].set_color(PINK)
        now_density.shift(1.0*UP + 1.0*RIGHT)
        self.next_slide()
        self.play(FadeIn(now_density))
        
        self.next_slide()
        not_enough = Tex(r"But this only gives us ", r"$$\sum_{k=1}^{\infty} \frac{3}{(k+1)^2} \approx 1.93 > 1$$").scale(0.8).next_to(now_density, DOWN, buff=MED_LARGE_BUFF)
        not_enough[1].set_color(YELLOW)
        self.play(FadeIn(not_enough))
        
        self.next_slide()


class WhatToDo(Slide):
    def construct(self):
        title = Text("What can we do?", font_size=60, color=YELLOW).to_edge(UP).shift(0.5*UP)
        self.play(FadeIn(title))
        first_five_terms = Text("Idea: look more carefully at the first few densities", font_size=36, t2c={"Idea": BLUE}).next_to(title, DOWN, buff=MED_LARGE_BUFF)
        self.next_slide()
        self.play(FadeIn(first_five_terms))
        self.next_slide()
        
        # densities = Text("We :", font_size=36, t2c={"densities": BLUE}).next_to(first_five_terms, DOWN, buff=MED_LARGE_BUFF)
        d1 = Tex(r"$\blacktriangleright$", r"\, $\textrm{density}_{\mathbb{Z}_{\ell_1}^2}(1) \leq 1/2$", font_size=36)
        d2 = Tex(r"$\blacktriangleright$", r"\, $\textrm{density}_{\mathbb{Z}_{\ell_1}^2}(2) \leq 1/5$", font_size=36)
        d3 = Tex(r"$\blacktriangleright$", r"\, $\textrm{density}_{\mathbb{Z}_{\ell_1}^2}(3) \leq 1/8$", font_size=36)
        d4 = Tex(r"$\blacktriangleright$", r"\, $\textrm{density}_{\mathbb{Z}_{\ell_1}^2}(4) \leq 1/10$", font_size=36)
        d5 = Tex(r"$\blacktriangleright$", r"\, $\textrm{density}_{\mathbb{Z}_{\ell_1}^2}(5) \leq 1/16$", font_size=36)
        dens = VGroup(d1, d2, d3, d4, d5).arrange(DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT).next_to(first_five_terms, DOWN, buff=MED_SMALL_BUFF)
        for d in dens:
            d[0].set_color(BLUE)
            self.play(FadeIn(d))
            self.next_slide()
        # wolfram_img = ImageMobject("img/first_terms.png").next_to(first_five_terms, DOWN, buff=MED_LARGE_BUFF)
        # self.play(FadeIn(wolfram_img))
        # self.next_slide()
        # self.play(FadeOut(wolfram_img))
        # self.next_slide()
        only_five = Text("This only proves we need at least 6 colors", font_size=36, t2c={"at least 6": YELLOW}).next_to(dens, DOWN, buff=MED_SMALL_BUFF)
        self.play(FadeIn(only_five))
        self.next_slide()
        careful = Tex(r"A much more careful analysis was used\\to show we need at least ", r"10 ", r"colors (Fiala et al. 2009)").scale(1.0).next_to(only_five, DOWN, buff=MED_SMALL_BUFF)
        careful.set_color_by_tex(r"10", YELLOW)
        self.play(FadeIn(careful))
        self.next_slide()
        
        history = Text("History of the problem shows we need computers to solve it!", t2c={"computers": BLUE}).scale(0.7).next_to(careful, DOWN, buff=LARGE_BUFF)
        sq = SurroundingRectangle(history, buff=MED_SMALL_BUFF)
        self.play(FadeIn(history), FadeIn(sq))
        self.next_slide()


class ThisTalk(Slide):
    def construct(self):
        title = Tex(r"So... what is ", r"$\chi_\rho(\mathbb{Z}^2) = $?", font_size=72, color=YELLOW).to_edge(UP)
        title.set_color_by_tex("\chi", PINK)
        self.play(FadeIn(title))
        g12_12 = Grid(10, 10, scale=0.15, infinite_columns=True, infinite_rows=True)
        g12_12.shift(2.5*LEFT + 3.5*DOWN)
        self.play(FadeIn(g12_12))
        
        text_rec = Rectangle(height=1.5, width=6, color=BLUE, fill_opacity=0.97)
        answer = Text("Answer: 15", font_size=72, color=BLACK, t2c={'15': PINK}).center()
        this_talk = Text("Rest of the talk is about how we used SAT-solvers to prove it!", color=BLACK, t2c={'SAT-solvers': PINK}, font_size=36)
        texts = Group(answer, this_talk).arrange(DOWN, buff=MED_LARGE_BUFF)
        text_rec.surround(texts)
        
        self.next_slide()
        self.play(Create(text_rec), FadeIn(answer))
        
        self.next_slide()
        self.play(FadeIn(this_talk))
        self.next_slide()


class PackingColorings(Slide):
    def construct(self):
        
        title = Text("Packing Colorings", font_size=72, color=BLUE).to_edge(UP)
        
        self.play(FadeIn(title))
        
        origin = Tex(r"$\blacktriangleright$", r" Proposed by Goddard et al. (2002) under the name of {{broadcast colorings}}", font_size=36)
        origin.set_color_by_tex(r"broadcast colorings", YELLOW)
        name_change = Tex(r"$\blacktriangleright$", r" Brešar et al. (2007), re-interpreted the notion and called it {{packing colorings}}.", font_size=36)
        name_change.set_color_by_tex(r"packing colorings", YELLOW)
        since_then = Tex(r"$\blacktriangleright$", r" Since then, {{over 70 papers}} have studied different aspects of packing colorings.", font_size=36)
        since_then.set_color_by_tex(r"over 70 papers", PINK)
        most_important_problem = Tex(r"$\blacktriangleright$", r" The latest survey of Brešar et al. (2020) states that\\ {{the most important open problem}} with respect to infinite graphs,\\ is to find the {{packing-chromatic number of the infinite square grid}}!", font_size=40)
        most_important_problem.set_color_by_tex(r"most important open problem", BLUE)
        most_important_problem.set_color_by_tex(r"packing-chromatic number of the infinite square grid", ORANGE)
        bpoints = VGroup(origin, name_change, since_then, most_important_problem).arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT).next_to(title, DOWN, buff=LARGE_BUFF)
        
        for bpoint in bpoints:
            bpoint.set_color_by_tex(r"blacktriangleright", BLUE)
                         
        self.next_slide()
        self.play(Write(origin))                                                        
        self.next_slide()
        radio1 = ImageMobject("img/radio_antenna.png", color=WHITE).scale(1).next_to(origin, DOWN, buff=MED_LARGE_BUFF).shift(5*LEFT)
        radio2 = ImageMobject("img/radio_antenna.png", color=WHITE).scale(1).next_to(radio1, RIGHT, buff=1.5*MED_LARGE_BUFF)
        radio3 = ImageMobject("img/radio_antenna.png", color=WHITE).scale(1).next_to(radio2, RIGHT, buff=1.5*MED_LARGE_BUFF)
        radio4 = ImageMobject("img/radio_antenna.png", color=WHITE).scale(1).next_to(radio3, RIGHT, buff=1.5*MED_LARGE_BUFF)
        freq1 = Text("99.4 Mhz", font_size=42, color=config.MY_COLORS[1]).next_to(radio1, DOWN, buff=MED_SMALL_BUFF)
        freq2 = Text("99.4 Mhz", font_size=42, color=config.MY_COLORS[1]).next_to(radio2, DOWN, buff=MED_SMALL_BUFF)
        freq3 = Text("99.4 Mhz", font_size=42, color=config.MY_COLORS[1]).next_to(radio3, DOWN, buff=MED_SMALL_BUFF)
        freq4 = Text("99.4 Mhz", font_size=42, color=config.MY_COLORS[1]).next_to(radio4, DOWN, buff=MED_SMALL_BUFF)
        self.play(FadeIn(radio1), FadeIn(radio2), FadeIn(radio3), FadeIn(radio4), FadeIn(freq1), FadeIn(freq2), FadeIn(freq3), FadeIn(freq4))
        self.next_slide()
        c1 = Circle(radius=3, color=config.MY_COLORS[1]).move_to(radio1)
        c2 = Circle(radius=3, color=config.MY_COLORS[1]).move_to(radio2)
        c3 = Circle(radius=3, color=config.MY_COLORS[1]).move_to(radio3)
        c4 = Circle(radius=3, color=config.MY_COLORS[1]).move_to(radio4)
        def bdcast(c, color): 
            return Broadcast(c, n_mobs=5, focal_point=c.get_center()+0.225*UP, color=color)
       
        self.play(bdcast(c1,  config.MY_COLORS[1]), bdcast(c2,config.MY_COLORS[1]), bdcast(c3,config.MY_COLORS[1]), bdcast(c4,config.MY_COLORS[1]))
        
        self.next_slide()
        freq2_changed = Text("101.7 Mhz", font_size=42, color=config.MY_COLORS[2]).next_to(radio2, DOWN, buff=MED_SMALL_BUFF)
        self.play(Transform(freq2, freq2_changed))
        self.next_slide()
        c2 = Circle(radius=5, color=config.MY_COLORS[2]).move_to(radio2)
        self.play(bdcast(c1,  config.MY_COLORS[1]), bdcast(c2,config.MY_COLORS[2]), bdcast(c3,config.MY_COLORS[1]), bdcast(c4,config.MY_COLORS[1]))
        self.next_slide()
        freq4_changed = Text("105.3 Mhz", font_size=42, color=config.MY_COLORS[3]).next_to(radio4, DOWN, buff=MED_SMALL_BUFF)
        self.play(Transform(freq4, freq4_changed))
        self.next_slide()
        c4 = Circle(radius=7, color=config.MY_COLORS[3]).move_to(radio4)
        self.play(bdcast(c1,  config.MY_COLORS[1]), bdcast(c2,config.MY_COLORS[2]), bdcast(c3,config.MY_COLORS[1]), bdcast(c4,config.MY_COLORS[3]))
        
        
        
        self.next_slide()
        self.play(FadeOut(radio1), FadeOut(radio2), FadeOut(radio3), FadeOut(radio4), FadeOut(freq1), FadeOut(freq2), FadeOut(freq3), FadeOut(freq4))
        self.next_slide()
        
        self.play(Write(name_change))
        self.next_slide()
        self.play(Write(since_then))
        self.next_slide()
        self.play(Write(most_important_problem))
        self.next_slide()
