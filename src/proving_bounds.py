from manim import *
import config
from manim_slides import Slide
from subgraphs import Grid
from empty import EmptyAnimation

class ProvingBounds(Slide):
    def construct(self):
        question = Text("How can we use a computer to prove bounds about infinite graphs?", t2c={'infinite': YELLOW})
        question.scale_to_fit_width(12)
        
        self.play(FadeIn(question))
        
        self.next_slide()
        
        self.play(question.animate.shift(3*UP))
        
        arr_left = Arrow(question.get_center() + 0.3*DOWN + 0.2*LEFT, question.get_center() + 1.5*DOWN + 4*LEFT, color=YELLOW)
        arr_right = Arrow(question.get_center() + 0.3*DOWN + 0.2*RIGHT, question.get_center() + 1.5*DOWN + 4*RIGHT, color=YELLOW)
        
        self.play(Create(arr_left), Create(arr_right))
        
        self.next_slide()
        
        lower = Tex(r"Lower bounds: ", r"$\chi_\rho(G) > k$", font_size=38).move_to(arr_left[1]).shift(0.5*DOWN)
        lower.set_color_by_tex(r"$\chi_\rho(G) > k$", YELLOW)
        upper = Tex(r"Upper bounds: ", r"$\chi_\rho(G) \leq k$", font_size=38).move_to(arr_right[1]).shift(0.5*DOWN)
        upper.set_color_by_tex(r"$\chi_\rho(G) \leq k$", YELLOW)
        self.play(FadeIn(upper), FadeIn(lower))
        
        self.next_slide()
        
        subgraph = Tex(r"\textbf{1.} ", r"Find an appropriate finite sub-graph ", r"$H \subset G$.", font_size=34).set_color_by_tex(r"$H \subset G$", RED).set_color_by_tex("1.", BLUE)
        prove = Tex(r"\textbf{2.} ", r"Prove that ", r"$\chi_\rho(H) > k$.", font_size=34).set_color_by_tex(r"$\chi_\rho(H) > k$", RED).set_color_by_tex("2.", BLUE)
        lower_group = VGroup(subgraph, prove).arrange(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        
        lower_group.next_to(lower, DOWN, buff=2*LARGE_BUFF).shift(0.5*RIGHT)
        
        arr_lower = Arrow(lower.get_center() + 0.1*DOWN, lower_group.get_center() + 0.5*UP + 0.5*LEFT, color=YELLOW)
        # rec=Rectangle(height=2*lower_group.get_height(), width=2*lower_group.get_width(), color=BLUE, fill_opacity=0.2)
        # rec.surround(lower_group, buff=0.5)
        
        self.play(Create(arr_lower))
        self.play(FadeIn(subgraph))
        self.next_slide()
        self.play(FadeIn(prove))
        
        aperiodic = Text("Aperiodic?", font_size=28).next_to(upper, DOWN, buff=LARGE_BUFF).shift(1.75*LEFT)
        periodic = Text("Periodic?", font_size=28).next_to(upper, DOWN, buff=LARGE_BUFF).shift(1.75*RIGHT)
        self.next_slide()
        
        periodic_arr, aperiodic_arr = [Arrow(upper.get_center() + 0.1*DOWN, obj.get_center() + 0.2*UP, color=YELLOW) for obj in [periodic, aperiodic]]
        
        self.play(Create(periodic_arr), Create(aperiodic_arr))
        self.play(FadeIn(periodic), FadeIn(aperiodic))
        
        
        self.next_slide()
        
        gg = Text("???", color=RED).next_to(aperiodic, DOWN, buff=LARGE_BUFF).shift(0.4*DOWN)
        gg_arr = Arrow(aperiodic.get_center() + 0.1*DOWN, gg.get_center() + 0.2*UP, color=YELLOW)
        self.play(Create(gg_arr), FadeIn(gg))
        self.next_slide()
        
        toroidal = Text("Use toroidal edges\n to encode periodicity!", t2c={'toroidal': RED}).next_to(periodic, DOWN, buff=LARGE_BUFF)
        toroidal.shift(0.55*LEFT+0.1*DOWN)
        toroidal.scale_to_fit_width(4)
        toroidal_arr = Arrow(periodic.get_center() + 0.1*DOWN, toroidal.get_center() + 0.25*UP, color=YELLOW)
        self.play(Create(toroidal_arr), FadeIn(toroidal))
        
        rect_with_toroidal = Rectangle(height=0.6, width=1.2, color=BLUE, fill_opacity=0.8)
        rect_with_toroidal.next_to(toroidal, DOWN, buff=MED_SMALL_BUFF)
        
        
        def custom_arrow_tip(length, **style):
            return ArrowTriangleFilledTip(length=0.15, width=0.15, **style)
        

        curved_vertical = CurvedDoubleArrow(start_point=rect_with_toroidal.get_center() + 0.32*DOWN, 
                                            end_point=rect_with_toroidal.get_center() + 0.32*UP, color=RED, angle=TAU/2.1, tip_shape_start=custom_arrow_tip,
                                            tip_shape_end=custom_arrow_tip)
        curved_horizontal = CurvedDoubleArrow(start_point=rect_with_toroidal.get_center() + 0.62*LEFT, 
                                            end_point=rect_with_toroidal.get_center() + 0.62*RIGHT, color=ORANGE, angle=TAU/2.1, tip_shape_start=custom_arrow_tip,
                                            tip_shape_end=custom_arrow_tip)
        
        h_toroidal = Tex(r"$H \subset G$", font_size=22).move_to(rect_with_toroidal.get_center())
        # curved_horizontal = CurvedDoubleArrow(start_point=rect_with_toroidal.get_center() + 0.3*LEFT, 
        #                                     end_point=rect_with_toroidal.get_center() + 0.3*RIGHT, color=ORANGE, radius=0.4)
        
        # self.next_slide()
        self.play(FadeIn(rect_with_toroidal), FadeIn(curved_vertical), FadeIn(curved_horizontal), Write(h_toroidal))
        
        
        
        self.next_slide()
        
        
        self.clear()
        
        example = Tex(r"\setuldepth{Exam}\ul{Example}: ", r"$\chi_\rho\left(\mathbb{Z}^1\right) = 3$", font_size=72).to_edge(UP)
        example.set_color_by_tex("3", RED)
        # example.set_color_by_tex("Example", BLUE)
        
        self.play(FadeIn(example))
        
        self.next_slide()
        
        lbound = Tex(r"Proving the lower bound ", r"$\chi_\rho(\mathbb{Z}^1\right) > 2$", font_size=48)
        lbound.next_to(example, DOWN, buff=MED_LARGE_BUFF)
        lbound.set_color_by_tex("2", YELLOW)
        self.play(FadeIn(lbound))
        
        
        g14 = Grid(1, 4).scale(2).next_to(lbound, DOWN, buff=MED_SMALL_BUFF)
        
        self.play(FadeIn(g14), Write(Tex(r'$P_4$', font_size=50).next_to(g14, LEFT, buff=LARGE_BUFF)))
                
        self.next_slide()
        
        self.play(g14.ColorNode(0, 0, 1))
        self.next_slide()
        self.play(g14.ColorNode(0, 1, 2))
        self.next_slide()
        self.play(g14.ColorNode(0, 2, 1))
        self.next_slide()
        self.play(g14.ColorNode(0, 3, 0, ":(", label_color=WHITE))
        
        self.next_slide()
        
        checkmark = Tex(r"\checkmark", color=GREEN).scale(3).next_to(lbound, RIGHT, buff=1.5*MED_SMALL_BUFF).shift(0.3*UP)
        
        self.play(Create(checkmark))
        
        self.next_slide()
        
        ubound = Tex(r"Proving the upper bound ", r"$\chi_\rho(\mathbb{Z}^1\right) \leq 3$", font_size=48)
        ubound.set_color_by_tex("3", YELLOW)
        ubound.next_to(g14, DOWN, buff=1.5*MED_LARGE_BUFF)
        self.play(FadeIn(ubound))
        self.next_slide()
        
        g14t = Grid(1, 4, toroidal=True).scale(2).next_to(ubound, DOWN, buff=MED_LARGE_BUFF)
        g14t.shift(1*RIGHT)
        p14_t = Tex(r"$C_4 = $", r"$\text{ Toroidal}$", r"$(P_4)$", font_size=38).next_to(g14t, LEFT, buff=MED_LARGE_BUFF)
        p14_t.set_color_by_tex("Toroidal", RED)
        
        
        self.play(FadeIn(g14t), FadeIn(p14_t))
        self.next_slide()
        
        self.play(g14t.ColorNode(0, 0, 1),
                  g14t.ColorNode(0, 1, 2),
                  g14t.ColorNode(0, 2, 1),
                  g14t.ColorNode(0, 3, 3),)
        
        self.next_slide()
        
          
        g18t = Grid(1, 8, toroidal=True).scale(1).next_to(g14t, DOWN, buff=1.1*MED_SMALL_BUFF)
        p18_t = Tex(r"$C_8 = $", r"$ \text{ Toroidal}$", r"$(P_8)$", font_size=38).next_to(g18t, LEFT, buff=MED_LARGE_BUFF)
        p18_t.set_color_by_tex("Toroidal", RED)
        
        
        self.play(FadeIn(g18t), FadeIn(p18_t))
        
        self.next_slide()
        
        self.play(g18t.ColorNode(0, 0, 1),
                    g18t.ColorNode(0, 1, 2),
                    g18t.ColorNode(0, 2, 1),
                    g18t.ColorNode(0, 3, 3))
        
        self.next_slide()
        self.play(g18t.ColorNode(0, 4, 1))
        self.next_slide()
        self.play(g18t.ColorNode(0, 5, 2))
        self.next_slide()
        self.play(g18t.ColorNode(0, 6, 1))
        self.next_slide()
        self.play(g18t.ColorNode(0, 7, 3))
        

        self.next_slide()
        
        checkmark = Tex(r"\checkmark", color=GREEN).scale(3).next_to(ubound, RIGHT, buff=1.5*MED_SMALL_BUFF).shift(0.3*UP)
        
        self.play(Create(checkmark))
        
        self.next_slide()
        
        