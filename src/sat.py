from manim import *
from manim_slides import Slide
from subgraphs import Grid
import config
import numpy as np
from empty import EmptyAnimation



class SatIntroSlide(Slide):
    def construct(self):
        self.play(EmptyAnimation())
        self.next_slide()

        back_img = ImageMobject("img/chessboard.png").set_opacity(0.25)

        # title = Tex(r"\textsc{The Surprising Effectiveness of }", r"\textsc{SAT-solvers}\\", r"\textsc{for }", r"\textsc{Discrete Mathematics}", should_center=True, font_size=68) # t2c={'SAT-solvers': PURPLE, 'Discrete Mathematics': BLUE})
        title = Tex(
            r"\textsc{We made a computer solve}\\",
            r" \textsc{my favorite graph coloring problem}\\",
            r"\textsc{and so can you!}",
            should_center=True,
            font_size=68,
        )  # t2c={'SAT-solvers': PURPLE, 'Discrete Mathematics': BLUE})
        title[2].set_color(PINK)
        # title[3].set_color(ORANGE)
        authors = Text("Bernardo Subercaseaux", font_size=36).next_to(
            title, DOWN, buff=LARGE_BUFF
        )  # .next_to(grid_for_title, DOWN, buff=MED_LARGE_BUFF)
        email = Tex(r"\texttt{bsuberca@cmu.edu}", font_size=32, color=BLUE).next_to(
            authors, DOWN
        )
        self.play(FadeIn(back_img), Write(title), run_time=2.2)
        self.play(FadeIn(authors), FadeIn(email), run_time=0.8)
        self.next_slide()


