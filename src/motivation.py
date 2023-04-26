from manim import *
from manim_slides import Slide 
from subgraphs import Grid, to_3d
import config
import numpy as np
from empty import EmptyAnimation



class Motivation(Slide):
    def construct(self):
        # title = Text("Motivation: Frequency Assignment", color=BLUE, t2c={'Frequency Assignment':WHITE}, font_size=48)
        # title.to_edge(UP)

        # self.play(FadeIn(title))

        # self.next_slide()

        # n_ants = 5
        # ants = [ImageMobject('img/radio_antenna.png').set_color(WHITE) for i in range(n_ants)]
        # ants[0].move_to((-4, 0, 0))
        # lines = []
        # for i in range(1, n_ants):
        #     ants[i].next_to(ants[i-1], RIGHT, buff=MED_LARGE_BUFF)
        #     lines.append(Line(ants[i-1].get_center(), ants[i].get_center(), buff=0.2))

        # antennas = Group(*ants)
        # lines = Group(*lines)
        # self.play(FadeIn(antennas), FadeIn(lines))

        # self.next_slide()

        # freq_subtitle = Text("Each station must be assigned a radio frequency — avoid conflicts!", font_size=28, color=YELLOW).next_to(antennas, DOWN, buff=LARGE_BUFF)
        # self.play(Write(freq_subtitle), run_time=0.8)

        # self.next_slide()

        # f2 = Text("101.7 MHz", color=config.MY_COLORS[1], font_size=24).next_to(ants[2], UP, MED_SMALL_BUFF)

        # self.play(Write(f2), ants[2].animate.set_color(config.MY_COLORS[1]))
        # self.next_slide()

        # f3 = Text("101.9 MHz", color=config.MY_COLORS[2], font_size=24).next_to(ants[3], UP, MED_SMALL_BUFF)

        # self.play(Write(f3), ants[3].animate.set_color(config.MY_COLORS[2]))
        # self.next_slide()

        # f0, f1, f4 = f2.copy(), f3.copy(), f2.copy()
        # f0.next_to(ants[0], UP, MED_SMALL_BUFF)
        # f1.next_to(ants[1], UP, MED_SMALL_BUFF)
        # f4.next_to(ants[4], UP, MED_SMALL_BUFF)
        
        # self.play(*[FadeIn(f) for f in [f0, f1, f4]], 
        #           *[ants[ant].animate.set_color(config.MY_COLORS[2] if ant%2 else config.MY_COLORS[1]) for ant in [0, 1, 4]])

        # self.next_slide()
        
        # self.play(*[Transform(f, Text("1", color=config.MY_COLORS[1], font_size=26).move_to(f)) for f in [f0, f2, f4]])
        # self.next_slide()
        # self.play(*[Transform(f, Text("2", color=config.MY_COLORS[2], font_size=26).move_to(f)) for f in [f1, f3]])
         
        # self.next_slide()
        
        # self.play(*[FadeOut(f) for f in [f0, f1, f2, f3, f4]],
        #           *[ant.animate.set_color(WHITE) for ant in ants])
        
        # self.next_slide()
        
        # self.play(ants[3].animate.scale(1.75), freq_subtitle.animate.shift(0.5*DOWN))
        # self.next_slide()
        
        # self.play(ants[3].animate.set_color(config.MY_COLORS[2]), FadeIn(f3), f3.animate.shift(0.3*UP))
        # self.next_slide()
        
        # self.play(*[ant.animate.set_color(config.MY_COLORS[1]) for ant in [ants[2], ants[4]]], FadeIn(f2), FadeIn(f4))
        # self.next_slide()
        
        # self.play(ants[1].animate.scale(2))
        # self.next_slide()
        # self.play(ants[1].animate.set_color(config.MY_COLORS[3]),
        #           FadeIn(f1),
        #           Transform(f1, Text("3", color=config.MY_COLORS[3], font_size=26).move_to(f1).shift(0.3*UP)),
        #          )
        # self.next_slide()
        
        # self.play(ants[0].animate.set_color(config.MY_COLORS[1]), FadeIn(f0))
        
        # self.next_slide()
        
        # broadcast_coloring = Text("This is the basic idea of Broadcast Colorings (Goddard et al., 2002)", t2c={'Broadcast Colorings': YELLOW}, font_size=28).next_to(antennas, DOWN, buff=MED_LARGE_BUFF)
        
        # self.play(Transform(freq_subtitle, broadcast_coloring))
        
        # self.next_slide()
        
        # self.clear()
        
        self.play(EmptyAnimation())
        self.next_slide()
        
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
        
        self.clear()
        
        z2 = Tex(r"What about ", r"$\mathbb{Z}^2$", r"?", font_size=72).set_color_by_tex("Z", YELLOW)
        z2.to_edge(UP)
        
        g12_12 = Grid(10, 10, scale=0.15, infinite_columns=True, infinite_rows=True).next_to(z2, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(z2), FadeIn(g12_12))
        
        text_rec = Rectangle(height=1.5, width=6, color=YELLOW, fill_opacity=1)
        answer = Text("Answer: 15", font_size=72, color=BLACK, t2c={'15': PINK}).center()
        this_talk = Text("This talk is about how we used SAT-solving to prove it!", color=BLACK, t2c={'SAT-solving': BLUE}, font_size=36)
        texts = Group(answer, this_talk).arrange(DOWN, buff=MED_LARGE_BUFF)
        text_rec.surround(texts)
        
        self.next_slide()
        self.play(Create(text_rec), FadeIn(answer))
        
        self.next_slide()
        self.play(Write(this_talk))
        self.next_slide()
        
        self.clear()
        
        title = Text("Packing Colorings", font_size=72, color=BLUE).to_edge(UP)
        
        self.play(FadeIn(title))
        
        origin = Tex(r"$\blacktriangleright$", r" Proposed by Goddard et al. (2002) under the name of {{broadcast colorings}}", font_size=36)
        origin.set_color_by_tex(r"broadcast colorings", YELLOW)
        name_change = Tex(r"$\blacktriangleright$", r" Brešar et al. (2007), re-interpreted the notion and called it {{packing colorings}}.", font_size=36)
        name_change.set_color_by_tex(r"packing colorings", YELLOW)
        since_then = Tex(r"$\blacktriangleright$", r" Since then, {{over 70 papers}} have studied different aspects of packing colorings.", font_size=36)
        since_then.set_color_by_tex(r"over 70 papers", PINK)
        most_important_problem = Tex(r"$\blacktriangleright$", r" The latest survey of Brešar et al. (2020) states that\\ {{the most important open problem}} with respect to infinite graphs,\\ is to find the {{packing-chromatic number of the infinite square grid}}!", font_size=36)
        most_important_problem.set_color_by_tex(r"most important open problem", BLUE)
        most_important_problem.set_color_by_tex(r"packing-chromatic number of the infinite square grid", ORANGE)
        bpoints = VGroup(origin, name_change, since_then, most_important_problem).arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT).next_to(title, DOWN, buff=LARGE_BUFF)
        
        for bpoint in bpoints:
            bpoint.set_color_by_tex(r"blacktriangleright", BLUE)
                         
        self.next_slide()
        self.play(Write(origin))                                                        
        self.next_slide()
        self.play(Write(name_change))
        self.next_slide()
        self.play(Write(since_then))
        self.next_slide()
        self.play(Write(most_important_problem))
        self.next_slide()
        

   