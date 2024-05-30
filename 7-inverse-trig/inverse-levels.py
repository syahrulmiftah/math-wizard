from manim import *

# manim -p inverse-levels.py Inverse


class Inverse(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "r=\\arcsin\left(\\theta\\right)",
                "Lets start with the basics",
            ],
            # index 2
            [
                "r=\\arctan\left(\\theta\\right)",
                "How about arctan",
            ],
            # index 3
            [
                "r=\\arccos\left(\cot\left(\\theta\\right)\\right)",
                "Lets try nested function",
            ],
            # index 4
            [
                "r=\\arccos\left(\cos\left(\\theta\\right)\\right)",
                "It's starting to form a shape",
            ],
            # index 5
            [
                "r=\\arccos\left(\\tan\left(1.5\\theta\\right)\\right)",
                "Decimals usually create interesting graphs",
            ],
            # index 6
            [
                """
                r&=\\arccos\left(\\tan\left(3\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\cot\left(3\\theta\\right)\\right)
                """,
                "That was fun, lets do it again",
            ],
            # index 7
            [
                "r=\\arccos\left(\\tan\left(1.1\\theta\\right)\\right)",
                "spiral",
            ],
            # index 8
            [
                """
                r&=\\arccos\left(\\tan\left(1.1\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\cot\left(1.1\\theta\\right)\\right)
                """,
                "Lets compare these two graph side by side",
            ],
            # index 9
            [
                """
                r&=\\arccos\left(\\tan\left(2\\theta\\right)+\cot\left(1.6\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\\tan\left(2\\theta+\\frac{\pi}{2}\\right)+\cot\left(1.6\\theta\\right)\\right)
                """,
                "Such a nice garphs",
            ],
            # index 10
            [
                """
                r&=\\arccos\left(\\tan\left(3\\theta\\right)+\cot\left(2.4\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\\tan\left(4\\theta\\right)+\cot\left(3.2\\theta\\right)\\right)
                """,
                "Do you notice the pattern here?",
            ],
            # index 11
            [
                "r=\\arccos\left(\\tan\left(0.3\\theta\\right)\\right)",
                "This is some serious gourmet sh*t!",
            ],
            # index 12
            [
                """
                r&=\\arccos\left(\\tan\left(0.3\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\cot\left(0.3\\theta\\right)\\right)
                """,
                "Let's add another colour",
            ],
            # index 15
            [
                """
                r&=\\arccos\left(\\frac{\\tan\left(1.2\\theta\\right)}{1.236}+\\frac{\cot\left(2.4\\theta\\right)}{1.236}\\right) \\\\
                r&=\pi \\\\
                r&=\\frac{\pi}{5}
                """,
                "Honestly, I don't understand how the graph was drawn the way it is",
            ],

            [
                "r=\\arccos\left(\sin\left(2\\theta\\right)\cos\left(2.1\\theta\\right)\\right)",
                "This one looks 3D",
            ],
            # index 13
            [
                """
                r&=\\arccos\left(\\frac{\\tan\left(0.2\\theta\\right)}{3.25}+\\frac{\cot\left(0.4\\theta\\right)}{3.25}\\right) \\\\
                r&=\\arccos\left(\\frac{\\tan\left(0.3\\theta\\right)}{3.25}+\\frac{\cot\left(0.6\\theta\\right)}{3.25}\\right) \\\\
                r&=\\arccos\left(\\frac{\\tan\left(0.4\\theta\\right)}{3.25}+\\frac{\cot\left(0.8\\theta\\right)}{3.25}\\right) \\\\
                r&=\\arccos\left(\\frac{\\tan\left(0.6\\theta\\right)}{3.25}+\\frac{\cot\left(1.2\\theta\\right)}{3.25}\\right)
                """,
                "I'm going full blast with this one",
            ],
            # index 14
            [
                """
                r&=\\arccos\left(\\frac{\\tan\left(0.7\\theta\\right)}{3.25}+\\frac{\cot\left(1.4\\theta\\right)}{3.25}\\right) \\\\
                r&=\\arccos\left(\\frac{\\tan\left(0.8\\theta\\right)}{3.25}+\\frac{\cot\left(1.6\\theta\\right)}{3.25}\\right) \\\\
                r&=\\arccos\left(\\frac{\\tan\left(0.9\\theta\\right)}{3.25}+\\frac{\cot\left(1.8\\theta\\right)}{3.25}\\right) \\\\
                r&=\\arccos\left(\\frac{\\tan\left(1.1\\theta\\right)}{3.25}+\\frac{\cot\left(2.2\\theta\\right)}{3.25}\\right)
                """,
                "MORE!!!",
            ],
            # index 16
            [
                "r=\\arccos\left(\\frac{\\tan\left(1.2\\right)}{-v_{1}+0.1}+\\frac{\cot\left(2.4\\theta\\right)}{-v_{1}+0.1}\\right)",
                "Introducing variables...",
            ],
            # index 17
            [
                """
                r&=\\arccos\left(\sin\left(2v\\theta\\right)\cos\left(\sin\left(v\\theta\\right)\\right)\\right) \\\\
                r&=\\arccos\left(\sin\left(2v\\theta\\right)\cos\left(\sin\left(v\\theta\\right)\\right)\\right) \\\\
                r&=\\arccos\left(\sin\left(2v\\theta\\right)\cos\left(\sin\left(v\\theta\\right)\\right)\\right)
                """,
                """
                Let me offer you a different perspective 

                upon seeing math graphs
                """,
            ],
            # index 18
            [
                """
                r&=\\arccos\left(\cos\left(0.6\\theta\\right)+v_{2}\sin\left(0.6\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\cos\left(0.8\\theta\\right)+v_{2}\sin\left(0.8\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\cos\left(1.2\\theta\\right)+v_{2}\sin\left(1.2\\theta\\right)\\right)
                """,
                "A nice quick animation",
            ],
            # index 19
            [
                """
                r&=\\arccos\left(\cos\left(1.2\\theta\\right)\\right) \\\\
                r&=\\arccos\left(\cos\left(1.2\\theta\\right)+0.7265\sin\left(1.2\\theta\\right)\\right)
                """,
                "These two graphs were meant for each other",
            ],
            # index 21
            [
                """
                r=\\arccos\left(\sin\left(\\frac{v_{4}}{3}\\theta\\right)\cos\left(v_{4}\sin\left(1.2\\theta\\right)\\right)\\right)\ 
                v_{4}=3
                """,
                "Can you guess the end result of this graph?",
            ],
            # index 22
            [
                "r=\\arctan\left(\\tan\left(1.9\\theta\\right)\\right)",
                "Simple but beautiful",
            ],
            # index 23

            # index 24
            [
                "r=\exp\left(v_{6}\\arcsin\left(\sin\left(1.2\\theta\\right)\\right)+v_{7}\cos\left(1.2\\theta\\right)\\right)",
                "its 'exp' time",
            ],
            # index 25
            [
                "r=\exp\left(\\arccos\left(\sin\left(\cos\left(1.2\\theta+\pi\\right)\\right)\cos\left(\sin\left(100\\theta\\right)\\right)\\right)\\right)",
                "I might summon a demon with this one",
            ],
            # index 26
            [
                """
                r&=5\exp\left(v_{9}v_{8}\\arctan\left(v_{8}\\tan\left(1.9\\theta\\right)\\right)\\right) \\\\
                r&=5\exp\left(v_{9}v_{8}\operatorname{arccot}\left(v_{8}\cot\left(1.9\\theta\\right)\\right)\\right)
                """,
                "I think this graph would make a good logo",
            ],
            # index 27
            [
                """
                r&=5\exp\left(v_{9}v_{8}\\arctan\left(v_{8}\cot\left(v_{9}1.9\\theta\\right)\\right)\\right) \\\\
                r&=5\exp\left(-v_{9}v_{8}\\arctan\left(v_{8}\\tan\left(v_{9}1.9\\theta\\right)\\right)\\right)
                """,
                "Lets animate the spiral",
            ],
            # index 28
            [
                """
                r=&5\exp\left(v_{10}\\arctan\left(cv_{10}\\tan\left(d\\theta+\\frac{\pi}{2}\\right)\\right)\\right) \\\\
                &+a\cos\left(ac\\theta\\right)
                """,
                "This is just too much variable...",
            ],
            # index 29
            [
                """
                r&=n_{1}\exp\left(v_{11}\\arctan\left(\\tan\left(6\\theta+\\frac{\pi}{2}\\right)\\right)\\right) \\\\
                n_{1}&=\left[0,...,5\\right]
                """,
                """
                Here's a little trick, im gonna use whats called array

                and the result looks like some ancient stuff or something
                """,
            ],
            # index 30
            [
                """
                r&=n_{1}\exp\left(v_{12}\ \\arctan\left(\\tan\left(a_{1}20\\theta\\right)\\right)\\right) \\\\
                r&=n_{1}\exp\left(v_{12}\ \\arctan\left(\\tan\left(20\\theta+2\\frac{\pi}{3}\\right)\\right)\\right) \\\\
                r&=n_{1}\exp\left(v_{12}\ \\arctan\left(\\tan\left(20\\theta+\\frac{\pi}{3}\\right)\\right)\\right) \\\\
                n_{1}&=\left[0,...,5\\right]
                """,
                """
                This would make a cool screensaver

                Thanks for watching
                """,
            ],
        ]

        lis = [
            [
                """
                r=&5\exp\left(v_{10}\\arctan\left(cv_{10}\\tan\left(d\\theta+\\frac{\pi}{2}\\right)\\right)\\right) \\\\
                &+a\cos\left(ac\\theta\\right)
                """,
                "From zero to hero",
            ],
        ]

        fix = 5

        # 1
        for i in range(len(lis)):
            equation = MathTex(lis[i][0]).scale(
                1.15).shift(UP).set_color(YELLOW)

            mini_text = Text(lis[i][1]).scale(0.5).next_to(equation, DOWN*3).set_color("##e0e0e0")

            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(mini_text, shift=UP))
            self.wait(3.5)
            self.clear()

# manim -p inverse-levels.py Inverse