class LoveStory(Slide):
    def construct(self):
        title = Text(
            "A love story with 4 years in the making...", font_size=48, color=YELLOW
        ).to_edge(UP)
        self.play(FadeIn(title))
        self.next_slide()

        these_days = Text(
            "As it's common these days, it all started on social media...", font_size=36
        ).next_to(title, DOWN, buff=MED_LARGE_BUFF)
        facebook_img = (
            ImageMobject("img/dylan-post.png")
            .scale(1)
            .next_to(these_days, DOWN, buff=MED_LARGE_BUFF)
        )
        self.play(FadeIn(these_days))
        self.next_slide()
        self.play(FadeIn(facebook_img))
        self.next_slide()
        self.play(FadeOut(facebook_img), FadeOut(these_days))

        year_trying_by_hand = Text(
            "1) For a year, I tried to solve it by hand, without success...",
            t2c={"1)": YELLOW},
            font_size=28,
        ).next_to(title, DOWN, buff=MED_LARGE_BUFF)
        then_cmu = Text(
            "2) Then I came to CMU in 2021 and asked Prof. Marijn Heule\n if his 'SAT solvers' could help...",
            font_size=28,
            t2c={"2)": YELLOW, "SAT solvers": YELLOW},
        ).next_to(year_trying_by_hand, DOWN, buff=MED_LARGE_BUFF)
        significant_progress = Text(
            "3) I learned about SAT solvers, and we made significant progress!\n The answer was between 13 and 15",
            font_size=28,
            t2c={"3)": YELLOW, "13": PINK, "15": PINK},
        ).next_to(then_cmu, DOWN, buff=MED_LARGE_BUFF)
        oh_no = Text(
            "4) Oh no! we realized the problem was from 2002,\n and our results were known :(",
            font_size=28,
            t2c={"4)": YELLOW, "Oh no!": RED},
        ).next_to(significant_progress, DOWN, buff=MED_LARGE_BUFF)
        but_we_kept = Text(
            "5) But we kept working, and after a year proved the answer was 14 or 15.",
            t2c={"5)": YELLOW, "14": YELLOW, "15": YELLOW},
            font_size=28,
        ).next_to(oh_no, DOWN, buff=MED_LARGE_BUFF)
        another = Text(
            "6) Another year later we proved 14 was not possible...",
            t2c={"6)": YELLOW},
            font_size=28,
        ).next_to(oh_no, DOWN, buff=MED_LARGE_BUFF)
        steps = VGroup(
            year_trying_by_hand,
            then_cmu,
            significant_progress,
            oh_no,
            but_we_kept,
            another,
        )
        steps.arrange(DOWN, center=False, aligned_edge=LEFT).shift(1 * LEFT)

        self.next_slide()
        self.play(FadeIn(year_trying_by_hand))

        self.next_slide()
        self.play(FadeIn(then_cmu))

        self.next_slide()
        self.play(FadeIn(significant_progress))

        self.next_slide()
        scream = (
            ImageMobject("img/scream.png")
            .scale(0.8)
            .next_to(oh_no, DOWN, buff=MED_LARGE_BUFF)
            .shift(0.5 * RIGHT)
        )
        self.play(FadeIn(oh_no), FadeIn(scream))

        self.next_slide()
        self.play(FadeOut(scream), FadeIn(but_we_kept))
        self.next_slide()

        self.play(FadeIn(another))
        self.next_slide()
        self.play(
            FadeOut(but_we_kept),
            FadeOut(oh_no),
            FadeOut(significant_progress),
            FadeOut(then_cmu),
            FadeOut(year_trying_by_hand),
            FadeOut(another),
        )
        quanta = (
            ImageMobject("img/quanta.png")
            .scale(0.75)
            .next_to(title, DOWN, buff=MED_LARGE_BUFF)
        )
        self.next_slide()
        self.play(FadeIn(quanta))
        self.next_slide()
        self.play(FadeOut(quanta))

        more_importantly = Text(
            "More importantly, I fell in love with the intersection between SAT and Math!",
            font_size=28,
        ).next_to(title, DOWN, buff=MED_LARGE_BUFF)
        convince_you = Text(
            "My goal now is to convince you that\n SAT solvers are amazing tools for Math!",
            color=PINK,
            font_size=42,
        ).next_to(more_importantly, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(more_importantly))
        self.next_slide()
        self.play(FadeIn(convince_you))
        self.next_slide()

        tcs_toolkit = (
            ImageMobject("img/tcs_toolkit.png")
            .scale(1.5)
            .next_to(convince_you, DOWN, buff=LARGE_BUFF)
            .shift(2 * RIGHT)
        )
        self.play(FadeIn(tcs_toolkit))
        self.next_slide()
        jackhammer = (
            ImageMobject("img/jackhammer.png")
            .scale(0.2)
            .next_to(tcs_toolkit, LEFT, buff=2.5 * LARGE_BUFF)
        )
        sat_solving = Text("SAT Solving", font_size=28).next_to(
            jackhammer, DOWN, buff=SMALL_BUFF
        )
        jackhammer_group = Group(jackhammer, sat_solving)
        self.play(FadeIn(jackhammer_group))
        self.next_slide()
        self.play(FadeOut(jackhammer_group, target_position=tcs_toolkit), runtime=1)
        self.next_slide()


