from manim import *
from manim_slides import Slide
from empty import EmptyAnimation

class DirectEncoding(Slide):
    def construct(self):
        title = Tex(r"\ul{Direct Encoding} for ", r"$\chi_\rho(D_r) \leq k$", font_size=64).to_edge(UP)
        title.set_color_by_tex("chi", YELLOW)
        
        self.play(FadeIn(title))
        
        vars = Tex(r"0.", r" Variables ", r"represent vertex $v$ taking color $c$", font_size=36)
        exp_vars = Tex(r"$x_{v, c}$", r" $ \enspace \forall v \in D_r, \text{ and } \forall c \in \{1, \ldots, k\}$", font_size=40)
        exp_vars.set_color_by_tex(r"$x_{v, c}$", YELLOW)
        aloc = Tex(r"1.", r" At Least One Color ", r"(\textsc{Aloc}) clauses", font_size=36)
        exp_aloc = VGroup(Tex(r"$$\bigvee_{c \in \{1, \ldots, k\}} x_{v, c}$$", font_size=40),
                         Tex(r" $ \enspace \forall v \in D_r$", font_size=40))
        exp_aloc.arrange(RIGHT, buff=0.3)
        
        exp_aloc[0].set_color_by_tex("x", YELLOW)
        exp_aloc[1].shift(0.2*UP)
        
        amod = Tex(r"2.", r" At Most One Distance ", r"(\textsc{Amod}) clauses", font_size=36)
        exp_amod = Tex(r"$\overline{x_{u, c}} \vee \overline{x_{v, c}}$", r" $ \enspace \forall u, v \in D_r$ such that $d(u, v) \leq c$", font_size=40)
        exp_amod.set_color_by_tex("x", YELLOW)
        center = Tex(r"3.", r" Center", r" clause", font_size=36)
        exp_center = Tex(r"$x_{(0,0), C}$", r" $\enspace $ for the chosen color $C$", font_size=40)
        exp_center.set_color_by_tex("x", YELLOW)
        
        vars.set_color_by_tex("0.", BLUE)
        aloc.set_color_by_tex("1.", BLUE)
        amod.set_color_by_tex("2.", BLUE)
        center.set_color_by_tex("3.", BLUE)
        header_color = PINK
        vars.set_color_by_tex("Variables", header_color)
        aloc.set_color_by_tex("At Least One Color", header_color)
        amod.set_color_by_tex("At Most One Distance", header_color)
        center.set_color_by_tex("C", header_color)
        
        clause_groups = VGroup(vars, aloc, amod, center).arrange(DOWN, buff=1.3*LARGE_BUFF, aligned_edge=LEFT)
        clause_groups.next_to(title, DOWN, buff=1.2*MED_SMALL_BUFF).shift(0.2*DOWN)
        exp_groups = VGroup(exp_vars, exp_aloc, exp_amod, exp_center).arrange(DOWN, buff=1.3*LARGE_BUFF, aligned_edge=LEFT)
        exp_groups.next_to(title, DOWN, buff=LARGE_BUFF).shift(0.05*UP)

        
        aloc.shift(0.2*UP)
        amod.shift(0.3*DOWN)
    
        exp_vars.shift(1.5*RIGHT + 0.2*DOWN)
        exp_aloc.shift(1.5*RIGHT)
        exp_amod.shift(1.5*RIGHT+0.2*UP)
        exp_center.shift(1.5*RIGHT + 0.6*UP)
        
        n_clauses_aloc = Tex(r"$|D_r| = O(r^2)$",  font_size=36)   
        n_clauses_aloc.set_color_by_tex(r"O(r^2)", RED)
        
        n_clauses_amod = VGroup(Tex(r"$$\sum_{c=1}^k \frac{|D_r| \cdot |D_c|}{2} $$", font_size=36, color=RED),
                               Tex(r"$$= O(r^2 k^3)$$", font_size=36, color=RED)).arrange(RIGHT)
        n_clauses_center = Tex(r"$O(1)$", font_size=36)
        n_clauses_center.set_color_by_tex(r"1", RED)
        
        n_clauses_aloc.next_to(exp_aloc, LEFT, buff=0.5*LARGE_BUFF)
        n_clauses_amod.next_to(exp_amod, LEFT, buff=0.5*LARGE_BUFF)
        n_clauses_center.next_to(exp_center, LEFT, buff=0.5*LARGE_BUFF)
        
        pairs = [(vars, exp_vars), (aloc, exp_aloc, n_clauses_aloc), (amod, exp_amod, n_clauses_amod[0], n_clauses_amod[1]), (center, exp_center, n_clauses_center)]
        
        for pair in pairs:
            for el in pair:
                self.play(Write(el))
                self.next_slide()
            
        self.play(*[FadeOut(el) for p in pairs for el in p])
        
        n_vars_and_clauses = Tex(r"$\blacktriangleright$", r" The direct encoding uses $O(r^2 k)$ variables and ", r"$O(r^2 k^3)$ clauses", font_size=40)
        n_vars_and_clauses.set_color_by_tex(r"O(r^2 k^3)", RED)
        n_vars_and_clauses.set_color_by_tex(r"\blacktriangleright", BLUE)
        
        our_case = Tex(r"$\blacktriangleright$", r" To prove a lower bound of 15 we need $r = k = 14$,\\ resulting in ", r"$\sim$1M clauses!", font_size=40)
        our_case.set_color_by_tex(r"$\sim$1M clauses!", RED)
        our_case.set_color_by_tex(r"\blacktriangleright", BLUE)
        
        bottleneck = Tex(r"$\blacktriangleright$", r" The bottleneck is in the", r" \textsc{Amod} ", r"clauses!", font_size=40)
        bottleneck.set_color_by_tex(r"\textsc{Amod}", RED)
        bottleneck.set_color_by_tex(r"\blacktriangleright", BLUE)
        
        prev_proposal = Tex(r"$\blacktriangleright$", r" In SAT'22 we proposed a \emph{recursive encoding} using $O(r^2 k \lg k)$ clauses", font_size=40)
        theoretical = Tex(r"But it was mainly ", r"\emph{theoretical}", r" as the $O(\cdot)$-constant is large.", font_size=40)
        theoretical.set_color_by_tex(r"\emph{theoretical}", BLUE)
        prev_proposal.set_color_by_tex(r"blacktriangleright", BLUE)
        prev_group = VGroup(prev_proposal, theoretical).arrange(DOWN, buff=SMALL_BUFF)
        
        
        actually_works = Tex(r"$\blacktriangleright$", r" We now present a ", r"\emph{practical}",r" encoding that works really well!", color=YELLOW, font_size=40)
        actually_works.set_color_by_tex(r"\emph{practical}", BLUE)
        actually_works.set_color_by_tex(r"\blacktriangleright", BLUE)
        
        t_group = VGroup(n_vars_and_clauses, our_case, bottleneck, prev_group, actually_works).arrange(DOWN, buff=0.7*LARGE_BUFF, aligned_edge=LEFT)
        t_group.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        t_group.shift(0.2*RIGHT)
        
        new_title = Tex(r"\ul{A better encoding} for ", r"$\chi_\rho(D_r) \leq k$", font_size=64).to_edge(UP)
        new_title.set_color_by_tex(r"$\chi_\rho(D_r) \leq k$", YELLOW)
        
        self.play(Transform(title, new_title))
        
        for el in t_group:
            self.next_slide()
            self.play(Write(el))

        self.next_slide()
        