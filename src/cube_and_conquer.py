from manim import *
from manim_slides import Slide
from subgraphs import Diamond

class CubeAndConquer(Slide):
    def construct(self):
        title = Text("Cube and Conquer", color=YELLOW, font_size=72)
        title.to_edge(UP)
        
        self.play(FadeIn(title))
        self.next_slide()
        
        general  = Text("General divide-and-conquer paradigm for SAT solving (Heule et al. 2012)", t2c={'divide-and-conquer': PINK}, font_size=30)
        general.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        
        self.play(FadeIn(general))
        assume = Tex(r"We have a CNF formula {{$\varphi$}} and a \ul{tautological} DNF {{$\phi = \bigvee\limits_{i=1}^m C_i$}}", font_size=36)
        assume.next_to(general, DOWN, buff=MED_LARGE_BUFF)
        assume.set_color_by_tex(r"\varphi", YELLOW)
        assume.set_color_by_tex(r"\phi", RED)
        
        self.next_slide()
        self.play(Write(assume))
        
        formula = MathTex(r"{{\textrm{SAT}}}({{\varphi}})", r"\iff {{\textrm{SAT}}}({{\varphi}} \land {{\phi}})", r"\iff",  r"{{\bigvee_{i = 1}^m}} {{\textrm{SAT}}}({{\varphi}} \land {{C_i}})", font_size=36)
        formula.set_color_by_tex(r"SAT", BLUE)
        formula.set_color_by_tex(r"\varphi", YELLOW)
        formula.set_color_by_tex(r"\phi", RED)
        formula.set_color_by_tex(r"C_i", RED)
        formula.set_color_by_tex(r"\bigvee", RED)
        rec_formula = Rectangle(width=1.2*formula.get_width(), height=1.2*formula.get_height(), color=BLUE)
        
        parallel = BraceLabel(formula[12:], r"\text{Solve in parallel}", DOWN, font_size=30, 
            label_constructor=lambda text, **kwargs: MathTex(text, **kwargs, color=PINK)).set_color(PINK)
        parallel.shift(0.8*DOWN)
        parallel[1].shift(0.2*UP)
        
        formula.next_to(assume, DOWN, buff=MED_LARGE_BUFF)
        rec_formula.move_to(formula.get_center())
        
        
        
        self.next_slide()
        formula_parts = [formula[0:4], formula[4:11], formula[11:]]
        
        for part in formula_parts:
            self.play(FadeIn(part))
            self.next_slide()
            
        self.play(Create(rec_formula))
        self.next_slide()
        self.play(FadeIn(parallel))
        self.next_slide()
        
        intuition = Tex(r"{{Intuition}}: the cubes of {{$\phi$}} represent an \ul{exhaustive} {{split}} of the problem into cases", font_size=38)
        intuition.set_color_by_tex(r"\phi", RED)
        intuition.set_color_by_tex(r"split", PINK)
        intuition.set_color_by_tex(r"Intuition", YELLOW)
        
        intuition.next_to(rec_formula, DOWN, buff=1.2*LARGE_BUFF)
        
        self.play(Write(intuition))
        
        self.next_slide()
        
        self.play(FadeOut(intuition), FadeOut(parallel), FadeOut(rec_formula), FadeOut(formula),
                    FadeOut(assume), FadeOut(general))
                    
    
        
        art = Text("The art of Cube and Conquer is about designing a good split into cases.", color=BLUE, font_size=30)
        art.next_to(title, DOWN, buff=MED_SMALL_BUFF)
        self.next_slide()
        self.play(FadeIn(art))
        
        number = Tex(r"$\blacktriangleright$", r" Number of cases: ", r"too few and we waste parellelism, ", r"too many and we waste the power of CDCL", font_size=36)
        number.set_color_by_tex(r"Number of cases", YELLOW)
        number.set_color_by_tex(r"\blacktriangleright", BLUE)
        
        similar_difficulty = Tex(r"$\blacktriangleright$", r" Similar difficulty: ", r"ideally the cases are similar in difficulty", font_size=36)
        similar_difficulty.set_color_by_tex(r"Similar difficulty", YELLOW)
        similar_difficulty.set_color_by_tex(r"\blacktriangleright", BLUE)
        
        previous_work = Tex(r"$\blacktriangleright$", r" Previous work: ", r"we did a split directly over the {{direct variables}}.\\ {{Example case}}: {{ $x_{(4,3), 5} \land x_{(9, 0), 13} \land \overline{x_{(3, 3), 7} } $}}", font_size=36)
        previous_work.set_color_by_tex(r"Previous work", YELLOW)
        previous_work.set_color_by_tex(r"\blacktriangleright", BLUE)
        previous_work.set_color_by_tex(r"Example case", PINK)
        previous_work.set_color_by_tex(r"\land", BLUE)
        
        
        this_work = Tex(r"$\blacktriangleright$", r" This work: ", r"we do a split over the {{Plus auxiliary variables}}. \\ {{Example case}}: {{$y_{(2,1), 7} \land y_{(4,5), 9} \land \overline{y_{(5,3), 11} } $}}", font_size=36)
        this_work.set_color_by_tex(r"This work", YELLOW)
        this_work.set_color_by_tex(r"\blacktriangleright", BLUE)
        this_work.set_color_by_tex(r"Example case", PINK)
        this_work.set_color_by_tex(r"\land", BLUE)
        
        bullets = VGroup(number, similar_difficulty, previous_work, this_work)
        bullets.arrange(DOWN, buff=1.3*MED_LARGE_BUFF, aligned_edge=LEFT)
        bullets.next_to(art, DOWN, buff=MED_LARGE_BUFF)
        
        for bullet in bullets:
            self.play(Write(bullet))
            self.next_slide()
            
        self.play(FadeOut(number), FadeOut(similar_difficulty), FadeOut(previous_work), FadeOut(art), this_work.animate.shift(5*UP))
        
        why_is_this_better = Tex(r"{{Why}} is this better?", font_size=56).center().shift(0.1*UP)
        why_is_this_better.set_color_by_tex(r"Why", YELLOW)
        
        self.next_slide()
        self.play(Write(why_is_this_better))
        
        old_split = Text("Old split", font_size=30)
        new_split = Text("New split", font_size=30)
        
        old_split.next_to(why_is_this_better, DOWN, buff=0.5*LARGE_BUFF)
        new_split.next_to(why_is_this_better, DOWN, buff=0.5*LARGE_BUFF)
        
        old_split.shift(2*LEFT)
        new_split.shift(2*RIGHT)
        
        arr_old = Arrow(why_is_this_better.get_center()+0.15*DOWN, old_split.get_center()+0.2*UP, color=BLUE, stroke_width=3)
        arr_new = Arrow(why_is_this_better.get_center()+0.15*DOWN, new_split.get_center()+0.2*UP, color=BLUE, stroke_width=3)
        
        self.next_slide()
        self.play(FadeIn(old_split), FadeIn(new_split), FadeIn(arr_old), FadeIn(arr_new))
        
        old_var = Tex(r"$x_{(4,3), 5}$", font_size=42).next_to(old_split, DOWN, buff=MED_LARGE_BUFF)
        new_var = Tex(r"$y_{(2,1), 7}$", font_size=42).next_to(new_split, DOWN, buff=MED_LARGE_BUFF)
        
        old_var_arr = Arrow(old_split.get_center(), old_var.get_center()+0.1*DOWN, color=BLUE, stroke_width=3, max_stroke_width_to_length_ratio=100)
        new_var_arr = Arrow(new_split.get_center(), new_var.get_center()+0.1*DOWN, color=BLUE, stroke_width=3, max_stroke_width_to_length_ratio=100)
        
        self.next_slide()
        self.play(FadeIn(old_var), FadeIn(new_var), FadeIn(old_var_arr), FadeIn(new_var_arr))
        
        old_pos = Tex(r"Positive", font_size=36).next_to(old_var, DOWN, buff=MED_LARGE_BUFF)
        old_pos.shift(1*LEFT)
        
        old_neg = Tex(r"Negative", font_size=36).next_to(old_var, DOWN, buff=MED_LARGE_BUFF)
        old_neg.shift(1*RIGHT)
        
        old_pos_arr = Arrow(old_var.get_center()+0.1*DOWN, old_pos.get_center()+0.1*UP, color=GREEN, stroke_width=3)
        old_neg_arr = Arrow(old_var.get_center()+0.1*DOWN, old_neg.get_center()+0.1*UP, color=RED, stroke_width=3)
        
        new_pos = Tex(r"Positive", font_size=36).next_to(new_var, DOWN, buff=MED_LARGE_BUFF)
        new_pos.shift(1*LEFT)
        
        new_neg = Tex(r"Negative", font_size=36).next_to(new_var, DOWN, buff=MED_LARGE_BUFF)
        new_neg.shift(1*RIGHT)
        
        new_pos_arr = Arrow(new_var.get_center()+0.1*DOWN, new_pos.get_center()+0.1*UP, color=GREEN, stroke_width=3)
        new_neg_arr = Arrow(new_var.get_center()+0.1*DOWN, new_neg.get_center()+0.1*UP, color=RED, stroke_width=3)
        
        old_pos_label = Tex(r"\blacksmiley{} \blacksmiley{}", color=GREEN)
        old_neg_label = Tex(r"\frownie{}", color=RED)
        
        new_pos_label = Tex(r"\blacksmiley{}", color=GREEN)
        new_neg_label = Tex(r"\blacksmiley{}", color=GREEN)
        
        old_pos_label.next_to(old_pos, DOWN, buff=0.7*MED_SMALL_BUFF)
        old_neg_label.next_to(old_neg, DOWN, buff=MED_SMALL_BUFF)
        old_neg_label.set_y(old_pos_label.get_y())
        
        new_pos_label.next_to(new_pos, DOWN, buff=MED_SMALL_BUFF)
        new_pos_label.set_y(old_pos_label.get_y())
        new_neg_label.next_to(new_neg, DOWN, buff=MED_SMALL_BUFF)
        new_neg_label.set_y(old_pos_label.get_y())
        
        self.next_slide()
        self.play(FadeIn(old_pos), FadeIn(old_pos_arr))
        self.next_slide()
        self.play(FadeIn(old_pos_label))
        
        self.next_slide()
        self.play(FadeIn(old_neg), FadeIn(old_neg_arr))
        self.next_slide()
        self.play(FadeIn(old_neg_label))
        
        self.next_slide()
        self.play(FadeIn(new_pos), FadeIn(new_pos_arr))
        self.next_slide()
        self.play(FadeIn(new_pos_label))
        
        self.next_slide()
        self.play(FadeIn(new_neg), FadeIn(new_neg_arr))
        self.next_slide()
        self.play(FadeIn(new_neg_label))
        
        remember = Tex(r"$\bigstar$", color=YELLOW, font_size=60)
        parallelism = Tex(r"For parallelism {{the more balanced the better}}!", color=YELLOW, font_size=36)
        parallelism.set_color_by_tex(r"balanced", YELLOW)
        parallelism.next_to(new_neg_label, DOWN, buff=MED_SMALL_BUFF)
        parallelism.shift(2.8*LEFT)
        remember.next_to(new_split, RIGHT, buff=MED_SMALL_BUFF)
        remember.shift(0.1*UP)
        
        
        self.next_slide()
        self.play(FadeIn(remember), FadeIn(parallelism))
        
        self.next_slide()
        self.play(FadeOut(remember), FadeOut(parallelism), FadeOut(new_neg), FadeOut(why_is_this_better), FadeOut(old_split),
        FadeOut(new_split), FadeOut(new_pos), FadeOut(old_pos), FadeOut(old_neg), FadeOut(old_pos_label),
            FadeOut(old_pos_arr), FadeOut(new_pos_arr), FadeOut(new_pos_label), FadeOut(old_neg_arr), FadeOut(old_neg_label),
            FadeOut(new_neg_arr), FadeOut(new_neg_label), FadeOut(this_work), FadeOut(old_var), FadeOut(new_var), FadeOut(old_var_arr),
            FadeOut(new_var_arr), FadeOut(arr_new), FadeOut(arr_old))
            
        self.next_slide()
        
        super_linear_speedup = Tex(r"We get linear speed-ups!", font_size=60).next_to(title, DOWN, buff=0.8*LARGE_BUFF)
        
        to_prove = Tex(r"Proving that $\chi_\rho(D_6) \geq 12$, with $6$ in the center", color=YELLOW).next_to(super_linear_speedup, DOWN, buff=MED_LARGE_BUFF)
        improvement = MathTex(r"{{ \text{Sequential} }}: \; & \quad 811.6s\\ {{ \text{Cube and Conquer } }} (128 \text{cores}): \; & \quad 6.6s", font_size=60).next_to(to_prove, DOWN, buff=MED_LARGE_BUFF)
        quotient = MathTex(r"\frac{811.6}{6.6} {{\sim}} 123 {{\sim}} 128.").next_to(improvement, DOWN, buff=MED_LARGE_BUFF)
        
        improvement.set_color_by_tex("Sequential", PINK)
        improvement.set_color_by_tex("Cube and Conquer", PINK)
        quotient.set_color_by_tex("\sim", BLUE)
        
        self.play(FadeIn(super_linear_speedup))
        self.next_slide()
        self.play(FadeIn(to_prove))
        self.next_slide()
        self.play(FadeIn(improvement))
        self.next_slide()
        self.play(FadeIn(quotient))
        self.next_slide()