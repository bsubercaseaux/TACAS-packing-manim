SLIDES="LineGraphExample Subgraphs"
LAST=True
if [ "$LAST" = True ]; then
    # last word of SLIDES
    SLIDES=${SLIDES##* }
fi

manim -qh src/Subgraphs.py $SLIDES
manim-slides $SLIDES
 # manim -qm src/introSlide.py InThisTalk
# manim -qk src/introSlide.py Interpretable
# manim-slides convert MythBusters IntroSlide Questions DecisionTree build/slides.html
# manim-slides convert Interpretable build/slides.html
# manim-slides convert $SLIDES build/slides.html
# open build/slides.html
