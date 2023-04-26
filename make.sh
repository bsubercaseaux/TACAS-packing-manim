LAST=True

manim -qk src/slides.py Tacas
manim-slides convert Tacas build/slides.html
 # manim -qm src/introSlide.py InThisTalk
# manim -qk src/introSlide.py Interpretable
# manim-slides convert MythBusters IntroSlide Questions DecisionTree build/slides.html
# manim-slides convert Interpretable build/slides.html
# manim-slides convert $SLIDES build/slides.html
# open build/slides.html
