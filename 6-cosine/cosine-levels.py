from manim import *

# manim -p desmos-levels.py CosineLevels


class CosineLevels(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "y=\cos\left(x\\right)",
                "Lets start with the basic cosine wave",
            ],
            # index 2
            [
                "y=\cos\left(15x\\right)",
                "Increase the value of x to get denser wave",
            ],
            # index 3
            [
                "y=25\cos\left(x\\right)",
                "Multipy the cosine value to get bigger wave",
            ],
            # index 4
            [
                "y=\cos\left(x+y\\right)",
                "Start adding some 'y'",
            ],
            # index 5
            [
                "y=\cos\left(x+y^{2}\\right)",
                "This is the fin-est math graphs. (pun intended)",
            ],
            # index 6
            [
                "y=9\cos\left(9x+9y\\right)",
                "Its 'nine' time",
            ],
            # index 7
            [
                "y=\cos\left(9x+9y^{2}\\right)",
                """
                OPTICAL ILLUSION: the left part appears smaller than the right
                
                despite being exactly the same size""",
            ],
            # index 8
            [
                "y=\cos\left(x\\right)+\cos\left(2x\\right)",
                "Lets play around with two cosines",
            ],
            # index 9
            [
                "y=\cos\left(x\\right)+\cos\left(20x\\right)",
                "Increase one of the 'x' to get wiggly graph",
            ],
            # index 10
            [
                "y=\cos\left(2y\\right)+\cos\left(2x\\right)",
                "raindrop",
            ],
            # index 11
            [
                "y=\cos\left(2y\\right)+\cos\left(2x\\right)+\cos\left(2x\\right)",
                "Add more cosine",
            ],
            # index 12
            [
                "y=\cos\left(2y\\right)+3\cos\left(2x\\right)",
                """
                Guess the shape of this graph. 

                If you're wrong, you have to subscribe to my channel.""",
            ],
            # index 13
            [
                "y=\cos\left(3y\\right)+\cos\left(2x\\right)+\cos\left(3x\\right)+\cos\left(4x\\right)",
                "This is the first face you will see today and certainly wont be the last",
            ],
            # index 14
            [
                "y=\cos\left(x\\right)^{3}",
                "A humble introduction to exponents",
            ],
            # index 15
            [
                "y=\cos\left(x\\right)^{99}-2\cos\left(x\\right)",
                "Things just went from 3 to 99 real quick",
            ],
            # index 16
            [
                "y=\cos\left(x\\right)^{99}-2\cos\left(x\\right)+\cos\left(5y\\right)",
                "This just looks like cosine wave but with extra steps",
            ],
            # index 17
            [
                "y=-\cos\left(x\\right)^{99}-3\cos\left(x\\right)+\cos\left(5y\\right)^{99}",
                "Spikey",
            ],
            # index 18
            [
                "y=\\frac{\cos\left(x\\right)}{\cos\left(y\\right)}",
                "Let's cook some graph using division",
            ],
            # index 19
            [
                "y=\\frac{\cos\left(x\\right)}{\cos\left(y\\right)}x",
                "This is the point where desmos start malfunctioning",
            ],
            # index 20
            [
                "y=\\frac{\cos\left(x\\right)}{\cos\left(y\\right)}-\exp\left(\cos\left(x\\right)\\right)+\cos\left(2y\\right)",
                "Happy boi",
            ],
            # index 21
            [
                "y=\\frac{\cos\left(2x\\right)}{\cos\left(y\\right)}\exp\left(2\cos\left(x\\right)\\right)+\cos\left(2y\\right)",
                "The graph seem kinda sus",
            ],
            # index 22
            [
                "\cos\left(x\\right)=\cos\left(y\\right)",
                "Finally, some nice graphs",
            ],
            # index 23
            [
                "\cos\left(x\\right)=-\cos\left(y\\right)",
                """
                Today i will do something different, 
                """,
            ],
            # index 23 b
            [
                """
                \cos\left(x\\right)&=\cos\left(y\\right) \\\\
                \cos\left(x\\right)&=-\cos\left(y\\right)
                """,
                """
                Today i will do something different, 

                you know what lets combine this graph with the previous one
                """,
            ],
            # index 24
            [
                """
                \cos\left(x\\right)=\\pm\cos\left(y\\right)^{2}
                """,
                "I know you want more of these graphs",
            ],
            # index 25
            [
                """
                \cos\left(x\\right)=\\pm\cos\left(y\\right)^{2}+\cos\left(y\\right)
                """,
                "The key is to have a plus and minus sign; it is that simple",
            ],
            # index 26
            [
                """
                \cos\left(x\\right)=\\pm\cos\left(y\\right)^{2}\cos\left(y\\right)
                """,
                "I hope you are not confused by this graph",
            ],
            # index 27
            [
                """
                \cos\left(x\\right)=\\pm\cos\left(y\\right)^{3}\exp\left(\cos\left(3x\\right)\\right)
                """,
                "You can make all sorts of two-color graphs",
            ],
            # index 28
            [
                """
                \cos\left(y\\right)=\cos\left(x\\right)^{3}\\pm\exp\left(9\cos\left(5x\\right)+9\cos\left(y\\right)\\right)
                """,
                "This is the closest I can get to a Batman logo",
            ],
            # index 29
            [
                """
                \cos\left(x\\right)=\cos\left(y\\right)^{3}\\pm\exp\left(\cos\left(6x\\right)+\cos\left(5y\\right)\\right)
                """,
                "This one is probably my favourite, it fit so perfectly",
            ],
            # index 30
            [
                """
                \cos\left(x\\right)&=\cos\left(y\\right)^{3}\\pm\exp\left(\cos\left(3x\\right)\\right) \\\\
                \cos\left(x\\right)&=\cos\left(y\\right)^{3}-\exp\left(\cos\left(3x\\right)\\right)\cos\left(2x\\right)
                """,
                """
                Desmos: You can make more than two graphs at once,
                
                My honest reaction:
                """,
            ],
            # index 31
            [
                "y=10\cos\left(xy\\right)\cos\left(x^{2}-y^{2}\\right)",
                "Scattered...",
            ],
            # index 32
            [
                "y=x\cos\left(x^{2}+y^{2}\\right)+\exp\left(x\\right)",
                "What a weird graphs",
            ],
            # index 33
            [
                "y=x\cos\left(x^{2}+y^{2}\\right)+x\cos\left(x\\right)",
                "Pattern in a pattern",
            ],
            # index 34
            [
                """
                \cos\left(xy\\right)&=\cos\left(x^{2}+y^{2}\\right) \\\\
                (x±1)^{2}+(y-1)^{2}&=0.2 \\\\
                y&=-\sqrt{1.-x^{2}}-0.5
                """,
                "I add a face to this graph to make it better",
            ],
            # index 35
            [
                "\cos\left(x\\right)=xy\cos\left(x^{2}+y^{2}\\right)",
                "We're in the Endgame now",
            ],
            # index 36
            [
                "\cos\left(2x+3y\\right)=2\cos\left(x^{2}+y^{2}\\right)",
                "Unstable...",
            ],
            # index 37
            [
                "\cos\left(2xy\\right)=\cos\left(x^{2}+y^{2}\\right)",
                """
                I wish this could be rendered in full detail
                
                By the way, comment down below which are your favorite graphs
                """,
            ],
            # index 38
            [
                "\cos\left(2xy\\right)=\cos\left(x^{2}+y^{2}\\right)+\cos\left(9x\\right)",
                "Behold!... The God of Graphs",
            ],
            # index 39
            [
                "",
                "",
            ],
            # index 40
            [
                "",
                "",
            ],
            # index 41
            [
                "",
                "",
            ],
            # index 42
            [
                "",
                "",
            ],
            # index 43
            [
                "",
                "",
            ],
            # index 44
            [
                "",
                "",
            ],
            # index 45
            [
                "",
                "",
            ],
        ]

        fix = [37,38]

        # 1
        for i in fix:
            equation = MathTex(lis[i][0]).scale(
                1.15).shift(UP).set_color(YELLOW)
            mini_text = Text(lis[i][1]).scale(0.5).next_to(equation, DOWN*3)
            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(mini_text, shift=UP))
            self.wait(3)
            self.clear()

# manim -p cosine-levels.py CosineLevels