class Outline(Slide):
    def construct(self):
        title = Text("Outline", font_size=60, color=YELLOW).to_edge(UP).shift(0.5 * UP)
        self.play(FadeIn(title))
        self.next_slide()
        basics_of_sat_solving = Text(
            "1) Basics of SAT-solving", font_size=36, color=BLUE
        ).next_to(title, DOWN, buff=LARGE_BUFF).shift(3.5*LEFT)
        sudoku = ImageMobject("img/sudoku.png").scale(0.2).next_to(basics_of_sat_solving, RIGHT, buff=MED_SMALL_BUFF)
        applications_to_math = Text(
            "2) Applications to Math", font_size=36, color=PURPLE
        ).next_to(basics_of_sat_solving, DOWN, buff=3*MED_LARGE_BUFF).shift(1*RIGHT)
        rubik_graph = ImageMobject("img/rubik_graph.png").scale(0.4).next_to(applications_to_math, RIGHT, buff=MED_SMALL_BUFF)
        packing_chromatic = Tex(
            r"3) Packing chromatic Number of $\mathbb{Z}^2$", font_size=48, color=GREEN
        ).next_to(applications_to_math, DOWN, buff=3*MED_LARGE_BUFF).shift(2*RIGHT)
        chessboard = ImageMobject("img/chessboard.png").scale(0.2).next_to(packing_chromatic, RIGHT, buff=MED_SMALL_BUFF)
        self.play(LaggedStart(Write(basics_of_sat_solving), FadeIn(sudoku), lag_ratio=0.5, run_time=1.2))
        self.next_slide()
        self.play(LaggedStart(Write(applications_to_math), FadeIn(rubik_graph), lag_ratio=0.5, run_time=1.2))
        self.next_slide()
        self.play(LaggedStart(Write(packing_chromatic), FadeIn(chessboard), lag_ratio=0.5, run_time=1.2))
        self.next_slide()


class Basics(Slide):
    def construct(self):
        title = Text("Let's start from the basics!", color=YELLOW).to_edge(UP)
        self.play(FadeIn(title))
        satisfiability = Text(
            "Satisfiability problems consists in receiving a set of constraints\n and deciding whether they can be simultaneously Satisfied.",
            t2c={"SAT": PINK, "Sat": PINK, "sat": PINK},
            font_size=32,
        )
        # sq = SurroundingRectangle(satisfiability, color=YELLOW, buff=0.5*MED_SMALL_BUFF)
        # satisfiability_group = VGroup(satisfiability, sq)
        satisfiability.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        self.next_slide()
        self.play(Write(satisfiability))
        self.next_slide()

        example_label = Text("Example:", font_size=42, color=BLUE).next_to(
            satisfiability, DOWN, buff=LARGE_BUFF
        )
        self.play(FadeIn(example_label))
        self.next_slide()

        example_high_level = BulletedList(
            "You cannot take both 15-112 and 15-210 on the same semester",
            "You must take either 15-210 or 15-251 on the same semester as 15-150",
            "They're not offering 15-251 this semester",
            font_size=38,
        )
        example_high_level.next_to(example_label, DOWN, buff=0.6 * MED_LARGE_BUFF)
        example_group = VGroup(example_label, example_high_level)

        for bullet in example_high_level:
            self.play(FadeIn(bullet))
            self.next_slide()

        cnf = Tex(r"CNF: ", r" (Clausal Normal Form)").scale(1.3)
        cnf[0].set_color(BLUE)

        # MathTex(r" {{(\overline{x_4} \lor \overline{x_1})}} \land {{(x_1 \lor x_3 \lor \overline{x_2})}} \land {{(\overline{x_3})}} ")
        cnf_example = MathTex(
            r" {{(\overline{x_{15\,112} } } \lor \overline{x_{15\,210} })}} \land {{(x_{15\,210} \lor x_{15\,251} \lor \overline{x_{15\,150} })}} \land {{(\overline{x_{15\,251} })}} "
        )
        cnf_example.next_to(cnf, DOWN, buff=0.7 * MED_LARGE_BUFF)
        cnf_example_group = VGroup(cnf, cnf_example)
        sq = SurroundingRectangle(
            cnf_example_group, color=YELLOW, buff=0.5 * MED_SMALL_BUFF
        )
        cnf_group = VGroup(cnf_example_group, sq)

        cnf_group.next_to(example_group, DOWN, buff=MED_LARGE_BUFF).shift(2 * UP)

        self.play(FadeOut(satisfiability), example_group.animate.shift(2 * UP))
        self.next_slide()
        self.play(FadeIn(cnf_group))

        self.next_slide()

        self.play(FadeOut(example_group), cnf_group.animate.shift(3 * UP))
        self.next_slide()

        cnf_example_s = MathTex(
            r" {{(\overline{x_{4} } \lor \overline{x_{1} })}} \land {{(x_{1} \lor x_{3} \lor \overline{x_{2} })}} \land {{(\overline{x_{3} })}} "
        )
        cnf_example_s.move_to(cnf_example)
        self.play(Transform(cnf_example, cnf_example_s))
        self.next_slide()
        # self.play(FadeOut(similar_to_ilp), cnf_group.animate.shift(UP*2.5))

        assignment = Tex(
            r"Consider the assignment: ", r"$x_1 = 0, x_2 = 1, x_3 = 0, x_4 = 1$"
        )
        assignment.next_to(cnf_group, DOWN, buff=MED_LARGE_BUFF * 1.4)

        self.next_slide()
        self.play(FadeIn(assignment))
        self.next_slide()
        self.play(assignment[1].animate.set_color(RED), runtime=1)

        # self.play(Indicate(cnf[2], color=YELLOW, scale_factor=1.3))

        self.next_slide()

        assignment2 = Tex(
            r"Consider the assignment: ", r"$x_1 = 1, x_2 = 0, x_3 = 0, x_4 = 0$"
        ).next_to(assignment, DOWN, buff=MED_LARGE_BUFF)

        self.play(FadeIn(assignment2))

        self.next_slide()
        self.play(assignment2[1].animate.set_color(PURE_GREEN), runtime=1)
        self.next_slide()

        sat = Tex(r"We say this formula is ", r" SAT ", r" (satisfiable)").next_to(
            assignment2, DOWN, buff=MED_LARGE_BUFF
        )
        sat[1].set_color(PURE_GREEN)
        self.play(FadeIn(sat))

        self.next_slide()


