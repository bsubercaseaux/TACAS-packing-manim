from manim import *
from manim_slides import Slide 

class ProofAndVerification(Slide):
    def construct(self):
        title = Text("Proof and Verification", font_size=72, color=YELLOW).to_edge(UP)
        self.play(FadeIn(title))
        
        to_prove = Tex(r"In order to prove {{$\chi_\rho(\mathbb{Z}^2) \geq 15$}} we use the following ingredients:", font_size=46)
        to_prove.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        to_prove.set_color_by_tex("15", BLUE)
        self.next_slide()
        self.play(FadeIn(to_prove))
        
        colors = Tex(r"$\blacktriangleright$", r" 14 colors, hoping to get UNSAT", font_size=36)
        graph = Tex(r"$\blacktriangleright$", r" The $D_{15}$ graph", font_size=36)
        center_6 = Tex(r"$\blacktriangleright$", r" Color 6 in the center", font_size=36)
        plus = Tex(r"$\blacktriangleright$", r" Plus encoding", font_size=36)
        sym = Tex(r"$\blacktriangleright$", r" Symmetry breaking (5 layers)", font_size=36)
        cube_and_conquer = Tex(r"$\blacktriangleright$", r" Cube and Conquer (5\,217\,031 cubes, \textsc{Ptr Algorithm}, 128 cores)", font_size=36)
        alod_clauses = Tex(r"$\blacktriangleright$", r"\textsc{Alod}   clauses", font_size=36)
        
        group = VGroup(colors, graph, center_6, plus, sym, cube_and_conquer, alod_clauses).next_to(to_prove, DOWN, buff=1.2*MED_LARGE_BUFF)
        group.arrange(DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
        
        group.shift(0.4*DOWN)
        
        self.next_slide()
        for el in group:
            el.set_color_by_tex(r"$\blacktriangleright$", BLUE)
            self.play(Write(el))
            self.next_slide()
            
        proof = Text("We obtain an UNSAT result after 4851 CPU hours (< 2 days on 128 cores)", t2c={'UNSAT': RED, '4851 CPU hours': GREEN}, font_size=28)
        proof_size = Text("We generate a DRAT proof of 34 terabytes (LRAT of 122 terabytes)", t2c={'DRAT proof': YELLOW, '34 terabytes': PINK}, font_size=28)
        
        proof.next_to(group, DOWN, buff=MED_LARGE_BUFF)
        proof_size.next_to(proof, DOWN, buff=MED_SMALL_BUFF)
        
        self.play(Write(proof))
        self.next_slide()
        self.play(Write(proof_size))
        self.next_slide()
        
        self.play(FadeOut(VGroup(to_prove, group, proof, proof_size)))
        self.next_slide()
        
        proof = Tex(r"We formally prove the correctness of each ingredient individually\\ combining different formal systems (cake\_lpr, SR, DRAT)\\ and stitch them together in the appropriate order", font_size=40)
        proof.shift(1*UP)
        self.play(Write(proof))
        self.next_slide()
        
        challenge = Text("No doubts remaining :)\n \n but an interesting challenge would be to have a full proof in Lean", should_center=True, t2c={"No doubts remaining": PURE_GREEN, "Lean": ORANGE}, font_size=30)
        challenge.next_to(proof, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(challenge))
        self.next_slide()
        # to_generate = Tex(r"In order to generate a DRAT proof we:", font_size=46)
        # to_generate.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        # self.play(FadeIn(to_generate))
        
        # self.next_slide()
        
        # prove_correctness = Tex(r"$\blacktriangleright$", r" Prove the correctness of each ingredient individually", font_size=36)
        # mix = Tex(r"$\blacktriangleright$", r" Stitch them together in the appropriate order", font_size=36)
        # example = Tex(r"$\blacktriangleright$", r" E.g.: Correctness of {{\textsc{Alod}}} clauses comes from them being {{blocked clauses}}", font_size=36)
        # example.set_color_by_tex("blocked clauses", BLUE)
        # example.set_color_by_tex(r"\textsc{Alod}", YELLOW)
        # cubes = Tex(r"$\blacktriangleright$", r" E.g.: Cubes need to be proved to form a {{tautology}}", font_size=36)
        # cubes.set_color_by_tex("tautology", RED)
        # symmetry = Tex(r"$\blacktriangleright$", r" E.g.: We implemented a prototype {{$\textrm{SR} \to \textrm{DRAT}$}} converter for proving symmetry breaking", font_size=36)
        # symmetry.set_color_by_tex(r"\textrm{SR}", PINK)
        
        # unverified = Tex(r"$\blacktriangleright$", r" The only unverified core (at time of writing the paper) was the {{direct encoding}},\\ which was only {{26 lines of Python}}", font_size=36)
        # unverified.set_color_by_tex("direct encoding", BLUE)
        # unverified.set_color_by_tex("26 lines of Python", GREEN)
        
        # final = Tex(r"$\blacktriangleright$", r" We end up with {{a single unified DRAT proof}} $\smiley$", font_size=36)
        # final.set_color_by_tex("a single unified DRAT proof", YELLOW)
        
        # group = VGroup(prove_correctness, mix, example, cubes, symmetry, unverified, final).next_to(to_generate, DOWN, buff=1.2*MED_LARGE_BUFF)
        # group.arrange(DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
        
        # group.shift(1.3*DOWN)
        
        # for el in group:
        #     el.set_color_by_tex(r"$\blacktriangleright$", BLUE)
        #     self.play(Write(el))
        #     self.next_slide()
