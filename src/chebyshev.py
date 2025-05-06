from manim import *
from manim_slides import Slide 
from subgraphs import Grid
import config
import numpy as np
from empty import EmptyAnimation


class Chebyshev(Slide):
    def construct(self):
        ch_title = Tex(r"Amazing example: ", r"Chebyshev's grid", font_size=72, color=YELLOW).set_color_by_tex("Chebyshev's grid", BLUE)
        ch_title.to_edge(UP)

        ch7_10 = Grid(7, 12, scale=0.25, infinite_columns=True, infinite_rows=True, chebyshev=True).next_to(ch_title, DOWN, buff=MED_LARGE_BUFF)
        ch4_4 = Grid(4, 4, scale=0.25, infinite_columns=True, infinite_rows=True, chebyshev=True).next_to(ch_title, DOWN, buff=MED_LARGE_BUFF)
        
        self.play(Write(ch_title), FadeIn(ch7_10))
        
        
        
        self.next_slide()
        sq = Square(side_length=4, color=RED)
        sqL = Square(side_length=4, color=BLUE).next_to(sq, LEFT, buff=0)
        sqR = Square(side_length=4, color=GREEN).next_to(sq, RIGHT, buff=0)
        self.play(Succession(Create(sqL), Create(sq), Create(sqR)))
        self.next_slide()
        self.play(FadeTransform(ch7_10, ch4_4), FadeOut(sqL), FadeOut(sqR))
        self.next_slide()      

        
        ones = Tex(r"Let's start\\ by placing ", r"1", r"'s").scale(0.8).next_to(ch4_4, LEFT, buff=MED_LARGE_BUFF)
        ones.set_color_by_tex("1", PINK)
        
        self.play(FadeIn(ones))
        self.next_slide()
        
        one_positions = [(0, 0), (0, 2), (2, 0), (2, 2)]
        
        
        self.play(*[ch4_4.ColorNode(p[0], p[1], 1) for p in one_positions])
        self.next_slide()
        
        only_one = Tex(r"We can cover at most\\ a $\frac{4}{16} = 0.25$ fraction!", color=YELLOW).scale(0.8).next_to(ch4_4, RIGHT, buff=MED_LARGE_BUFF)
        self.play(FadeIn(only_one))
        
        self.next_slide()
        density_one = Tex(r"This is a ``\emph{density}'' argument: ",  r"$\textrm{density}_{\mathbb{Z}_{\text{Ch}}^2}(1) \leq 1/4$").next_to(ch4_4, DOWN, buff=MED_SMALL_BUFF)
        density_one[1].set_color(PINK)
        self.play(FadeIn(density_one)) 
        
       
        self.next_slide()
        
        MATH_SIGNAL = False
        if MATH_SIGNAL:
            rec = RoundedRectangle(height=2.5, width=13.5, corner_radius=0.2, color=WHITE, fill_color=WHITE, fill_opacity=1)
            
            math_signal = ImageMobject("img/math_signal.png").scale(0.25)
            math_signal.shift(5.75*LEFT)
            gen_density = MathTex(r"\textrm{density}_{G}(k) =  \sup_{f} \sup_{v \in V(G)} \limsup_{r \to \infty} \frac{|f^{-1}(k) \cap B(v, r)|}{|B(v, r)|}", color=BLACK)
            
            gen_density.next_to(math_signal, RIGHT, buff=MED_LARGE_BUFF)
            self.play(FadeIn(rec), FadeIn(math_signal), FadeIn(gen_density))
            
            self.next_slide()
            self.play(FadeOut(rec), FadeOut(math_signal), FadeOut(gen_density))
            self.next_slide()
        
       
        self.play(FadeOut(sq))
        self.play(FadeOut(ones), FadeOut(only_one), FadeOut(density_one), ch4_4.animate.shift(LEFT*4))
        
        wbuthree = Tex(r"What about the ", r"3", r"'s?").next_to(ch4_4, RIGHT, buff=MED_LARGE_BUFF).shift(1*UP + 0.5*RIGHT)
        wbuthree.set_color_by_tex("3", BLUE)
        
        self.next_slide()
        self.play(FadeIn(wbuthree))
        self.next_slide()
        self.play(ch4_4.ColorNode(3, 3, 3))
        
        self.next_slide()
        only_three = Tex(r"We can cover at most\\ a $\frac{1}{16} = 0.0625$ fraction!", color=YELLOW).next_to(wbuthree, DOWN, buff=LARGE_BUFF).shift(0.5*RIGHT)
        self.play(FadeIn(only_three))
        self.next_slide()
        density_three = Tex(r"$\textrm{density}_{\mathbb{Z}_{\text{Ch}}^2}(3) \leq 1/16$", color=PINK).next_to(only_three, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(density_three))
        self.next_slide()
        
        self.play(FadeOut(wbuthree), FadeOut(only_three), FadeOut(density_three), FadeOut(ch4_4))
        
        ## general case:
        
        self.next_slide()
        general_case = Tex(r"In general, $\textrm{density}_{\mathbb{Z}_{\text{Ch}}^2}(k) \leq \frac{1}{(k+1)^2}$").next_to(ch_title, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(general_case))
        total_density = Tex(r"So we cannot color more than a $\sum_{k=1}^{\infty} \frac{1}{(k+1)^2}$ fraction!", color=YELLOW).next_to(general_case, DOWN, buff=MED_SMALL_BUFF)
        self.next_slide()
        self.play(FadeIn(total_density))
        argument = MathTex(r"\sum_{k=1}^{\infty} \frac{1}{(k+1)^2} &= \left(\sum_{k=1}^{\infty} \frac{1}{k^2}\right) - 1", r"\\&= \frac{\pi^2}{6} - 1", r"\approx 0.645 < 1").next_to(total_density, DOWN, buff=MED_SMALL_BUFF)
        self.next_slide()
        self.play(Write(argument[0]))
        self.next_slide()
        # euler = ImageMobject("img/euler.jpeg").scale(0.4).next_to(argument[1], RIGHT, buff=LARGE_BUFF)
        # euler_text = Text("PLEASE LOOK UP THE ORIGINAL PROOF!", color=RED).scale(0.4).next_to(euler, DOWN, buff=MED_SMALL_BUFF)
        # self.play(FadeIn(euler), FadeIn(euler_text))
        self.next_slide()
        self.play(Write(argument[1].set_color(PINK)))
        
        
        
     
        # self.next_slide()
        # self.play(FadeOut(euler), FadeOut(euler_text))
        self.next_slide()
        self.play(Write(argument[2].set_color(BLUE)))
        
        self.next_slide()
        
        naw = ImageMobject("img/NAW_cover.png").scale(0.5)
        naw_text = Text("Link: bit.ly/eulerProof", t2c={'bit.ly/eulerProof': BLUE}).next_to(naw, DOWN, buff=MED_SMALL_BUFF)
        self.play(FadeIn(naw_text), FadeIn(naw))
        
        self.next_slide()