class SuccessOfSat(Slide):
    def construct(self):
        modern_solvers = Text(
            "Modern SAT-solvers\n are amazing pieces of engineering!",
            should_center=True,
            font_size=62,
            color=YELLOW,
        ).to_edge(UP)
        self.play(FadeIn(modern_solvers))
        self.next_slide()

        bullets = BulletedList(
            "Extremely efficient",
            "Extremely reliable",
            "Free and open source",
            "Nice interfaces",
            font_size=58,
        ).next_to(modern_solvers, DOWN, buff=MED_LARGE_BUFF)
        for bullet in bullets:
            self.play(FadeIn(bullet))
            self.next_slide()

        self.play(FadeOut(bullets), FadeOut(modern_solvers))
        stories = Text(
            "Successes of SAT in Math problems:", font_size=58, color=BLUE
        ).to_edge(UP)
        list_of_successes = BulletedList(
            "(2014) Boolean Erdős Discrepancy Problem",
            "(2016) Boolean Pytagorean Triples Problem",
            "(2018) Schur Number Five",
            "(2019) Keller's Conjecture",
            r"(2023) Packing-Chromatic Number of $\mathbb{Z}^2$",
            font_size=42,
        ).next_to(stories, DOWN, buff=MED_LARGE_BUFF)
        list_of_successes[4].set_color(YELLOW)
        self.next_slide()
        self.play(FadeIn(stories))
        self.next_slide()
        for bullet in list_of_successes:
            self.play(Write(bullet))
            self.next_slide()
        success = Text(
            "Their success is due to a combination of factors!", font_size=38
        ).next_to(list_of_successes, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(success))
        self.next_slide()
        self.play(FadeOut(list_of_successes), success.animate.shift(4.5 * UP))
        success_bullets = BulletedList(
            "Hardware advances",
            "Software advances",
            "Better encodings and automated-reasoning techniques",
            font_size=50,
        ).next_to(success, DOWN, buff=MED_LARGE_BUFF)
        success_bullets[1].set_color(ORANGE)
        success_bullets[2].set_color(PURE_GREEN)
        self.play(FadeIn(success_bullets[0]))
        self.next_slide()
        self.play(FadeIn(success_bullets[1]))
        self.next_slide()
        plot = ImageMobject("img/SatCompetition2023.png").scale(0.75)
        self.play(FadeIn(plot))
        self.next_slide()
        self.play(FadeOut(plot))
        self.next_slide()
        self.play(FadeIn(success_bullets[2]))
        self.next_slide()


