from manim import *
from manim_slides import Slide
from subgraphs import Diamond
import config

class PlusEncoding(Slide):
    def construct(self):
        title = Tex(r"Plus Encoding", r" for $\chi_\rho(D_r) \leq k$", font_size=64).to_edge(UP)
        title.set_color_by_tex(r"Plus Encoding", PINK)
        
        self.play(FadeIn(title))
        
        bva =  Tex(r"$\blacktriangleright$", r" \textbf{BVA} ", r"(Bounded Variable Addition), an automatic reencoding technique, ", r"substantially reduces the number of clauses", font_size=36)
        however =  Tex(r"$\blacktriangleright$", r" However, solution times don't improve much with BVA :(", font_size=36)
        reverse_engineer =  Tex(r"$\blacktriangleright$", r" We ", r"reverse-engineered ", r"BVA to understand what it's doing!", font_size=36)
        
        bva.set_color_by_tex(r"\blacktriangleright", BLUE)
        bva.set_color_by_tex(r"BVA", YELLOW)
        however.set_color_by_tex(r"\blacktriangleright", BLUE)
        reverse_engineer.set_color_by_tex(r"\blacktriangleright", BLUE)
        
        bva.set_color_by_tex(r"substantially", YELLOW)
        reverse_engineer.set_color_by_tex(r"reverse-engineered", PINK)
        
        bullet_points = VGroup(bva, however, reverse_engineer).arrange(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        
        bullet_points.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        
        self.next_slide()
        self.play(Write(bva))
        self.next_slide()
        self.play(Write(however))
        self.next_slide()
        self.play(Write(reverse_engineer))
        
        
        d_3 = Diamond(3, scale=0.4, node_constructor=Square, color=WHITE).next_to(reverse_engineer, DOWN, buff=1.2*MED_LARGE_BUFF)
        d_3.shift(2.5*LEFT)
        r_1 = [(1, 0), (1, 1), (1, 2)]
        r_2 = [(0, 0), (-1, 0), (0, 1), (-1, 1)]
        
        for cell in r_1:
            d_3.nodes[cell].set_fill(RED, opacity=0.5)
            
        for cell in r_2:
            d_3.nodes[cell].set_fill(BLUE, opacity=0.5)
        
        
        self.next_slide()
        self.play(FadeIn(d_3))
        
        regional_clauses = Text("We discovered that BVA creates regional clauses!", t2c={"regional clauses": PINK},font_size=28).next_to(d_3, RIGHT, buff=MED_LARGE_BUFF)
        regional_clauses.shift(1*UP + 0.5*LEFT)
        r_1_clause =  Tex(r"$y_1 $", r"$\iff x_{(1, 0), 4} \; $", r"$\lor$", r"$ \; x_{(1, 1), 4} \; $", r"$\lor$", r"$ \; x_{(1, 2), 4}$", font_size=36)
        r_1_clause.set_color_by_tex(r"$y_1 $", RED)
        r_1_clause.set_color_by_tex(r"\lor", YELLOW)
        r_2_clause =  Tex(r"$y_2 $", r"$\iff x_{(0, 0), 4} \; $", r"$\lor$", r"$ \; x_{(1, 0), 4} \; $", r"$\lor$", r"$ \; x_{(-1, 0), 4} \; $", r"$\lor$",  r"$ \; x_{(-1, -1), 4}$", font_size=36 )
        r_2_clause.set_color_by_tex(r"$y_2 $", BLUE)
        r_2_clause.set_color_by_tex(r"\lor", YELLOW)
        
        r_clauses = VGroup(r_1_clause, r_2_clause).arrange(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        r_clauses.next_to(regional_clauses, DOWN, buff=MED_SMALL_BUFF)
        
        self.next_slide()
        self.play(Write(regional_clauses))
        self.next_slide()
        self.play(Write(r_1_clause))
        self.next_slide()
        self.play(Write(r_2_clause))
        
        self.next_slide()
        
        self.play(FadeOut(bullet_points), d_3.animate.shift(3*UP), regional_clauses.animate.shift(3*UP), r_clauses.animate.shift(3*UP))
        self.next_slide()
        
        why = Tex(r"$\blacktriangleright$", r" Why ", r"do regional clauses reduce formula size?", font_size=36)
        why.set_color_by_tex(r"\blacktriangleright", BLUE)
        why.set_color_by_tex(r"Why", PINK)
        why.next_to(d_3, DOWN, buff=MED_LARGE_BUFF)
        why.shift(2*RIGHT)
        
        because = Tex(r"Because now we can say: ", r"$\overline{y_1}$", r"$\;\lor\;$", r"$\overline{y_2}$", font_size=36)
        because.next_to(why, DOWN, buff=MED_SMALL_BUFF)
        because.set_color_by_tex(r"$\overline{y_1}$", RED)
        because.set_color_by_tex(r"$\overline{y_2}$", BLUE)
        because.set_color_by_tex(r"\lor", YELLOW)
        
        because.shift(1*RIGHT)
        
        self.play(Write(why))
        self.next_slide()
        self.play(Write(because))
        
        self.next_slide()
        
        issue = Tex(r"$\blacktriangleright$", r" The problem: ", r"BVA creates diffrent shapes of regions\\ and places them awkwardly :(", font_size=36)
        issue.set_color_by_tex(r"\blacktriangleright", BLUE)
        issue.set_color_by_tex(r"The problem", RED_E)
        
        issue.next_to(because, DOWN, buff=MED_LARGE_BUFF)
        issue.shift(0.6*RIGHT)
        
        self.play(Write(issue))
        
        self.next_slide()
        d_6 =  Diamond(6, scale=0.4, node_constructor=Square, color=WHITE).next_to(title, DOWN, buff=MED_LARGE_BUFF)
        
                
        plus_centers = [(0, 0), (1, -2), (-2, -1), (2, 1), (-1, 2), (-1, -3), (1, 3), (3, -1), (-3, 1), (0, 5), (0, -5), (5, 0), (-5, 0)]
        vdirs = [(0,0), (-1, 0), (1, 0), (0, 1), (0, -1)]
        for i, cell in enumerate(plus_centers):
            for vdir in vdirs:
                ncell = (cell[0] + vdir[0], cell[1] + vdir[1])
                d_6.nodes[ncell].set_fill(config.MY_COLORS[i+2], opacity=0.85)
                d_6.nodes[ncell].set_stroke(WHITE, opacity=1, width=4)
        
        self.play(FadeOut(d_3), FadeOut(regional_clauses), FadeOut(r_clauses), FadeOut(why), FadeOut(because), FadeOut(issue),
                FadeIn(d_6))
        
        self.next_slide()
        
        plus = Tex(r"$\blacktriangleright$", r" The solution: ", r"Use a 'plus' (+) shape and place them in a structrued manner!", font_size=36)
        plus.set_color_by_tex(r"\blacktriangleright", BLUE)
        plus.set_color_by_tex(r"The solution", GREEN_C)
        plus.next_to(d_6, DOWN, buff=MED_LARGE_BUFF)
        
        table = Table(
            [["935", "1559", "1039"],
            ["21086", "3928", "7548"],
            ["10774", "2539", "811"]],
            row_labels=[Text("# of vars"), Text("# of clauses"), Text("Runtime [s]")],
            col_labels=[Text("direct"), Text("BVA"), Text("Plus")],
            top_left_entry=Tex(r'$\chi_\rho(D_6) \geq 12$', font_size=60, color=BLUE))
            
        lab = table.get_col_labels()
        for item in lab:
            item.set_color(YELLOW)
        table.scale(0.5)
        self.play(Write(plus))
        table.next_to(d_6, RIGHT, buff=MED_LARGE_BUFF)
        table.shift(3.5*LEFT)
        
        self.next_slide()
        self.play(d_6.animate.shift(3.5*LEFT), Write(table))
        
        self.next_slide()
        
        self.play(table.animate.add_highlighted_cell((0,0), color=GREEN))
        self.next_slide()
        
        
class StructuredBVA(Slide):
    def construct(self):
        analyzing = Text("An interesting success of 'structured' variable addition", t2c={"structured": GREEN}, font_size=36).to_edge(UP)
        self.play(FadeIn(analyzing))
        self.next_slide()
        based = Text("Based on this, Andrew Haberlandt and Harrison Green developed SBVA", t2c={"SBVA": PINK}, font_size=32).next_to(analyzing, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(based))
        self.next_slide()
        winners = ImageMobject("img/sbva.png").next_to(based, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(winners))
        self.next_slide()