SLIDES="LineGraphExample Subgraphs Motivation IntroSlide"
LAST=True
if [ "$LAST" = True ]; then
    # last word of SLIDES
    SLIDES=${SLIDES##* }
fi

manim -qk src/motivation2.py $SLIDES
manim-slides present $SLIDES
 # manim -qm src/introSlide.py InThisTalk
# manim -qk src/introSlide.py Interpretable
# manim-slides convert MythBusters IntroSlide Questions DecisionTree build/slides.html
# manim-slides convert Interpretable build/slides.html
# manim-slides convert $SLIDES build/slides.html
# open build/slides.html