class Solvers(Slide):
    def construct(self):
        overview = Text("How do solvers work?", font_size=48, color=YELLOW).to_edge(UP)
        self.play(FadeIn(overview))
        self.next_slide()
        complete_solvers = Text("Complete", font_size=42, color=BLUE).next_to(
            overview, DOWN, buff=MED_LARGE_BUFF
        )
        complete_solvers.shift(3.5 * LEFT)
        sls = Text("Stochastic-Local-Search", font_size=42, color=BLUE).next_to(
            complete_solvers, RIGHT, buff=MED_LARGE_BUFF
        )
        sls.shift(2.5 * RIGHT)
        # arrows = VGroup(Arrow(overview, sls), Arrow(overview, complete_solvers))
        dividing_line = DashedLine([0, -3, 0], [0, 3, 0]).next_to(
            overview, DOWN, buff=MED_LARGE_BUFF
        )

        self.play(FadeIn(complete_solvers), FadeIn(dividing_line), FadeIn(sls))
        complete_description = Text(
            "UNSAT proof or SAT assignment", font_size=28
        ).next_to(complete_solvers, DOWN, buff=MED_LARGE_BUFF)
        sls_description = Text("SAT assignment", font_size=28).next_to(
            sls, DOWN, buff=MED_LARGE_BUFF
        )
        self.next_slide()
        self.play(FadeIn(complete_description), FadeIn(sls_description))
        self.next_slide()

        complete_based = Text(
            "Based on smart back-tracking and learning \n (DPLL and CDCL are the main algorithms)",
            font_size=24,
            color=ORANGE,
        ).next_to(complete_description, DOWN, buff=MED_LARGE_BUFF)
        sls_based = Text(
            "Based on flipping variables randomly\n to improve some metric",
            font_size=24,
            color=PINK,
        ).next_to(sls_description, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(complete_based))
        self.next_slide()
        self.play(FadeIn(sls_based))
        self.next_slide()

        complete_kideas = Text(
            "Key ideas: unit propagation,\n learning from conflicts",
            font_size=24,
            t2c={"Key ideas": GREEN},
        ).next_to(complete_based, DOWN, buff=MED_LARGE_BUFF)
        sls_kideas = Text(
            "Key ideas: pick the right variable to flip,\n restart when stuck",
            font_size=24,
            t2c={"Key ideas": GREEN},
        ).next_to(sls_based, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(complete_kideas))
        self.next_slide()
        self.play(FadeIn(sls_kideas))
        self.next_slide()

        complete_example = Text(
            "Examples: Kissat and CaDiCaL", font_size=28, t2c={"Examples:": YELLOW}
        ).next_to(complete_kideas, DOWN, buff=MED_LARGE_BUFF)
        sls_example = Text(
            "Examples: YalSAT and DDFW", font_size=28, t2c={"Examples:": YELLOW}
        ).next_to(sls_kideas, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(complete_example))
        self.next_slide()
        self.play(FadeIn(sls_example))
        self.next_slide()
        self.clear()
        mini_demo = Text("Mini demo :)", color=YELLOW)
        self.play(FadeIn(mini_demo))
        self.next_slide()


