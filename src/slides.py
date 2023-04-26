from manim import *
from motivation import Motivation
from intro_slide import IntroSlide
from historical_progress import HistoricalSummary
from subgraphs import Subgraphs
from proving_bounds import ProvingBounds
from translational_symmetry import Translational
from direct_encoding import DirectEncoding
from plus_encoding import PlusEncoding
from chessboard import Chessboard
from symmetry_breaking import SymmetryBreaking
from cube_and_conquer import CubeAndConquer
from verification import ProofAndVerification
from alod import Alod
from final import Final
from fun import Fun
from manim_slides import Slide




#list_of_slides = [Motivation, IntroSlide, HistoricalSummary, ProvingBounds, Subgraphs, Translational, DirectEncoding,  PlusEncoding,  SymmetryBreaking,  CubeAndConquer, Alod, ProofAndVerification, Fun, Chessboard, Final]
list_of_slides = [Fun]

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
    