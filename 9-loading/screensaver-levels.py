from manim import *

# manim -p screensaver-levels.py ScreensaverLevels
# &\left(t+v_{6},\sin\left(t+v_{6}+\pi\\right)\\right)


class ScreensaverLevels(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "r=4\log_{2}\left(v_{1}\\right)",
                """
                Let's begin with a basic design,
                
                a zooming circle will do.
                """,
            ],
            # index 2
            [
                """
                r&=\sin\left(\\theta+v_{2}\\right) \\\\
                4&=(x+\sin\left(v_{2}\\right))^{2}+(y+\cos\left(v_{2}\\right))^{2}
                """,
                "Let's make it with two circles",
            ],
            # index 3
            [
                "\left(2\cos\left(t\\right),2\sin\left(t+\sin\left(v_{3}\\right)\\right)\\right)",
                "Clean and simple",
            ],
            # index 4
            [
                "\left(\cos\left(t\\right),\sin\left(t+3v_{4}\\right)+\\tan\left(v_{4}\\right)\\right)",
                "Swipe up loading screen are underrated",
            ],
            # index 5
            [
                "\left(t,\sin\left(t+v_{5}\\right)\\right)",
                "Sine waves are fun to watch",
            ],
            # index 6
            [
                "\left(t+v_{6},\sin\left(t+v_{6}\\right)\\right)",
                "Let's make the waves move, shall we?",
            ],
            # index 7 &\left(t+v_{6},\sin\left(t+v_{6}+\pi\\right)\\right)
            # manim -p screensaver-levels.py ScreensaverLevels
            [
                """
                \left(t+v_{6},\sin\left(t+v_{6}\\right)\\right) \\\\
                \left(t+v_{6},\sin\left(t+v_{6}+\pi\\right)\\right)
                """,
                "Add another wave and see what happens...",
            ],
            # index 8 \left(&v_{6}+2\pi,\left|\sin\left(t+v_{6}\\right)\\right|+0.2\\right)
            [
                """
                \left(t+v_{6},\left|\sin\left(t+v_{6}\\right)\\right|+0.2\\right) \\\\
                \left(v_{6}+2\pi,\left|\sin\left(t+v_{6}\\right)\\right|+0.2\\right)
                """,
                "Who would have thought a bouncing ball would make a cool loading screen?",
            ],
            # index 9
            [
                "\left(\cos\left(t\\right),\sin\left(t+\sin\left(t+v_{7}\\right)\\right)\\right)",
                "How about some shapeshifting?",
            ],
            # index 10
            [
                "\left(\cos\left(t\\right),\sin\left(t+\sin\left(t+\sin\left(t+v_{8}\\right)\\right)\\right)\\right)",
                "This shapeshifting stuff is really good",
            ],
            # index 11
            [
                "\left(\cos\left(t+\cos\left(t+v_{10}\\right)\\right),\sin\left(t+\sin\left(t+\sin\left(t+v_{10}\\right)\\right)\\right)\\right)",
                "You can add as many sine functions as you like",
            ],
            # index 12
            [
                "\left(\cos\left(t+\cos\left(2t+v_{11}\\right)\\right),\sin\left(t+\sin\left(2t+\sin\left(t+v_{11}\\right)\\right)\\right)\\right)",
                "I can watch this all day!",
            ],
        ]

        lis = [
            # index 13 0 t
            [
                "\left(\cos\left(t\\right),\sin\left(t\\right)\\right)",
                "Cut the range of t to get that average loading screen",
                "v_{12}",
                "\pi+v_{12}+1",
            ],
            # index 14 1 t
            [
                "\left(0.8\cos\left(t\\right),0.8\sin\left(t\\right)\\right)",
                "Stack the previous one with this to get a better result",
                "-\left(\pi+v_{12}+1\\right)",
                "-v_{12}",
            ],
            # index 15 2 t
            [
                "\left(\cos\left(t\\right),\sin\left(t+\sin\left(2\\right)\\right)\\right)",
                "Here, I want to show you something cool...",
                "v_{13}",
                "1+v_{13}",
            ],
            # index 16 3 t
            [
                "\left(\cos\left(t\\right),\sin\left(t+\sin\left(2\\right)\\right)\\right)",
                "Let's increase the length",
                "v_{13}",
                "2.5+v_{13}",
            ],
            # index 17 4 r
            [
                "r=2\sin\left(3\\theta\\right)",
                "I still can't believe it was this simple",
                "v_{14}",
                "v_{14}+1",
            ],
            # index 18 5 r
            [
                "r=2\sin\left(2\\theta\\right)",
                "Wow, that was amazing. Let's do it again",
                "v_{14}",
                "v_{14}+3",
            ],
            # index 19 6 r
            [
                "r=\exp\left(\\frac{\sin\left(5\\theta\\right)}{5}\\right)",
                "This is grown man stuff",
                "v_{15}",
                "v_{15}+g_{1}",
            ],
            # index 20 7 r
            [
                "r=2\sin\left(\\frac{1}{2}\\theta\\right)",
                "Let's make another pattern",
                "v_{16}",
                "v_{16}+2\pi",
            ],
            # index 21 8 r
            [
                "r=2\sin\left(\\frac{1}{2}\\theta\\right)",
                "Add a new color and behold...",
                "v_{16}+2\pi",
                "v_{16}+4\pi",
            ],
            # index 22
            [
                "",
                "",
            ],
            # index 23
            [
                "",
                "",
            ],
            # index 24
            [
                "",
                "",
            ],

        ]

        lis = [
            [
                "\left(\cos\left(t\\right),\sin\left(t+\sin\left(2\\right)\\right)\\right)",
                "v_{13}",
                "1+v_{13}",
                "2.5+v_{13}",
                "4+v_{13}",
                "6+v_{13}",
                "4 Stages of awesomeness"
            ],

            [
                "r=2\sin\left(\\frac{2}{3}\\theta\\right)",
                "v_{17}",
                "v_{17}+2\pi",
                "v_{17}+4\pi",
                "v_{17}+6\pi",
                "This is work of art",
            ],
        ]

        # 1
        """
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

        for i in range(4,9):
            equation = MathTex(lis[i][0]).scale(
                1.25).shift(UP).set_color(YELLOW)

            k_range = MathTex(f"{lis[i][2]} \\leq \\theta \\leq {lis[i][3]}").next_to(
                equation, DOWN*3).set_color(YELLOW)

            mini_text = Text(lis[i][1]).scale(0.5).next_to(k_range, DOWN*3).set_color("##e0e0e0")

            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(k_range, shift=UP))
            self.play(FadeIn(mini_text, shift=UP))
            self.wait(3.5)
            self.clear() """

        for i in range(len(lis)-1):
            equation = MathTex(lis[i][0]).scale(
                1).shift(UP*3).set_color(YELLOW)

            v1 = MathTex(f"{lis[i][1]} \\leq t \\leq {lis[i][2]}").next_to(
                equation, DOWN*2).set_color(YELLOW)
            
            v2 = MathTex(f"{lis[i][1]} \\leq t \\leq {lis[i][3]}").next_to(
                v1, DOWN*2).set_color(YELLOW)
            
            v3 = MathTex(f"{lis[i][1]} \\leq t \\leq {lis[i][4]}").next_to(
                v2, DOWN*2).set_color(YELLOW)
            
            v4 = MathTex(f"{lis[i][1]} \\leq t \\leq {lis[i][5]}").next_to(
                v3, DOWN*2).set_color(YELLOW)

            mini_text = Text(lis[i][6]).scale(0.5).next_to(
                v4, DOWN*3).set_color("##e0e0e0")

            self.wait(0.25)
            self.play(FadeIn(equation))
            self.play(FadeIn(v1, shift=UP))
            self.play(FadeIn(v2, shift=UP))
            self.play(FadeIn(v3, shift=UP))
            self.play(FadeIn(v4, shift=UP))
            self.play(FadeIn(mini_text, shift=UP))
            self.wait(3.5)
            self.clear()


# manim -p screensaver-levels.py ScreensaverLevels
