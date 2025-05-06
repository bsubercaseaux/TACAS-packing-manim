from manim import *
from manim_slides import Slide
import cv2

class Final(Slide):
    def construct(self):
        final_treat = Text("Upper Bound", color=YELLOW, font_size=72).to_edge(UP)
        self.play(FadeIn(final_treat))
        already_known = Tex(r"Martin et al. (2017) already showed that 15 was an upper bound,\\by modifying a previous solution with 16 colors.", font_size=36)
        already_known.next_to(final_treat, DOWN, buff=MED_LARGE_BUFF)
        self.next_slide()
        
        self.play(Write(already_known))
        
        we_reprove = Tex(r"{{We reprove this result using}}:\\ local search solver + $\text{Toroidal}(72 \times 72 \text{ grid})$ + \textsc{Chessboard} + central 6", font_size=36, substrings_to_isolate="+")
        we_reprove.set_color_by_tex("+", YELLOW)
        we_reprove.set_color_by_tex("reprove", BLUE)
        
        self.next_slide()
        self.play(Write(we_reprove))
        
        open_problem = Tex(r"{{Open problem}}: is there a periodic packing coloring of smaller tile size than $72 \times 72$?", font_size=36)
        open_problem.next_to(we_reprove, DOWN, buff=MED_LARGE_BUFF)
        open_problem.set_color_by_tex("Open problem", RED)
        
        self.next_slide()
        self.play(Write(open_problem))
        
        to_conclude = Tex(r"To conclude, an animation of our solution by {{@dvdp}} (David Szakaly). $\smiley$", font_size=36)
        to_conclude.next_to(open_problem, DOWN, buff=MED_LARGE_BUFF)
        to_conclude.set_color_by_tex("dvdp", BLUE)
        
        self.next_slide()
        self.play(Write(to_conclude))
        
        self.next_slide()
    
        cap = cv2.VideoCapture("img/ChromaticPacking-byDVDP-Lede-original.mp4")
        flag = True
        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame)
                self.add(frame_img)
                self.wait(0.04)
                self.remove(frame_img)
        cap.release()
