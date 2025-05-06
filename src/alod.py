from manim import *
from manim_slides import Slide 
from subgraphs import Diamond
from empty import EmptyAnimation

class Alod(Slide):
    def construct(self):
        title = Tex(r"{{\textsc{Alod} }} (At-Least-One-Distance) clauses", font_size=72).to_edge(UP)
        title.set_color_by_tex("Alod", YELLOW)
        
        idea = Tex(r"{{ Idea: }} every sub-$D_1$ must contain a 1.", font_size=48)
        idea.set_color_by_tex("Idea", BLUE)
        idea.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        
        self.play(FadeIn(title))
        self.next_slide()
        
        self.play(Write(idea))
        
        self.next_slide()
        
        assignment_no_alod = {
            (-3, 0): 1,
            (-2, 0): 2,
            (-1, 0): 1,
            (0, 0): 3,
            (1, 0): 1,
            (2, 0): 2,
            (3, 0): 1,
            (-2, -1): 1,
            (-1, -1): 4,
            (0, -1): 1,
            (1, -1): 5,
            (2, -1): 1,
            (-1, -2): 1,
            (0, -2): 2,
            (1, -2): 1,
            (0, -3): 1,
            (-2, 1): 1,
            (-1, 1): 6,
            (0, 1): 1,
            (1, 1): 7,
            (2, 1): 1,
            (-1, 2): 1,
            (0, 2): 2,
            (1, 2): 4,
            (0, 3): 1,
        }
        
        assignment_alod = {
            (-3, 0): 1,
            (-2, 0): 2,
            (-1, 0): 1,
            (0, 0): 3,
            (1, 0): 1,
            (2, 0): 2,
            (3, 0): 1,
            (-2, -1): 1,
            (-1, -1): 4,
            (0, -1): 1,
            (1, -1): 5,
            (2, -1): 1,
            (-1, -2): 1,
            (0, -2): 2,
            (1, -2): 1,
            (0, -3): 1,
            (-2, 1): 1,
            (-1, 1): 6,
            (0, 1): 1,
            (1, 1): 7,
            (2, 1): 1,
            (-1, 2): 1,
            (0, 2): 2,
            (1, 2): 1,
            (0, 3): 1,
        }
        
        d_3_no_alod = Diamond(3, scale=0.5, node_constructor=Square, color=WHITE, assignment=assignment_no_alod)
        d_3_alod = Diamond(3, scale=0.5, node_constructor=Square, color=WHITE, assignment=assignment_alod)
        
        d_3_no_alod.next_to(idea, DOWN, buff=MED_LARGE_BUFF)
        d_3_alod.next_to(idea, DOWN, buff=MED_LARGE_BUFF)
        d_3_no_alod.shift(LEFT*2.5)
        d_3_alod.shift(RIGHT*2.5)
        
        label_alod = Tex(r"with {{\textsc{Alod}}}", font_size=36).next_to(d_3_alod, DOWN, buff=MED_SMALL_BUFF)
        label_no_alod = Tex(r"without {{\textsc{Alod}}}", font_size=36).next_to(d_3_no_alod, DOWN, buff=MED_SMALL_BUFF)
        label_alod.set_color_by_tex("Alod", YELLOW)
        label_no_alod.set_color_by_tex("Alod", YELLOW)
        
        
        self.play(FadeIn(d_3_no_alod), Write(label_no_alod))
        self.next_slide()
        self.play(FadeIn(d_3_alod), Write(label_alod))
        self.next_slide()
        
        correctness = Tex(r"{{ Correctness: }} if not \textsc{Alod}, we can always set the center of $D_1$ to $1$.", font_size=36).next_to(d_3_alod, DOWN, buff=1.5*MED_LARGE_BUFF)
        correctness.set_color_by_tex("Correctness", BLUE)
        correctness.shift(2*LEFT)
        self.play(Write(correctness))
        why = Tex(r"{{ Why does it help? }} makes solutions more structured (?)", font_size=36).next_to(correctness, DOWN, buff=MED_SMALL_BUFF)
        why.set_color_by_tex("Why", BLUE)
        self.next_slide()
        self.play(Write(why))
        self.next_slide()
        
        ablation_title = Tex(r"{{ Ablation Study }}", color=YELLOW, font_size=72).to_edge(UP)
        
        self.play(FadeOut(idea), FadeOut(correctness), FadeOut(why), FadeOut(label_alod), FadeOut(label_no_alod), FadeOut(d_3_alod), FadeOut(d_3_no_alod), FadeOut(title), FadeIn(ablation_title))
        
        # table = Table(
        #     [["935", "1559", "1039"],
        #     ["21086", "3928", "7548"],
        #     ["10774", "2539", "811"]],
        #     row_labels=[Text("# of vars"), Text("# of clauses"), Text("CDCL time [s]")],
        #     col_labels=[Text("direct"), Text("BVA"), Text("Plus")],
        #     top_left_entry=Tex(r'$\chi_\rho(D_6) \geq 12$', font_size=60, color=BLUE))
        
        table_tex = Tex(r'''\begin{tabular}{c@{~~~}c@{~~~}c@{~~~}|@{~~~}c@{~~~~}c@{~~~~}c@{~~~}|@{~~~}c@{~~~}c@{~~~}c}
		\toprule
			sym & {\sc alod} & {\sf Plus} & \#var & \#cls & runtime [s] & derivation & proof & check [s]\\ \midrule
  & &  & \phantom{0}935 & 21086 & 10741 & 0 b & 11.99 Gb & 31731\\
 & & x  & 1039 & \phantom{0}7548 & \phantom{00}809  & 149 Kb & \phantom{0}1.29 Gb & \phantom{0}1720\\
  & x & & \phantom{0}935 & 21171 & \phantom{0}8422 & 1.6 Kb & \phantom{0}8.11 Gb & 21732\\
 & x & x & 1039 & \phantom{0}7633 & \phantom{00}389 & 151 Kb & \phantom{0}1.29 Gb & \phantom{0}1708\\
x   & & & \phantom{0}935 & 21286 & \phantom{00}273& 436 Mb & \phantom{0}0.63 Gb  & \phantom{0}1390\\ % direct
 x & & x & 1039 & \phantom{0}7748 & \phantom{000}66 & 436 Mb & \phantom{0}0.14 Gb & \phantom{0}1022\\ 
  x & x & & \phantom{0}935 & 21371 & \phantom{00}252 & 436 Mb & \phantom{0}0.68 Gb& \phantom{0}1359\\ % direct
 x & x & x & 1039 &  \phantom{0}7833 & \phantom{000}55 & 436 Mb & \phantom{0}0.10 Gb & \phantom{00}997 \\  %
			 \bottomrule
\end{tabular}''')
        table_tex.scale(0.7)
            
        table_tex.next_to(title, DOWN, buff=LARGE_BUFF)
        
        single_core = Text("(All experiments run in a single core)", color=BLUE, font_size=32).next_to(table_tex, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(table_tex), Write(single_core))
        self.next_slide()
        
