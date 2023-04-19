from manim import *
from motivation import Motivation
from intro_slide import IntroSlide
from historical_progress import HistoricalSummary
from subgraphs import Subgraphs
from proving_bounds import ProvingBounds
from manim_slides import Slide


list_of_slides = [Motivation, IntroSlide, HistoricalSummary, ProvingBounds, Subgraphs]
list_of_slides = [HistoricalSummary]

LAST = False
if LAST:
    list_of_slides = [list_of_slides[-1]]

class Tacas(Slide):
    def construct(self):
        for slide in list_of_slides:
            slide.construct(self)
            if len(self.mobjects) >= 1:
                    self.remove(*self.mobjects)
     
        
        # historical_summary = HistoricalSummary()
        # subgraphs = Subgraphs()
        
        # self.add(motivation)
    