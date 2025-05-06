from manim import *
from motivation import Motivation, SquareGrid, PackingColorings, WhatToDo, ThisTalk
from intro_slide import IntroSlide
from historical_progress import HistoricalSummary
from subgraphs import Subgraphs
from proving_bounds import ProvingBounds
from translational_symmetry import Translational
from direct_encoding import DirectEncoding
from plus_encoding import PlusEncoding, StructuredBVA
from chessboard import Chessboard
from symmetry_breaking import SymmetryBreaking
from cube_and_conquer import CubeAndConquer
from verification import ProofAndVerification
from alod import Alod
from final import Final
from fun import Fun
from chebyshev import Chebyshev
from questions import Questions
from sat import LoveStory, SatIntroSlide, Outline, Basics, Solvers, SuccessOfSat, SudokuExample, ArtOfSat
from math_applications import MathApplications
from manim_slides import Slide

## Solvers, is commented out

preliminaries = [LoveStory, Outline, Basics, SudokuExample, ArtOfSat,  MathApplications, Questions]
total_slides = [Motivation, PackingColorings, Chebyshev, SquareGrid, WhatToDo, ThisTalk, Questions,  IntroSlide, HistoricalSummary, ProvingBounds, Subgraphs, Translational, DirectEncoding,  PlusEncoding, StructuredBVA, Questions,   SymmetryBreaking,  CubeAndConquer, Alod, ProofAndVerification, Fun, Chessboard, Final]

particulars = [ArtOfSat] #, Basics, SudokuExample] # SudokuExample, ArtOfSat, SuccessOfSat, Solvers]

COMPILE_EVERYTHING = True

if COMPILE_EVERYTHING:
    list_of_slides = total_slides
else:
    list_of_slides = particulars


class Tacas(Slide):
    def construct(self):
        for slide in list_of_slides:
            slide.construct(self)
            if len(self.mobjects) >= 1:
                self.remove(*self.mobjects)
