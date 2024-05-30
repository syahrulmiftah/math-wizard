from manim import *

# manim -p straight-line-levels.py StraightLineLevels


class StraightLineLevels(Scene):
    def construct(self):
        lis = [
            # index 1
            [
                "\left(t\cos\left(v\\right),t\sin\left(v\\right)\\right)",
                "Let's start with simple a line",
            ],
            # index 2
            [
                "y=\pm \sin\left(v_{1}\\right)x",
                "Now lets add another line",
            ],
            # index 3
            [
                "\left(\sin\left(v_{1}\\right)+t,t\\right)",
                "\left(\sin\left(-v_{1}\\right)-t,t\\right)",
                "\left(\sin\left(v_{1}\\right)+t-2,t+2\\right)",
                "\left(\sin\left(-v_{1}\\right)+t+2,-t+2\\right)",
                "Just some random square",
            ],
 
            # index 4
            [
                "y=\sin\left(v_{1}\\right)+x",
                """
                Quiz time! In which direction does this line move? 
                
                Write your answer in the comment section below!
                """,
            ],
            # index 5
            [
                "y=\sin\left(v_{1}\\right)\pm x",
                "How about this one?",
            ],
            # index 6
            [
                "y=\sin\left(v_{1}\\right)\pm x",
                "\left(\sin\left(v_{1}\\right)+t,t\\right)",
                "\left(\sin\left(-v_{1}\\right)-t,t\\right)",
                "\left(\sin\left(v_{1}\\right)+t-2,t+2\\right)",
                "\left(\sin\left(-v_{1}\\right)+t+2,-t+2\\right)",
                "Well, here is the answer",
            ],
            # index 7
            [
                "\left(t+m_{2},m_{1}\\right)",
                "m_{1}=\cos\left(l_{2}+v\\right)",
                "m_{2}=\sin\left(l_{2}+v\\right)",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "Water wheel",
            ],            
            # index 9
            [
                "\left(0,t\\right)",
                "\left(t,0\\right)",
                "\left(l,t\\right)",
                "\left(t,l\\right)",
                "l=\left[2,-2\\right]",
                "keep it simple...",
            ],
            # index 10
            [
                "\left(\sin v_{2},\cos t\\right)",
                "\left(\cos t,\sin v_{2}\\right)",
                "\left(\cos t,-\sin v_{2}\\right)",
                "\left(-\sin v_{2},\cos t\\right)",
                "Four color, one square"
            ],                       
            # index 11
            [
                "\left(t\cos\left(v_{5}\\right)+1,t\sin\left(-v_{5}\\right)\\right)",
                "\left(t\cos\left(v_{5}\\right),t\sin\left(v_{5}\\right)+\cos\left(v_{5}\\right)4\\right)",
                "This is some action movie shit",
            ],
            # index 12
            [
                "\left(0,t\sin\left(v_{5}+1\\right)\\right)",
                "Just up and down ?!",
            ],
            # index 13
            [
                "\left(0,t\sin\left(v_{5}+1\\right)\\right)",
                "\left(\\frac{\pi}{6},t\sin\left(v_{5}+1.5\\right)\\right)",
                """
                Up and down again ?!
                
                This guy is up to something""",
            ],
            # index 14
            [
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "\left(l_{2},t\sin\left(v_{6}+l_{2}\\right)\\right)",
                "LET HIM COOK!",
            ],
            # index 15
            [
                "\left(l_{2},t\sin\left(2v_{6}+l_{2}\\right)\\right)",
                "Oh man, I should've put this in my previous video fr",
            ],
            # index 16
            [
                "\left(l_{2},t\sin\left(v_{6}+l_{2}\\right)\\right)",
                "\left(l_{2},t\sin\left(2v_{6}+l_{2}\\right)\\right)",
                "Wombo Combo! (squint your eyes to see better)",
            ],
            # index 17
            [
                "l_{3}=\left[-4\pi,-2\\frac{11}{6}\pi,...,4\pi\\right]",
                "\left(\\frac{l_{3}}{2}+t,1t\sin\left(v_{7}+l_{3}\\right)\\right)",
                """
                I refuse to believe that i just made 3d looking animation 
                
                with a curve using only lines """,
            ],
            # index 18
            [
                "\left(\\frac{l_{3}}{2}+t\sin\left(v_{7}\ \\right),t\sin\left(v_{7}+l_{3}\\right)\\right)",
                "And now i can move it left to right",
            ],
            # index 19
            [
                "\left(l_{2}+t,t\sin\left(v_{6}+l_{2}\\right)\\right)",
                "This one is very satisfying to watch",
            ],
            # index 20
            [
                "\left(l_{3}t\sin\ \left(v_{8}\\right),l_{3}+t\sin\left(v_{8}\\right)\\right)",
                "Honestly, I don't know what to call this one",
            ],
            # index 21
            [
                "\left(\pm l_{3}t\sin\ \left(v_{8}\\right),l_{3}+t\sin\left(v_{8}\\right)\\right)",
                "Prepare for trouble, and make it double",
            ],
            # index 22

            [
                "l_{4}=\left[0,2,...,10\\right]",
                "\left(-t+2l_{2}+\sin\left(v_{9}\\right),t\\right)",
                "\left(-t+2l_{2}+\sin\left(-v_{9}\\right),-t\\right)",
                "This one is for designers",
            ],
            # index 23

            [
                "l_{6}=\left[0,2,...,8\\right]",
                "\left(-t+2l_{2}+\sin\left(v_{10}\\right),\pm t+l_{6}\\right)",
                "Bravo six, going fullscreen",
            ],
            # index 24

            [
                "\left(-t+2l_{2}+\sin\left(-v_{9}\\right),-t\\right)",
                "\left(-t+2l_{2}+\sin\left(v_{9}\\right),t\\right)",
                "Trippy math graphs",
            ],
            # index 25

            [
                "\left(-t+2l_{2}+\sin\left(2\cos\left(v_{9}\\right)+2\sin\left(2v_{9}\\right)\\right),t\\right)",
                "\left(-t+2l_{2}+\sin\left(2\cos\left(2v_{9}\\right)+2\sin\left(-v_{9}\\right)\\right),-t\\right)",
                "Trippy pro max",
            ],
            # index 26

            [
                "l_{5}=\left[-7,-6.9,...,7\\right]",
                "\left(l_{5}+t,t\sin\left(v_{12}+l_{5}\\right)\\right)",
                "remember the graph at 02:31? He has reached his final form...",
            ],


        ]

        lis = [
            [
                "m_{1}=\cos\left(l_{2}+v_{11}\\right)",
                "m_{2}=\sin\left(l_{2}+v_{11}\\right)",
                "\left(t+m_{2}+\sin\left(v_{11}\\right),m_{1}+\cos\left(v_{11}\\right)+t\\right)",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "You know what, let's change the angle...",
            ],
            [
                "m_{1}=\cos\left(5l_{2}+v_{11}\\right)",
                "m_{2}=\sin\left(2l_{2}+v_{11}\\right)",
                "\left(t+m_{2}+\sin\left(v_{11}\\right),m_{1}+\cos\left(v_{11}\\right)\\right)",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "This is so fun to watch",
            ],
            [
                "\left(l_{2}+t,t\sin\left(v_{6}+l_{2}\\right)+l_{2}\\right)",
                "l_{2}=\left[-2\pi,-\\frac{11}{6}\pi,...,2\pi\\right]",
                "Kinda looks like DNA",

            ],
            [
                "l_{7}=\left[0,0.5,...,2\\right]",
                "\left(l_{7}\sin v_{2},l_{7}\cos t\\right)",
                "\left(l_{7}\cos t,l_{7}\sin v_{2}\\right)",
                "\left(l_{7}\cos\left(t\\right),-l_{7}\sin v_{2}\\right)",
                "\left(-l_{7}\sin v_{2},l_{7}\cos t\\right)",
                "Let's add more boxes",
            ],
            [
                "l_{5}=\left[-7,-6.9,...,7\\right]",
                "\left(l_{5}+t,t\sin\left(v_{12}+l_{5}\\right)\\right)",
                "This is an earlier graph, but i give him maximum power...",
            ],
            [
                "",
                "",
                "",
                "",
                "",
            ],
            [
                "",
                "",
                "",
                "",
                "",
            ],
        ]

        for item in lis:
            first_eq = MathTex(item[0]).to_edge(UP).set_color(YELLOW)

            mini_text = Text(item[-1]).scale(0.5).set_color("##e0e0e0")            
            variables = {}
            equations = item[1:-1]
            for i in range(len(equations)):
                # Create variables v1, v2, v3, ..., vn with values 1, 2, 3, ..., n
                variables[f"v{i+1}"] = MathTex(equations[i]).set_color(YELLOW)

            vars = [variables[f"v{i}"] for i in range(1, len(equations) + 1)]
            vg = VGroup(first_eq, *vars, mini_text)
            vg.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

            self.wait(0.25)
            [self.play(FadeIn(x, shift=UP)) for x in vg]
            self.wait(3.5)
            self.clear()

            
# manim -p straight-line-levels.py StraightLineLevels
