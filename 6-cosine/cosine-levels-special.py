from manim import *

# manim -p desmos-levels.py CosineLevels


class CosineLevels(Scene):
    def construct(self):
        lis = [
            "\cos\left(x\\right)=-\cos\left(y\\right)",
            "\cos\left(x\\right)&=\cos\left(y\\right)",
            "Today i will do something different",
            """
            You know what, let's combine this graph with the previous one 
            
            and see what happens
                """,
        ]

        equation_first = MathTex(lis[0]).scale(
            1.15).shift(UP).set_color(YELLOW)
        equation_second = MathTex(lis[1]).scale(
            1.15).shift(UP).set_color(YELLOW).next_to(equation_first, UP*2).align_to(equation_first, LEFT)

        mini_text1 = Text(lis[2]).scale(0.5).next_to(equation_first, DOWN*3)
        mini_text2 = Text(lis[3]).scale(0.5).next_to(mini_text1, DOWN*3)

        self.wait(0.25)
        self.play(FadeIn(equation_first))
        self.play(FadeIn(mini_text1, shift=UP))
        self.wait(1.5)
        self.play(FadeIn(mini_text2))
        self.wait(1)
        self.play(FadeIn(equation_second, shift=DOWN))
        self.wait(2)
        self.clear()

# manim -p cosine-levels-special.py CosineLevels
