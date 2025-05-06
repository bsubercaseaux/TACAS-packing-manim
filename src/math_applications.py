from manim import *
from manim_slides import Slide
from subgraphs import Grid
import config
import numpy as np
from empty import EmptyAnimation


class MathApplications(Slide):
    def construct(self):
        stories = Text(
            "Successes of SAT in Math problems:", font_size=58, color=BLUE
        ).to_edge(UP)
        self.play(FadeIn(stories))
        list_of_successes = BulletedList(
            "(2014) Boolean Erdős Discrepancy Problem",
            "(2016) Boolean Pytagorean Triples Problem",
            "(2018) Schur Number Five",
            "(2019) Keller's Conjecture",
            r"(2023) Packing-Chromatic Number of $\mathbb{Z}^2$",
            r"(2024) Empty Hexagon Number",
            font_size=42,
        ).next_to(stories, DOWN, buff=MED_LARGE_BUFF)
        list_of_successes[4].set_color(YELLOW)
       
        self.next_slide()
        for bullet in list_of_successes:
            self.play(Write(bullet))
            self.next_slide()
        success = Text(
            "Their success is due to a combination of factors!", font_size=38
        ).next_to(list_of_successes, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(success))
        self.next_slide()
        self.play(FadeOut(list_of_successes), success.animate.shift(4.5 * UP))
        success_bullets = BulletedList(
            "Hardware advances",
            "Software advances",
            "Better encodings and automated-reasoning techniques",
            font_size=50,
        ).next_to(success, DOWN, buff=MED_LARGE_BUFF)
        success_bullets[1].set_color(ORANGE)
        success_bullets[2].set_color(PURE_GREEN)
        self.play(FadeIn(success_bullets[0]))
        self.next_slide()
        self.play(FadeIn(success_bullets[1]))
        self.next_slide()
        plot = ImageMobject("img/SatCompetition2023.png").scale(0.75)
        self.play(FadeIn(plot))
        self.next_slide()
        self.play(FadeOut(plot))
        self.next_slide()
        self.play(FadeIn(success_bullets[2]))
        self.next_slide()
        self.play(FadeOut(stories), FadeOut(success_bullets), FadeOut(success))
        self.next_slide()
        p_examples = Text(
            "In my own research:", font_size=48, color=BLUE
        ).to_edge(UP)
        self.play(FadeIn(p_examples))
        self.next_slide()
        
        gadget_cons = Text("Building gadgets for NP-hardness proofs", font_size=36).next_to(p_examples, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(gadget_cons))
        self.next_slide()
        
        gadget_1 = ImageMobject("img/gadget_1.jpg").next_to(gadget_cons, DOWN, buff=MED_LARGE_BUFF)
        gadget_2 = ImageMobject("img/gadget_2.jpg").next_to(gadget_cons, DOWN, buff=MED_LARGE_BUFF)
        gadget_3 = ImageMobject("img/gadget_3.jpg").next_to(gadget_cons, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(gadget_1))
        self.next_slide()
        self.play(FadeOut(gadget_1), FadeIn(gadget_2))
        self.next_slide()
        self.play(FadeOut(gadget_2), FadeIn(gadget_3))
        self.next_slide()
        
        self.play(FadeOut(gadget_3), FadeOut(gadget_cons), FadeOut(p_examples))
        
        rubiks = Text("A big success of computational math: Rubik's cube diameter is 20", t2c={"Rubik's cube diameter is 20": YELLOW}, font_size=32).to_edge(UP)
        self.play(FadeIn(rubiks))
        self.next_slide()
        opposite = Text("I'm interested in the opposite question: how slowly can we solve it?", t2c={"how slowly": BLUE}, font_size=32).next_to(rubiks, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(opposite))
        self.next_slide()
        related_to = Text("Related to several conjectures of Lovász\n on Hamiltonian-connectedness of Cayley graphs", t2c={"Cayley graphs": PINK}, font_size=32).next_to(opposite, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(related_to))
        self.next_slide()
        
        graph123 = ImageMobject("img/1x2x3_graph.jpg").next_to(related_to, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(graph123))
        self.next_slide()