class SudokuExample(Slide):
    def construct(self):
        example_title = Text(
            "Example: Sudoku", font_size=72, t2c={"Sudoku": YELLOW}
        ).to_edge(UP)
        example_title.shift(0.25 * UP)
        self.play(FadeIn(example_title))

        self.next_slide()

        sudoku_img = (
            ImageMobject("img/sudoku.png")
            .scale(0.5)
            .next_to(example_title, DOWN, buff=MED_LARGE_BUFF)
            .shift(LEFT * 4.5 + 0.5 * DOWN)
        )
        self.play(FadeIn(sudoku_img))

        self.next_slide()

        variables = (
            Tex(
                r"Variables: ",
                r"$x_{i,j,n}$ ",
                r" for $i, j, n \in \{1, \ldots, 9\}$",
                font_size=42,
            )
            .next_to(sudoku_img, RIGHT, buff=LARGE_BUFF)
            .shift(UP * 2.7)
        )
        variables[0].set_color(BLUE)
        variables[1].set_color(YELLOW)
        self.play(FadeIn(variables))

        self.next_slide()

        clauses = Tex(r"Clauses:", color=BLUE, font_size=42).next_to(
            variables, DOWN, buff=MED_SMALL_BUFF
        )
        self.play(FadeIn(clauses))

        cells_get_numbers = Tex(
            r"1)",
            r" Each cell $(i, j)$ gets some number",
            r"$$ \left(\bigvee_{n = 1}^9 x_{i,j,n}\right)$$",
            font_size=38,
        ).next_to(clauses, DOWN)
        cells_get_numbers[0].set_color(PINK)
        cells_get_numbers[2].set_color(YELLOW)

        respect_given_numbers = Tex(
            r"2)",
            r" Respect given clues\\",
            r" \quad \; \; \; \; \; \; \; \; e.g., ",
            r"$(x_{1,1,5}) \land (x_{2,1,6}) \land \cdots$",
            font_size=38,
        ).next_to(cells_get_numbers, DOWN, buff=MED_LARGE_BUFF)
        respect_given_numbers[0].set_color(PINK)
        respect_given_numbers[3].set_color(YELLOW)

        at_most_one = Tex(
            r"3)",
            r" At-Most-One constraints\\",
            r"e.g., ",
            r"$(\overline{x_{2,2,7}} \lor \overline{x_{3, 1, 7}})$",
            font_size=38,
        ).next_to(respect_given_numbers, DOWN, buff=MED_LARGE_BUFF)
        at_most_one[0].set_color(PINK)
        at_most_one[3].set_color(YELLOW)

        clause_group = VGroup(cells_get_numbers, respect_given_numbers, at_most_one)
        clause_group.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.next_slide()
        self.play(FadeIn(cells_get_numbers))
        self.next_slide()
        self.play(FadeIn(respect_given_numbers))
        self.next_slide()
        self.play(FadeIn(at_most_one))

        self.next_slide()
        self.clear()
        sat_title = Text(r"Brief Demo :)", font_size=72, color=YELLOW)
        self.play(FadeIn(sat_title))

        self.next_slide()


