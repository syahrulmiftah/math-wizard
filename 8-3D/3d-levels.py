from manim import *

# manim -p 3d-levels.py ThreeDimension


class ThreeDimension(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "x",
                "Lets start with simple plane",
            ],
            # index 2
            [
                "x\cdot y",
                "Lets put some 'y'",
            ],
            # index 3
            [
                "x^{2}",
                "How about square huh",
            ],
            # index 4
            [
                "x^{2}+y",
                "Add 'y' to chane the angle",
            ],
            # index 5
            [
                "x^{2}-y^{2}",
                "Would you eat colored chips?",
            ],
            # index 6
            [
                "x^{2}-y^{3}",
                "Not really the best shapes of slides, innit?",
            ],
            # index 7
            [
                "x^{2}+y^{2}",
                "As a math lover, the only thing i can pull is this graph",
            ],
            # index 8
            [
                "\sin\left(x\\right)",
                "It's trig time baby",
            ],
            # index 9
            [
                "\sin\left(x+y\\right)",
                "Lets roll it sideways",
            ],
            # index 10
            [
                "\sin \left(x\cdot y\\right)",
                "This graph looks like a water ripple, but in the wrong direction",
            ],
            # index 11
            [
                "\sin\left(2x\\right)+\sin\left(2y\\right)",
                "This one looks like an egg tray",
            ],
            # index 12
            [
                "\sin\left(2x\\right)\cdot\cos\left(y\\right)\cdot x+y",
                "What do you think this looks like?",
            ],
            # index 13
            [
                "\left[\cos\left(\phi\\right)\cdot\sin\left(\\theta\\right),\ \sin\left(\phi\\right)\cdot\sin\left(\\theta\\right),2\cos\left(\\theta\\right)\\right]",
                "Now moved on to sphere",
            ],
            # index 14
            [
                "\left[\cos\left(\phi\\right)\cdot\sin\left(\\theta\\right),\ \sin\left(\phi\\right)\cdot\sin\left(\\theta\\right),2\cos\left(\\theta\\right)\\right]",
                "Let's try parametric surface",
            ],

            # index 15
            [
                "\left[\left(\cos\left(u\\right)+3\\right)\cos\left(c\cdot v\\right)\ ,\left(\cos\left(u\\right)+3\\right)\cdot\sin\left(v\\right),\ 2\cdot\sin\left(u\\right)\\right]",
                "This is a torus, or in football terms, a donut",
            ],
            # index 16
            [
                "\left[\sin\left(u\\right)+\cos\left(v\\right),\cos\left(1.95u\\right)+\sin\left(v\\right),4\left(\sin\left(v\\right)+\cos\left(4u\\right)\\right)\\right]",
                "Just some cool exhaust tips",
            ],
            # index 17
            [
                "\left[\cos\left(\phi\\right)\cdot\sin\left(\\theta\\right),\ \sin\left(\phi\\right)\cdot\sin\left(\\theta\\right),2\cos\left(3\\theta\\right)\\right]",
                "Look, i made a jet engine",
            ],
            # index 18
            [
                "\left[\cos\left(\phi\\right)\cdot\sin\left(\\theta c\\right),\ \sin\left(\phi\\right)\cdot\sin\left(\\theta\\right),2\cos\left(\\theta\\right)\\right]",
                "Lets try out some animations",
            ],
            # index 19
            [
                """
                \left[\left(\cos\left(cu\\right)+3\\right)\cos\left(v\\right),\ \left(\cos\left(cu\\right)+3\\right)\sin\left(v\\right),\ 2\sin\left(u\\right)\\right]
                """,
                "Now we animate the donut",
            ],

            # index 20
            [
                "\sin\left(x+d\\right)",
                "How about some wave",
            ],
            # index 21
            [
                "2\sin\left(x+d\\right)+\cos\left(x+y\\right)\cos\left(d\\right)",
                "Slightly better wave",
            ],
            # index 22
            [
                "\sin\left(x\cdot y+d\\right)",
                "Nice animation",
            ],
            # index 23
            [
                "\left[\sin\left(u+d\\right),u+\cos\left(v+d\\right),v+\cos\left(u+d\\right)\\right]",
                "Pretty sure this is how snakes move",
            ],
        ]
        lis = [
            [
                "\left[\cos\left(\phi\\right)\cdot\sin\left(\\theta\\right),\ \sin\left(\phi\\right)\cdot\sin\left(\\theta\\right),2\cos\left(\\theta\\right)\\right]",
                "Now, let's move on to spheres",
            ]
        ]        

        fix = 5

        # 1
        for i in range(len(lis)):
            equation = MathTex(lis[i][0]).scale(
                1).shift(UP).set_color(YELLOW)

            mini_text = Text(lis[i][1]).scale(0.5).next_to(
                equation, DOWN*3).set_color("##e0e0e0")

            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(mini_text, shift=UP))
            self.wait(3.5)
            self.clear()

# manim -p 3d-levels.py ThreeDimension
