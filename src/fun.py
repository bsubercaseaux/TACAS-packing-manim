from manim import *
from manim_slides import Slide

class Fun(Slide):
    def construct(self):
        main_talk = Text("The core of my talk is over :)", t2c={':)': YELLOW}, font_size=60)
        fun = Text("I'll now present 3 FUN things that happened while working on this project!", t2c={'FUN': PINK})
        fun.scale_to_fit_width(12)
        
        fun.next_to(main_talk, DOWN, buff=LARGE_BUFF)
        
        self.play(Write(main_talk))
        self.next_slide()
        self.play(Write(fun))
        
        knuth = Text("Donald Knuth is very interested in the SAT solving + graph coloring combo", t2c={'Donald Knuth': YELLOW, 'SAT solving + graph coloring': BLUE}, font_size=36)
        knuth.scale_to_fit_width(12)
        we_sent = Text("So we sent him a copy of our paper...", font_size=32)
        comments = Text("and he sent us back many comments!", font_size=32)
        
        group = VGroup(knuth, we_sent, comments)
        
        group.arrange(DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
        group.to_edge(UP)
        
        self.next_slide()
        self.play(FadeOut(main_talk), FadeOut(fun), FadeIn(knuth))
        
        self.next_slide()
        self.play(Write(we_sent))
        self.next_slide()
        self.play(Write(comments))
        
        self.next_slide()
        # first_email = ImageMobject("img/first_email.png")
        # first_email.next_to(group, DOWN, buff=MED_LARGE_BUFF)
        # first_email.shift(2*LEFT)
        
        first_email = Text('Knuth (paraphrased): \n     "The tiling of Fig 4b. (Plus encoding) appears promimently\n behind the altar on the church of Røa, Norway,\n which my wife and I visited during 1972 and 1973"', font_size=26, t2c={'Knuth':YELLOW}, t2s={'The tiling of Fig 4b. (Plus encoding) appears promimently\n behind the altar on the church of Røa, Norway,\n whhich my wife and I visited during 1972 and 1973': ITALIC})
        first_email.next_to(group, DOWN, buff=MED_LARGE_BUFF)
        first_email.shift(1.5*LEFT)
        self.play(FadeIn(first_email))
        
        church = ImageMobject("img/plusses3.png")
        church.next_to(first_email, RIGHT, buff=MED_LARGE_BUFF)
        church.shift(2.0*DOWN + 2.5*LEFT) 
        
        self.next_slide()
        self.play(FadeIn(church))
        
        
        second_email = ImageMobject("img/second_email.png")
        second_email.next_to(church, RIGHT, buff=MED_LARGE_BUFF)
        second_email.shift(13*LEFT +0.2*DOWN)
        self.next_slide()
        self.play(FadeIn(second_email))
        self.next_slide()