class ArtOfSat(Slide):
    def construct(self):
        art_title = Text(
            "A glimpse into the Art of Encodings",
            font_size=48,
            color=PINK,
            t2c={"art": PINK},
        ).to_edge(UP)

        self.play(FadeIn(art_title))
        self.next_slide()

        at_most_one = Tex(
            r"How to encode that at most one of ",
            r"$x_1, \ldots, x_n$",
            r" is true?",
            font_size=42,
        ).next_to(art_title, DOWN, buff=MED_LARGE_BUFF)
        at_most_one[1].set_color(YELLOW)

        self.play(FadeIn(at_most_one))
        self.next_slide()

        naive_idea = Tex(
            r"The naive encoding is to create clauses ",
            r"$(\overline{x_i} \lor \overline{x_j})$",
            r" for all $i \neq j$",
        ).next_to(at_most_one, DOWN, buff=MED_LARGE_BUFF)
        naive_idea[1].set_color(RED)
        self.play(FadeIn(naive_idea))
        self.next_slide()

        nb_clauses = Tex(r"This uses", r" $O(n^2)$ ", r"many clauses!").next_to(
            naive_idea, DOWN, buff=MED_LARGE_BUFF
        )
        nb_clauses[1].set_color(RED)

        self.play(FadeIn(nb_clauses))

        do_better = Tex(
            r"It turns out we can do better and use only ",
            r"$O(n)$",
            r" clauses,\\ by adding $O(n)$ new variables!",
        ).next_to(nb_clauses, DOWN, buff=MED_LARGE_BUFF)
        do_better[1].set_color(YELLOW)
        self.next_slide()
        self.play(FadeIn(do_better))
        self.next_slide()

        self.play(FadeOut(naive_idea), FadeOut(nb_clauses), FadeOut(do_better))
        idea = MathTex(
            r"\textsc{AMO}(x_1, \ldots, x_n) \equiv \textsc{AMO}(x_1, x_2, x_3, y_1) \land \textsc{AMO}(\overline{y_1}   , x_4, \ldots, x_n)",
            font_size=36,
            substrings_to_isolate=[r"y_1", r"\overline{y_1}", r"\textsc{AMO}"],
        ).next_to(at_most_one, DOWN, buff=MED_LARGE_BUFF * 1.3)
        idea.set_color_by_tex(r"y_1", RED)
        idea.set_color_by_tex(r"\neg", RED)
        idea.set_color_by_tex(r"AMO", BLUE)

        key = Tex(
            r"Key idea: ",
            r"Introduce a new variable $y_1$ to ``coordinate'' a divide-and-conquer",
            font_size=36,
        ).next_to(idea, DOWN, buff=MED_LARGE_BUFF)
        key[0].set_color(YELLOW)

        key_idea = VGroup(idea, key)
        krec = SurroundingRectangle(key_idea, color=YELLOW, buff=MED_SMALL_BUFF)
        kidea = VGroup(key_idea, krec)

        self.next_slide()
        self.play(FadeIn(kidea))

        # self.play(FadeIn(key))
        self.next_slide()

        recursively = Tex(
            r"We do this recursively, and the base case is\\ when $n \leq 4$ we use the naive encoding",
            font_size=36,
        )
        recursively.next_to(key, DOWN, buff=MED_LARGE_BUFF)

        self.play(FadeIn(recursively))
        self.next_slide()

        nb_clauses = Tex(
            r"Number of clauses", r" $f(n)$", r" satisfies ", r"$f(n) = f(4) + f(n-2)$"
        ).next_to(recursively, DOWN, buff=MED_LARGE_BUFF)
        nb_clauses[1].set_color(ORANGE)
        nb_clauses[3].set_color(ORANGE)
        self.play(FadeIn(nb_clauses))
        self.next_slide()

        # equations = Tex(r"$f(n) = f(4) + f(n-2)$", r"$ \; = 6 + f(n-2)$", r"$\quad f(1) = 0, f(2) = 1, f(3) = 3.$", font_size=36, color=ORANGE).next_to(nb_clauses, DOWN, buff=MED_LARGE_BUFF)
        # self.play(FadeIn(equations[0]))
        # self.next_slide()
        # self.play(FadeIn(equations[1]))
        # self.next_slide()
        # equations[2].set_color(GREEN)
        # self.play(FadeIn(equations[2]))
        # self.next_slide()

        conclusion = Tex(
            r"So we use $f(n) = O(n)$ many clauses!", color=YELLOW
        ).next_to(nb_clauses, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(conclusion))
        self.next_slide()
        self.play(FadeOut(conclusion), FadeOut(nb_clauses), FadeOut(recursively), FadeOut(kidea), FadeOut(at_most_one))
        why_not = Text("Why not a balanced-tree recursion?", font_size=36, color=RED).next_to(art_title, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(why_not))
        self.next_slide()
        img_1 = ImageMobject("img/comparison.png").scale(0.6).next_to(why_not, DOWN, buff=MED_LARGE_BUFF)
        img_2 = ImageMobject("img/bin_tree.png").scale(1.25).next_to(why_not, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(img_1))
        self.next_slide()
        self.play(FadeOut(img_1), FadeIn(img_2))
        self.next_slide()
